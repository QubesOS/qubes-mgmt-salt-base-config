%{!?version: %define version %(make get-version)}
%{!?rel: %define rel %(make get-release)}
%{!?package_name: %define package_name %(make get-package_name)}
%{!?package_summary: %define package_summary %(make get-summary)}
%{!?package_description: %define package_description %(make get-description)}

%{!?formula_name: %define formula_name %(make get-formula_name)}
%{!?state_name: %define state_name %(make get-state_name)}
%{!?saltenv: %define saltenv %(make get-saltenv)}
%{!?pillar_dir: %define pillar_dir %(make get-pillar_dir)}
%{!?formula_dir: %define formula_dir %(make get-formula_dir)}

Name:      %{package_name}
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   %{package_summary}
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  salt
Requires:  salt-minion
Requires:  qubes-mgmt-salt-config
Requires:  qubes-mgmt-salt-base-overrides
Requires:  qubes-mgmt-salt-base-overrides-libs
Requires:  qubes-mgmt-salt-base-topd
Requires(post): /usr/bin/salt-call

%define _builddir %(pwd)

%description
%{package_description}

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# NOTE: Use salt-call since qubesctl is not installed yet

# Sync all modules
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable States
qubesctl top.enable qubes.directories saltenv=%{saltenv} -l quiet --out quiet > /dev/null || true
qubesctl top.enable qubes.user-dirs saltenv=%{saltenv} -l quiet --out quiet > /dev/null || true
qubesctl top.enable config saltenv=%{saltenv} -l quiet --out quiet > /dev/null || true

# Enable Pillar States
qubesctl top.enable config saltenv=%{saltenv} pillar=true -l quiet --out quiet > /dev/null || true
qubesctl top.enable config.modules saltenv=%{saltenv} pillar=true -l quiet --out quiet > /dev/null || true

# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%attr(750, root, root) %dir /srv/salt/config
/srv/salt/config/defaults.yaml
/srv/salt/config/files/minion.d/f_defaults.conf
/srv/salt/config/init.sls
/srv/salt/config/init.top
/srv/salt/config/LICENSE
/srv/salt/config/map.jinja
/srv/salt/config/README.rst

%attr(750, root, root) %dir /srv/salt/_modules
/srv/salt/_modules/ext_config.py*

%attr(750, root, root) %dir /srv/salt/qubes
/srv/salt/qubes/directories.sls
/srv/salt/qubes/directories.top
/srv/salt/qubes/files/locale.sls
/srv/salt/qubes/files/pillar.sls
/srv/salt/qubes/files/top.sls
/srv/salt/qubes/LICENSE
/srv/salt/qubes/README.rst
/srv/salt/qubes/user-dirs.sls
/srv/salt/qubes/user-dirs.top

%attr(750, root, root) %dir /srv/pillar/config
%config(noreplace) /srv/pillar/config/init.sls
/srv/pillar/config/init.top
%config(noreplace) /srv/pillar/config/modules.sls
/srv/pillar/config/modules.top

/srv/pillar/vmtype.jinja

%changelog
