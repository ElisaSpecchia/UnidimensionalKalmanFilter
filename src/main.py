from flask import Flask, send_file, Response, request
from visualization import plot_output
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from parse_input_parameters import parse_simulation_inputs, parse_plot_estimates, parse_plot_uncertainty, parse_plot_measurements
from kalman_simulation import simulation


# initialize the server
app = Flask(__name__, static_folder='../assets', static_url_path='')


# home route returns information from index.html
@app.route('/')
def home():
    return send_file('../assets/index.html')


# plot route runs the simulation and returns a plot
@app.route('/plot', methods=['POST'])
def create_plot():
    input_data = request.json
    parsed_input_data = parse_simulation_inputs(input_data)
    output_state, output_uncertainty = simulation(parsed_input_data['initial_state_guess'],
                                                  parsed_input_data['initial_state_cov_matrix'],
                                                  parsed_input_data['measurements'],
                                                  parsed_input_data['measurement_cov_matrix'],
                                                  parsed_input_data['state_transition_matrix'])
    fig = plot_output(parse_plot_estimates(output_state), parse_plot_uncertainty(output_uncertainty),
                      parse_plot_measurements(parsed_input_data['measurements']))

    # return the plot to the client
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run()