from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from cadastro import TelaCadastro
import database

ui_file = "interface/tela_login.ui"

class TelaLogin(QMainWindow):
    registerSignalLogin = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TelaLogin, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Tela de Login")
        self.loginBtn.clicked.connect(self.authenticate_login)
        self.cadastrarBtn.clicked.connect(self.openTelaCadastro)
        self.tela_cadastro = TelaCadastro(self)

    def authenticate_login(self):
        cpf = self.inserirCPF.text()
        senha = self.inserirSenha.text()

        if cpf and senha:
            db = database.createConnection()
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE cpf = %s AND senha = %s"
            values = (cpf, senha)
            cursor.execute(sql, values)
            result = cursor.fetchone()

            if result:
                self.close()  
                self.registerSignalLogin.emit(cpf) 
            else:
                message = "CPF ou senha incorretos"
                QMessageBox.warning(self, "Erro de Login", message)
        else:
            message = "Por favor, preencha todos os campos"
            QMessageBox.warning(self, "Erro de Login", message)

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()
