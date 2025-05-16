from PyQt6 import QtWidgets, uic
from pin_eingabe import PinEingabe
import sys

class Sperrbildschirm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("sperrbildschirm.ui", self) 
        self.pinButton.clicked.connect(self.zeige_pin_eingabe) #Zugriff auf sperrbildschirm.ui datei

    def zeige_pin_eingabe(self):
        self.pin_screen = PinEingabe()
        self.setCentralWidget(self.pin_screen) #Zugriff auf pin_eingabe.ui datei

app = QtWidgets.QApplication(sys.argv)
window = Sperrbildschirm()
window.show()
sys.exit(app.exec())