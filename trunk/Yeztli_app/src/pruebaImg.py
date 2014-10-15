# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-
import cv2
from vista.ventana import CrearVentana
import sys
from scipy.ndimage import measurements,morphology
import numpy as np
from PIL import *
from pylab import *
from Tkinter import *

ventana = CrearVentana(Tk())





#################
#def cerrarVentana():
    #cv2.destroyAllWindows()
    #sys.exit()

#operacion = FileChooser()
#ruta = operacion.abrirImagen()
#print(ruta)
#imagen = cv2.imread(ruta)
##imagen original
#img = cv2.resize(imagen, (800, 600))
#cv2.imshow('original', img)
#cv2.waitKey(0)
#dian = operacion.dianositos(img)
#cv2.imshow('dian', dian)
#cv2.waitKey(0)
#img,numObj = operacion.labelingObj(dian)
#cv2.imshow('etiquetado', img)
#cv2.waitKey(0)
#print 'numero de objetos', numObj
#areas = operacion.areasObjetos(img,numObj)
#print areas
#img = operacion.eliminaObjGauss(img, areas)
#cv2.imshow('correjida', img)
#cv2.waitKey(0)
#img = operacion.eliminaObjOrillas(img)
#cv2.imshow('quitando bordes', img)
#cv2.waitKey(0)
#imshow(img)
#show()

####################

#imagen otsu
#img = operacion.metodoOtsuColor(img)
#cv2.imshow('otsu', img)
#cv2.waitKey(0)
#imagen filtro medio
#img = cv2.medianBlur(img, 7)
#cv2.imshow('filtro med', img)
#cv2.waitKey(0)
##imagen cerradura
#img = operacion.cerraduraElipColor(img, 7)
#cv2.imshow('cerradura', img)
#cv2.waitKey(0)
##imagen erosion
#img = operacion.erosionElipColor(img, 7)
#cv2.imshow('erosion', img)
#cv2.waitKey(0)
##imagen grises y binarizada
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.GaussianBlur(img, (5, 5), 0)
#ret3, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow('filtro bin', img)
#cv2.waitKey(0)



k = cv2.waitKey(0)
if k == 27:
    cerrarVentana()
elif k == ord('s'):
    cv2.imwrite('/home/christian/Escritorio/pruebasTT/imagenPrueba.jpg')
    cerrarVentana()

