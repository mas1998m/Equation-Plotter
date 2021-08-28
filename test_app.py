import pytest
import pytestqt
from package.app import *
from PySide2 import QtCore, QtWidgets
import random
from time import sleep

@pytest.fixture
def app(qtbot):
    test_eq_plotter = Window()
    qtbot.addWidget(test_eq_plotter)
    return test_eq_plotter


def test_plotting(app, qtbot):
    equations = ['x+5', "sin(x)*x", 'X^2', '5x^2-3x+3', '1/(x^2+5)']
    for i in range(100):
        app.equationLine.setText("")
        app.startLine.setText("")
        app.endLine.setText("")
        app.stepLine.setText("")
        qtbot.keyClicks(app.equationLine, random.choice(equations))
        start = (random.random()-0.5)*100
        end = (random.random()-0.5)*100
        if start > end:
            start, end = end, start
        step = random.random()*10
        qtbot.keyClicks(app.startLine, str(start))
        qtbot.keyClicks(app.endLine, str(end))
        qtbot.keyClicks(app.stepLine, str(step))
        qtbot.mouseClick(app.plotPushButton, QtCore.Qt.LeftButton)
        assert hasattr(app, "plotWidget")
        assert not hasattr(app, "error")


def test_error_handling(app, qtbot):
    qtbot.keyClicks(app.equationLine, 'aef2')
    qtbot.keyClicks(app.startLine, '1')
    qtbot.keyClicks(app.endLine, '2')
    qtbot.keyClicks(app.stepLine, '0.1')
    qtbot.mouseClick(app.plotPushButton, QtCore.Qt.LeftButton)
    assert hasattr(app, "error")
    app.error.done(0)




