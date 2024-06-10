import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Converter")

        # Creating GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Frame to hold input widgets
        input_frame = ttk.Frame(self.master)
        input_frame.pack(padx=10, pady=10)

        # Entry for temperature input
        self.temp_entry = ttk.Entry(input_frame, width=10, font=('Helvetica', 12))
        self.temp_entry.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown for selecting conversion type
        self.conversion_type = ttk.Combobox(input_frame, values=["Fahrenheit to Celsius", "Celsius to Fahrenheit"], state="readonly", font=('Helvetica', 12))
        self.conversion_type.grid(row=0, column=1, padx=5, pady=5)
        self.conversion_type.current(0)

        # Button to perform conversion
        self.convert_button = ttk.Button(input_frame, text="Convert", command=self.convert, width=10)
        self.convert_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame to hold result label
        result_frame = ttk.Frame(self.master)
        result_frame.pack(padx=10, pady=5)

        # Label to display result
        self.result_label = ttk.Label(result_frame, text="", font=('Helvetica', 12))
        self.result_label.pack()

    def convert(self):
        try:
            temperature = float(self.temp_entry.get())
            conversion_index = self.conversion_type.current()

            if conversion_index == 0:  # Fahrenheit to Celsius
                converted_temp = (temperature - 32) * 5/9
                result_text = f"{temperature:.2f}°F = {converted_temp:.2f}°C"
            else:  # Celsius to Fahrenheit
                converted_temp = (temperature * 9/5) + 32
                result_text = f"{temperature:.2f}°C = {converted_temp:.2f}°F"

            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Invalid input")

def main():
    root = tk.Tk()
    root.geometry("300x150")
    temperature_converter = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
