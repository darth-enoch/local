#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "trigger-%s-data" % get.srcVERSION()

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    fixperms(".")
    for dirs in ("maps", "fonts", "vehicles", "materials", "textures", "events", "sounds", "plugins"):
        shelltools.copytree(dirs, "%s/usr/share/trigger" % get.installDIR())

    for files in ("crap.obj", "trigger.config.defs"):
        pisitools.insinto("/usr/share/trigger", files)

    pisitools.dodoc("*.txt")

