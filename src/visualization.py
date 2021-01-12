import matplotlib.pyplot as plt
import numpy as np


def plot_output(plot_inputs, plots_uncertainties, measurements):
    steps = np.arange(1, len(plot_inputs[0]) + 1)

    plt.style.use('seaborn')
    fig, axs = plt.subplots(2, 1, figsize=(15, 15))

    axs[0].errorbar(steps, plot_inputs[0], yerr=plots_uncertainties[0],
                    linestyle=':', marker='o', markersize=6, color='black', ecolor='black', elinewidth=2,
                    fmt='.k', label='estimated position')
    axs[0].scatter(steps, measurements[0], color='r', label='measurements')
    axs[0].set_xticks(steps)
    axs[0].set_ylabel('position (m)')
    axs[0].legend(bbox_to_anchor=(0.98, 0.2), fontsize=12)

    axs[1].errorbar(steps, plot_inputs[1], yerr=plots_uncertainties[1],
                    linestyle=':', marker='o', markersize=6, color='black', ecolor='black', elinewidth=2,
                    fmt='.k', label='estimated velocity')
    axs[1].scatter(steps, measurements[1], color='r', label='measurements')
    axs[1].set_xticks(steps)
    axs[1].set_xlabel('steps')
    axs[1].set_ylabel('velocity (m/s)')
    axs[1].legend(bbox_to_anchor=(0.98, 0.9), fontsize=12)

    return fig

