import numpy as np
import kalman_equations_matrix_form as kalman

observation_matrix = np.array([[1, 0], [0, 1]])


def extrapolate_initial_state_guess(initial_state_guess, state_transition_matrix):
    next_state_vector = kalman.state_extrapolation(
        initial_state_guess.T, state_transition_matrix)
    return next_state_vector


def extrapolate_initial_state_cov_matrix(initial_state_cov_matrix, state_transition_matrix):
    next_state_cov_matrix = kalman.covariance_extrapolation(
        initial_state_cov_matrix, state_transition_matrix)
    return next_state_cov_matrix


def simulation(initial_state_guess, initial_state_cov_matrix, measurements, measurement_cov_matrix,
               state_transition_matrix):
    output_simulation = []
    output_simulation_uncertainty = []

    # extrapolation of initial state guess and covariance matrix
    previous_state_vector = np.array([extrapolate_initial_state_guess(initial_state_guess, state_transition_matrix)]).T
    previous_state_cov_matrix = extrapolate_initial_state_cov_matrix(initial_state_cov_matrix, state_transition_matrix)

    for step in range(measurements.shape[0]):
        # Update step
        measure = np.array([measurements[step]]).T
        kg = kalman.kalman_gain(
            previous_state_cov_matrix, measurement_cov_matrix, observation_matrix)

        current_state_vector = kalman.state_update(
            previous_state_vector, measure, observation_matrix, kg)
        output_simulation.append(current_state_vector)
        current_state_cov_matrix = kalman.covariance_update(
            previous_state_cov_matrix, measurement_cov_matrix, observation_matrix, kg)
        output_simulation_uncertainty.append(current_state_cov_matrix)

        # Propagate step
        next_state_vector = kalman.state_extrapolation(
            current_state_vector, state_transition_matrix)
        next_state_cov_matrix = kalman.covariance_extrapolation(
            current_state_cov_matrix, state_transition_matrix)

        # Repeat the process
        previous_state_vector = next_state_vector
        previous_state_cov_matrix = next_state_cov_matrix
    return output_simulation, output_simulation_uncertainty



