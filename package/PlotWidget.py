import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PlotWidget(FigureCanvasQTAgg):
    """
    widget inheriting FigureCanvasQTAgg class to support using matplotlib figures as Qt Widgets
    """

    def __init__(self,width,height):
        """
        constructor of the widget
        :arg width: the width of the figure
        :type width: int
        :arg heigh: the heigh of the figure
        :type heigh: int
        """

        self.fig = Figure(figsize=(width,height))
        super(PlotWidget, self).__init__(self.fig)

    def addPlot(self,x,y):
        """
        graphs the relation into the figure(widget)
        :param x: the x axis values
        :type x: list of float/int
        :param y: the y axis values
        :type y: list of float/int
        """

        self.axes =self.fig.add_subplot(111)
        self.axes.cla()
        self.axes.plot(x,y)
        self.axes.set(xlabel='x', ylabel='y')
        self.axes.grid()




