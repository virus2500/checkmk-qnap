#!/usr/bin/env python

from mkp import dist

dist({
    'author': 'Michael Kronika',
    'description': '##Changelog 1.4.5\n- Fix CPU/Temperature order. Issue #4\n\n## Changelog 1.4.4\n- Fix location of WATO Plugins\n\n## Changelog 1.4.3\n- FIX: "If more than one volume was existing only the first one was shown correctly" by Yogibaer75\n- Fixed typo found by Erik\n\n## Changelog 1.4.2\n- Minor cleanups\n\n## Changelog 1.4.1\n- Edited qnap_fans so it can support more then 2 fans.\n- Added Wato Interface for qnap_fans and qnap_temp\n\n## Changelog 1.4\n- Original from Andre Eckstein, Christian Burmeister\n- Removed HDD check since this is covered by an built in check (qnap_disks) already\n- Made it checkmk 1.6 compatible\n',
    'download_url': 'https://github.com/virus2500/checkmk-qnap',
    'name': 'qnap',
    'title': 'Check Qnap Storage',
    'version': '1.4.5-alpha1',
    'version.min_required': '1.6.0',
})
