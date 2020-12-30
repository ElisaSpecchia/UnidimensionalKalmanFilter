def state_extrapolation(current_estimate_x, current_estimate_v, delta_time):
    next_estimate_x = current_estimate_x + current_estimate_v * delta_time
    next_estimate_v = current_estimate_v
    return next_estimate_x, next_estimate_v


def state_update(previous_estimate_x, previous_estimate_v, measure, delta_time, kg):
    current_estimate_x = previous_estimate_x + kg * (measure - previous_estimate_x)
    current_estimate_v = previous_estimate_v + kg * ((measure - previous_estimate_x) / delta_time)
    return current_estimate_x, current_estimate_v


def kalman_gain(previous_estimate_uncertainty_x, measure_uncertainty_x):
    kg = previous_estimate_uncertainty_x / (previous_estimate_uncertainty_x + measure_uncertainty_x)
    return kg


def estimate_uncertainty_extrapolation(current_estimate_uncertainty_x, current_estimate_uncertainty_v, delta_time):
    next_estimate_uncertainty_x = current_estimate_uncertainty_x + (delta_time ** 2) * current_estimate_uncertainty_v
    next_estimate_uncertainty_v = current_estimate_uncertainty_v
    return next_estimate_uncertainty_x, next_estimate_uncertainty_v


def estimate_uncertainty_update(previous_estimate_uncertainty_x, previous_estimate_uncertainty_v, kg):
    current_estimate_uncertainty_x = (1 - kg) * previous_estimate_uncertainty_x
    current_estimate_uncertainty_v = (1 - kg) * previous_estimate_uncertainty_v
    return current_estimate_uncertainty_x, current_estimate_uncertainty_v
