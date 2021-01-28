import numpy as np
import kalman_equations as kalman
from matrix_utilities import is_symmetric

observation_matrix = np.array([[1, 0], [0, 1]])


def extrapolate_initial_state_guess(initial_state_guess, state_transition_matrix):
    """Implementation of state extrapolation equation, using the initial state guess as input.

    :param initial_state_guess: initial guess of all estimated states of the system,
    :param state_transition_matrix: matrix for the implementation of the dynamic model.

    :returns: next_state_vector: state vector at the next time step, before the first
              update process occurs."""

    next_state_vector = kalman.state_extrapolation(
        initial_state_guess.T, state_transition_matrix)
    return next_state_vector


def extrapolate_initial_state_cov_matrix(initial_state_cov_matrix, state_transition_matrix):
    """" Implementation of covariance extrapolation equation, using the initial
    state covariance matrix as input.

    :param initial_state_cov_matrix: state covariance matrix (defining the uncertainty in each
                                     of the initial guess estimates),
    :param state_transition_matrix: matrix for the implementation of the dynamic model.

    :returns: next_state_cov_matrix: state covariance matrix at the next time step,
              before the first update process occurs.
    """

    next_state_cov_matrix = kalman.covariance_extrapolation(
        initial_state_cov_matrix, state_transition_matrix)
    return next_state_cov_matrix


def simulation(initial_state_guess, initial_state_cov_matrix, measurements, measurement_cov_matrix,
               state_transition_matrix):
    """Implementation of the Kalman filter simulation:
    1. extrapolation of initial state guess and covariance matrix,
    2. implementation of the update step,
    3. implementation of the propagation step,
    4. repetition of the process (update of the propagated step and so on).

    Returns:
    output_simulation = array containing the estimated state vectors for each time step
                        (the state vector includes all estimated states of the system),
    output_simulation_uncertainty = array containing the state covariance matrices for each time step
                        (the state covariance matrix defines the uncertainty in each
                         of the estimated states).


    :param initial_state_guess: initial guess of all estimated states of the system,
    :param initial_state_cov_matrix: state covariance matrix (defining the uncertainty in each
                               of the initial guess estimates),
    :param measurements: array containing the measurement vectors for each time step
                   (the measurement vector stores all measured states),
    :param measurement_cov_matrix: covariance matrix defining the uncertainty in each of the measurements,
    :param state_transition_matrix: matrix for the implementation of the dynamic model.

    :returns: array of estimated state vectors, array of state covariance matrices"""

    output_simulation = []
    output_simulation_uncertainty = []

    if is_symmetric(initial_state_cov_matrix) is False or is_symmetric(measurement_cov_matrix) is False:
        raise ValueError('Covariance matrices are not symmetric')

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

        # Propagation step
        next_state_vector = kalman.state_extrapolation(
            current_state_vector, state_transition_matrix)
        next_state_cov_matrix = kalman.covariance_extrapolation(
            current_state_cov_matrix, state_transition_matrix)

        # Repeat the process
        previous_state_vector = next_state_vector
        previous_state_cov_matrix = next_state_cov_matrix
    return output_simulation, output_simulation_uncertainty
