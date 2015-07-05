# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

##
# qubes.config
# ============
#
# Qubes Configuration
#
# - Sets formula file_roots and updates salt configuration setting in
#   /etc/salt/minion.s/f_defaults based on pillar data located in 
#   /srv/pillar/base/qubes/config.sls.
#
# - Ensures salt-minion service is dead
#
# Execute:
# --------
#   qubesctl state.sls qubes.config
##

{% from "config/map.jinja" import salt_settings with context %}

salt-standalone-config:
  file.recurse:
    - name: {{ salt_settings.config_path }}/minion.d
    - template: jinja
    - source: salt://{{ slspath }}/files/minion.d
    - clean: {{ salt_settings.clean_config_d_dir }}
    - exclude_pat: _*
    - context:
        standalone: True
  
  service.dead:
    - enable: False
    - name: {{ salt_settings.minion_service }}
    - require:
      - file: salt-standalone-config
