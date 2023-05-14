from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import mysql.connector
from models.User import User
import dbconnection

notas = [10, 20, 50, 100]
ui_file = "interface/tela_saque.ui"
ui_file2 = "interface/fimsaque.ui"

import dbconnection
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_saque.ui"
ui_file2 = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telasaque2.ui"

class TelaSaque(QMainWindow):
    def __init__(self, parent=None):
        super(TelaSaque, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.setWindowTitle("Tela de Saque")
        self.confirmarBtn.clicked.connect(self.processarSaque)

        self.logged_in_user_cpf = None  # Store the logged-in user's CPF

    def setLoggedInUser(self, cpf):
        self.logged_in_user_cpf = cpf

    def processarSaque(self):
        # Retrieve the logged-in user's CPF
        cpf = self.logged_in_user_cpf

        # Retrieve user data from the database
        user = self.getUserByCPF(cpf)
        if user:
            self.user = user
            self.calcularNotas()
            self.atualizarSaldo()
            self.abrirFimSaque()
        else:
            message = "Usuário não encontrado"
            QMessageBox.warning(self, "Erro", message)
            
    def getUserByCPF(self, cpf):
        try:
            conn = dbconnection.connect()
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE cpf = %s"
            values = (cpf,)
            cursor.execute(query, values)
            user_data = cursor.fetchone()
            cursor.close()
            conn.close()
            if user_data:
                # Assign the values to variables
                user_id, user_nome, user_saldo, cpf, *_ = user_data

                # Create a User object using the values
                user = User(user_id, user_nome, cpf, user_saldo)

                return user
            else:
                return None 
        except mysql.connector.Error as error:
            print("Erro conectando com o banco de dados:", error)
            return None

    def setValorInserido(self, value):
        self.valor = int(value) if value.isdigit() else 0
        print(self.valor)

    def set_valor(self, value):
        self.valor = value
        print(self.valor)

    def calcularNotas(self):
        self.setValorInserido(self.inserirValor.text())
        resto = self.user.saldo - self.valor
        self.resultado = "\n".join(f"Serão {self.valor // nota} de R${nota}" for nota in reversed(notas) if self.valor >= nota)
        self.valor %= notas[-1]

    def atualizarSaldo(self):
        try:
            conn = dbconnection.connect()
            cursor = conn.cursor()
            query = "UPDATE users SET saldo = %s WHERE cpf = %s"
            values = (self.user.saldo - self.valor, self.user.cpf)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            self.user.saldo -= self.valor
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

    def abrirFimSaque(self):
        self.fimSaque = FimSaque(self.resultado, self.user.saldo)
        self.close()
        self.fimSaque.show()

class FimSaque(QMainWindow):
    def __init__(self, resultado, saldo, parent=None):
        super(FimSaque, self).__init__(parent)
        uic.loadUi(ui_file2, self)
        self.setWindowTitle("Fim Saque")
        self.exibirValor.setText(resultado)
        self.saldoLbl.setText(str(saldo))

