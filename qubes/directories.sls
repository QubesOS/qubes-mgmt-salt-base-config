# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

##
# qubes.directories
# =================
#
# Set salt file and directory permissions of:
#   /srv/salt
#   /srv/pillar
#   /srv/formulas
#   /srv/spm
#   /srv/reactor
#
# Execute:
# --------
#   qubesctl state.sls qubes.directories
#
# TODO:
#   Add option to pillar to specify dir permissions of all file_roots
#
# Note:
#   Using using custom ID's to prevent possible conflicts
##

directory_srv_pillar:
  file.directory:
    - name: /srv/pillar
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

directory_srv_salt:
  file.directory:
    - name: /srv/salt
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

directory_srv_reactor:
  file.directory:
    - name: /srv/reactor
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

directory_srv_formulas:
  file.directory:
    - name: /srv/formulas
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

directory_srv_spm:
  file.directory:
    - name: /srv/spm
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode
