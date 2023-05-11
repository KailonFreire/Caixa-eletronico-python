from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
import dbconnection

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_login.ui"
# ui_file2 = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telacadastro.ui"

class TelaLogin(QMainWindow):
    registerSignalLogin = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TelaLogin, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Tela de Login")
        self.loginBtn.clicked.connect(self.authenticate_login)
        # self.cadastrarBtn.clicked.connect(self.openTelaCadastro)
        # self.tela_cadastro = TelaCadastro(self)
        # self.tela_login = TelaLogin(self)  # Add this line

        # self.tela_login.registerSignalLogin.connect(self.openMainWindowWithCPFLogin)

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
                self.registerSignalLogin.emit(cpf)  # Pass the CPF to the main window
            else:
                message = "CPF ou senha incorretos"
                QMessageBox.warning(self, "Erro de Login", message)
        else:
            message = "Por favor, preencha todos os campos"
            QMessageBox.warning(self, "Erro de Login", message)

    def openTelaCadastro(self):
        self.hide()
        self.tela_cadastro.show()

# class TelaCadastro(QMainWindow):
#     registerSignalCadastro = pyqtSignal(str)

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
#            if nome and cpf and endereco and senha and saldo:
#             # Connect to the database
#             db = dbconnection.connect()

#             # Insert user data into the database
#             cursor = db.cursor()
#             sql = "INSERT INTO users (nome, cpf, endereco, senha, saldo) VALUES (%s, %s, %s, %s, %s)"
#             values = (nome, cpf, endereco, senha, saldo)
#             cursor.execute(sql, values)
#             db.commit()
#             db.close()

#             message = "Cadastro completo!"
#             QMessageBox.information(self, "Sucesso", message)
#             self.registerSignalCadastro.emit(cpf)  # Emit the signal with the CPF value  message = "Cadastro completo!"
#         else:
#             message = "Por favor, preencha todos os campos"
#             QMessageBox.warning(self, "Erro", message)
