import numpy as np
import matplotlib.pyplot as plt

from .plot_designer import PlotDesigner
from ..history import BaseHistory


def plot_fitness_history(history, title, designer=None, save=None):

    """
    Generates a plot of the optimisations fitness / iterations.

    Parameters
    ----------
    history : BaseHistory
        Contains all the information used to generate the plots.
    title : str
        Title to be placed on the plot.
    designer : PlotDesigner
        Contains information required to format the plot.
    save : bool
        Whether to save the plot or not.
    """

    if not issubclass(type(history), BaseHistory):
        raise TypeError('history must be a class of BaseHistory.')

    n_iterations = len(history.arr_best_fitness)

    if designer is None:
        designer = PlotDesigner()
        designer.label = ['Iterations', 'Fitness']

    fig, ax = plt.subplots(1, 1, figsize=designer.figsize)

    ax.scatter(np.arange(n_iterations), history.arr_best_fitness, label='Best')
    ax.scatter(np.arange(n_iterations), history.arr_mean_fitness, label='Mean')

    ax.set_title(title, fontsize=designer.title_fontsize)
    ax.legend(fontsize=designer.text_fontsize)

    ax.set_xlabel(designer.label[0])
    ax.set_ylabel(designer.label[1])

    ax.tick_params(labelsize=designer.text_fontsize)

    if save:
        plt.savefig(save, bbox_inches='tight')
    else:
        plt.show()
