from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QFont

class PinEingabe(QtWidgets.QMainWindow):
    def __init__(self, correct_pin="1234"): #WICHTIG: PIN musst noch festgelegt werden
        super().__init__()
        uic.loadUi("pin_eingabe.ui", self) 
        self.pin = ""
        self.correct_pin = correct_pin

        # Alle Ziffern-Buttons verbinden
        for i in range(10):
            getattr(self, f"btn{i}").clicked.connect(lambda _, x=i: self.add_digit(str(x)))

        self.btnBack.clicked.connect(self.remove_digit) #Lösch Button
        self.btnOk.clicked.connect(self.validate_pin) #OK Button

    #Eingabe der Pinziffern
    def add_digit(self, digit):
        if len(self.pin) < 4:
            self.pin += digit
            self.update_dots()

    #Löschen der Pinziffern
    def remove_digit(self):
        self.pin = self.pin[:-1]
        self.update_dots()

    #Umwandlung des Bereichs der Pineingabe, wenn einen Ziffer eingeben wird
    def update_dots(self):
        for i in range(1, 5):
            dot = getattr(self, f"pinDot{i}")
            if i <= len(self.pin):
                dot.setText("●")
            else:
                dot.setText("○")

    #Validierung des PINs
    def validate_pin(self):
        if self.pin == self.correct_pin:
            print("✔️ Richtige PIN – weiter zur Karte")
            
        else:
            self.errorLabel.setText("❌ Falsche PIN")
            self.pin = ""
            self.update_dots()
            
#Test
if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     window = PinEingabe()
     window.show()
     sys.exit(app.exec())        