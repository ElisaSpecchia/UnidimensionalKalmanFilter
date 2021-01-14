import numpy as np


def parse_simulation_inputs(parameters_object):
    initial_state_guess = np.array(parameters_object['initial_state_guess'])
    initial_state_cov_matrix = np.array(parameters_object['initial_state_cov_matrix'])
    state_transition_matrix = np.array(parameters_object['state_transition_matrix'])
    measurement_cov_matrix = np.array(parameters_object['measurement_cov_matrix'])
    measurements = np.array(parameters_object['measurements'])

    input_data = {'initial_state_guess': initial_state_guess,
                  'initial_state_cov_matrix': initial_state_cov_matrix,
                  'state_transition_matrix': state_transition_matrix,
                  'measurement_cov_matrix': measurement_cov_matrix,
                  'measurements': measurements}

    return input_data


def parse_plot_inputs(estimate_array):
    """parse the output of the simulation,
    in order to create the plot.
    Define an array of two arrays:
    the first one contains all position estimates,
    the second one contains all velocity estimates."""
    plot_inputs = []
    for i in range(len(estimate_array)):
        for j in range(len(estimate_array[i])):
            if i == 0:
                plot_inputs.append([])
            plot_inputs[j].append(estimate_array[i][j][0])
    return plot_inputs


def parse_plot_uncertainty(uncertainty_array):
    """parse the output of the simulation,
    in order to create the plot.
    Define an array of two arrays:
    the first one contains all position uncertainties (standard deviation),
    the second one contains all velocity uncertainties (standard deviation)."""
    plot_uncertainties = []
    for i in range(len(uncertainty_array)):
        for j in range(len(uncertainty_array[i])):
            if i == 0:
                plot_uncertainties.append([])
            for k in range(len(uncertainty_array[i][j])):
                if j == k:
                    plot_uncertainties[j].append(np.sqrt(uncertainty_array[i][j][j]))
    return plot_uncertainties


def parse_plot_measurements(estimate_array):
    """parse the measurements,
    in order to create the plot.
    Define an array of two arrays:
    the first one contains all position measurements,
    the second one contains all velocity measurements."""
    plot_inputs = []
    for i in range(len(estimate_array)):
        for j in range(len(estimate_array[i])):
            if i == 0:
                plot_inputs.append([])
            plot_inputs[j].append(estimate_array[i][j])
    return plot_inputs
