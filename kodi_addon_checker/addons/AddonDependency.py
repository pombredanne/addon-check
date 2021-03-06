"""
    Copyright (C) 2018 Team Kodi
    This file is part of Kodi - kodi.tv

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/README.md for more information.
"""

from distutils.version import LooseVersion
import xml.etree.ElementTree as ET


class AddonDependency(object):
    def __init__(self, import_xml: ET.Element):
        super(AddonDependency, self).__init__()
        self.id = import_xml.get('addon')
        self.version = None
        if import_xml.get('version') is not None:
            self.version = LooseVersion(import_xml.get('version'))
        self.optional = import_xml.get('optional', False)
