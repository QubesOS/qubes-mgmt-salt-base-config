# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

{%- from "vmtype.jinja" import vmtype %}

#
# NOTE: WIP, Not yet implemented
# 
# WIP: Not Implemented
#      (Manually added in mgmt-salt-base-config/pillar/config/init.sls)
#

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
# modules.sls
# ===========
#
# config path locations
#
# Extra configuration to be added by the config module to Salt's configuration
# file located at:
#   /etc/salt/minion.d/f_defaults.conf
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 

salt-modules:
  config:
    # ──────────────────────────────────────────────────────────────────────────
    # Root formula directories
    # Default: /srv/formulas
    # ──────────────────────────────────────────────────────────────────────────
    formula_dirs:
      - /srv/formulas
      - /srv/user_formulas
