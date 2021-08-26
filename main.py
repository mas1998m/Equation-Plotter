from package.app import App
import sys

if __name__ == '__main__':

    myApp = App(sys.argv)
    sys.exit(myApp.exec_())




