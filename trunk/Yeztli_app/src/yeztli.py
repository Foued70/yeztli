# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/christian/Documentos/YEZTLI/gui/yeztli.ui'
#
# Created: Mon Nov 17 04:23:13 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Metodos, copy, cv2
from dialogUmbral import Ui_Umbral
from dialogFiltroKernel import Ui_Filtro
from dialogMorfologia import Ui_morfologia


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VentanaPrincipal(object):
    
    def __init__(self):
        self.img = None
        self.imgOriginal = None
        self.sure_bg = None
        self.posicionDes = 0
        self.memoria = ["1","2","3","4","5","6","7","8","9","10"]
        
        
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName(_fromUtf8("VentanaPrincipal"))
        VentanaPrincipal.resize(1120, 732)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../pruebasTT/pruebadiano.TIF")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaPrincipal.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 220, 151, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 610, 21, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.valorX = QtGui.QLabel(self.centralwidget)
        self.valorX.setGeometry(QtCore.QRect(56, 610, 61, 21))
        self.valorX.setObjectName(_fromUtf8("valorX"))
        self.valorY = QtGui.QLabel(self.centralwidget)
        self.valorY.setGeometry(QtCore.QRect(56, 630, 61, 21))
        self.valorY.setObjectName(_fromUtf8("valorY"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 630, 21, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(134, 610, 41, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.valorRojo = QtGui.QLabel(self.centralwidget)
        self.valorRojo.setGeometry(QtCore.QRect(180, 610, 61, 21))
        self.valorRojo.setObjectName(_fromUtf8("valorRojo"))
        self.valorVerde = QtGui.QLabel(self.centralwidget)
        self.valorVerde.setGeometry(QtCore.QRect(180, 630, 61, 21))
        self.valorVerde.setObjectName(_fromUtf8("valorVerde"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(134, 630, 51, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.valorAzul = QtGui.QLabel(self.centralwidget)
        self.valorAzul.setGeometry(QtCore.QRect(180, 650, 61, 21))
        self.valorAzul.setObjectName(_fromUtf8("valorAzul"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(134, 650, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 200, 1061, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(550, 220, 20, 381))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 131, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.select_imagen_original = QtGui.QRadioButton(self.centralwidget)
        self.select_imagen_original.setGeometry(QtCore.QRect(30, 30, 131, 26))
        self.select_imagen_original.setObjectName(_fromUtf8("select_imagen_original"))
        self.select_imagen_modificada = QtGui.QRadioButton(self.centralwidget)
        self.select_imagen_modificada.setGeometry(QtCore.QRect(30, 50, 151, 26))
        self.select_imagen_modificada.setObjectName(_fromUtf8("select_imagen_modificada"))
        self.labelimagenOriginal = QtGui.QLabel(self.centralwidget)
        self.labelimagenOriginal.setGeometry(QtCore.QRect(40, 250, 500, 350))
        self.labelimagenOriginal.setMouseTracking(False)
        self.labelimagenOriginal.setAutoFillBackground(False)
        self.labelimagenOriginal.setLineWidth(1)
        self.labelimagenOriginal.setText(_fromUtf8(""))
        self.labelimagenOriginal.setPixmap(QtGui.QPixmap(_fromUtf8("../../../NetBeansProjects/Yeztli_app/recursos/default_image_01.png")))
        self.labelimagenOriginal.setScaledContents(True)
        self.labelimagenOriginal.setObjectName(_fromUtf8("labelimagenOriginal"))
        self.labelImagenModificada = QtGui.QLabel(self.centralwidget)
        self.labelImagenModificada.setGeometry(QtCore.QRect(580, 250, 500, 350))
        self.labelImagenModificada.setMouseTracking(False)
        self.labelImagenModificada.setAutoFillBackground(False)
        self.labelImagenModificada.setLineWidth(1)
        self.labelImagenModificada.setText(_fromUtf8(""))
        self.labelImagenModificada.setPixmap(QtGui.QPixmap(_fromUtf8("../../../NetBeansProjects/Yeztli_app/recursos/default_image_01.png")))
        self.labelImagenModificada.setScaledContents(True)
        self.labelImagenModificada.setObjectName(_fromUtf8("labelImagenModificada"))
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuEdicioon = QtGui.QMenu(self.menubar)
        self.menuEdicioon.setObjectName(_fromUtf8("menuEdicioon"))
        self.menuMetodo_Otsu = QtGui.QMenu(self.menuEdicioon)
        self.menuMetodo_Otsu.setObjectName(_fromUtf8("menuMetodo_Otsu"))
        self.menuNegar = QtGui.QMenu(self.menuEdicioon)
        self.menuNegar.setObjectName(_fromUtf8("menuNegar"))
        self.menuBinarizacion = QtGui.QMenu(self.menuEdicioon)
        self.menuBinarizacion.setObjectName(_fromUtf8("menuBinarizacion"))
        self.menuFiltros = QtGui.QMenu(self.menubar)
        self.menuFiltros.setObjectName(_fromUtf8("menuFiltros"))
        self.menuMediana = QtGui.QMenu(self.menuFiltros)
        self.menuMediana.setObjectName(_fromUtf8("menuMediana"))
        self.menuGaussiano = QtGui.QMenu(self.menuFiltros)
        self.menuGaussiano.setObjectName(_fromUtf8("menuGaussiano"))
        self.menuBilateral = QtGui.QMenu(self.menuFiltros)
        self.menuBilateral.setObjectName(_fromUtf8("menuBilateral"))
        self.menuMorfologia = QtGui.QMenu(self.menubar)
        self.menuMorfologia.setObjectName(_fromUtf8("menuMorfologia"))        
        self.menuHistograma = QtGui.QMenu(self.menubar)
        self.menuHistograma.setObjectName(_fromUtf8("menuHistograma"))
        self.menuSegmentacion = QtGui.QMenu(self.menubar)
        self.menuSegmentacion.setObjectName(_fromUtf8("menuSegmentacion"))
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        VentanaPrincipal.setStatusBar(self.statusbar)
        
        
        self.actionAbrir = QtGui.QAction(VentanaPrincipal)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionGuardar = QtGui.QAction(VentanaPrincipal)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionDeshacer = QtGui.QAction(VentanaPrincipal)
        self.actionDeshacer.setObjectName(_fromUtf8("actionDeshacer"))
        self.actionEscala_de_grises = QtGui.QAction(VentanaPrincipal)
        self.actionEscala_de_grises.setObjectName(_fromUtf8("actionEscala_de_grises"))
        self.actionOtsu_Por_color = QtGui.QAction(VentanaPrincipal)
        self.actionOtsu_Por_color.setObjectName(_fromUtf8("actionOtsu_Por_color"))
        self.actionOtsu_Grices = QtGui.QAction(VentanaPrincipal)
        self.actionOtsu_Grices.setObjectName(_fromUtf8("actionOtsu_Grices"))
        self.actionMediana = QtGui.QAction(VentanaPrincipal)
        self.actionMediana.setObjectName(_fromUtf8("actionMediana"))
        self.actionGauss = QtGui.QAction(VentanaPrincipal)
        self.actionGauss.setObjectName(_fromUtf8("actionGauss"))
        self.actionBilateral = QtGui.QAction(VentanaPrincipal)
        self.actionBilateral.setObjectName(_fromUtf8("actionBilateral"))
        self.actionNegar_Canal_rojo = QtGui.QAction(VentanaPrincipal)
        self.actionNegar_Canal_rojo.setObjectName(_fromUtf8("actionNegar_Canal_rojo"))
        self.actionNegar_Canal_verde = QtGui.QAction(VentanaPrincipal)
        self.actionNegar_Canal_verde.setObjectName(_fromUtf8("actionNegar_Canal_verde"))
        self.actionNegar_Canal_azul = QtGui.QAction(VentanaPrincipal)
        self.actionNegar_Canal_azul.setObjectName(_fromUtf8("actionNegar_Canal_azul"))
        self.actionNegar_Todos_los_canales = QtGui.QAction(VentanaPrincipal)
        self.actionNegar_Todos_los_canales.setObjectName(_fromUtf8("actionNegar_Todos_los_canales"))
        self.actionBinario = QtGui.QAction(VentanaPrincipal)
        self.actionBinario.setObjectName(_fromUtf8("actionBinario"))        
        self.actionApertura = QtGui.QAction(VentanaPrincipal)
        self.actionApertura.setObjectName(_fromUtf8("actionApertura"))
        self.actionCerradura = QtGui.QAction(VentanaPrincipal)
        self.actionCerradura.setObjectName(_fromUtf8("actionCerradura"))
        self.actionErosion = QtGui.QAction(VentanaPrincipal)
        self.actionErosion.setObjectName(_fromUtf8("actionErosion"))
        self.actionDilatacion = QtGui.QAction(VentanaPrincipal)
        self.actionDilatacion.setObjectName(_fromUtf8("actionDilatacion"))
        self.actionVer_histograma = QtGui.QAction(VentanaPrincipal)
        self.actionVer_histograma.setObjectName(_fromUtf8("actionVer_histograma"))
        self.actionEcualizacion_del_histograma = QtGui.QAction(VentanaPrincipal)
        self.actionEcualizacion_del_histograma.setObjectName(_fromUtf8("actionEcualizacion_del_histograma"))
        self.actionWatershed = QtGui.QAction(VentanaPrincipal)
        self.actionWatershed.setObjectName(_fromUtf8("actionWatershed"))
        self.actionRellenar_hoyos = QtGui.QAction(VentanaPrincipal)
        self.actionRellenar_hoyos.setObjectName(_fromUtf8("actionRellenar_hoyos"))
        self.actionDeteccionCirculo = QtGui.QAction(VentanaPrincipal)
        self.actionDeteccionCirculo.setObjectName(_fromUtf8("actionDeteccionCirculo"))
        
        self.actionTrans_Rapida_de_distancia = QtGui.QAction(VentanaPrincipal)
        self.actionTrans_Rapida_de_distancia.setObjectName(_fromUtf8("actionTrans_Rapida_de_distancia"))
        self.actionEtiquetar = QtGui.QAction(VentanaPrincipal)
        self.actionEtiquetar.setObjectName(_fromUtf8("actionEtiquetar"))
        self.actionEliminar_objetos_de_los_bordes = QtGui.QAction(VentanaPrincipal)
        self.actionEliminar_objetos_de_los_bordes.setObjectName(_fromUtf8("actionEliminar_objetos_de_los_bordes"))
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuMetodo_Otsu.addSeparator()
        self.menuMetodo_Otsu.addAction(self.actionOtsu_Por_color)
        self.menuMetodo_Otsu.addAction(self.actionOtsu_Grices)
        self.menuNegar.addAction(self.actionNegar_Canal_rojo)
        self.menuNegar.addAction(self.actionNegar_Canal_verde)
        self.menuNegar.addAction(self.actionNegar_Canal_azul)
        self.menuNegar.addAction(self.actionNegar_Todos_los_canales)
        self.menuBinarizacion.addAction(self.actionBinario)
        self.menuEdicioon.addAction(self.actionDeshacer)
        self.menuEdicioon.addSeparator()
        self.menuEdicioon.addAction(self.menuNegar.menuAction())
        self.menuEdicioon.addAction(self.menuMetodo_Otsu.menuAction())
        self.menuEdicioon.addAction(self.actionEscala_de_grises)
        self.menuEdicioon.addAction(self.menuBinarizacion.menuAction())
        
        self.menuFiltros.addAction(self.actionMediana)
        self.menuFiltros.addAction(self.actionGauss)
        self.menuFiltros.addAction(self.actionBilateral)
        
        self.menuMorfologia.addAction(self.actionApertura)
        self.menuMorfologia.addAction(self.actionCerradura)
        self.menuMorfologia.addAction(self.actionErosion)
        self.menuMorfologia.addAction(self.actionDilatacion)
        
        
        self.menuHistograma.addAction(self.actionVer_histograma)
        self.menuHistograma.addAction(self.actionEcualizacion_del_histograma)
        self.menuSegmentacion.addAction(self.actionEliminar_objetos_de_los_bordes)
        self.menuSegmentacion.addAction(self.actionEtiquetar)
        self.menuSegmentacion.addSeparator()
        self.menuSegmentacion.addAction(self.actionWatershed)
        self.menuSegmentacion.addAction(self.actionDeteccionCirculo)
        self.menuSegmentacion.addAction(self.actionRellenar_hoyos)
        self.menuSegmentacion.addAction(self.actionTrans_Rapida_de_distancia)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEdicioon.menuAction())
        self.menubar.addAction(self.menuFiltros.menuAction())
        self.menubar.addAction(self.menuMorfologia.menuAction())
        self.menubar.addAction(self.menuHistograma.menuAction())
        self.menubar.addAction(self.menuSegmentacion.menuAction())

        
        #senales de los widgets
        self.actionAbrir.triggered.connect(self.abrirImg)
        self.actionDeshacer.triggered.connect(self.deshacer)
        self.actionNegar_Canal_rojo.triggered.connect(self.negarRojo)
        self.actionNegar_Canal_verde.triggered.connect(self.negarVerde)
        self.actionNegar_Canal_azul.triggered.connect(self.negarAzul)
        self.actionNegar_Todos_los_canales.triggered.connect(self.negarImg)
        self.actionOtsu_Por_color.triggered.connect(self.otsuColor)
        self.actionOtsu_Grices.triggered.connect(self.otsuGrises)
        self.actionEscala_de_grises.triggered.connect(self.escalaGrises)
        self.actionBinario.triggered.connect(self.binario)
        self.actionMediana.triggered.connect(self.filtroMediana)
        self.actionGauss.triggered.connect(self.filtroGauss)
        self.actionBilateral.triggered.connect(self.filtroBilateral)
        self.actionApertura.triggered.connect(self.apertura)
        self.actionCerradura.triggered.connect(self.cerradura)
        self.actionErosion.triggered.connect(self.erosion)
        self.actionDilatacion.triggered.connect(self.dilatacion)
        self.actionTrans_Rapida_de_distancia.triggered.connect(self.transDistancia)
        self.actionRellenar_hoyos.triggered.connect(self.rellenarHoyos)
        self.actionWatershed.triggered.connect(self.watershed)
        self.actionDeteccionCirculo.triggered.connect(self.deteccionCirculos)
        
        
        
        self.actionVer_histograma.triggered.connect(self.graficarHistograma)
        
        
        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QtGui.QApplication.translate("VentanaPrincipal", "Yeztli", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VentanaPrincipal", "Imagen original", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("VentanaPrincipal", "Imagen modificada", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("VentanaPrincipal", "x:", None, QtGui.QApplication.UnicodeUTF8))
        self.valorX.setText(QtGui.QApplication.translate("VentanaPrincipal", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.valorY.setText(QtGui.QApplication.translate("VentanaPrincipal", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("VentanaPrincipal", "y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("VentanaPrincipal", "Rojo:", None, QtGui.QApplication.UnicodeUTF8))
        self.valorRojo.setText(QtGui.QApplication.translate("VentanaPrincipal", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.valorVerde.setText(QtGui.QApplication.translate("VentanaPrincipal", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("VentanaPrincipal", "Verde:", None, QtGui.QApplication.UnicodeUTF8))
        self.valorAzul.setText(QtGui.QApplication.translate("VentanaPrincipal", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("VentanaPrincipal", "Azul:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("VentanaPrincipal", "Modificaciones en:", None, QtGui.QApplication.UnicodeUTF8))
        self.select_imagen_original.setText(QtGui.QApplication.translate("VentanaPrincipal", "Imagen original", None, QtGui.QApplication.UnicodeUTF8))
        self.select_imagen_modificada.setText(QtGui.QApplication.translate("VentanaPrincipal", "Imagen modificada", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdicioon.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Edicion", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMetodo_Otsu.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Quitar fondo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNegar.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Negar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBinarizacion.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Binarizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFiltros.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Filtros", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMorfologia.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Morfologia", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHistograma.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Histograma", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSegmentacion.setTitle(QtGui.QApplication.translate("VentanaPrincipal", "Segmentacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("VentanaPrincipal", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGuardar.setText(QtGui.QApplication.translate("VentanaPrincipal", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeshacer.setText(QtGui.QApplication.translate("VentanaPrincipal", "Deshacer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEscala_de_grises.setText(QtGui.QApplication.translate("VentanaPrincipal", "Escala de grises", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOtsu_Por_color.setText(QtGui.QApplication.translate("VentanaPrincipal", "Otsu por color", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOtsu_Grices.setText(QtGui.QApplication.translate("VentanaPrincipal", "Otsu por escala de grices", None, QtGui.QApplication.UnicodeUTF8))
        
                
        self.actionMediana.setText(QtGui.QApplication.translate("VentanaPrincipal", "Mediana", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGauss.setText(QtGui.QApplication.translate("VentanaPrincipal", "Gaussiano", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBilateral.setText(QtGui.QApplication.translate("VentanaPrincipal", "Bilateral", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNegar_Canal_rojo.setText(QtGui.QApplication.translate("VentanaPrincipal", "canal rojo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNegar_Canal_verde.setText(QtGui.QApplication.translate("VentanaPrincipal", "canal verde", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNegar_Canal_azul.setText(QtGui.QApplication.translate("VentanaPrincipal", "canal azul", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNegar_Todos_los_canales.setText(QtGui.QApplication.translate("VentanaPrincipal", "todos los canales", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBinario.setText(QtGui.QApplication.translate("VentanaPrincipal", "Aplicar Binarizacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionApertura.setText(QtGui.QApplication.translate("VentanaPrincipal", "Apertura", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCerradura.setText(QtGui.QApplication.translate("VentanaPrincipal", "Cerradura", None, QtGui.QApplication.UnicodeUTF8))
        self.actionErosion.setText(QtGui.QApplication.translate("VentanaPrincipal", "Erosion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDilatacion.setText(QtGui.QApplication.translate("VentanaPrincipal", "Dilatacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVer_histograma.setText(QtGui.QApplication.translate("VentanaPrincipal", "Ver histograma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEcualizacion_del_histograma.setText(QtGui.QApplication.translate("VentanaPrincipal", "Ecualizacion del histograma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWatershed.setText(QtGui.QApplication.translate("VentanaPrincipal", "Watershed", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeteccionCirculo.setText(QtGui.QApplication.translate("VentanaPrincipal", "deteccion de circulos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRellenar_hoyos.setText(QtGui.QApplication.translate("VentanaPrincipal", "Rellenar hoyos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTrans_Rapida_de_distancia.setText(QtGui.QApplication.translate("VentanaPrincipal", "Trans. Rapida de distancia", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEtiquetar.setText(QtGui.QApplication.translate("VentanaPrincipal", "Etiquetar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEliminar_objetos_de_los_bordes.setText(QtGui.QApplication.translate("VentanaPrincipal", "Eliminar objetos de los bordes", None, QtGui.QApplication.UnicodeUTF8))
        

    def abrirImg(self):
        ruta = QtGui.QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.tif);;")
        if ruta == '':
            print 'No se selecciono ninguna imagen'
        else:
            self.img = Metodos.abrirImagen(str(ruta))
            self.img = cv2.resize(self.img, (800, 600))
            self.imgOriginal = copy.deepcopy(self.img)
            #tranforma la imagen que abrimos a RGB
            cv2.cvtColor(self.img, cv2.cv.CV_BGR2RGB, self.img)
            cv2.cvtColor(self.imgOriginal, cv2.cv.CV_BGR2RGB, self.imgOriginal)            
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelimagenOriginal.setPixmap(q)
            self.labelImagenModificada.setPixmap(q)
            self.posicionDes = 0
            self.agregarMemoria(self.img)
    
    def negarRojo(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        elif len(self.img.shape) < 3:
            QtGui.QMessageBox.warning(None,'Error','Operacion invalida para imagenes en escala de grises.')
        else:
            self.img = Metodos.negarRojo(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
            
    
            
    def negarVerde(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        elif len(self.img.shape) < 3:
            QtGui.QMessageBox.warning(None,'Error','Operacion invalida para imagenes en escala de grises.')
        else:
            self.img = Metodos.negarVerde(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
            
    
    def negarAzul(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        elif len(self.img.shape) < 3:
            QtGui.QMessageBox.warning(None,'Error','Operacion invalida para imagenes en escala de grises.')
        else:
            self.img = Metodos.negarAzul(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)   
            
            
    
    def negarImg(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        elif len(self.img.shape) < 3:
            QtGui.QMessageBox.warning(None,'Error','Operacion invalida para imagenes en escala de grises.')
        else:
            self.img = Metodos.negarImg(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)   
            
    
    def graficarHistograma(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            Metodos.histograma(self.img)
            
        
    
    def otsuColor(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        elif len(self.img.shape) < 3:
            QtGui.QMessageBox.warning(None,'Error','Operacion invalida para imagenes en escala de grises.')
        else:
            self.img = Metodos.otsuColor(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
            
    
    def otsuGrises(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = Metodos.otsuGrises(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
            
    
    def escalaGrises(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = Metodos.escalaGrises(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
            
    
    def binario(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            opciones = Ui_Umbral.getParams()
            print opciones            
            self.img = Metodos.binarizacion(self.img, opciones)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)         
            
    
    def filtroMediana(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            tamKernel = Ui_Filtro.getParams()
            print "tam del kernel: ", tamKernel            
            self.img = Metodos.filtroMediana(self.img, tamKernel)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
    
    def filtroGauss(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            tamKernel = Ui_Filtro.getParams()
            print tamKernel            
            self.img = Metodos.fitroGauss(self.img, tamKernel)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
            
    def filtroBilateral(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            tamKernel = Ui_Filtro.getParams()
            print tamKernel            
            self.img = Metodos.filtroBilateral(self.img, tamKernel)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
    
    
    def apertura(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            opciones = Ui_morfologia.getParams()            
            self.img = Metodos.apertura(self.img, opciones)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
            
    def cerradura(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            opciones = Ui_morfologia.getParams()            
            self.img = Metodos.cerradura(self.img, opciones)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)  
            
    def dilatacion(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            opciones = Ui_morfologia.getParams()            
            self.img = Metodos.dilatacion(self.img, opciones)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
    
    def erosion(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            opciones = Ui_morfologia.getParams()            
            self.img = Metodos.erosion(self.img, opciones)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)  
    

    def transDistancia(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img,self.sure_bg = Metodos.transDistancia(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 


    def watershed(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = Metodos.watershed(self.img, self.sure_bg,self.imgOriginal)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
            

    def deteccionCirculos(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = Metodos.deteccionCirculos(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q) 
    

    
    def rellenarHoyos(self):
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = Metodos.rellenar(self.img)
            self.agregarMemoria(self.img)
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)
    
    
    
    def imageOpenCv2ToQImage (sef,cv_img):
        if len(cv_img.shape) == 3:            
            height, width, bytesPerComponent = cv_img.shape
            bytesPerLine = bytesPerComponent * width;        
            return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        else:
            height, width = cv_img.shape
            bytesPerLine = 1 * width;        
            return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_Indexed8)
        
    
    
    def agregarMemoria(self, img):
        print "agrego a memoria"
        if self.posicionDes < 10:
            print "memoria pos = ", self.posicionDes
            self.memoria[self.posicionDes]=self.img
            print self.memoria[self.posicionDes][100,100]
            self.posicionDes = self.posicionDes + 1
        else:
            self.posicionDes = 0
            print "memoria pos = ", self.posicionDes
            self.memoria[self.posicionDes]=img
            print img[100,100]
            self.posicionDes = self.posicionDes + 1
        
    
    def deshacer(self):
        print "entro al metodo deshacer"
        self.posicionDes = self.posicionDes - 1
        if self.posicionDes < 0:
            self.posicionDes = 0       
        print "memoria pos = ", self.posicionDes
        if self.imgOriginal == None:
            QtGui.QMessageBox.warning(None,'Precaución','Debe abrir una imagen para usar esta operación.')
        else:
            self.img = self.memoria[self.posicionDes]
            print "En imagen",self.img[100,100]
            print "En memoria",self.memoria[self.posicionDes][100,100]
            q = QtGui.QPixmap.fromImage(self.imageOpenCv2ToQImage(self.img))
            self.labelImagenModificada.setPixmap(q)            