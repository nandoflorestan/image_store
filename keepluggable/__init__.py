# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from bag import resolve


def read_setting(settings, key, default=None):
    if default is None:
        try:
            return settings[key]
        except KeyError:
            raise RuntimeError('The config file does not contain a "{}" entry '
                               'in its [keepluggable] section.'.format(key))
    else:
        return settings.get(key, default)


def resolve_setting(settings, key, default=None):
    resource_spec = read_setting(settings, key, default)
    return resolve(resource_spec)