# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/christian/Documentos/YEZTLI/gui/dialogMorfologia.ui'
#
# Created: Mon Jan  5 23:29:39 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_morfologia(object):
    def setupUi(self, morfologia):
        morfologia.setObjectName(_fromUtf8("morfologia"))
        morfologia.resize(389, 224)
        self.buttonBox = QtGui.QDialogButtonBox(morfologia)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(morfologia)
        self.label.setGeometry(QtCore.QRect(10, 30, 171, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.CruzButton = QtGui.QRadioButton(morfologia)
        self.CruzButton.setGeometry(QtCore.QRect(10, 60, 108, 26))
        self.CruzButton.setObjectName(_fromUtf8("CruzButton"))
        self.elipseButton = QtGui.QRadioButton(morfologia)
        self.elipseButton.setGeometry(QtCore.QRect(150, 60, 108, 26))
        self.elipseButton.setObjectName(_fromUtf8("elipseButton"))
        self.rectanguloButton = QtGui.QRadioButton(morfologia)
        self.rectanguloButton.setGeometry(QtCore.QRect(270, 60, 108, 26))
        self.rectanguloButton.setObjectName(_fromUtf8("rectanguloButton"))
        self.label_2 = QtGui.QLabel(morfologia)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.kernelBox = QtGui.QSpinBox(morfologia)
        self.kernelBox.setGeometry(QtCore.QRect(140, 110, 211, 31))
        self.kernelBox.setMinimum(3)
        self.kernelBox.setMaximum(15)
        self.kernelBox.setSingleStep(2)
        self.kernelBox.setObjectName(_fromUtf8("kernelBox"))

        self.retranslateUi(morfologia)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), morfologia.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), morfologia.reject)
        QtCore.QMetaObject.connectSlotsByName(morfologia)

    def retranslateUi(self, morfologia):
        morfologia.setWindowTitle(QtGui.QApplication.translate("morfologia", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("morfologia", "Elemento de estructura", None, QtGui.QApplication.UnicodeUTF8))
        self.CruzButton.setText(QtGui.QApplication.translate("morfologia", "Cruz", None, QtGui.QApplication.UnicodeUTF8))
        self.elipseButton.setText(QtGui.QApplication.translate("morfologia", "Elipse", None, QtGui.QApplication.UnicodeUTF8))
        self.rectanguloButton.setText(QtGui.QApplication.translate("morfologia", "Rectangulo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("morfologia", "TamaNo del kernel", None, QtGui.QApplication.UnicodeUTF8))

    def morfologia(self):        
        tamKernel = int(self.kernelBox.value())        
        if self.CruzButton.isChecked():
            print " cruz ", tamKernel
            return (tamKernel, 1)
        elif self.elipseButton.isChecked():
            print "elipse ", tamKernel
            return (tamKernel, 2)
        elif self.rectanguloButton.isChecked():
            print "rectangulo ", tamKernel
            return (tamKernel, 3)
    
    @staticmethod
    def getParams(parent = None):
        d = QtGui.QDialog()
        ui = Ui_morfologia()
        ui.setupUi(d)
        resultado = d.exec_()
        print resultado
        opciones = ui.morfologia()
        return opciones