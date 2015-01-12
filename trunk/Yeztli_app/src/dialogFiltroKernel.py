# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/christian/Documentos/YEZTLI/gui/dialogFiltroKernel.ui'
#
# Created: Mon Jan  5 23:28:33 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Filtro(object):
    def setupUi(self, Filtro):
        Filtro.setObjectName(_fromUtf8("Filtro"))
        Filtro.resize(394, 180)
        self.buttonBox = QtGui.QDialogButtonBox(Filtro)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Filtro)
        self.label.setGeometry(QtCore.QRect(40, 50, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.kernelBox = QtGui.QSpinBox(Filtro)
        self.kernelBox.setGeometry(QtCore.QRect(170, 50, 201, 31))
        self.kernelBox.setMinimum(3)
        self.kernelBox.setMaximum(15)
        self.kernelBox.setSingleStep(2)
        self.kernelBox.setObjectName(_fromUtf8("kernelBox"))

        self.retranslateUi(Filtro)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Filtro.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Filtro.reject)
        QtCore.QMetaObject.connectSlotsByName(Filtro)

    def retranslateUi(self, Filtro):
        Filtro.setWindowTitle(QtGui.QApplication.translate("Filtro", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Filtro", "TamaNo del kernel", None, QtGui.QApplication.UnicodeUTF8))

    def tamKernel(self):        
        tamKernel = int(self.kernelBox.value())        
        return tamKernel

   
    @staticmethod
    def getParams(parent = None):
        d = QtGui.QDialog()
        ui = Ui_Filtro()
        ui.setupUi(d)
        resultado = d.exec_()
        print resultado
        kernel = ui.tamKernel()
        return kernel