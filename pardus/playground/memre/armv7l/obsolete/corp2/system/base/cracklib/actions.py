#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--with-default-dict=/usr/share/cracklib/pw_dict \
                          --disable-static")

def build():
    crosstools.make("all")

def install():
    crosstools.install()

    # Create dictionary files
    shelltools.system("cat /usr/share/dict/words | cracklib-packer %s/usr/share/cracklib/pw_dict" % get.installDIR())

    pisitools.domo("po/tr.po","tr","cracklib.mo")
    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "README*", "NEWS", "COPYING", "AUTHORS")