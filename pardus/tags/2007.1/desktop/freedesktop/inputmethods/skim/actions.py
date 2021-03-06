#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    scons.make("configure prefix=%s" % get.kdeDIR() )

def build():
    scons.make( )

def install():
    scons.install(argument="DESTDIR")

    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")

