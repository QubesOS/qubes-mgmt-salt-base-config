# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

##
# qubes.user-dirs
# ===============
#
# Install and maintain user salt and pillar directories for personal state
# configurations:
#
#   Includes a simple locale state file
#
#   User defined scripts will not be removed on removal of qubes-mgmt-salt
#   by design nor will they be modified on any updates, other than permissions
#   being enforced.
#
# Execute:
# --------
#   qubesctl state.sls qubes.user-dirs
#
# Note:
#   Using using custom ID's to prevent possible conflicts
##

directory_srv_user_salt:
  file.directory:
    - name: /srv/user_salt
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

# User 'pillar' directory and file permissions
# Note: using custom ID due to possible conflicts
directory_srv_user_pillar:
  file.directory:
    - name: /srv/user_pillar
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

# User 'formulas' directory and file permissions
# Note: using custom ID due to possible conflicts
directory_srv_user_formulas:
  file.directory:
    - name: /srv/user_formulas
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

# User 'state' top.sls file
/srv/user_salt/top.sls:
  file.managed:
    - source: salt://qubes/files/top.sls
    - replace: False
    - makedirs: True
    - user: root
    - group: root
    - mode: 640
    - require:
      - file: /srv/user_salt

# User 'pillar' top.sls file
/srv/user_pillar/top.sls:
  file.managed:
    - name: 
    - source: salt://qubes/files/pillar.sls
    - replace: False
    - makedirs: True
    - user: root
    - group: root
    - mode: 640
    - require:
      - file: /srv/user_pillar

# Sample locale state directory
/srv/user_salt/locale:
  file.directory:
    - user: root
    - group: root
    - dir_mode: 750
    - file_mode: 640
    - recurse:
      - user
      - group
      - mode

# Sample locale state file
/srv/user_salt/locale/init.sls:
  file.managed:
    - source: salt://qubes/files/locale.sls
    - replace: False
    - makedirs: True
    - user: root
    - group: root
    - mode: 640
    - require:
      - file: /srv/user_salt/locale

