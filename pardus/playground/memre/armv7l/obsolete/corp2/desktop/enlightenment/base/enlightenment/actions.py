#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-shared \
                         --enable-nls \
                         --enable-pam \
                         --disable-rpath \
                         --disable-illume \
                         --disable-illume2 \
                         --with-x \
                         --with-edje-cc=/usr/bin/edje_cc \
                         --with-eet-eet=/usr/bin/eet")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
