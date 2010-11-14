# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

import os
from __init__ import mVersion

import splitterdialog

class shapefile_splitter( object ):

  def __init__( self, iface ):
    self.iface = iface
    self.iface = iface
    try:
      self.QgisVersion = unicode( QGis.QGIS_VERSION_INT )
    except:
      self.QgisVersion = unicode( QGis.qgisVersion )[ 0 ]

    # For i18n support
    userPluginPath = QFileInfo( QgsApplication.qgisUserDbFilePath() ).path() + "/python/plugins/shapefile_splitter"
    systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/shapefile_splitter"

    overrideLocale = QSettings().value( "locale/overrideFlag", QVariant( False ) ).toBool()
    if not overrideLocale:
      localeFullName = QLocale.system().name()
    else:
      localeFullName = QSettings().value( "locale/userLocale", QVariant( "" ) ).toString()

    if QFileInfo( userPluginPath ).exists():
      translationPath = userPluginPath + "/i18n/shpsplitter_" + localeFullName + ".qm"
    else:
      translationPath = systemPluginPath + "/i18n/shpsplitter_" + localeFullName + ".qm"

    self.localePath = translationPath
    if QFileInfo( self.localePath ).exists():
      self.translator = QTranslator()
      self.translator.load( self.localePath )
      QCoreApplication.installTranslator( self.translator )

  def initGui(self):
    if int( self.QgisVersion ) < 1:
      QMessageBox.warning( self.iface.mainWindow(), "Shapefile splitter",
                           QCoreApplication.translate( "Shapefile splitter", "Quantum GIS version detected: " ) + unicode( self.QgisVersion ) + ".xx\n" +
                           QCoreApplication.translate( "Shapefile splitter", "This version of Shapefile Splitter requires at least QGIS version 1.0.0\nPlugin will not be enabled." ) )
      return None

    self.actionRun = QAction("Split shapefile", self.iface.mainWindow())
    self.actionRun.setStatusTip("Splits shapefile into many using text field with unique values")
    self.actionRun.setWhatsThis( "Split shapefile into many" )
    self.actionAbout = QAction( "About", self.iface.mainWindow() )

    QObject.connect(self.actionRun, SIGNAL("triggered()"), self.run)
    QObject.connect( self.actionAbout, SIGNAL( "triggered()" ), self.about )

    self.iface.addPluginToMenu("Split shapefile", self.actionRun)
    self.iface.addPluginToMenu( "Split shapefile", self.actionAbout )

  def unload(self):
    self.iface.removePluginMenu("Split shapefile",self.actionRun)
    self.iface.removePluginMenu( "Split shapefile", self.actionAbout )

  def about( self ):
    dlgAbout = QDialog()
    dlgAbout.setWindowTitle( QApplication.translate( "Shapefile splitter", "About Shapefile splitter", "Window title" ) )
    lines = QVBoxLayout( dlgAbout )
    title = QLabel( QApplication.translate( "Shapefile splitter", "<b>Shapefile splitter</b>" ) )
    title.setAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
    lines.addWidget( title )
    version = QLabel( QApplication.translate( "Shapefile splitter", "Version: %1" ).arg( mVersion ) )
    version.setAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
    lines.addWidget( version )
    lines.addWidget( QLabel( QApplication.translate( "Shapefile splitter", "Splits shapefile into many using\ntext field with unique values" ) ) )
    lines.addWidget( QLabel( QApplication.translate( "Shapefile splitter", "<b>Developers:</b>" ) ) )
    lines.addWidget( QLabel( "  Maxim Dubinin" ) )
    #lines.addWidget( QLabel( QApplication.translate( "Shapefile splitter", "<b>Homepage:</b>") ) )

    #overrideLocale = QSettings().value( "locale/overrideFlag", QVariant( False ) ).toBool()
    #if not overrideLocale:
    #  localeFullName = QLocale.system().name()
    #else:
    #  localeFullName = QSettings().value( "locale/userLocale", QVariant( "" ) ).toString()

    #localeShortName = localeFullName[ 0:2 ]
    #if localeShortName in [ "ru", "uk" ]:
    #  link = QLabel( "<a href=\"http://gis-lab.info/qa/merge-shapes.html\">http://gis-lab.info/qa/merge-shapes.html</a>" )
    #else:
    #  link = QLabel( "<a href=\"http://gis-lab.info/qa/merge-shapes.html\">http://gis-lab.info/qa/merge-shapes.html</a>" )

    #link.setOpenExternalLinks( True )
    #lines.addWidget( link )

    btnClose = QPushButton( QApplication.translate( "Shapefile splitter", "Close" ) )
    lines.addWidget( btnClose )
    QObject.connect( btnClose, SIGNAL( "clicked()" ), dlgAbout, SLOT( "close()" ) )

    dlgAbout.exec_()

  def run(self):
    dlg = splitterdialog.SplitterDialog()
    dlg.exec_()
