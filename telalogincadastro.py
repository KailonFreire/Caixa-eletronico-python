from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from cadastro import TelaCadastro

from login import TelaLogin

notas = [10, 20, 50, 100]
ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telalogincadastro.ui"


class TelaLoginCadastro(QMainWindow):
    def __init__(self, parent=None):
        super(TelaLoginCadastro, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.tela_cadastro = TelaCadastro(self)
        self.tela_login = TelaLogin(self)
        self.cadastrarBtn_5.clicked.connect(self.abrirCadastro)
        self.loginBtn_5.clicked.connect(self.abrirLogin)

    def abrirLogin(self):
        self.close()
        self.tela_login.show()
    
    def abrirCadastro(self):
        self.close()
        self.tela_cadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLoginCadastro()
    window.show()
    sys.exit(app.exec_())
