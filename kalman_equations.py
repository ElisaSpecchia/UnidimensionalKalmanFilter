def state_extrapolation_equation(x, v, delta_time):
    next_x = x + v * delta_time
    next_v = v
    return next_x, next_v

