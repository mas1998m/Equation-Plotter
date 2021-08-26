from PySide2.QtWidgets import QApplication
from package.Window import Window
import sys



class App(QApplication):
    def __init__(self,sys_argv):
        super(App, self).__init__(sys_argv)
        self.window = Window()
        self.window.show()





