# from PyQt5 import uic
# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtWidgets import QMainWindow, QMessageBox
# import dbconnection

# ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/telacadastro.ui"


# class TelaCadastro(QMainWindow):
#     registerSignalCadastro = pyqtSignal(str)

#     def __init__(self, parent=None):
#         super(TelaCadastro, self).__init__(parent)
#         uic.loadUi(ui_file, self)
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
