import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import dbconnection

ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_login.ui"

class TelaLogin(QMainWindow):
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
                message = "Login successful!"
                QMessageBox.information(self, "Success", message)
                self.close()
                # Open the main window or perform other operations
            else:
                message = "Invalid CPF or senha. Please try again."
                QMessageBox.warning(self, "Login Error", message)
        else:
            message = "Please enter CPF and senha."
            QMessageBox.warning(self, "Login Error", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec_())
