import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QLabel,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.temperatures = []
        self.revenues = []
        self.selected_file = ''
 

        self.setWindowTitle("Ice Cream Project")
        self.resize(800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)
        layout.addWidget(self.load_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about)
        layout.addWidget(self.about_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.draw_initial_graph()
        self.canvas = FigureCanvasQTAgg(self.fig)
        layout.addWidget(self.canvas, stretch=1)

        self.setCentralWidget(central_widget)

    def draw_initial_graph(self):
        data_x = np.linspace(-10, 10, 21)
        data_y = data_x**2
        self.ax.plot(data_x, data_y)

    def load_file(self):
        selected_file, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "CSV files (*.csv);;All files (*)",
        )
        if not selected_file:
            return

        self.selected_file = selected_file
        with open(self.selected_file, 'r') as f:
            next(f) # מקדם בשורה אחת
            for line in f:
                parts = line.split(',')
                self.temperatures.append(float(parts[0]))
                self.revenues.append(int(parts[1]))
        self.draw_graph()

    def draw_graph(self):
        self.ax.clear()
        self.ax.set_title("Revenues for different temperatures")
        self.ax.set_xlabel('Temperature', fontsize=14)
        self.ax.set_ylabel('Revenue', fontsize=14)
        self.ax.scatter(self.temperatures, self.revenues, label='Data', s=1,
                color='blue', marker='x')

        # Add Labels and Legend
        self.canvas.draw()

    def about(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()