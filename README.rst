====================
qubes-config-forumla
====================

Qubes+Salt Management base configuration for SaltStack's Salt Infrastructure
automation and management system

Available States
================

.. contents::
    :local:

``config``
----------

- Sets formula file_roots and updates salt configuration setting in
  ``/etc/salt/minion.s/f_defaults.conf`` based on pillar data located in 
  ``/srv/pillar/base/config.sls``.

- Ensures salt-minion service is dead

``qubes.directories``
---------------------

Sets salt's main file and directory permissions for:

::

    /srv/salt
    /srv/pillar
    /srv/formulas
    /srv/reactor
    /srv/spm

``qubes.user-dirs``
-------------------

Install and maintain user salt and pillar directories for personal state
configurations:

::

    /srv/user_salt
    /srv/user_pillar

User defined scripts will not be removed on removal of qubes-mgmt-salt
by design nor will they be modified on any updates, other than permissions
being enforced.

Included Pillar Data
====================

``config``
----------

Contains all salt configuration data user to configure the salt.

``qubes``
---------

Contains all the qubes default setting for various states


``Configuration``
=================
Every option available in the templates can be set in pillar. Settings under
'salt' will be overridden by more specific settings under ``salt['master']``,
``salt['minion']`` or ``salt['cloud']``

::

    salt:
      ret_port: 4506
      master:
        user: saltuser
        ...
      minion:
        user: saltuser
        ...
      cloud:
        providers: ec2
        ...

``Extending``
=============
Additional templates can be added by the user under salt/files/minion.d and
master.d. This might be useful if, for example, a recently-added configuration
option is not yet provided by the default template.
