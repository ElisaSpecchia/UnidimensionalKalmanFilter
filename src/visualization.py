import matplotlib.pyplot as plt
import numpy as np


def plot_output(plot_estimates, plot_uncertainties, plot_measurements):
    time_steps = np.arange(1, len(plot_estimates[0]) + 1)

    plt.style.use('seaborn')
    fig, axs = plt.subplots(4, 1, figsize=(10, 20), sharex='all',
                            gridspec_kw={'height_ratios': [2, 1.5, 1, 1]}, constrained_layout=True)
    fig.suptitle("Kalman filter simulation output", fontsize=25)

    # plot position estimates
    axs[0].plot(time_steps, plot_estimates[0], linestyle=':', marker='o', markersize=6, color='black',
                label='estimated position')
    axs[0].scatter(time_steps, plot_measurements[0], color='r', label='measured position')
    axs[0].set_ylabel('position (m)', fontsize=12)
    axs[0].legend(bbox_to_anchor=(0.98, -0.01), fontsize=14)
    axs[0].set_title('Position', fontsize=15, x=0.5, y=0.99)

    # plot position uncertainty
    axs[1].plot(time_steps, plot_uncertainties[0],
                linestyle=':', marker='o', markersize=6, color='orange')
    axs[1].set_ylabel('position uncertainty (m)', fontsize=12)
    axs[1].set_title('Position  Uncertainty', fontsize=15, x=0.5, y=0.99)

    # plot velocity estimates
    axs[2].plot(time_steps, plot_estimates[1],
                linestyle=':', marker='o', markersize=6, color='black',
                label='estimated velocity')
    axs[2].scatter(time_steps, plot_measurements[1], color='r', label='measured velocity')
    axs[2].set_ylabel('velocity (m/s)', fontsize=12)
    axs[2].legend(bbox_to_anchor=(0.98, -0.01), fontsize=14)
    axs[2].set_title('Velocity', fontsize=15, x=0.5, y=0.99)

    # plot velocity uncertainty
    axs[3].plot(time_steps, plot_uncertainties[1],
                linestyle=':', marker='o', markersize=6, color='orange')
    axs[3].set_ylabel('velocity uncertainty (m/s)', fontsize=12)
    axs[3].set_title('Velocity Uncertainty', fontsize=15, x=0.5, y=0.99)

    axs[3].set_xticks(time_steps)
    axs[3].set_xlabel('steps', fontsize=14)

    return fig
