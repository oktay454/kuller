#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lapack-lite-%s" % get.srcVERSION()

def setup():
    shelltools.copy("INSTALL/make.inc.gfortran", "make.inc")

    pisitools.dosed("make.inc", "-funroll-all-loops -O3", "%s -fPIC -funroll-all-loops -O3" % get.CFLAGS())

def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib","SRC/liblapack.*")
    pisitools.insinto("/usr/lib","BLAS/SRC/libblas.*")

    pisitools.insinto("/usr/lib","lapack_LINUX.a","liblapack.a")
    pisitools.insinto("/usr/lib","blas_LINUX.a","libblas.a")

    pisitools.dodoc("COPYING", "README")
