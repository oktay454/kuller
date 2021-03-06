#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import coreutils
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.9")

    # Fix all linkage problems :(((
    shelltools.export("CC", "gcc")

    # Fetching revision info (same as "dateinfo = srcDIR/.mkstamp < srcDIR/ChangeLog")
    revinfo = (coreutils.cat("ChangeLog") | coreutils.grep("\s\$Revision") | coreutils.join).split()
    dateinfo = " (%s %s %s)" % (revinfo[1], revinfo[4], revinfo[5])

    shelltools.copy("ltmain.in", "ltmain.shT")
    pisitools.dosed("ltmain.shT", "@VERSION@", get.srcVERSION())
    pisitools.dosed("ltmain.shT", "@PACKAGE@", get.srcNAME())
    pisitools.dosed("ltmain.shT", "@TIMESTAMP@", dateinfo)
    shelltools.move("ltmain.shT", "ltmain.sh")

    # Two steps just to be *really* sure :)
    shelltools.copy("libtool.m4", "acinclude.m4T")
    shelltools.move("acinclude.m4T", "acinclude.m4")

    shelltools.touch("libltdl/acinclude.m4")

    for d in [".", "libltdl"]:
        shelltools.cd(d)
        shelltools.touch("acinclude.m4")
        autotools.aclocal()
        autotools.automake("-c -a")
        autotools.autoconf()

    shelltools.cd("../")

    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README", "THANKS", "TODO", "doc/PLATFORMS")

    dir = "/usr/share/libtool/"

    for f in ["config.sub", "config.guess"]:
        for d in ["", "libltdl/"]:
            pisitools.remove(dir + d + f)
            pisitools.dosym(dir + "../gnuconfig/" + f, dir + d + f)

    dir = "/usr/share/libtool/libltdl/"

    for pf in ["guess", "sub"]:
        pisitools.remove(dir + "config." + pf)
        pisitools.dosym(dir + "../config." + pf, dir + "config." + pf)

    # Fix default lib paths
    pisitools.dosed("%s/usr/bin/libtool" % get.installDIR() ,"sys_lib_search_path_spec=.*","sys_lib_search_path_spec=\"/lib /usr/lib /usr/local/lib\"")
    pisitools.dosed("%s/usr/bin/libtool" % get.installDIR() ,"sys_lib_dlsearch_path_spec=.*","sys_lib_dlsearch_path_spec=\"/lib /usr/lib /usr/local/lib\"")

    # Don't let gcc paths sneak in
    pisitools.dosed("%s/usr/bin/libtool" % get.installDIR() ,"predep_objects=.*","predep_objects=\"\"")
    pisitools.dosed("%s/usr/bin/libtool" % get.installDIR() ,"postdep_objects=.*","postdep_objects=\"\"")
    pisitools.dosed("%s/usr/bin/libtool" % get.installDIR() ,"compiler_lib_search_path=.*","compiler_lib_search_path=\"\"")
