import random
import pytest
import kalman_equations as kalman


def test_state_extrapolation():
    current_estimate_x = 30000
    current_estimate_v = 40
    delta_time = 5

    next_estimate_x, next_estimate_v = kalman.state_extrapolation(
        current_estimate_x, current_estimate_v, delta_time)

    expected_x = 30200
    expected_v = 40

    assert next_estimate_x == expected_x
    assert next_estimate_v == expected_v


def build_test_state_update_by_kg(kg, expected_x, expected_v):
    previous_estimate_x = 30000
    previous_estimate_v = 40
    measure = 30095
    delta_time = 5

    current_estimate_x, current_estimate_v = kalman.state_update(
        previous_estimate_x, previous_estimate_v, measure,
        delta_time, kg)

    assert current_estimate_x == expected_x
    assert current_estimate_v == expected_v


def test_state_update():
    build_test_state_update_by_kg(0.5, 30047.5, 49.5)


def test_state_update_kg_0():
    build_test_state_update_by_kg(0, 30000, 40)


def test_state_update_kg_1():
    build_test_state_update_by_kg(1, 30095, 59)


def test_kalman_gain_range():
    for i in range(0, 10000):
        previous_estimate_uncertainty_x = random.uniform(0.1, 10000)
        measure_uncertainty_x = random.uniform(0.1, 10000)
        kg = kalman.kalman_gain(previous_estimate_uncertainty_x, measure_uncertainty_x)

        assert kg >= 0
        assert kg <= 1


def test_kalman_gain_zero_division():
    previous_estimate_uncertainty_x = 0
    measure_uncertainty_x = 0

    with pytest.raises(ZeroDivisionError):
        kalman.kalman_gain(previous_estimate_uncertainty_x, measure_uncertainty_x)


def test_estimate_uncertainty_extrapolation():
    current_estimate_uncertainty_x = 10000
    current_estimate_uncertainty_v = 100
    delta_time = 5

    next_estimate_uncertainty_x, next_estimate_uncertainty_v = kalman.estimate_uncertainty_extrapolation(
        current_estimate_uncertainty_x, current_estimate_uncertainty_v, delta_time)

    expected_x = 12500
    expected_v = 100

    assert next_estimate_uncertainty_x == expected_x
    assert next_estimate_uncertainty_v == expected_v


def build_test_estimate_uncertainty_update_by_kg(kg, expected_x, expected_v):
    previous_estimate_uncertainty_x = 10000
    previous_estimate_uncertainty_v = 100

    current_estimate_uncertainty_x, current_estimate_uncertainty_v = kalman.estimate_uncertainty_update(
        previous_estimate_uncertainty_x, previous_estimate_uncertainty_v, kg)

    assert current_estimate_uncertainty_x == expected_x
    assert current_estimate_uncertainty_v == expected_v


def test_estimate_uncertainty_update():
    build_test_estimate_uncertainty_update_by_kg(0.5, 5000, 50)


def test_estimate_uncertainty_update_kg_0():
    build_test_estimate_uncertainty_update_by_kg(0, 10000, 100)


def test_estimate_uncertainty_update_kg_1():
    build_test_estimate_uncertainty_update_by_kg(1, 0, 0)