import json
import sys
import matplotlib.pyplot as plt
from parse_input_parameters import parse_simulation_inputs, parse_plot_estimates, parse_plot_uncertainty, parse_plot_measurements
from kalman_simulation import simulation
from visualization import plot_output


with open(sys.argv[1]) as json_data:
    input_data = json.load(json_data)

    parsed_input_data = parse_simulation_inputs(input_data)
    output_state, output_uncertainty = simulation(parsed_input_data['initial_state_guess'],
                                                  parsed_input_data['initial_state_cov_matrix'],
                                                  parsed_input_data['measurements'],
                                                  parsed_input_data['measurement_cov_matrix'],
                                                  parsed_input_data['state_transition_matrix'])
    fig = plot_output(parse_plot_estimates(output_state), parse_plot_uncertainty(output_uncertainty),
                      parse_plot_measurements(parsed_input_data['measurements']))
    plt.show()
