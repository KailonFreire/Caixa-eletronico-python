import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cadastro import TelaCadastro
from login import TelaLogin
from saque import TelaSaque

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telainicial.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_file)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tela_saque = TelaSaque(self)
        self.tela_cadastro = TelaCadastro(self)
        self.tela_login = TelaLogin(self)
        self.saqueBtn.clicked.connect(self.openTelaSaque)
        self.cadastroBtn.clicked.connect(self.openTelaCadastro)

        self.tela_cadastro.registerSignal.connect(self.openMainWindow)

    def openTelaSaque(self):
        self.hide()
        self.openTelaLogin()
        if self.tela_login.authenticate_login():  # Use the correct method name 'authenticate_login'
            self.tela_saque.show()
        else:
            self.show()

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()

    def openTelaLogin(self):
        self.hide()
        self.tela_login.show()

    def openMainWindow(self):
        self.tela_cadastro.close()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
