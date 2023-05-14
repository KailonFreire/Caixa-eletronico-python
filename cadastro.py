import dbconnection
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

ui_file2 = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telacadastro.ui"

class TelaCadastro(QMainWindow):
    def __init__(self, parent=None):
        super(TelaCadastro, self).__init__(parent)
        uic.loadUi(ui_file2, self)
        self.setWindowTitle("Tela de Cadastro")
        self.confirmarBtn_4.clicked.connect(self.register_user)

    def register_user(self):
        nome = self.inserirNome.text()
        cpf = self.inserirCPF.text()
        endereco = self.inserirEndereco.text()
        senha = self.inserirSenha.text()
        saldo = self.inserirSaldo.text()

        if nome and cpf and endereco and senha and saldo:
            db = dbconnection.connect()
            cursor = db.cursor()

            # Check if CPF already exists
            sql_select = "SELECT * FROM users WHERE cpf = %s"
            cursor.execute(sql_select, (cpf,))
            result = cursor.fetchone()

            if result:
                db.close()
                message = "CPF já cadastrado"
                QMessageBox.warning(self, "Erro", message)
                return

            # Insert user data into the database
            sql_insert = "INSERT INTO users (nome, cpf, endereco, senha, saldo) VALUES (%s, %s, %s, %s, %s)"
            values = (nome, cpf, endereco, senha, saldo)
            cursor.execute(sql_insert, values)
            db.commit()
            db.close()

            message = "Cadastro completo!"
            QMessageBox.information(self, "Sucesso", message)
            self.close()  # Close the cadastro window

            main_window = self.parent().parent()  # Access parent's parent (MainWindow)
            if main_window:
                main_window.openMainWindowWithCPFCadastro(cpf)  # Call the function in the main window
        else:
            message = "Por favor, preencha todos os campos"
            QMessageBox.warning(self, "Erro", message)
