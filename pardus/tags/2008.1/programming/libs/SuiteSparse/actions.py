#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="SuiteSparse"

def build():
    shelltools.makedirs("dist")
    shelltools.export("SYSTEM_CFLAGS","%s -fPIC -O3" % get.CFLAGS())

    autotools.make()

def install():
    for header in ["UFconfig/UFconfig.h", "AMD/Include/amd.h", "BTF/Include/btf.h", "CHOLMOD/Include/*.h",
                   "COLAMD/Include/colamd.h", "CCOLAMD/Include/ccolamd.h", "KLU/Include/klu.h", "UMFPACK/Include/*.h",
                   "CAMD/Include/*.h", "CXSparse/Include/cs.h", "LDL/Include/ldl.h"]:
        shelltools.chmod(header, 0644)
        pisitools.insinto("/usr/include/suitesparse", header)

    for lib in ["CXSparse", "CSparse", "KLU", "COLAMD", "CCOLAMD", "LDL", "UMFPACK", "CHOLMOD",
                "AMD", "CAMD", "BTF"]:

        pisitools.dolib_so("%s/Lib/lib%s.so.3.1.0" % (lib, lib.lower()))
        pisitools.dosym("/usr/lib/lib%s.so.3.1.0" % lib.lower(), "/usr/lib/lib%s.so" % lib.lower())

    pisitools.dodoc("README.txt")
