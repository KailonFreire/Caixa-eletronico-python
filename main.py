import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import TelaLogin
from saque import TelaSaque
from cadastro import TelaCadastro

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telainicial.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_file)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tela_saque = TelaSaque(self)
        self.tela_cadastro = TelaCadastro(self)
        self.saqueBtn.clicked.connect(self.openTelaSaque)
        self.cadastroBtn.clicked.connect(self.openTelaCadastro)
        self.tela_cadastro.registerSignal.connect(self.openMainWindowWithCPF)
   # Connect to the updated slot
        self.tela_login = TelaLogin(self)
        self.tela_login.registerSignal.connect(self.openMainWindow)

        # Create and show the TelaLogin instance
        self.tela_login.show()

    def openTelaSaque(self, saldo):
        self.hide()
        self.tela_saque.saldo = saldo
        self.tela_saque.show()

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()

    def openMainWindow(self):
        self.tela_login.close()
        self.show()
        
    def openMainWindowWithCPF(self, cpf):
        self.tela_login.close()
        self.show()
        # Use the CPF value as needed
        print("CPF:", cpf)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
