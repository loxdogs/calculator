import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("calculator?")

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.label = QLabel("", self)
        self.vbox.addWidget(self.label)

        self.equal = QLabel("",self)
        self.vbox.addWidget(self.equal)

        self.LineShow = QLineEdit()

        #buttons here
        self.buttonEqual = QPushButton("=")
        self.vbox.addWidget(self.buttonEqual)
        self.buttonEqual.clicked.connect(self._equal)

        self.buttonZero = QPushButton("0")
        self.vbox.addWidget(self.buttonZero)
        self.buttonZero.clicked.connect(self._zero)

        self.buttonOne = QPushButton("1")
        self.vbox.addWidget(self.buttonOne)
        self.buttonOne.clicked.connect(self._one)

        self.buttonTwo = QPushButton("2")
        self.vbox.addWidget(self.buttonTwo)
        self.buttonTwo.clicked.connect(self._two)

        self.buttonThree = QPushButton("3")
        self.vbox.addWidget(self.buttonThree)
        self.buttonThree.clicked.connect(self._three)

        self.buttonFour = QPushButton("4")
        self.vbox.addWidget(self.buttonFour)
        self.buttonFour.clicked.connect(self._four)

        self.buttonFive = QPushButton("5")
        self.vbox.addWidget(self.buttonFive)
        self.buttonFive.clicked.connect(self._five)

        self.buttonSix = QPushButton("6")
        self.vbox.addWidget(self.buttonSix)
        self.buttonSix.clicked.connect(self._six)

        self.buttonSeven = QPushButton("7")
        self.vbox.addWidget(self.buttonSeven)
        self.buttonSeven.clicked.connect(self._seven)

        self.buttonEight = QPushButton("8")
        self.vbox.addWidget(self.buttonEight)
        self.buttonEight.clicked.connect(self._eight)

        self.buttonNine = QPushButton("9")
        self.vbox.addWidget(self.buttonNine)
        self.buttonNine.clicked.connect(self._nine)

        self.buttonPlus = QPushButton("+")
        self.vbox.addWidget(self.buttonPlus)
        self.buttonPlus.clicked.connect(self._plus)

        self.buttonSub = QPushButton("-")
        self.vbox.addWidget(self.buttonSub)
        self.buttonSub.clicked.connect(self._subtract)

        self.buttonMulti = QPushButton("*")
        self.vbox.addWidget(self.buttonMulti)
        self.buttonMulti.clicked.connect(self._multiple)

        self.buttonDiv = QPushButton("/")
        self.vbox.addWidget(self.buttonDiv)
        self.buttonDiv.clicked.connect(self._division)
        #buttons end

        self.setLayout(self.vbox)
        self.setLayout(self.hbox)
    # all button connections
    def _zero(self):
        self.label.setText(self.label.text() + "0")

    def _one(self):
        self.label.setText(self.label.text() + "1")

    def _two(self):
        self.label.setText(self.label.text() + "2")

    def _three(self):
        self.label.setText(self.label.text() + "3")

    def _four(self):
        self.label.setText(self.label.text() + "4")

    def _five(self):
        self.label.setText(self.label.text() + "5")

    def _six(self):
        self.label.setText(self.label.text() + "6")

    def _seven(self):
        self.label.setText(self.label.text() + "7")

    def _eight(self):
        self.label.setText(self.label.text() + "8")

    def _nine(self):
        self.label.setText(self.label.text() + "9")

    def _plus(self):
        self.label.setText(self.label.text() + "+")

    def _subtract(self):
        self.label.setText(self.label.text() + "-")

    def _multiple(self):
        self.label.setText(self.label.text() + "*")

    def _division(self):
        self.label.setText(self.label.text() + "/")

    def _equal(self):

        equasion = self.label.text()
        self.label.setText("")

        str(equasion)

        print("equasion: ", equasion)


        numbers = list()
        signs = list()
        num = ""

        for i in range(len(equasion)):
            if equasion[i] not in "+-*/":
                num += equasion[i]
            else:
                numbers.append(float(num))
                signs.append(equasion[i])
                num = ""
            if (i == len(equasion) - 1):
                numbers.append(float(num))


        print("numbers: ", numbers)

        num = numbers[0]
        print(num)
        for i in range(len(signs)):
            if signs[i] == "*":
                num = num * numbers[i + i]
            elif signs[i] == "/" and numbers[i+1] != 0:
                num = num / numbers[i + 1]
            elif signs[i] == "+":
                num = num + numbers[i+1]
            elif signs[i] == "-":
                num = num - numbers[i+1]

        self.equal.setText(str(num))




app = QApplication(sys.argv)

win = Window()

win.show()

sys.exit(app.exec_())

