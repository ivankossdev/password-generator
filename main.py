import sys
from des import *
import random
import pyperclip
# pyuic5 Pas.ui -o des.py
# pyinstaller -F -w main.py
random.seed()


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.random_generator)
        self.st = ''

    def random_generator(self):
        length = self.ui.spinBox.text()
        Character = []
        Result = []
        if self.ui.checkBox.isChecked():
            Character.extend(list('1234567890'))

        if self.ui.checkBox_2.isChecked():
            Character.extend(list('qwertyuiopasdfghjklzxcvbnm'))

        if self.ui.checkBox_3.isChecked():
            Character.extend(list('!@#$%^&*()_+'))

        if self.ui.checkBox_4.isChecked():
            Character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

        if self.ui.checkBox.isChecked() or self.ui.checkBox_2.isChecked() \
                or self.ui.checkBox_3.isChecked() or self.ui.checkBox_4.isChecked():
            for x in range(int(length)):
                Result += random.choice(Character)

        self.st = ''.join(Result)
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(self.st)

        try:
            with open("passwords.txt", "a") as file:
                file.write(f"{self.st}\n")
        except FileNotFoundError:
            pass

        pyperclip.copy(self.st)
        QtWidgets.QMessageBox.information(self, 'Сообщение', f"Пароль {self.st} скопирован")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())
