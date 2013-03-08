#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

WorkDir = "gtk+-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--with-gdktarget=x11 \
               --enable-xinerama \
               --with-xinput=yes \
               --enable-xkb \
               --enable-shm \
               --enable-silent-rules \
               --enable-introspection \
               --disable-papi"

    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))
    #gtk2 needs -DGTK_COMPILATION CPPFLAG when compiling itself
    #Avoid "Only <gtk/gtk.h> can be included directly error"
    shelltools.export("CPPFLAGS", "-DGTK_COMPILATION")


    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin \
                     --disable-cups"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CC())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS().replace("-fomit-frame-pointer",""))
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
        shelltools.export("CPPFLAGS", "-DGTK_COMPILATION")

    #libtools.libtoolize("--copy --force")
    autotools.autoreconf("-vif")
    autotools.configure(options)

    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove empty dir
    #pisitools.removeDir("/usr/share/man")
    pisitools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

    if get.buildTYPE() == "_emul32":
        for binaries in ["gtk-query-immodules-2.0", "gtk-demo"]:
            pisitools.domove("/_emul32/bin/%s" % binaries, "/usr/bin/", "%s-32bit" % binaries)
        pisitools.removeDir("/_emul32")
