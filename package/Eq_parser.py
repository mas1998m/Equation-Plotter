import numpy as np
import parser
from math import *


def eq_parser(eq_string,start=0,end=5,step=0.1):
    """
    do the needed job to parse the equation to points to be plotted
    :param eq_string: the equation string
    :type eq_string:string
    :param start: start value of x
    :type start: float,int
    :param end: end value of x
    :type end: float,int
    :param step: distance between points on graph
    :type step: float,int
    :return: the points to be plotted
    :rtype: 2d list
    """

    points = np.arange(start, end, step)
    # replacing any ^ with ** as in python ^ means xor not power
    eq_string = eq_string.replace("^", "**")
    # replacing X with x so the parser can work without problems
    eq_string = eq_string.replace("X", "x")

    # adding * operator between x variable and the factor if not added by the user
    i=0
    while i<len(eq_string)-1:
        if eq_string[i].isdigit() and eq_string[i+1] == 'x':
            i=i+1
            eq_string = eq_string[:i] + "*" + eq_string[i:]
        i = i+1

    eq = parser.expr(eq_string).compile()

    # evaluating the function value for every value of x and appending it to y
    y = [eval(eq) for x in points]
    return [points,y]



