# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from yeztli_app import Yeztli_app
import Tkinter as tk

if __name__ == "__main__":
    ventana = tk.Tk()
    Yeztli_app(ventana)    
    ventana.geometry("800x600")
    ventana.mainloop()
