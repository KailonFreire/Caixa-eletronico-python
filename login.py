from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import dbconnection

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_login.ui"


class TelaLogin(QMainWindow):
    registerSignal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(TelaLogin, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Tela de Login")
        self.loginBtn.clicked.connect(self.authenticate_login)

    def authenticate_login(self):
        cpf = self.inserirCPF.text()
        senha = self.inserirSenha.text()

        if cpf and senha:
            # Connect to the database
            db = dbconnection.connect()

            # Perform login verification
            cursor = db.cursor()
            sql = "SELECT * FROM users WHERE cpf = %s AND senha = %s"
            values = (cpf, senha)
            cursor.execute(sql, values)
            result = cursor.fetchone()

            db.close()

            if result:
                username = result[1]  # Assuming the username is in the second column
                saldo = result[5]  # Assuming the saldo is in the sixth column

                message = "Login realizado!"
                QMessageBox.information(self, "Success", message)
                self.registerSignal.emit({"username": username, "saldo": saldo})
            else:
                message = "CPF ou senha inválidos. Por favor tente novamente."
                QMessageBox.warning(self, "Login Error", message)
        else:
            message = "Por favor insira CPF e senha."
            QMessageBox.warning(self, "Login Error", message)
