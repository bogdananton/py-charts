
from demomodule.graph import Graph
import numpy as np


def test_default_title_is_no_title():
    graph0 = Graph()
    assert graph0.title == 'No Title'


def test_title_can_be_assigned():
    graph0 = Graph('new name')
    assert graph0.title == 'new name'


def test_draw2d_show_sample():
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    graph1 = Graph()
    graph1.draw2D(x, y)

