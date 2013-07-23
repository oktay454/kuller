#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ipv6 \
                         --disable-strict\
                         --disable-static \
                         --enable-debug=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc/ortp/*")
    pisitools.dodoc("README","ChangeLog","NEWS","COPYING","AUTHORS","TODO")
    pisitools.dohtml("doc/html/*")