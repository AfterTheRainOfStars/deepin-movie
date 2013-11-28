#! /usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Wang Yong
# 
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtCore import QSize
from PyQt5 import QtCore
import sys
import os
import signal
from window import Window
from database import Database
from config import Config

if __name__ == "__main__":
    movie_file = sys.argv[1]
    
    app = QApplication(sys.argv)
    database = Database()
    config = Config()
    
    view = Window()
    
    qml_context = view.rootContext()
    qml_context.setContextProperty("windowView", view)
    qml_context.setContextProperty("qApp", qApp)
    qml_context.setContextProperty("movie_file", movie_file)
    qml_context.setContextProperty("database", database)
    qml_context.setContextProperty("config", config)
    
    view.setSource(QtCore.QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), 'Main.qml')))
    view.setMinimumSize(QSize(900, 518))
    view.show()
    
    view.windowStateChanged.connect(view.rootObject().monitorWindowState)
    app.lastWindowClosed.connect(view.rootObject().monitorWindowClose)
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())