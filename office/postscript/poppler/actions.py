#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--disable-static \
               --disable-poppler-qt \
               --disable-gtk-doc-html \
               --disable-zlib \
               --disable-gtk-test \
               --enable-poppler-qt4 \
               --enable-cairo-output \
               --enable-xpdf-headers \
               --enable-libjpeg \
               --enable-libopenjpeg"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --disable-utils \
                     --disable-gtk-test \
                     --disable-poppler-cpp \
                     --disable-poppler-qt4"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.autoreconf("-fi")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/lib32", "poppler/.libs/libpoppler.so*")
        pisitools.insinto("/usr/lib32", "glib/.libs/libpoppler-glib.so*")
        pisitools.insinto("/usr/lib32/pkgconfig", "poppler.pc")
        pisitools.insinto("/usr/lib32/pkgconfig", "poppler-glib.pc")
        return
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
