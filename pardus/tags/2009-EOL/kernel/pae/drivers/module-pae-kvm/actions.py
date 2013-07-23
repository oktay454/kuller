#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kvm-kmod-%s" % get.srcVERSION()

def setup():
    # Fix PREFIX
    pisitools.dosed("Makefile", "^PREFIX =.*$", "PREFIX = /usr")
    pisitools.dosed("Makefile", "etc\/udev", "lib\/udev")

    autotools.rawConfigure('--arch=%s \
                            --kerneldir=/lib/modules/%s/build' % (get.ARCH().replace("i686", "x86"),
                                                                  kerneltools.getKernelVersion()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "modules_install")