from PySide2.QtWidgets import QWidget, QPushButton, QMessageBox, QLabel, \
    QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QTextLine
from package.PlotWidget import *
from package.Eq_parser import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equation Plotter")
        self.setGeometry(300, 300, 500, 500)
        self.equationLabel = QLabel("Equation:")
        self.startLabel = QLabel("Start:")
        self.endLabel = QLabel("End:")
        self.stepLabel = QLabel("Step:")
        self.plotPushButton = QPushButton("Plot")
        self.equationLine = QLineEdit()
        self.equationLine.setPlaceholderText("as a function of x")
        self.stepLine = QLineEdit()
        self.stepLine.setPlaceholderText("distance between points")
        self.startLine = QLineEdit()
        self.startLine.setPlaceholderText("start value of x")
        self.endLine = QLineEdit()
        self.endLine.setPlaceholderText("final value of x")

        self.layout = QVBoxLayout()
        self.formLayout = QFormLayout()

        self.formLayout.addRow(self.equationLabel,self.equationLine)
        self.formLayout.addRow(self.stepLabel,self.stepLine)
        self.formLayout.addRow(self.startLabel,self.startLine)
        self.formLayout.addRow(self.endLabel,self.endLine)



        self.layout.addLayout(self.formLayout)
        self.layout.addWidget(self.plotPushButton, Alignment=Qt.AlignTop)
        self.setLayout(self.layout)
        self.plotWidget = PlotWidget(10, 10)





        self.plotPushButton.clicked.connect(self.plotGraph)

    def plotGraph(self):
        # delattr(self, "plotWidget")
        self.plotWidget.setParent(None)
        self.plotWidget = PlotWidget(10, 10)

        equation = self.equationLine.text()
        start = float(self.startLine.text())
        end = float(self.endLine.text())
        step = float(self.stepLine.text())
        x,y = eq_parser(equation,start,end,step)
        self.plotWidget.addPlot(x,y)
        self.layout.insertWidget(2,self.plotWidget)






# x, y = eq_parser("sin(x)")
# fig = plt.figure(figsize=(10,10))
# plt.plot(x, y)
# plt.show()

