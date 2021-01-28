import numpy as np


# implementation of all Kalman filter equations

def state_extrapolation(current_state_vector, state_transition_matrix):
    """" Implementation of state extrapolation equation.

    Input parameters:
    current_state_vector = state vector (including all estimated states of the system)
                           after the update step,
    state_transition_matrix = matrix for the implementation of the dynamic model.

    Returns:
    next_state_vector = state vector at the next time step, before the update.
    """

    next_state_vector = np.dot(state_transition_matrix, current_state_vector)
    return next_state_vector


def state_update(previous_state_vector, measurements, observation_matrix, kg):
    """" Implementation of state update equation.

    Input parameters:
    previous_state_vector = state vector (including all estimated states of the system)
                            before the update step,
    measurements = vector storing all measured states at a specific time step,
    observation_matrix = matrix converting the measurement vector of the system into the
                         state vector,
    kg = Kalman gain (it weights the measurements).

    Returns:
    current_state_vector = state vector after the update.
    """

    current_state_vector = previous_state_vector + np.dot(kg, np.subtract(
        measurements, np.dot(observation_matrix, previous_state_vector)))
    return current_state_vector


def kalman_gain(previous_state_cov_matrix, measurement_cov_matrix, observation_matrix):
    """" Implementation of Kalman gain equation.

    Input parameters:
    previous_state_vector = state vector (including all estimated states of the system)
                            before the update step,
    measurements_cov_matrix = covariance matrix defining the uncertainty in each of the measurements,
    observation_matrix = matrix converting the measurement vector of the system into the
                         state vector.

    Returns:
    kg = Kalman gain (it weights the measurements).
    """

    intermediate_calculation = np.dot(np.dot(
        observation_matrix, previous_state_cov_matrix),
        observation_matrix.T) + measurement_cov_matrix

    kg = np.dot(np.dot(previous_state_cov_matrix, observation_matrix.T), np.linalg.inv(intermediate_calculation))
    return kg


def covariance_extrapolation(current_state_cov_matrix, state_transition_matrix):
    """" Implementation of covariance extrapolation equation.

    Input parameters:
    current_state_cov_matrix = state covariance matrix (defining the uncertainty in each of the estimates)
                               after the update step,
    state_transition_matrix = matrix for the implementation of the dynamic model.

    Returns:
    next_state_cov_matrix = state covariance matrix at the next time step, before the update.
    """

    next_state_cov_matrix = np.dot(state_transition_matrix, np.dot(
        current_state_cov_matrix, state_transition_matrix.T))
    return next_state_cov_matrix


def covariance_update(previous_state_cov_matrix, measurement_cov_matrix, observation_matrix, kg):
    """" Implementation of state update equation.

    Input parameters:
    previous_state_cov_matrix = state covariance matrix (defining the uncertainty in each of the estimates)
                                before the update step,
    measurement_cov_matrix = covariance matrix defining the uncertainty in each of the measurements,
    observation_matrix = matrix converting the measurement vector of the system into the
                         state vector,
    kg = Kalman gain (it weights the measurements).

    Returns:
    current_state_cov_matrix = state covariance matrix after the update step.
    """

    identity = np.identity(np.shape(previous_state_cov_matrix)[0])
    intermediate_calculation = identity - np.dot(kg, observation_matrix)

    current_state_cov_matrix = np.dot(np.dot(intermediate_calculation, previous_state_cov_matrix, ),
                                      intermediate_calculation.T) + np.dot(np.dot(kg, measurement_cov_matrix), kg.T)
    return current_state_cov_matrix
