const add_button = document.getElementById('add')
const remove_button = document.getElementById('remove')
const measurement_container = document.getElementById('measurements')
const start = document.getElementById('start')

add_button.addEventListener("click", function () {
    const measurement = document.createElement('div')
    measurement.innerHTML = '<input/> <input/>'
    measurement_container.append(measurement)
})

remove_button.addEventListener("click", function () {
    if (measurement_container.childElementCount > 5) {
        measurement_container.removeChild(measurement_container.lastElementChild)
    }
})


function input_parameters_as_json() {
    const initial_guess_position = parseFloat(document.getElementById('initial_guess_position').value)
    const initial_guess_velocity = parseFloat(document.getElementById('initial_guess_velocity').value)
    const initial_guess_pos_variance = parseFloat(document.getElementById("initial_guess_pos_variance").value)
    const initial_guess_vel_variance = parseFloat(document.getElementById("initial_guess_pos_variance").value)
    const initial_guess_covariance1 = parseFloat(document.getElementById('initial_guess_covariance1').value)
    const initial_guess_covariance2 = parseFloat(document.getElementById('initial_guess_covariance2').value)
    const delta_time = parseFloat(document.getElementById('delta_time').value)
    const measurement_pos_variance = parseFloat(document.getElementById("measurement_pos_variance").value)
    const measurement_vel_variance = parseFloat(document.getElementById("measurement_pos_variance").value)
    const measurement_covariance1 = parseFloat(document.getElementById('measurement_covariance1').value)
    const measurement_covariance2 = parseFloat(document.getElementById('measurement_covariance2').value)

    const rows = measurement_container.querySelectorAll("div")
    const measurements = []
    for (const row of rows) {
        const inputs = Array.from(row.querySelectorAll("input"))
        measurements.push([parseFloat(inputs[0].value), parseFloat(inputs[1].value)])
    }

    const initial_state_guess = [initial_guess_position, initial_guess_velocity]
    const initial_state_cov_matrix = [[initial_guess_pos_variance, initial_guess_covariance1],
        [initial_guess_covariance2, initial_guess_vel_variance]]
    const state_transition_matrix = [[1, delta_time], [0, 1]]
    const measurement_cov_matrix = [[measurement_pos_variance, measurement_covariance1],
        [measurement_covariance2, measurement_vel_variance]]


    return {
        initial_state_guess,
        initial_state_cov_matrix,
        state_transition_matrix,
        measurement_cov_matrix,
        measurements

    }
}


start.addEventListener("click", async function () {
    const input_parameters = input_parameters_as_json()
    const response = await fetch('/plot', {
        method: 'POST', body: JSON.stringify(input_parameters),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    const plot = await response.blob()
    const plot_url = URL.createObjectURL(plot)
    const plot_container = document.getElementById('plot')
    plot_container.innerHTML = `<img src="${plot_url}">`
})
