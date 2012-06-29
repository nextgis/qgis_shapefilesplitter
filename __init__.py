# -*- coding: utf-8 -*-
mVersion = "0.1.2"
def name():
  return "ShapefileSplitter"
def description():
  return "Splits shapefile into many using text field as a source"
def category():
  return "Vector"
def qgisMinimumVersion():
  return "1.0.0"
def version():
  return "0.1.2"
def authorName():
  return "Maxim Dubinin (NextGIS)"
def classFactory(iface):
  from shapefile_splitter import shapefile_splitter
  return shapefile_splitter(iface)
