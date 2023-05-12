import dbconnection
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cadastro import TelaCadastro

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_login.ui"

class TelaLogin(QMainWindow):
    def __init__(self, parent=None):
        super(TelaLogin, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Tela de Login")
        self.loginBtn.clicked.connect(self.authenticate_login)
        self.cadastrarBtn.clicked.connect(self.openTelaCadastro)
        self.tela_cadastro = TelaCadastro(self)
        self.loginCallback = None

    def setLoginCallback(self, callback):
        self.loginCallback = callback
        print(self.loginCallback)

    def authenticate_login(self):
        cpf = self.inserirCPF.text()
        senha = self.inserirSenha.text()

        if cpf and senha:
            db = dbconnection.connect()
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE cpf = %s AND senha = %s"
            values = (cpf, senha)
            cursor.execute(sql, values)
            result = cursor.fetchone()

            if result:
                self.close()  # Close the login window
                if self.loginCallback:
                    self.loginCallback(cpf)  # Invoke the callback function with the CPF
            else:
                message = "CPF ou senha incorretos"
                QMessageBox.warning(self, "Erro de Login", message)
        else:
            message = "Por favor, preencha todos os campos"
            QMessageBox.warning(self, "Erro de Login", message)

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()
        

# ui_file2 = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telacadastro.ui"

import dbconnection
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

ui_file2 = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telacadastro.ui"

# class TelaCadastro(QMainWindow):
#     def __init__(self, parent=None):
#         super(TelaCadastro, self).__init__(parent)
#         uic.loadUi(ui_file2, self)
#         self.setWindowTitle("Tela de Cadastro")
#         self.confirmarBtn_4.clicked.connect(self.register_user)

#     def register_user(self):
#         nome = self.inserirNome.text()
#         cpf = self.inserirCPF.text()
#         endereco = self.inserirEndereco.text()
#         senha = self.inserirSenha.text()
#         saldo = self.inserirSaldo.text()

#         if nome and cpf and endereco and senha and saldo:
#             db = dbconnection.connect()
#             cursor = db.cursor()
#             sql = "INSERT INTO users (nome, cpf, endereco, senha, saldo) VALUES (%s, %s, %s, %s, %s)"
#             values = (nome, cpf, endereco, senha, saldo)
#             cursor.execute(sql, values)
#             db.commit()
#             db.close()

#             message = "Cadastro completo!"
#             QMessageBox.information(self, "Sucesso", message)
#             self.close()  # Close the cadastro window

#             # Get a reference to the main window
#             main_window = self.parent()
#             if main_window:
#                 main_window.openMainWindowWithCPFCadastro(cpf)  # Call the function in the main window
#         else:
#             message = "Por favor, preencha todos os campos"
#             QMessageBox.warning(self, "Erro", message)
