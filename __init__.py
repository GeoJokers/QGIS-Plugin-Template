# -*- coding: utf-8 -*-
"""
This script initializes the plugin, making it known to QGIS.
"""

PLUGIN_NAME = "My Plugin"
PLUGIN_MENU = "GeoJokers"


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .plugin import Plugin

    return Plugin(iface, PLUGIN_NAME, PLUGIN_MENU)
