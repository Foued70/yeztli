from PyQt4 import QtCore,QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Umbral(QtGui.QDialog):
    def __init__(self, parent = None):
        super(Umbral, self).__init__(parent)

        #layout = QVBoxLayout(self)

        # nice widget for editing the date
        #self.datetime = QDateTimeEdit(self)
        #self.datetime.setCalendarPopup(True)
        #self.datetime.setDateTime(QDateTime.currentDateTime())
        #layout.addWidget(self.datetime)
        self.parametros = (0,0)
        
        #Umbral.setObjectName(_fromUtf8("Umbral"))
        #Umbral.resize(449, 304)
#        self.buttonBox = QtGui.QDialogButtonBox(Umbral)
#        self.buttonBox.setGeometry(QtCore.QRect(70, 250, 341, 32))
#        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
#        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Umbral)
        self.label.setGeometry(QtCore.QRect(120, 190, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.umbralEdit = QtGui.QLineEdit(Umbral)
        self.umbralEdit.setGeometry(QtCore.QRect(190, 190, 191, 31))
        self.umbralEdit.setObjectName(_fromUtf8("umbralEdit"))
        self.label_2 = QtGui.QLabel(Umbral)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 301, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.binary = QtGui.QRadioButton(Umbral)
        self.binary.setGeometry(QtCore.QRect(40, 70, 108, 26))
        self.binary.setObjectName(_fromUtf8("binary"))
        self.binaryInv = QtGui.QRadioButton(Umbral)
        self.binaryInv.setGeometry(QtCore.QRect(40, 100, 131, 26))
        self.binaryInv.setObjectName(_fromUtf8("binaryInv"))
        self.trunc = QtGui.QRadioButton(Umbral)
        self.trunc.setGeometry(QtCore.QRect(180, 70, 108, 26))
        self.trunc.setObjectName(_fromUtf8("trunc"))
        self.toZero = QtGui.QRadioButton(Umbral)
        self.toZero.setGeometry(QtCore.QRect(180, 100, 108, 26))
        self.toZero.setObjectName(_fromUtf8("toZero"))
        self.toZeroInv = QtGui.QRadioButton(Umbral)
        self.toZeroInv.setGeometry(QtCore.QRect(290, 70, 141, 26))
        self.toZeroInv.setObjectName(_fromUtf8("toZeroInv"))
        self.label_3 = QtGui.QLabel(Umbral)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        
        Umbral.setWindowTitle(QtGui.QApplication.translate("Umbral", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Umbral", "umbral", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Umbral", "Ingrese valor dentro del intervalo 0 -255", None, QtGui.QApplication.UnicodeUTF8))
        self.binary.setText(QtGui.QApplication.translate("Umbral", "Binaria", None, QtGui.QApplication.UnicodeUTF8))
        self.binaryInv.setText(QtGui.QApplication.translate("Umbral", "Binaria Inverza", None, QtGui.QApplication.UnicodeUTF8))
        self.trunc.setText(QtGui.QApplication.translate("Umbral", "Trunca", None, QtGui.QApplication.UnicodeUTF8))
        self.toZero.setText(QtGui.QApplication.translate("Umbral", "a Zero", None, QtGui.QApplication.UnicodeUTF8))
        self.toZeroInv.setText(QtGui.QApplication.translate("Umbral", "a Zero Inverzo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Umbral", "Tipo de umbralizacion", None, QtGui.QApplication.UnicodeUTF8))
        

        # OK and Cancel buttons
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        layout.addWidget(self.buttons)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)


    def binarizacion(self):
        umbral = int(self.umbralEdit.text())
        if self.binary.isChecked():
            print "umbralizacion binaria con umbral ", umbral
            return (umbral, 1)
        elif self.binaryInv.isChecked():
            print "umbralizacion binaryInv con umbral ", umbral
            return (umbral, 2)
        elif self.trunc.isChecked():
            print "umbralizacion trunc con umbral ", umbral
            return (umbral, 3)
        elif self.toZero.isChecked():
            print "umbralizacion toZero con umbral ", umbral
            return (umbral, 4)
        elif self.toZeroInv.isChecked():
            print "umbralizacion toZeroInv con umbral ", umbral
            return (umbral, 5)
        



    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getParams(parent = None):
        dialog = Umbral(parent)
        result = dialog.exec_()
        opciones = dialog.dateTime()
        return opciones