#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --enable-python \
                         --enable-introspection \
                         --libexecdir=/usr/lib/vte \
                         --localstatedir=/var \
                         --without-glX \
                         --disable-gtk-doc \
                         --with-gtk=2.0")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "MAINTAINERS", "COPYING", "NEWS", "README")
