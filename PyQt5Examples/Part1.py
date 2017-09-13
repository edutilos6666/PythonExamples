import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHBoxLayout, QGroupBox , QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFormLayout

from PyQt5.QtWidgets import QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


import numpy as np

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem



def example7():
    """QTableWidget"""

    class Person:
        def __init__(self, id, name,age , wage , active):
            self.id , self.name, self.age, self.wage , self.active = id, name, age, wage, active

        def __repr__(self):
            return "Person({0},{1},{2},{3},{4})".format(self.id. self.name, self.age, self.wage, self.active)



    def generate_people_data():
        ret = [
            Person(1, "foo", 10, 100.0, True),
            Person(2, "bar", 20, 200.0, False),
            Person(3, "bim", 30, 300.0, True),
            Person(4, "pako", 40, 400.0, False)
        ]

        return ret


    class App(QDialog):
        def __init__(self):
            super().__init__()
            self.title = "QTableWidget example"
            self.left , self.top , self.width , self.height = 10 , 10, 500, 500
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left , self.top, self.width , self.height)
            self.mainLayout = QVBoxLayout()
            self.addComponents()
            self.registerEvents()
            self.setLayout(self.mainLayout)
            self.show()

        def addComponents(self):
            self.tableWidget = QTableWidget()
            data = generate_people_data()

            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(5)

            for i, person in enumerate(data):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(person.id)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(person.name))
                self.tableWidget.setItem(i, 2,QTableWidgetItem(str(person.age)))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(person.wage)))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(person.active)))

            self.tableWidget.setHorizontalHeaderLabels(["Id", "Name", "Age", "Wage", "Active"])
            self.mainLayout.addWidget(self.tableWidget)



        def registerEvents(self):
            self.tableWidget.doubleClicked.connect(self.onTableWidgetDoubleClicked)

        @pyqtSlot()
        def onTableWidgetDoubleClicked(self):
            for selected in self.tableWidget.selectedItems():
                print(selected.row(), selected.column(), selected.text())


    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())





def example6():
    """matplot inside pyqt5"""
    class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.left , self.top, self.width , self.height = 10 , 10, 500, 500
            self.title = "matplotlib embedded inside pyqt5 "
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left , self.top, self.width , self.height)

            m = PlotCanvas(self, width = 5, height = 4)
            m.move(0, 0)

            button = QPushButton("PyQt5 button", self)
            button.setToolTip("Simple Push button")
            button.move(500, 0)
            button.resize(140, 100)

            self.show()

    class PlotCanvas(FigureCanvas):
        def __init__(self, parent = None , width = 5, height = 4, dpi = 100):
            fig = Figure(figsize = (width , height), dpi= dpi)
            self.axes = fig.add_subplot(111)

            FigureCanvas.__init__(self, fig)
            self.setParent(parent)

            FigureCanvas.setSizePolicy(self,
                                       QSizePolicy.Expanding ,
                                       QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)
            self.plot()

        def plot(self):
            x = np.linspace(-np.pi, np.pi, 100)
            y_sin, y_cos = np.sin(x), np.cos(x)
            ax = self.figure.add_subplot(111)
            ax.plot(x, y_sin, x, y_cos)
            ax.set_title("Matplot with pyqt5")
            self.draw()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())






def example5():
    """QFormLayout example"""
    class App(QDialog):
        def __init__(self):
            super().__init__()
            self.title = "Example 5"
            self.left , self.top, self.width , self.height = 10, 10, 500, 500
            self.initUI()

        def initUI(self):
            self.mainLayout = QFormLayout()
            self.addComponents()
            self.registerEvents()
            self.setLayout(self.mainLayout)
            self.show()

        def addComponents(self):
            self.lblTitle = QLabel("QFormLayout example")
            self.lblEmpty = QLabel("")

            self.lblId = QLabel("Id: ")
            self.editId = QTextEdit()

            self.lblName = QLabel("Name: ")
            self.editName = QTextEdit()

            self.lblAge = QLabel("Age: ")
            self.editAge = QTextEdit()

            self.lblWage = QLabel("Wage: ")
            self.editWage = QTextEdit()

            self.lblActive = QLabel("Active: ")
            self.editActive = QTextEdit()

            self.btnOk = QPushButton("Ok")
            self.btnClear = QPushButton("Clear")

            # add components into mainLayout
            self.mainLayout.addRow(self.lblTitle, self.lblEmpty)
            self.mainLayout.addRow(self.lblId, self.editId)
            self.mainLayout.addRow(self.lblName, self.editName)
            self.mainLayout.addRow(self.lblAge, self.editAge)
            self.mainLayout.addRow(self.lblWage, self.editWage)
            self.mainLayout.addRow(self.lblActive, self.editActive)
            self.mainLayout.addRow(self.btnOk, self.btnClear)


        def registerEvents(self):
            self.btnOk.clicked.connect(self.onBtnOkClicked)
            self.btnClear.clicked.connect(self.onBtnClearClicked)

        @pyqtSlot()
        def onBtnOkClicked(self):
            try:
                id = int(self.editId.toPlainText())
                name = self.editName.toPlainText()
                age = int(self.editAge.toPlainText())
                wage = float(self.editWage.toPlainText())
                temp = self.editActive.toPlainText().lower()
                active = True if(temp == "true") else False
                msg = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}""".format(id, name, age, wage, active)
                QMessageBox.information(self, "<<Information>>", msg)
            except:
                QMessageBox.critical(self, "<<Error>>", "Something wrong happened.")

        @pyqtSlot()
        def onBtnClearClicked(self):
            self.editId.setText("")
            self.editName.setText("")
            self.editAge.setText("")
            self.editWage.setText("")
            self.editActive.setText("")


    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




def example4():
    """QGridLayout example"""
    class App(QDialog):
        def __init__(self):
            super().__init__()
            self.title = "Example 4"
            self.left , self.top, self.width , self.height = 10, 10 , 400 , 400
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width , self.height)
            self.mainLayout = QGridLayout()
            self.mainLayout.setColumnStretch(0, 4)
            self.mainLayout.setColumnStretch(1, 4)
            self.addComponents()
            self.registerEvents()
            self.setLayout(self.mainLayout)
            self.show()

        def addComponents(self):
            # title
            self.lblTitle = QLabel("Welcome to the PyQt5")
            self.lblEmpty = QLabel("")
            # id
            self.lblId = QLabel("Id: ")
            self.editId =  QTextEdit()
            # name
            self.lblName = QLabel("Name: ")
            self.editName = QTextEdit()
            # age
            self.lblAge = QLabel("Age: ")
            self.editAge = QTextEdit()
            # wage
            self.lblWage = QLabel("Wage: ")
            self.editWage = QTextEdit()
            # active
            self.lblActive = QLabel("Active: ")
            self.editActive = QTextEdit()
            # buttons
            self.btnOk = QPushButton("Ok")
            self.btnClear = QPushButton("Clear")

            self.mainLayout.addWidget(self.lblTitle , 0, 0)
            self.mainLayout.addWidget(self.lblEmpty, 0, 1)
            self.mainLayout.addWidget(self.lblId , 1, 0)
            self.mainLayout.addWidget(self.editId, 1, 1)
            self.mainLayout.addWidget(self.lblName, 2, 0)
            self.mainLayout.addWidget(self.editName, 2, 1)
            self.mainLayout.addWidget(self.lblAge, 3, 0)
            self.mainLayout.addWidget(self.editAge, 3, 1)
            self.mainLayout.addWidget(self.lblWage, 4, 0)
            self.mainLayout.addWidget(self.editWage, 4, 1)
            self.mainLayout.addWidget(self.lblActive, 5, 0)
            self.mainLayout.addWidget(self.editActive, 5, 1)
            self.mainLayout.addWidget(self.btnOk , 6, 0)
            self.mainLayout.addWidget(self.btnClear, 6, 1)


        def registerEvents(self):
            self.btnOk.clicked.connect(self.onBtnOkClicked)
            self.btnClear.clicked.connect(self.onBtnClearClicked)

        @pyqtSlot()
        def onBtnOkClicked(self):
            try:
                id = int(self.editId.toPlainText())
                name = self.editName.toPlainText()
                age = int(self.editAge.toPlainText())
                wage = float(self.editWage.toPlainText())
                temp = self.editActive.toPlainText().lower()
                active = True if (temp == "true") else False
                msg = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}
                """.format(id, name, age, wage, active)
                QMessageBox.information(self, "<<Information>>", msg)
                # that does not work
                # msgBox = QMessageBox()
                # msgBox.setIcon(QMessageBox.Information)
                # msgBox.setText(msg)
                # msgBox.setInformativeText(msg)
                # msgBox.setWindowTitle("<<Information>>")
                # msgBox.show()
            except:
                msg = "something was wrong."
                # that does not work
                # msgBox = QMessageBox()
                # msgBox.setIcon(QMessageBox.Critical)
                # msgBox.setText(msg)
                # msgBox.setInformativeText(msg)
                # msgBox.setWindowTitle("<<Error>>")
                # msgBox.show()
                QMessageBox.critical(self, "<<Error>>", msg)

        @pyqtSlot()
        def onBtnClearClicked(self):
            self.editId.setText("")
            self.editName.setText("")
            self.editAge.setText("")
            self.editWage.setText("")
            self.editActive.setText("")


    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def example3():
    class App(QDialog):
        def __init__(self):
            super().__init__()
            self.title = "Example3"
            self.left , self.top, self.width , self.height = 10, 10, 400, 400
            self.initUI()


        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left , self.top, self.width , self.height)
            self.createGridLayout()

            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)
            self.setLayout(windowLayout)
            self.show()

        def createGridLayout(self):
            self.horizontalGroupBox = QGroupBox("Grid")
            layout = QGridLayout()
            layout.setColumnStretch(1, 4)
            layout.setColumnStretch(2, 4)

            layout.addWidget(QPushButton("1"), 0, 0)
            layout.addWidget(QPushButton("2"), 0, 1)
            layout.addWidget(QPushButton("3"), 0, 2)
            layout.addWidget(QPushButton("4"), 1, 0)
            layout.addWidget(QPushButton("5"), 1,1)
            layout.addWidget(QPushButton("6"), 1, 2)
            layout.addWidget(QPushButton("7"), 2, 0)
            layout.addWidget(QPushButton("8"), 2, 1)
            layout.addWidget(QPushButton("9"), 2, 2)
            self.horizontalGroupBox.setLayout(layout)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def example2():
    class App(QWidget):
        def __init__(self):
            super().__init__()
            self.title = "Example2"
            self.left , self.top, self.width , self.height = 10, 10, 400, 400
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width , self.height)

            button = QPushButton("PyQt5 button", self)
            button.setToolTip("This is an example button")
            button.move(100, 70)
            button.clicked.connect(self.on_click)
            self.show()

        @pyqtSlot()
        def on_click(self):
            print("PyQt5 button was clicked.")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



def example1():
    class App(QWidget):
        def __init__(self):
            super().__init__()
            self.title = "Example1"
            self.left = 10
            self.top = 10
            self.width = 500
            self.height = 500
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left , self.top, self.width , self.height)
            self.show()

    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
