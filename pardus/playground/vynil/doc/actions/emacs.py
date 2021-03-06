#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='{$pkg}-%s' % get.srcVERSION().replace('_','')

def install():
    for data in ['cogre', 'common', 'contrib', 'ede', 'eieio', 'semantic', 'speedbar']:
        pisitools.insinto('/usr/share/emacs/site-lisp/${pkg}/', data)
