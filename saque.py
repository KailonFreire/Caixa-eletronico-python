from PyQt5 import uic;
import sys;
from PyQt5.QtWidgets import QApplication, QMainWindow;

notas = [10,20,50,100];
ui_file = "C:/Users/kaiki/Desktop/Coding/projetopython/interface/tela_saque.ui"
Ui_MainWindow, _ = uic.loadUiType(ui_file)

class TelaSaque(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TelaSaque, self).__init__()
        self.setupUi(self)

        self.saque20.clicked.connect(lambda: self.set_valor(20))
        self.saque50.clicked.connect(lambda: self.set_valor(50))
        self.saque100.clicked.connect(lambda: self.set_valor(100))
        self.saque150.clicked.connect(lambda: self.set_valor(150))
         
        self.confirmarBtn.clicked.connect(self.calcularNotas)

        self.saldo = 2000
        self.notas = [10, 20, 50, 100]
        self.valor = 0

    def setValorInserido(self, value):
        if self.inserirValor.text() is not None:
            self.set_valor(self.inserirValor.text())


    def set_valor(self, value):
        try:
            self.valor = int(value)
            print(self.valor)
        except ValueError:
            print("deu probrema");
            
    def calcularNotas(self):
        resto = self.valor
        resultado = []

        for nota in self.notas[::-1]:
            quantidade_notas = resto // nota
            resto = resto % nota

            if quantidade_notas > 0:
                resultado.append((quantidade_notas, nota))

        
            print(f"Serão {quantidade_notas} notas de {nota}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaSaque()
    window.show()
    sys.exit(app.exec_())
