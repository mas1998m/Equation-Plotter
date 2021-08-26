from PySide2.QtWidgets import QApplication
from package.Window import Window
import sys



class App(QApplication):
    """
    a wrapper class to run the application in fewest steps
    """


    def __init__(self,sys_argv):
        """
        :arg sys_argv: arguments taken from the cmd window when running the script
        """
        super(App, self).__init__(sys_argv)
        self.window = Window()
        self.window.show()





