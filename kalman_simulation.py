import numpy as np
import kalman_equations_matrix_form as kalman

initial_state_guess = np.array([[260, 6]]).T
initial_state_cov_matrix = np.array([[100, 0], [0, 25]])
state_transition_matrix = np.array([[1, 5], [0, 1]])
measurements = np.array([[301, 5], [333, 5.3], [360, 5.5]])
measurement_cov_matrix = np.array([[4, 0], [0, 25]])
observation_matrix = np.array([[1, 0], [0, 1]])


def extrapolate_initial_state_guess():
    next_state_vector = kalman.state_extrapolation(
        initial_state_guess, state_transition_matrix)
    return next_state_vector


def extrapolate_initial_state_cov_matrix():
    next_state_cov_matrix = kalman.covariance_extrapolation(
        initial_state_cov_matrix, state_transition_matrix)
    return next_state_cov_matrix


def simulation():
    previous_state_vector = extrapolate_initial_state_guess()
    previous_state_cov_matrix = extrapolate_initial_state_cov_matrix()
    for time in range(measurements.shape[0]):
        measure = np.array([measurements[time]]).T
        kg = kalman.kalman_gain(
            previous_state_cov_matrix, measurement_cov_matrix, observation_matrix)

        current_state_vector = kalman.state_update(
            previous_state_vector, measure, observation_matrix, kg)
        current_state_cov_matrix = kalman.covariance_update(
            previous_state_cov_matrix, measurement_cov_matrix, observation_matrix, kg)

        next_state_vector = kalman.state_extrapolation(
            current_state_vector, state_transition_matrix)
        next_state_cov_matrix = kalman.covariance_extrapolation(
            current_state_cov_matrix, state_transition_matrix)

        previous_state_vector = next_state_vector
        previous_state_cov_matrix = next_state_cov_matrix

        print(current_state_vector)


simulation()

