from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from package.PlotWidget import *
from package.Eq_parser import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equation Plotter")
        self.setGeometry(300, 300, 700, 700)
        self.setCentralWidget(QWidget(self))
        
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
        self.centralWidget().setLayout(self.layout)

        self.plotPushButton.clicked.connect(self.plotGraph)

    def plotGraph(self):
        if hasattr(self,"plotWidget"):
            self.plotWidget.setParent(None)
            delattr(self, "plotWidget")

        if hasattr(self,"toolbar"):
            self.toolbar.setParent(None)
            delattr(self, "toolbar")

        equation = self.equationLine.text()
        self.plotWidget = PlotWidget(9, 9)
        self.toolbar = NavigationToolbar(self.plotWidget, self)

        try:
            start = float(self.startLine.text())
            end = float(self.endLine.text())
            step = float(self.stepLine.text())
            if(start>end):
                raise RuntimeError
        except:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Warning)
            self.error.setWindowTitle("Parameters Error")
            self.error.setText("<b>invalid input</b>")
            self.error.setInformativeText("start,end & step must be numbers\n\nstart must be less than end\n")
            self.error.exec()
            return


        try:
            x,y = eq_parser(equation,start,end,step)
        except:
            self.error = QMessageBox()
            self.error.setIcon(QMessageBox.Warning)
            self.error.setWindowTitle("Equation Error")
            self.error.setText("<b>invalid input</b>")
            self.error.setInformativeText("Wrong Equation Format\nEquation must be function of x\n ")
            self.error.exec()
            return

        self.plotWidget.addPlot(x,y)
        self.layout.insertWidget(2,self.plotWidget)
        self.layout.insertWidget(2,self.toolbar)




