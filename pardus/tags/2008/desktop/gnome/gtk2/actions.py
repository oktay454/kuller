#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gtk+-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-jpeg \
                         --with-libjpeg \
                         --with-libtiff \
                         --with-png \
                         --with-gdktarget=x11 \
                         --with-xinput")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README*", "HACKING", "TODO", "ChangeLog*", "NEWS*")
