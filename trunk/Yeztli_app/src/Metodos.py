# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
from matplotlib import pyplot as plt
from PyQt4 import QtGui
import numpy as np
from pylab import *
from scipy.ndimage import measurements
#from skimage import morphology




#funcion para abrir una imagen
def abrirImagen(ruta):
    img = cv2.imread(ruta)
    return img

#funcion que niega el canal rojo de una imagen
def negarRojo(img):
    print 'negar el canal rojo'
    img[:,:,0] = 255 - img[:,:,0]
    return img

#funcion que niega el canal verde de una imagen
def negarVerde(img):
    print 'negar el canal verde'
    img[:,:,1] = 255 - img[:,:,1]
    return img

#funcion que niega el canal azul de una imagen
def negarAzul(img):
    print 'negar el canal azul'
    img[:,:,2] = 255-img[:,:,2]
    return img

#funcion que niega los tres canales de la imagen
def negarImg(img):
    print "negar imagen completa"
    img[:,:,0] = 255 - img[:,:,0]
    img[:,:,1] = 255 - img[:,:,1]
    img[:,:,2] = 255 - img[:,:,2]
    return img

# funcion que grafica el histograma de una imagen RGB o en escala de grises
# calcHist: @primer parametro: imagen para calcular el histograma
# @segundo parametro: Es el indice de canal para el que se calcula el histograma
# Por ejemplo, si la entrada es una imagen en escala de grises, su valor es [0]
# Imagen en color, puedes pasar [0], [1] o [2] para calcular el histograma de 
# canal azul, verde o rojo, respectivamente.
# @tercer parametro: mascara de la imagen, por si desea encontrar el histograma
# de una region determinada de la imagen
# @cuarto parametro: representa nuestra cuenta BIN. Necesidad de ser dado en 
# corchetes. Para la escala completa, pasamos [256].
# @quinto parametro: rango de valores del eje x
def histograma(img):
    imgTipo = len(img.shape)
    if imgTipo == 3: 
        print "hisrograma imagen de color"
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [1, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
    else:
         print "histograma imagen escala de grises"
         histr = cv2.calcHist([img], [0], None, [256], [1, 256])
         plt.plot(histr, color='gray')
         plt.xlim([0, 256])
        
    plt.show()


# En una imagen bimodal (imagen que su histograma tiene dos picos) se calcula
# automaticamente el valor del umbral, que se encontrara en medio de estos dos 
# picos, la binarizacion otsu calcula este umbral optimo y realiza la binarizacion
# la funcion encuentra el valor optimo del umbral para los tres canales y los
# junta de nuevo en una imagen 
# funcion cv2.threshold
# @primer argumento: imagen origen
# @segundo argumento: valor del umbral que se usa para clasificar, 
# se pone 0 para discriminar ya que otsu lo calculara automaticamente
# @tercer parametro: valor maximo al que se ira si el valor del pixel es mayor al umbral
# @cuarto parametro: indica el tipo de umbral
def otsuColor(img):
    #aplicamos un filtro gausssiano 
    #imgBlur = cv2.GaussianBlur(img,(5,5),0)     
   
    umbR,imgR = cv2.threshold(img[:,:,0],0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    umbG,imgG = cv2.threshold(img[:,:,1],0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    umbB,imgB = cv2.threshold(img[:,:,2],0,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    print "otsu color: umbrales optimos R=",umbR,", G=",umbG,", B=",umbB
    img[:,:,0]= imgR
    img[:,:,1]= imgG
    img[:,:,2]= imgB   
    return img

# aplica una binarizacion de otsu para una imagen en escala de grises 
# @primer argumento: imagen origen
# @segundo argumento: valor del umbral que se usa para clasificar, 
# se pone 0 para discriminar ya que otsu lo calculara automaticamente
# @tercer parametro: valor maximo al que se ira si el valor del pixel es mayor al umbral
# @cuarto parametro: indica el tipo de umbral
def otsuGrises(img):
    #aplicamos un filtro gausssiano 
    #imgBlur = cv2.GaussianBlur(img,(5,5),0) 
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       
    umb,imgGris = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)    
    print "otsu Grises: umbral optimo=",umb    
    return imgGris

#funcion para convertir imagen RGB a escala de grises
def escalaGrises(img):    
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       
    print "escala de Grises"
    return img


#funcion que realiza algun tipo de binarizacion en una imagen dependiendo de la 
# tupla enviada en el segundo parametro
def binarizacion(img,opciones):
    if opciones[0] > 255:
        QtGui.QMessageBox.warning(None,'Precaucion','Valor de umbral no valido')
        return img
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        
    if opciones[1] == 1:
        ret,img = cv2.threshold(img,opciones[0],255,cv2.THRESH_BINARY)
        print "binarizacion binaria"
    elif opciones[1] == 2:
        ret,img = cv2.threshold(img,opciones[0],255,cv2.THRESH_BINARY_INV)
        print "binarizacion binaria inversa"
    elif opciones[1] == 3:
        ret,img = cv2.threshold(img,opciones[0],255,cv2.THRESH_TRUNC)
        print "binarizacion trunca"
    elif opciones[1] == 4:
        ret,img = cv2.threshold(img,opciones[0],255,cv2.THRESH_TOZERO)
        print "binarizacion to zero"
    elif opciones[1] == 5:
        ret,img = cv2.threshold(img,opciones[0],255,cv2.THRESH_TOZERO_INV)
        print "binarizacion to zero inversa"
    return img


def filtroMediana(img,tamKernel):
    imgBlur = cv2.medianBlur(img,tamKernel)     
    print "filtro mediana con tam kernel ", tamKernel
    return imgBlur

def fitroGauss(img,tamKernel):
    imgBlur = cv2.GaussianBlur(img,(tamKernel,tamKernel),0)   
    print "filtro gaussiano con tam kernel ", tamKernel
    return imgBlur

def filtroBilateral(img,tamKernel):
    imgBlur = cv2.bilateralFilter(img,tamKernel,75,75)   
    print "filtro bilateral con tam kernel ", tamKernel
    return imgBlur
    


def apertura(img,opciones):
    #imagen a color
    if len(img.shape) == 3:            
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_OPEN, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_OPEN, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_OPEN, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_OPEN, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_OPEN, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_OPEN, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_OPEN, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_OPEN, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_OPEN, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB    
    #imagen en escala de grises
    else:
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)            
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    print "apertura con kernel tam ", opciones[0]    
    return img    


def cerradura(img,opciones):
    #imagen a color
    if len(img.shape) == 3:            
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_CLOSE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_CLOSE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_CLOSE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_CLOSE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_CLOSE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_CLOSE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_CLOSE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_CLOSE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_CLOSE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB    
    #imagen en escala de grises
    else:
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)            
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    print "cerradura con kernel tam ", opciones[0]    
    return img    

def dilatacion(img,opciones):
    #imagen a color
    if len(img.shape) == 3:            
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_DILATE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_DILATE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_DILATE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_DILATE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_DILATE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_DILATE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_DILATE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_DILATE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_DILATE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB    
    #imagen en escala de grises
    else:
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)            
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
    print "dilatacion con kernel tam ", opciones[0]
    return img


def erosion(img,opciones):
    #imagen a color
    if len(img.shape) == 3:            
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_ERODE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_ERODE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_ERODE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_ERODE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_ERODE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_ERODE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            closR = cv2.morphologyEx(img[:, :, 0], cv2.MORPH_ERODE, kernel)
            closG = cv2.morphologyEx(img[:, :, 1], cv2.MORPH_ERODE, kernel)
            closB = cv2.morphologyEx(img[:, :, 2], cv2.MORPH_ERODE, kernel)
            img[:, :, 0] = closR
            img[:, :, 1] = closG
            img[:, :, 2] = closB    
    #imagen en escala de grises
    else:
        if opciones[1] == 1:
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)            
        elif opciones[1] == 2:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
        elif opciones[1] == 3:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opciones[0], opciones[0]))
            img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
    print "Erosion con kernel tam ", opciones[0]
    return img


def transDistancia(img):
    #aplicamos un filtro gausssiano 
    #imgBlur = cv2.GaussianBlur(img,(5,5),0) 
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print "convirtio la imagen a grises"

    #binarizacion de otsu
    ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)   
    
    
    # removiendo ruido
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)    
    
    #area segura 
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    
    #transformada de la distancia
    dist_transform = cv2.distanceTransform(opening,cv2.cv.CV_DIST_L2,3)
    imshow(dist_transform)
    show()
    
    img = np.uint8(dist_transform)   
    print "Transformada de distancia"    
    return img,sure_bg


def rellenar(img):
    print "rellenar hoyos"
    des = cv2.bitwise_not(img)
    imshow(des)
    show()
    contour,hier = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    tam = hier[0][-1][3]
    print tam
    for i in range(tam):
        cv2.drawContours(des,[contour[i]],0,255,-1)
    #gray2 = cv2.bitwise_not(des)
    grayf=cv2.bitwise_or(des,img)
    imshow(grayf)
    show()
    return grayf


def watershed(img,sure_bg,original):
    #aplicamos un filtro gausssiano 
    #imgBlur = cv2.GaussianBlur(img,(5,5),0) 
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print "convirtio la imagen a grises"
      
    #saca el area mas lejos del centro de los objetos
    ret, sure_fg = cv2.threshold(img,0.7*img.max(),255,0)
    imshow(sure_fg)
    show()
    
  
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    imshow(unknown)
    show()     
    
    # Marker labelling
    ret, markers = measurements.label(sure_fg)
    
    ret = recorrerLabels(ret,markers)   

    imshow(ret)
    show()  
    
    ret[unknown==255] = 0
    
    imshow(ret)
    show()      
     
    
    cv2.watershed(original,ret)
    original[ret == -1] = [0,0,255]
    
    imshow(ret)
    show()
    
    imshow(original)
    show()
    
    return original



def deteccionCirculos(img):
    cimg = img
    if len(img.shape) == 3:            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print "convirtio la imagen a grises"
    
    circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
    param1=50,param2=30,minRadius=20,maxRadius=70)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    return cimg
    


def recorrerLabels(img,numLabels):
    imgAux = img
    print "num etiquetas ", numLabels
    print type(img)
    tam = img.shape
    print tam
    for x in range(tam[0]):
            for y in range(tam[1]):
                img[x,y] = img[x,y] + 1

    
    return imgAux
    