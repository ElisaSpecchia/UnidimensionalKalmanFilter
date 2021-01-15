import numpy as np
from kalman_simulation import simulation


def test_simulation():
    initial_state_guess = np.array([[30000, 40]])
    initial_state_cov_matrix = np.array([[100, 0], [0, 25]])
    measurements = np.array([[30200, 40], [30400, 40]])
    measurement_cov_matrix = np.array([[100, 0], [0, 25]])
    state_transition_matrix = np.array([[1, 5], [0, 1]])

    simulation_result = simulation(initial_state_guess, initial_state_cov_matrix, measurements,
                                   measurement_cov_matrix, state_transition_matrix)

    expected_output = np.array([[[30200], [40]], [[30400], [40]]]), np.array(
        [[[206.25, 31.25], [31.25, 12.5]], [[232.938, 23.437], [23.437, 9.275]]])

    np.array_equal(simulation_result, expected_output)
