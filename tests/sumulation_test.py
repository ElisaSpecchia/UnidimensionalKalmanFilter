import numpy as np
import pytest
from kalman_simulation import simulation


def test_simulation():
    initial_state_guess = np.array([300, 5])
    initial_state_cov_matrix = np.array([[0, 0], [0, 0]])
    measurements = np.array([[355, 5.5], [402, 4.9]])
    measurement_cov_matrix = np.array([[25, 0], [0, 1]])
    state_transition_matrix = np.array([[1, 10], [0, 1]])

    position_estimate, velocity_estimate = simulation(initial_state_guess, initial_state_cov_matrix,
                                                      measurements, measurement_cov_matrix, state_transition_matrix)

    expected_position, expected_velocity = [np.array([[350], [5]]), np.array([[400], [5]])], [np.array(
        [[0, 0], [0, 0]]), np.array([[0, 0], [0, 0]])]

    assert np.array_equal(position_estimate, expected_position)
    assert np.array_equal(velocity_estimate, expected_velocity)


def test_initial_state_cov_matrix_not_symmetric():
    initial_state_guess = np.array([300, 5])
    initial_state_cov_matrix = np.array([[100, 10], [0, 4]])
    measurements = np.array([[355, 5.5], [402, 4.9]])
    measurement_cov_matrix = np.array([[25, 0], [0, 1]])
    state_transition_matrix = np.array([[1, 10], [0, 1]])

    with pytest.raises(ValueError):
        simulation(initial_state_guess, initial_state_cov_matrix, measurements, measurement_cov_matrix,
                   state_transition_matrix)


def test_measurement_cov_matrix_not_symmetric():
    initial_state_guess = np.array([300, 5])
    initial_state_cov_matrix = np.array([[100, 0], [0, 4]])
    measurements = np.array([[355, 5.5], [402, 4.9]])
    measurement_cov_matrix = np.array([[25, 3], [0, 1]])
    state_transition_matrix = np.array([[1, 10], [0, 1]])

    with pytest.raises(ValueError):
        simulation(initial_state_guess, initial_state_cov_matrix, measurements, measurement_cov_matrix,
                   state_transition_matrix)
