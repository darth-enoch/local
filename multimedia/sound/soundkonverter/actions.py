#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="soundkonverter-"+get.srcVERSION()

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.dodoc("CHANGELOG", "INSTALL", "README")
