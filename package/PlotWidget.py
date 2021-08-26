import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PlotWidget(FigureCanvasQTAgg):
    """":arg
    :ivar
    :param

    """
    def __init__(self,width,height):
        fig = Figure(figsize=(width,height))
        self.axes =fig.add_subplot(111)
        self.axes.set(xlabel='x', ylabel='y')
        self.axes.grid()
        super(PlotWidget, self).__init__(fig)

    def addPlot(self,x,y):
        self.axes.cla()
        self.axes.plot(x,y)



