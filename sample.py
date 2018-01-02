from demomodule.graph import Graph
import numpy as np


instance = Graph('sample', True, True)

x = np.arange(0, 5, 0.1)
y = np.sin(x)
instance.draw2D(x, y)

instance.draw3D()
