from kalman_equations import state_extrapolation_equation


def test_state_extrapolation_equation():
    x = 30000
    v = 40
    delta_time = 5

    next_x, next_v = state_extrapolation_equation(x, v, delta_time)

    expected_x = 30200
    expected_v = 40

    assert next_x == expected_x
    assert next_v == expected_v