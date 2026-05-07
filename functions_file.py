# -*- coding: utf-8 -*-
"""
Created on Thu May  8 15:00:47 2025

@author: Dahiana
"""

import matplotlib.pyplot as plt



def func_scatter(x, y,xlabel,ylabel, title):
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def func_line(x, y,xlabel,ylabel, title):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()