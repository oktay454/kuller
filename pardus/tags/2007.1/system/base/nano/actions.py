#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-color --enable-nanorc --enable-utf8 --disable-speller")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())    
    pisitools.dodoc("ChangeLog", "README", "doc/nanorc.sample", "AUTHORS", "BUGS", "NEWS", "TODO")
    pisitools.dodoc("*.html")
    pisitools.insinto("/etc/", "doc/nanorc.sample", "nanorc")
    pisitools.dosym("/usr/bin/nano", "/bin/nano")
