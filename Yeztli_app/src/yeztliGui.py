# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#compilar interface 
#python  '/usr/lib/python2.7/dist-packages/PyQt4/uic/pyuic.py' -o '/home/christian/Documentos/YEZTLI/GUIcompilado/yeztli.py' '/home/christian/Documentos/YEZTLI/gui/yeztli.ui'



from PyQt4.QtGui import QApplication, QMainWindow
from yeztli import Ui_VentanaPrincipal
    
if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_VentanaPrincipal()
    main_window.setupUi(window)
    window.show()
    app.exec_()
        
