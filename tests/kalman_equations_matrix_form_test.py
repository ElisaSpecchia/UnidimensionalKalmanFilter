import numpy as np
import kalman_equations as kalman
import pytest


def test_state_extrapolation():
    current_state_vector = np.array([[30000], [40]])
    state_transition_matrix = np.array([[1, 5], [0, 1]])

    next_state_vector = kalman.state_extrapolation(
        current_state_vector, state_transition_matrix)

    expected_output = np.array([[30200], [40]])

    assert np.array_equal(next_state_vector, expected_output)


def build_test_state_update_by_kg_only_position_measurements(kg, expected_output):
    previous_state_vector = np.array([[30000], [40]])
    measurements = np.array([[30095]])
    observation_matrix = np.array([[1, 0]])

    current_state_vector = kalman.state_update(previous_state_vector, measurements, observation_matrix, kg)

    assert np.array_equal(current_state_vector, expected_output)


def test_state_update_only_position_measurements():
    build_test_state_update_by_kg_only_position_measurements(
        np.array([[0.5], [0]]), np.array([[30047.5], [40]]))


def test_state_update_kg_0_only_position_measurements():
    build_test_state_update_by_kg_only_position_measurements(
        np.array([[0], [0]]), np.array([[30000], [40]]))


def test_state_update_kg_1_only_position_measurements():
    build_test_state_update_by_kg_only_position_measurements(
        np.array([[1], [0]]), np.array([[30095], [40]]))


def build_test_state_update_by_kg(kg, expected_output):
    previous_state_vector = np.array([[30000], [40]])
    measurements = np.array([[30095], [58]])
    observation_matrix = np.array([[1, 0], [0, 1]])

    current_state_vector = kalman.state_update(previous_state_vector, measurements, observation_matrix, kg)

    assert np.array_equal(current_state_vector, expected_output)


def test_state_update():
    build_test_state_update_by_kg(np.array([[0.5, 0], [0, 0.5]]), np.array([[30047.5], [49]]))


def test_state_update_kg_0():
    build_test_state_update_by_kg(np.array([[0, 0], [0, 0]]), np.array([[30000], [40]]))


def test_state_update_kg_1():
    build_test_state_update_by_kg(np.array([[1, 0], [0, 1]]), np.array([[30095], [58]]))


def test_kalman_gain():
    previous_state_cov_matrix = np.array([[100, 0], [0, 25]])
    measurement_cov_matrix = np.array([[100, 0], [0, 25]])
    observation_matrix = np.array([[1, 0], [0, 1]])

    kg = kalman.kalman_gain(
        previous_state_cov_matrix, measurement_cov_matrix, observation_matrix)

    expected_output = np.array([[0.5, 0], [0, 0.5]])
    assert np.array_equal(kg, expected_output)


def test_kalman_gain_is_1():
    previous_state_cov_matrix = np.array([[100, 0], [0, 25]])
    measurement_cov_matrix = np.array([[0, 0], [0, 0]])
    observation_matrix = np.array([[1, 0], [0, 1]])

    kg = kalman.kalman_gain(
        previous_state_cov_matrix, measurement_cov_matrix, observation_matrix)

    expected_output = np.array([[1, 0], [0, 1]])
    assert np.array_equal(kg, expected_output)


def test_kalman_gain_is_0():
    previous_state_cov_matrix = np.array([[0, 0], [0, 0]])
    measurement_cov_matrix = np.array([[100, 0], [0, 25]])
    observation_matrix = np.array([[1, 0], [0, 1]])

    kg = kalman.kalman_gain(
        previous_state_cov_matrix, measurement_cov_matrix, observation_matrix)

    expected_output = np.array([[0, 0], [0, 0]])
    assert np.array_equal(kg, expected_output)


def test_covariance_extrapolation():
    current_state_cov_matrix = np.array([[100, 0], [0, 25]])
    state_transition_matrix = np.array([[1, 5], [0, 1]])

    next_state_cov_matrix = kalman.covariance_extrapolation(
        current_state_cov_matrix, state_transition_matrix)

    expected_output = np.array([[725, 125], [125, 25]])

    assert np.array_equal(next_state_cov_matrix, expected_output)


def test_covariance_update():
    previous_state_cov_matrix = np.array([[100, 0], [0, 25]])
    measurement_cov_matrix = np.array([[100, 0], [0, 25]])
    observation_matrix = np.array([[1, 0], [0, 1]])
    kg = np.array([[0.5, 0], [0, 0.5]])

    current_state_cov_matrix = kalman.covariance_update(
        previous_state_cov_matrix, measurement_cov_matrix,
        observation_matrix, kg)

    expected_output = np.array([[50, 0], [0, 12.5]])

    assert np.array_equal(current_state_cov_matrix, expected_output)


def test_covariance_update_kg_1():
    previous_state_cov_matrix = np.array([[100, 0], [0, 25]])
    measurement_cov_matrix = np.array([[0, 0], [0, 0]])
    observation_matrix = np.array([[1, 0], [0, 1]])
    kg = np.array([[1, 0], [0, 1]])

    current_state_cov_matrix = kalman.covariance_update(
        previous_state_cov_matrix, measurement_cov_matrix,
        observation_matrix, kg)

    expected_output = np.array([[0, 0], [0, 0]])

    assert np.array_equal(current_state_cov_matrix, expected_output)


def test_covariance_update_kg_0():
    previous_state_cov_matrix = np.array([[0, 0], [0, 0]])
    measurement_cov_matrix = np.array([[100, 0], [0, 25]])
    observation_matrix = np.array([[0, 0], [0, 0]])
    kg = np.array([[0, 0], [0, 0]])

    current_state_cov_matrix = kalman.covariance_update(
        previous_state_cov_matrix, measurement_cov_matrix,
        observation_matrix, kg)

    expected_output = np.array([[0, 0], [0, 0]])

    assert np.array_equal(current_state_cov_matrix, expected_output)

