# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from shapefilesplitterdialogbase import Ui_ShapefileSplitterDialog

class SplitterDialog( QDialog, Ui_ShapefileSplitterDialog ):
  def __init__( self ):
    QDialog.__init__( self )
    self.setupUi( self )

    self.btnOk = self.buttonBox.button( QDialogButtonBox.Ok )

    QObject.connect( self.inputLayerCombo, SIGNAL( "currentIndexChanged( QString )" ), self.updateFieldList )
    QObject.connect( self.btnSelectDir, SIGNAL( "clicked()" ), self.inputDir )

    self.manageGui()

  def manageGui( self ):
    layers = self.getVectorLayers()
    self.inputLayerCombo.addItems( layers )

  def updateFieldList( self, inputLayer ):
    self.splitFieldCombo.clear()
    layer = self.getLayerByName( inputLayer )
    fields = self.getFieldList( layer )
    for i in fields:
      self.splitFieldCombo.addItem( unicode( fields[i].name() ) )

  def inputDir( self ):
    outDir = QFileDialog.getExistingDirectory( self,
              self.tr( "Select directory to save results to" ), "." )

    if outDir.isEmpty():
      return

    self.leOutputDir.setText( outDir )

  def reject( self ):
    QDialog.reject( self )

  def accept( self ):
    if self.inputLayerCombo.currentText() == "":
      QMessageBox.information( self, self.tr( "Shapefile splitter" ), self.tr( "No input layer specified" ) )
    elif self.leOutputDir.text() == "":
      QMessageBox.information( self, self.tr( "Shapefile splitter" ), self.tr( "Please specify output directory" ) )
    else:
      inField = self.splitFieldCombo.currentText()
      inLayer = self.getLayerByName( unicode( self.inputLayerCombo.currentText() ) )
      outPath = self.leOutputDir.text()

      QApplication.setOverrideCursor( QCursor( Qt.WaitCursor ) )
      self.btnOk.setEnabled( False )

      self.split( inLayer, inField, outPath )

      self.restoreGui()

  def getVectorLayers( self ):
    layerMap = QgsMapLayerRegistry.instance().mapLayers()
    layerList = []
    for name, layer in layerMap.iteritems():
      if layer.type() == QgsMapLayer.VectorLayer:
        layerList.append( unicode( layer.name() ) )
    return layerList

  def getLayerByName( self, layerName ):
    layerMap = QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layerMap.iteritems():
      if layer.type() == QgsMapLayer.VectorLayer and layer.name() == layerName:
        if layer.isValid():
          return layer
        else:
          return None

  def getFieldList( self, vLayer ):
    vProvider = vLayer.dataProvider()
    feat = QgsFeature()
    allAttrs = vProvider.attributeIndexes()
    vProvider.select( allAttrs )
    fieldList = vProvider.fields()
    return fieldList

  def restoreGui( self ):
    self.progressBar.setValue( 0 )
    QApplication.restoreOverrideCursor()
    self.btnOk.setEnabled( True )

  def split( self, layer, field, dir ):
    vProvider = layer.dataProvider()
    index = vProvider.fieldNameIndex( field )
    allAttrs = vProvider.attributeIndexes()
    vProvider.select( allAttrs )

    # get uniquie values in field
    uValues = []
    ft = QgsFeature()
    while vProvider.nextFeature( ft ):
      atMap = ft.attributeMap()
      if atMap.values()[ index ].toString() not in uValues:
        uValues.append( atMap.values()[ index ].toString() )

    self.progressBar.setRange( 0, len( uValues ) )

    # start split
    for i in uValues:
      vProvider.rewind()
      selection=[]
      while vProvider.nextFeature( ft ):
        atMap = ft.attributeMap()
        if atMap.values()[ index ].toString() == i:
          selection.append( ft.id() )
      layer.setSelectedFeatures(selection)
      self.progressBar.setValue( self.progressBar.value() + 1 )

      # write selection as shapefile
      if i == '':
        name = 'empty'
      else:
        name = i
      fileName = dir + "\\" + name + ".shp"
      QgsVectorFileWriter.writeAsShapefile( layer, fileName, 'UTF-8', None, True )
