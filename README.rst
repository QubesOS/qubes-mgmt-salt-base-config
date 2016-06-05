====================
qubes-config-forumla
====================

Qubes+Salt Management base configuration for SaltStack's Salt Infrastructure
automation and management system

Available States
================

.. contents::
    :local:

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

``qubes``
---------

Contains all the qubes default setting for various states

