#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-examples \
                         --enable-gnome-vfs \
                         --enable-libvisual \
                         --enable-experimental \
                         --enable-introspection=no \
                         --with-package-name='Pardus gstreamer-plugins-base package' \
                         --with-package-origin='http://www.pardus-anka.org'")
                         
    if get.buildTYPE() == "emul32":
        options = "--disable-static \
                   --disable-rpath \
                   --disable-examples \
                   --disable-gnome-vfs \
                   --enable-libvisual \
                   --enable-experimental \
                   --enable-introspection=no \
                   --with-package-name='Pardus gstreamer-plugins-base package' \
                   --with-package-origin='http://www.pardus-anka.org'"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        autotools.configure(options)

def build():
    autotools.make()

# tests fail sandbox
#def check():
#    autotools.make("-C tests/check check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
