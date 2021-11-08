import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


numbers = list()
signs = list()
i = list()

class Window(QWidget):

    def __init__(self):

        super(Window, self).__init__()

        self.setWindowTitle("calculator?")

        self.setGeometry(10, 10, 400, 200)

        self.vbox = QVBoxLayout()
        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        # labels here(showLine(where all numbers appear) and equal(where result appears))
        self.showLine = QLabel("", self)
        self.vbox.addWidget(self.showLine)

        self.equal = QLabel("", self)
        self.vbox.addWidget(self.equal)

        self.LineShow = QLineEdit()

        # buttons here

        # button zero
        self.btn_0 = QPushButton("0")
        self.hbox4.addWidget(self.btn_0)
        self.btn_0.clicked.connect(self._zero)
        # button dot
        self.btn_dot = QPushButton(".")
        self.hbox4.addWidget(self.btn_dot)
        self.btn_dot.clicked.connect(self._dot)
        # button equal
        self.btn_equal = QPushButton("=")
        self.hbox4.addWidget(self.btn_equal)
        self.btn_equal.clicked.connect(self._equal)
        # button one
        self.btn_1 = QPushButton("1")
        self.hbox3.addWidget(self.btn_1)
        self.btn_1.clicked.connect(self._one)
        # button two
        self.btn_2 = QPushButton("2")
        self.hbox3.addWidget(self.btn_2)
        self.btn_2.clicked.connect(self._two)
        # button three
        self.btn_3 = QPushButton("3")
        self.hbox3.addWidget(self.btn_3)
        self.btn_3.clicked.connect(self._three)
        # button plus
        self.btn_plus = QPushButton("+")
        self.hbox3.addWidget(self.btn_plus)
        self.btn_plus.clicked.connect(self._plus)
        # button four
        self.btn_4 = QPushButton("4")
        self.hbox2.addWidget(self.btn_4)
        self.btn_4.clicked.connect(self._four)
        # button five
        self.btn_5 = QPushButton("5")
        self.hbox2.addWidget(self.btn_5)
        self.btn_5.clicked.connect(self._five)
        # button six
        self.btn_6 = QPushButton("6")
        self.hbox2.addWidget(self.btn_6)
        self.btn_6.clicked.connect(self._six)
        # button minus
        self.btn_sub = QPushButton("-")
        self.hbox2.addWidget(self.btn_sub)
        self.btn_sub.clicked.connect(self._subtract)
        # button seven
        self.btn_7 = QPushButton("7")
        self.hbox1.addWidget(self.btn_7)
        self.btn_7.clicked.connect(self._seven)
        # button eight
        self.btn_8 = QPushButton("8")
        self.hbox1.addWidget(self.btn_8)
        self.btn_8.clicked.connect(self._eight)
        # button nine
        self.btn_9 = QPushButton("9")
        self.hbox1.addWidget(self.btn_9)
        self.btn_9.clicked.connect(self._nine)
        # button multiply
        self.btn_mul = QPushButton("*")
        self.hbox1.addWidget(self.btn_mul)
        self.btn_mul.clicked.connect(self._multiple)
        # button clear all
        self.btn_AC = QPushButton("AC")
        self.hbox0.addWidget(self.btn_AC)
        self.btn_AC.clicked.connect(self._clear)
        # button root
        self.btn_rt = QPushButton("√")
        self.hbox0.addWidget(self.btn_rt)
        self.btn_rt.clicked.connect(self._root)
        # button divide
        self.btn_dvd = QPushButton("/")
        self.hbox0.addWidget(self.btn_dvd)
        self.btn_dvd.clicked.connect(self._division)

        # layouts here(the higher number the higher the row)
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        # buttons end
    # all button functions
    def _clear(self):
        self.showLine.clear()
        self.equal.clear()

    def _root(self):
        if len(signs) == 0 and len(self.showLine.text()) > 0 :
            self.equal.setText(str(sqrt(float(self.showLine.text()))))
            self.showLine.clear()
        elif len(self.showLine.text()) > 0:
            if float(self.showLine.text()) < 0:
                self.equal.setText("error")
        else:
            self.equal.setText("error")

    def _dot(self):
        if "." not in self.showLine.text() and len(self.showLine.text()) != 0:
            self.showLine.setText(self.showLine.text() + ".")
        elif "." in self.showLine.text():
            self.equal.setText("error")
            self.showLine.clear()
        else:
            self.equal.setText("error")
    def _zero(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "0")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "0")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "0")

    def _one(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "1")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "1")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "1")

    def _two(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "2")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "2")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "2")

    def _three(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "3")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "3")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "3")

    def _four(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "4")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "4")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "4")

    def _five(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "5")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "5")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "5")

    def _six(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "6")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "6")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "6")

    def _seven(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "7")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "7")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "7")

    def _eight(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "8")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "8")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "8")

    def _nine(self):
        if len(signs) == 0:
            self.showLine.setText(self.showLine.text() + "9")
        elif len(signs) == 1 and len(i) == 0:
            i.append("")
            self.showLine.clear()
            self.showLine.setText(self.showLine.text() + "9")
        elif len(signs) == 1 and len(i) >= 1:
            self.showLine.setText(self.showLine.text() + "9")

    def _plus(self):
        if len(numbers) == 0 and len(signs) == 0:
            numbers.append(float(self.showLine.text()))
            signs.append("+")
        elif len(numbers) == 1 or len(signs) == 1:
            self.equal.setText("error")
        else:
            self.equal.setText("error")

    def _subtract(self):
        if len(numbers) == 0 and len(signs) == 0:
            numbers.append(float(self.showLine.text()))
            signs.append("-")
            i.clear()
        elif len(numbers) == 1 or len(signs) == 1:
            self.equal.setText("error")
            self.showLine.clear()
        else:
            self.equal.setText("error")
            self.showLine.clear()


    def _multiple(self):
        if len(numbers) == 0 and len(signs) == 0:
            numbers.append(float(self.showLine.text()))
            signs.append("*")
        elif len(numbers) == 1 or len(signs) == 1:
            self.equal.setText("error")
            self.showLine.clear()
        else:
            self.equal.setText("error")
            self.showLine.clear()

    def _division(self):
        if len(numbers) == 0 and len(signs) == 0:
            numbers.append(float(self.showLine.text()))
            signs.append("/")
        elif len(numbers) == 1 or len(signs) == 1:
            self.equal.setText("error")
            self.showLine.clear()
        else:
            self.equal.setText("error")
            self.showLine.clear()

    def _equal(self):
        numbers.append(float(self.showLine.text()))
        result = "error"

        if signs[0] == "+":
            result = numbers[0] + numbers[1]
        elif signs[0] == "-":
            result = numbers[0] - numbers[1]
        elif signs[0] == "*":
            result = numbers[0] * numbers[1]
        elif signs[0] == "/" and (numbers[1] != 0):
            result = numbers[0] / numbers[1]
        elif signs[0] == "/" and (numbers[1] == 0):
            self.equal.setText("error")
            self.showLine.clear()
        else:
            self.equal.setText("error")
            self.showLine.clear()

        self.equal.setText(str(result))
        self.showLine.setText("")

        i.clear()
        numbers.clear()
        signs.clear()



app = QApplication(sys.argv)

win = Window()

win.show()

sys.exit(app.exec_())

