from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import Models.User

notas = [10, 20, 50, 100]
ui_file = "interface/tela_saque.ui"
ui_file2 = "interface/fimsaque.ui"

class TelaSaque(QMainWindow):
    def __init__(self, parent=None):
        super(TelaSaque, self).__init__(parent)
        uic.loadUi(ui_file, self)
        self.saque50.clicked.connect(lambda: self.set_valor(50))
        self.saque100.clicked.connect(lambda: self.set_valor(100))
        self.saque150.clicked.connect(lambda: self.set_valor(150))
        self.confirmarBtn.clicked.connect(self.abrirFimSaque)
        self.saldo = 2000
        self.valor = 0

    def setValorInserido(self, value):
        if value:
            try:
                self.valor = int(value).as_integer_ratio
                print(self.valor)
            except ValueError:
                print("Valor inválido")

    def set_valor(self, value):
        self.valor = value
        print(self.valor)

    def calcularNotas(self):
        if self.inserirValor.text():
            self.setValorInserido(self.inserirValor.text())
        resto = self.saldo - int(self.valor)
        resultado = ""

        for nota in reversed(notas):
            if int(self.valor) >= nota:
                quantidade_notas = int(self.valor) // nota
                resultado += f"Serão {quantidade_notas} de R${nota}\n"
                self.valor = int(self.valor) % nota

        return resultado, resto

    def abrirFimSaque(self):
        resultado, saldo_atualizado = self.calcularNotas()
        self.fimSaque = FimSaque(resultado, saldo_atualizado)
        self.close()
        self.fimSaque.show()


class FimSaque(QMainWindow):
    def __init__(self, resultado, saldo, parent=None):
        super(FimSaque, self).__init__(parent)
        uic.loadUi(ui_file2, self)
        self.setWindowTitle("Fim Saque")
        self.exibirValor.setText(resultado)
        self.saldoLbl.setText(str(saldo))


if __name__ == "__main__":
    app = QApplication([])
    window = TelaSaque()
    window.show()
    sys.exit(app.exec_())
