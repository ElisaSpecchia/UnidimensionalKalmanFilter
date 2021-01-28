import numpy as np


def parse_simulation_inputs(parameters_object):
    """
    Input:
    parameters_object = json containing all input parameters needed for the Kalman simulation.

    Define a numpy array for each of the input parameters.
    Return a dictionary containing all inputs.
    """

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


def parse_plot_estimates(estimate_array):
    """Parse the output of the simulation, to create the plot.

    Input:
    estimate array = array containing the estimated state vectors for
                    each time step in the simulation.

    Return a list formed of two lists:
    put all position estimates in the first list,
    put all velocity estimates in the second list."""

    plot_inputs = []
    for i in range(len(estimate_array)):
        for j in range(len(estimate_array[i])):
            if i == 0:
                plot_inputs.append([])
            plot_inputs[j].append(estimate_array[i][j][0])
    return plot_inputs


def parse_plot_uncertainty(uncertainty_array):
    """Parse the output of the simulation, to create the plot.

    Input:
    uncertainty_array = array containing the state covariance matrices for each time step
                        in the simulation.

    Return a list formed of two lists:
    put all position uncertainties (standard deviation) in the first list,
    put all velocity uncertainties (standard deviation) in the second list."""

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
    """Parse the measurements, to create the plot.
    Define a list formed of two lists:
    put all position measurements in the first list,
    put all velocity measurements in the second list."""

    plot_inputs = []
    for i in range(len(estimate_array)):
        for j in range(len(estimate_array[i])):
            if i == 0:
                plot_inputs.append([])
            plot_inputs[j].append(estimate_array[i][j])
    return plot_inputs
