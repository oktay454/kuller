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

WorkDir = "glibc-20080408T0706"

def undef_variables():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CFLAGS", "-mtune=generic -march=i686 -O3 -pipe -fomit-frame-pointer -mno-tls-direct-seg-refs -g -ggdb")

def setup():
    undef_variables()

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                       --with-tls \
                       --with-__thread \
                       --enable-add-ons=nptl,libidn \
                       --enable-bind-now \
                       --enable-kernel=2.6.24 \
                       --without-cvs \
                       --without-selinux \
                       --build=%s \
                       --host=%s \
                       --disable-profile \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --libexecdir=/usr/lib/misc" % (get.HOST(), get.HOST()))

def build():
    undef_variables()

    shelltools.cd("build")
    autotools.make()

def check():
    undef_variables()
    shelltools.chmod("scripts/begin-end-check.pl")

    shelltools.cd("build")

    shelltools.export("TIMEOUTFACTOR", "16")
    autotools.make("-k check 2>error.log")

def install():
    # These should not be set, else the zoneinfo do not always get installed ...
    undef_variables()

    # install glibc/glibc-locale files
    shelltools.cd("build")
    autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # Some things want this, notably ash
    pisitools.dosym("libbsd-compat.a", "/usr/lib/libbsd.a")

    # We'll take care of the cache ourselves
    pisitools.remove("/etc/ld.so.cache")

    # It previously has 0755 perms which was killing things
    shelltools.chmod("%s/usr/lib/misc/pt_chown" % get.installDIR(), 04711)

    # Prevent overwriting of the /etc/localtime symlink
    pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    shelltools.cd("..")
    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "INTERFACE", "NEWS", "NOTES", "PROJECTS", "README*", "LICENSE")
