from PyQt5 import uic;
import sys;
from PyQt5.QtWidgets import QApplication, QMainWindow
from saque import TelaSaque;

notas = [10,20,50,100];
ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telainicial.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_file)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    withdraw_window = TelaSaque()
   

    main_window.show()

    main_window.saqueBtn.clicked.connect(TelaSaque.show)

    sys.exit(app.exec_())