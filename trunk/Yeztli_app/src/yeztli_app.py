# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk #sudo apt-get install python-imaging-tk
import tkFileDialog
import cv2
import numpy as np

class Yeztli_app(tk.Frame):
    #la aplicacion deriva de tkinter es por eso que tenemos que llamar al
    #constructor de tkinter
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        #inicializar Tkinter: metodo donde van todos los widgets
        self.inicialize()

    def inicialize(self):
        self.parent.title("Yeztli: sistema de deteccion de anomalias en eritrocitos")
        self.pack(fill = tk.BOTH, expand = 1)
        self.grid()
        
        self.label1 = tk.Label(self,border=20)
        self.label1.grid(row = 1, column = 1)
        
        
        
        barraMenu = Menu(self)
        menuArchivo = Menu(barraMenu)
        menuArchivo.add_command(label="Abrir", command=self.abrirImagen)
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=self.destroy)
        barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
        self.parent.config(menu=barraMenu)
        
        #label para la imagen
#        self.rutaImg = self.abrirImagen()        
#        print self.rutaImg
#        self.img = Image.open(self.rutaImg)
#        self.resized = self.img.resize((400, 300),Image.ANTIALIAS)
#        self.img1 = ImageTk.PhotoImage(self.resized,size=(200,200))        
#        panel = Label(self, image = self.img1)
#        panel.pack(side='top', fill='both', expand='yes')
#        panel.img = self.img1
#        panel.grid(column=0, row=0)      
#       
#        
#        self.entryVariable = Tkinter.StringVar()
#        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
#        self.entry.grid(column=0, row=0, sticky='EW')
#        self.entry.bind("<Return>", self.OnPressEnter)
#        exDiano = Tkinter.Button(self, text="Examinar dianositos", command=self.OnButtonClick)
#        exDiano.grid(column=1, row=0, sticky='EW')
#        
#        self.variable = Tkinter.StringVar()
#        label = Tkinter.Label(self,textvariable=self.variable ,anchor="w",fg="white", bg="blue")
#        label.grid(column=0, row=1, columnspan=2, sticky='EW')        
#        self.variable.set(u"Hola!")
#        
#        self.grid_columnconfigure(0,weight=1)
#        self.resizable(True,False)
        
    def OnButtonClick(self):
        self.variable.set(self.entryVariable.get() + "presionaste el boton")
    
    def OnPressEnter(self,event):
        self.variable.set(self.entryVariable.get() + "presionaste enter!")
    
    def setImg(self):
       self.img = Image.open(self.rutaImg)
       self.I = np.asarray(self.img)
       alto,ancho = self.img.size
       text = str(2*alto+100)+"x"+str(ancho+50)+"+0+0"
       print "variable text: ",text
       self.parent.geometry(text)
       self.resImg = self.img.resize((500, 400),Image.ANTIALIAS)
       imagen = ImageTk.PhotoImage(self.resImg)
       self.label1.configure(image=imagen)
       self.label1.image = imagen
        
    
    
    def abrirImagen(self):
       #Open Callback
        ftypes = [('Image Files', '*.TIF *.jpg *.png')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        self.rutaImg = filename
        #print self.fn #prints filename with path here
        self.setImg()
    
   
        
        
        


#ventana = Tk()
#ventana.geometry("600x600")
#ventana.title("Yeztli")


##se crea el objeto para las operaciones de la ventana
#opVen = OpVentana()

################## barra menu #################
##se crea la barra del menu
#barraMenu = Menu(ventana)

##se crean los menus
#menuArchivo = Menu(barraMenu)

##crear los comandos de los menus
#menuArchivo.add_command(label="Abrir", command=opVen.abrirImagen)
#menuArchivo.add_command(label="Nuevo analisis")
#menuArchivo.add_command(label="Guardar")
#menuArchivo.add_separator()
#menuArchivo.add_command(label="Salir", command=ventana.destroy)

##agregar los menus a la barra de menus
#barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

##agregar a barra de menu a la ventana
#ventana.config(menu=barraMenu)

################## creacion de frames #################
#derFrame = Frame(ventana, bg="red")
#derFrame.pack(side=LEFT)
#izqFrame = Frame(ventana, bg="blue")
#izqFrame.pack(side=RIGHT)

#uno = Label(derFrame, text="One", fg="white", bg="green")
#uno.pack(fill=Y)
#dos = Label(izqFrame, text="two", fg="white", bg="purple")
#dos.pack(fill=Y)


#ventana.mainloop()






