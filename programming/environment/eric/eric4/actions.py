#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

NoStrip = ["/usr/bin", "/usr/lib", "/usr/qt/4/qsci/api"]
conf = {"bindir": "/usr/bin",
        "installdir": get.installDIR(),
        "site-packages": "/usr/lib/%s/site-packages" % get.curPYTHON()}

def install():
    pythonmodules.run("install.py -z \
                                  -b %(bindir)s \
                                  -i %(installdir)s \
                                  -d %(site-packages)s \
                                  -c" % conf)
    pythonmodules.fixCompiledPy()
    for lang in ["cs", "de", "es", "fr", "it", "ru", "tr"]:
        pisitools.insinto("%(site-packages)s/eric4/i18n" % conf, "eric/i18n/eric4_%s.qm" % lang)
    pisitools.dodoc("changelog", "LICENSE.GPL3", "THANKS", "README*")
