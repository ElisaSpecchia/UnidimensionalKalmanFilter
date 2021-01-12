import numpy as np
import matrix_utilities as utilities


def state_extrapolation(current_state_vector, state_transition_matrix):
    next_state_vector = np.dot(state_transition_matrix, current_state_vector)
    return next_state_vector


def state_update(previous_state_vector, measurements, observation_matrix, kg):
    current_state_vector = previous_state_vector + np.dot(kg, np.subtract(
        measurements, np.dot(observation_matrix, previous_state_vector)))
    return current_state_vector


def kalman_gain(previous_state_cov_matrix, measurement_cov_matrix, observation_matrix):

    intermediate_calculation = np.dot(np.dot(
        observation_matrix, previous_state_cov_matrix),
        observation_matrix.T) + measurement_cov_matrix

    kg = np.dot(np.dot(previous_state_cov_matrix, observation_matrix.T), np.linalg.inv(intermediate_calculation))
    return kg


def covariance_extrapolation(current_state_cov_matrix, state_transition_matrix):

    next_state_cov_matrix = np.dot(state_transition_matrix, np.dot(
        current_state_cov_matrix, state_transition_matrix.T))
    return next_state_cov_matrix


def covariance_update(previous_state_cov_matrix, measurement_cov_matrix, observation_matrix, kg):

    identity = np.identity(np.shape(previous_state_cov_matrix)[0])
    intermediate_calculation = identity - np.dot(kg, observation_matrix)

    current_state_cov_matrix = np.dot(np.dot(intermediate_calculation, previous_state_cov_matrix, ),
                                      intermediate_calculation.T) + np.dot(np.dot(kg, measurement_cov_matrix), kg.T)
    return current_state_cov_matrix
