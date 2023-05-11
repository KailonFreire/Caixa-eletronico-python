import database
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import TelaLogin
from saque import TelaSaque
from cadastro import TelaCadastro
from telalogincadastro import TelaLoginCadastro

ui_file = "interface/telainicial.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_file)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)

        self.tela_saque = TelaSaque(self)
        self.tela_cadastro = TelaCadastro(self)
        self.tela_login = TelaLogin(self)
        self.tela_LoginCadastro = TelaLoginCadastro(self)

        self.saqueBtn.clicked.connect(self.openTelaSaque)
        self.cadastroBtn.clicked.connect(self.openTelaCadastro)
        self.tela_cadastro.registerSignalCadastro.connect(self.openMainWindowWithCPFCadastro)
        self.tela_login.registerSignalLogin.connect(self.openMainWindowWithCPFLogin)

        self.tela_LoginCadastro.show()

    def openTelaSaque(self, saldo):
        self.hide()
        self.tela_saque.saldo = saldo
        self.tela_saque.show()

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()

        
    def openMainWindowWithCPFCadastro(self, cpf):
        self.tela_cadastro.close()
        self.show()
    
    def openMainWindowWithCPFLogin(self, cpf):
        self.tela_login.close()
        self.show()


if __name__ == "__main__":
    database.start()
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()
