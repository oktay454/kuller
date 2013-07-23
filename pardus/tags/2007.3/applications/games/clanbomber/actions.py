#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 


def setup():
    shelltools.export("CXXFLAGS", "%s -I/usr/include/clanlib-0.6.5" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s -L/usr/lib/clanlib-0.6.5" % get.LDFLAGS())
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "IDEAS", "QUOTES", "README")