from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        self.combobox = QComboBox()
        self.combobox.addItems(['Metric (km)', 'Imperial (miles)'])

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combobox, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        hours = float(self.time_line_edit.text())

        avg_speed = round((distance / hours), 2)
        if self.combobox.currentText() == "Metric (km)":
            unit = "km/h"
        if self.combobox.currentText() == "Imperial (miles)":
            unit = "mi/h"

        self.output_label.setText(f"Average speed: {avg_speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
