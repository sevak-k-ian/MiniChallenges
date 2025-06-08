from nicegui import ui
import functions

# Title
ui.label('Metric Converter!').style('font-size: 200%;font-weight: bold')

# Functions
def convert():
    try:
        result_meter = functions.convert_to_meter(float(feet_input.value), float(inch_input.value))
        result_label.set_text(f"The result is: {round(result_meter, 2)} meters.")
    except ValueError:
        ui.notify("❗ Please enter valid whole numbers (integers) in both input fields.")

# Page layout
with ui.row():
    with ui.column():
        with ui.row():
            feet_input = ui.input('Enter feet', placeholder="Float numbers")
            inch_input = ui.input('Enter inch', placeholder="Float numbers")
        result_label = ui.label("").style('font-size: 130%; font-weight: bold')

    with ui.column():
        convert_btn = ui.button('Convert',
                                on_click=convert)

# Run the app
ui.run()
