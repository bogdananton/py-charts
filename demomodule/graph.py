import matplotlib.pyplot as plt
import uuid

# used in draw3D sample
from mpl_toolkits.mplot3d import Axes3D # used for 3d projection
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


class Graph:
    def __init__(self, title='No Title', display_chart = False, save_jpg = False):
        self.title = title
        self.display_chart = display_chart
        self.save_jpg = save_jpg
        self.identifier = str(uuid.uuid4())

    def draw2D(self, x, y):
        plt.figure(num=None, figsize=(5, 4), dpi=150, facecolor='w', edgecolor='k')
        plt.plot(x, y)

        if self.save_jpg:
            plt.savefig('2d-' + self.identifier + '.png')

        if self.display_chart:
            plt.show()

    def draw3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make data.
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        if self.save_jpg:
            plt.savefig('3d-' + self.identifier + '.png')

        if self.display_chart:
            plt.show()
