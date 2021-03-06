#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde.configure()
    
def build():
    kde.make()
    
def install():
    kde.install()
    # fix #3460
    shelltools.chmod("%s/usr/kde/3.5/bin/smb4k_mount" % get.installDIR(), 04755)
    shelltools.chmod("%s/usr/kde/3.5/bin/smb4k_umount" % get.installDIR(), 04755)
