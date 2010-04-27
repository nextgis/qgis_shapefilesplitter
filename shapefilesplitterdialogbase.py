# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shapefilesplitterdialogbase.ui'
#
# Created: Sun Apr 25 12:26:01 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ShapefileSplitterDialog(object):
    def setupUi(self, ShapefileSplitterDialog):
        ShapefileSplitterDialog.setObjectName("ShapefileSplitterDialog")
        ShapefileSplitterDialog.resize(307, 232)
        self.verticalLayout = QtGui.QVBoxLayout(ShapefileSplitterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(ShapefileSplitterDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputLayerCombo = QtGui.QComboBox(ShapefileSplitterDialog)
        self.inputLayerCombo.setObjectName("inputLayerCombo")
        self.verticalLayout.addWidget(self.inputLayerCombo)
        self.label_2 = QtGui.QLabel(ShapefileSplitterDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.splitFieldCombo = QtGui.QComboBox(ShapefileSplitterDialog)
        self.splitFieldCombo.setObjectName("splitFieldCombo")
        self.verticalLayout.addWidget(self.splitFieldCombo)
        self.label_3 = QtGui.QLabel(ShapefileSplitterDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leOutputDir = QtGui.QLineEdit(ShapefileSplitterDialog)
        self.leOutputDir.setObjectName("leOutputDir")
        self.horizontalLayout.addWidget(self.leOutputDir)
        self.btnSelectDir = QtGui.QPushButton(ShapefileSplitterDialog)
        self.btnSelectDir.setObjectName("btnSelectDir")
        self.horizontalLayout.addWidget(self.btnSelectDir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtGui.QProgressBar(ShapefileSplitterDialog)
        self.progressBar.setProperty("value", QtCore.QVariant(0))
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(ShapefileSplitterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ShapefileSplitterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ShapefileSplitterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ShapefileSplitterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShapefileSplitterDialog)

    def retranslateUi(self, ShapefileSplitterDialog):
        ShapefileSplitterDialog.setWindowTitle(QtGui.QApplication.translate("ShapefileSplitterDialog", "Shapefile splitter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ShapefileSplitterDialog", "Input layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ShapefileSplitterDialog", "Split by field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ShapefileSplitterDialog", "Save to", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectDir.setText(QtGui.QApplication.translate("ShapefileSplitterDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))

