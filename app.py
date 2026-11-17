import sys

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
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

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout.addWidget(self.canvas, stretch=1)

        self.setCentralWidget(central_widget)

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

    def about(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()