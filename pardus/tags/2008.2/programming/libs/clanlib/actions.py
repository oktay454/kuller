#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

conf = {"version": get.srcVERSION(),
        "installdir": get.installDIR(),
        "docdir": "%s/%s" % (get.docDIR(), get.srcTAG())}


WorkDir = "ClanLib-%(version)s" % conf

def fixfiles(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name == ".cvsignore":
                try:
                    os.unlink(os.path.join(root,name))
                except:
                    pass


def setup():
    shelltools.export("CFLAGS", "%s -fno-omit-frame-pointer" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-omit-frame-pointer" % get.CXXFLAGS())

    pisitools.dosed("Setup/Unix/clanlib-config.in", "@comp_mode@")
    autotools.configure("--enable-dyn \
                         --enable-clansound \
                         --libdir=/usr/lib/clanlib-%(version)s \
                         --includedir=/usr/include/clanlib-%(version)s \
                         --enable-network \
                         --enable-asm386 \
                         --enable-x11 \
                         --enable-opengl \
                         --enable-vorbis \
                         --enable-png \
                         --enable-ttf \
                         --enable-mikmod \
                         --enable-joystick \
                         --enable-vidmode \
                         --disable-debug" % conf)

def build():
    autotools.make()

def install():
    autotools.rawInstall('prefix=%(installdir)s/usr \
                          LIB_PREFIX=%(installdir)s/usr/lib/clanlib-%(version)s \
                          INC_PREFIX=%(installdir)s/usr/include/clanlib-%(version)s' % conf)

    # No static libs
    pisitools.remove("/usr/lib/clanlib-%(version)s/*.a" % conf)

    pisitools.rename("/usr/bin/clanlib-config", "clanlib0.6-config")

    fixfiles("Documentation/Examples")
    pisitools.insinto(conf["docdir"], "Documentation/Examples")

    pisitools.dodoc("BUGS", "CODING_STYLE", "HARDWARE", "NEWS", "PATCHES", "PORTING", "README*", "ROADMAP")

    shelltools.cd("%(installdir)s/usr/lib/clanlib-%(version)s" % conf)
    for f in shelltools.ls("*.2"):
        shelltools.sym("clanlib-%s/%s" % (conf["version"], f), "../%s" % f)

