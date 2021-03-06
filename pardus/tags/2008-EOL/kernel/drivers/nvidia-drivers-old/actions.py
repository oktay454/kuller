#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "NVIDIA-Linux-x86-%s" % get.srcVERSION()
NoStrip = ["/lib/modules"]

base = "/usr/lib/xorg/nvidia-old"

def setup():
    pisitools.dosed("usr/lib/libGL.la", "__LIBGL_PATH__", "/usr/lib/")

def build():
    shelltools.export("SYSSRC","/lib/modules/%s/source/" % get.curKERNEL())
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % get.curKERNEL(), "usr/src/nv/nvidia.ko", "nvidia_old.ko")

    # Libraries and X modules
    pisitools.insinto("%s/lib" % base, "usr/X11R6/lib/*")
    pisitools.insinto("%s/lib" % base, "usr/lib/*")
    pisitools.domove("%s/lib/modules/*" % base, base)
    pisitools.removeDir("%s/lib/modules" % base)

    # Headers
    pisitools.insinto(base, "usr/include")

    # Our libc is TLS enabled so use TLS library
    pisitools.remove("%s/lib/libnvidia-tls.so.*" % base)

    # Remove static libs
    pisitools.remove("%s/lib/*.a" % base)

    # Documentation
    pisitools.dodoc("usr/share/doc/*")
