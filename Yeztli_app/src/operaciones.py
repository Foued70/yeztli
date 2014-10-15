# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

import Tkinter
import tkFileDialog
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import *
from pylab import *
from scipy.ndimage import measurements,morphology


class FileChooser:

    #constructor
    def __init__(self):
        print("se creo el objeto")

    #metodo para abrir imagen
    def abrirImagen(self):
        root = Tkinter.Tk()
        root.withdraw()
        file_path = tkFileDialog.askopenfilename()
        return file_path

    #metodo para graficar histograma
    def histograma(self, img):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [1, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.show()

    def ecualizarHistColor(self, img):
        eqb = cv2.equalizeHist(img[:, :, 0])
        eqg = cv2.equalizeHist(img[:, :, 1])
        eqr = cv2.equalizeHist(img[:, :, 2])
        img[:, :, 0] = eqb
        img[:, :, 1] = eqg
        img[:, :, 2] = eqr
        return img

    def metodoOtsuColor(self, img):
        umB, otsuB = cv2.threshold(img[:, :, 0], 0, 50, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
        umG, otsuG = cv2.threshold(img[:, :, 1], 0, 50, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
        umR, otsuR = cv2.threshold(img[:, :, 2], 0, 50, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
        img[:, :, 0] = otsuB
        img[:, :, 1] = otsuG
        img[:, :, 2] = otsuR
        return img

    def cerraduraElipColor(self, img, valor):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (valor, valor))
        closB = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_CLOSE, kernel)
        closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_CLOSE, kernel)
        closR = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_CLOSE, kernel)
        img[:, :, 0] = closB
        img[:, :, 1] = closG
        img[:, :, 2] = closR
        return img

    def erosionElipColor(self, img, valor):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (valor, valor))
        closB = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_ERODE, kernel)
        closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_ERODE, kernel)
        closR = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_ERODE, kernel)
        img[:, :, 0] = closB
        img[:, :, 1] = closG
        img[:, :, 2] = closR
        return img

    def diltacionElipColor(self, img, valor):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (valor, valor))
        closB = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_DILATE, kernel)
        closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_DILATE, kernel)
        closR = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_DILATE, kernel)
        img[:, :, 0] = closB
        img[:, :, 1] = closG
        img[:, :, 2] = closR
        return img

    def aperturaElipColor(self, img, valor):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (valor, valor))
        closB = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_OPEN, kernel)
        closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_OPEN, kernel)
        closR = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_OPEN, kernel)
        img[:, :, 0] = closB
        img[:, :, 1] = closG
        img[:, :, 2] = closR
        return img

    def dianositos(self, img):
        img = self.metodoOtsuColor(img)
        img = self.ecualizarHistColor(img)
        img = cv2.medianBlur(img, 9)
        return img

    def labelingObj(self, img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        img = 1 * (img < 255)
        labels, nbr_objects = measurements.label(img)
        print "Number of objects:", nbr_objects
        print labels
        print type(labels)
        return [uint8(labels), nbr_objects]

    def areasObjetos(self, img, numObj):
        lista = [0] * (numObj + 1)
        print len(lista)
        tam = img.shape
        print tam
        for x in range(tam[0]):
            for y in range(tam[1]):
                posicion = img[x][y]
                lista[posicion] = lista[posicion] + 1
        return lista

    def desviacion(self, arreglo):
        tam = len(arreglo)
        suma = 0.0
        for x in range(1, tam):
            suma = suma + arreglo[x]
        media = suma / (tam - 1)
        suma = 0
        for x in range(1, len(arreglo)):
            suma = suma + ((arreglo[x] - media)) ** 2
        desv = sqrt(suma / (len(arreglo) - 2))
        maximo = int(max(arreglo[1:]))
        minimo = int(min(arreglo[1:]))
        valores = (media, desv, maximo, minimo)
        return valores

    def eliminaObjGauss(self, img, areas):
        desv = self.desviacion(areas)
        aux = desv[0] - desv[1]*0.8
        aux2 = desv[0] + desv[1]*0.8
        print aux, aux2
        tam = img.shape
        print tam
        for x in range(tam[0]):
            for y in range(tam[1]):
                posicion = img[x][y]
                if (areas[posicion] < aux ) or (areas[posicion] > aux2 ):
                    img[x][y]=0
        return img

    def eliminaObjOrillas(self, img):
        tam = img.shape
        alto = tam[0]
        ancho = tam[1]
        lista = []
        for x in range(ancho):
            if (img[0][x] != 0) and ((img[0][x] in lista) == False):
                lista.append(img[0][x])
            if (img[alto - 1][x] != 0) and ((img[alto - 1][x] in lista) == False):
                lista.append(img[alto -1][x])
        for x in range(alto):
            if (img[x][0] != 0) and ((img[x][0] in lista) == False):
                lista.append(img[x][0])
            if (img[x][ancho - 1] != 0) and ((img[x][ancho - 1] in lista) == False):
                lista.append(img[x][ancho - 1])
        for x in range(alto):
            for y in range(ancho):
                valor = img[x][y]
                if (valor in lista) == True:
                    img[x][y] = 0
        return img