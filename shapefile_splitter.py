# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from shapefile_splitter_dlgselfield import dlgSelField
import os

class shapefile_splitter:

  def __init__(self, iface):
    """Initialize the class"""
    self.iface = iface
  
  def initGui(self):
    self.action = QAction("Split shapefile", self.iface.mainWindow())
    self.action.setStatusTip("Splits shapefile into many using text field with unique values")
    QObject.connect(self.action, SIGNAL("activated()"), self.run)
    self.iface.addPluginToMenu("&Split shapefile", self.action)
  def unload(self):
    self.iface.removePluginMenu("&Split shapefile",self.action)

  def run(self):
    layersmap=QgsMapLayerRegistry.instance().mapLayers()
    layerslist=[]
    curLayer = self.iface.mapCanvas().currentLayer()
    if (curLayer == None):
      infoString = QString("No layers selected")
      QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
      return
    if (curLayer.type() <> curLayer.VectorLayer):
      infoString = QString("Not a vector layer")
      QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
      return
    adir = QFileDialog.getExistingDirectory(None, "Choose results folder", QDir.currentPath())
    if adir == "":
        return
    featids = range(curLayer.featureCount())
    fProvider = curLayer.dataProvider()
    fEncoding = fProvider.encoding()
    fCRS = fProvider.crs()
    myFields = fProvider.fields()
    allFieldsNames= [f.name() for f in myFields.values()]
    myFieldsNames=[]
    for f in myFields.values():
       if f.typeName() == "String":
          myFieldsNames.append(f.name())
    if len(myFieldsNames) == 0:
       QMessageBox.information(self.iface.mainWindow(),"Warning","No string field names. Exiting")
       return
    elif len(myFieldsNames) == 1:
       attrfield = myFieldsNames[0]
    else:
      res = dlgSelField(myFieldsNames)
      if res.exec_():
        attrfield=res.selectedAttr()
      else:
        return
    fldIndex = allFieldsNames.index(attrfield)
    #get a list of unique values from a text field    
    vals=[]
    for fid in featids: 
       features={}
       features[fid]=QgsFeature()
       curLayer.featureAtId(fid,features[fid])
       attrmap=features[fid].attributeMap()
       attr=attrmap.values()[fldIndex]
       attr=attr.toString()
       if attr not in vals:
            vals.append(attr)
    for entry in vals:
        fProvider.rewind()
        selection=[]
        for fid in featids: 
            features={}
            features[fid]=QgsFeature()
            curLayer.featureAtId(fid,features[fid])
            attrmap=features[fid].attributeMap()
            attr=attrmap.values()[fldIndex]
            if attr.toString() == entry:
                selection.append(fid)
        curLayer.setSelectedFeatures(selection)
        
        #save selection as new shape-file
        if entry == "":
            entry = "empty"
        shapefileName = adir + "\\" + entry + ".shp"
        QgsVectorFileWriter.writeAsShapefile(curLayer, shapefileName, fEncoding, fCRS, True)
        #writer = QgsVectorFileWriter(shapefileName, "CP1251", myFields, fProvider.geometryType(), fProvider.crs())
        #proceed to the next entry value