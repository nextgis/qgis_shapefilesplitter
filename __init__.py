# -*- coding: utf-8 -*-
mVersion = "0.1.0"
def name():
  return "ShapefileSplitter"
def description():
  return "Splits shapefile into many using text field as a source"
def qgisMinimumVersion():
  return "1.0"
def version():
  return mVersion
def authorName():
  return "Maxim Dubinin, sim@gis-lab.info"
def classFactory(iface):
  from shapefile_splitter import shapefile_splitter
  return shapefile_splitter(iface)
