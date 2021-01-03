from flask import Flask, send_file, Response, request
from visualization import plot_output
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from parse_input_parameters import parse_parameters, parse_plot_inputs, parse_plot_uncertainty, parse_plot_measurements
from kalman_simulation import simulation

app = Flask(__name__, static_folder='assets', static_url_path='')


@app.route('/')
def home():
    return send_file('assets/index.html')


@app.route('/plot', methods=['POST'])
def create_plot():
    input_data = request.json
    parsed_input_data = parse_parameters(input_data)
    output_state, output_uncertainty = simulation(parsed_input_data['initial_state_guess'],
                                                  parsed_input_data['initial_state_cov_matrix'],
                                                  parsed_input_data['measurements'],
                                                  parsed_input_data['measurement_cov_matrix'],
                                                  parsed_input_data['state_transition_matrix'])
    fig = plot_output(parse_plot_inputs(output_state), parse_plot_uncertainty(output_uncertainty),
                      parse_plot_measurements(parsed_input_data['measurements']))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run()