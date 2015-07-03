%{!?version: %define version %(cat version)}
%{!?rel: %define rel %(cat rel)}
%{!?formula_name: %define formula_name %(cat formula_name)}

Name:      qubes-mgmt-salt-template
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   Formula description
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt-base
Requires:  qubes-mgmt-salt-config

%define _builddir %(pwd)

%description
Formula description.

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
# TODO:
# - Add formula path to file_roots
# - Add formula to salt top.sls
# - Add formula to pillar top.sls if contains pillar data
qubesctl saltutil.sync_all -l quiet --out quiet

%preun
# TODO:
# - Remove formula path to file_roots
# - Remove formula to salt top.sls
# - Remove formula to pillar top.sls if contains pillar data
qubesctl saltutil.sync_all -l quiet --out quiet

%files
%defattr(-,root,root)
#
# XXX: See if we can use var set in Makefile
#

%attr(750, root, root) %dir /srv/formulas/%{formula_name}
/srv/formulas/%{formula_name}/*

%changelog
