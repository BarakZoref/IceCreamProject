
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 1. Main Window Setup
        self.setWindowTitle("About Me")
        self.setFixedSize(350, 480)
        self.setStyleSheet('background-color: darkslategray; font-family: Arial')

        # 2. Profile Image Label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 40, 150, 150)
        pixmap = QPixmap("profile_image.jpg")
        self.image_label.setPixmap(pixmap.scaled(150, 150,))

        # 3. Name Label
        self.name_label = QLabel("Barak Zoref", self)
        self.name_label.setGeometry(0, 210, 350, 40)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet("color: white; font-size: 26px; font-weight: bold;")

        # 4. Subtitle Label
        self.subtitle_label = QLabel("Mechanical Engineering Student\nAfeka Academic College", self)
        self.subtitle_label.setGeometry(0, 250, 350, 40)
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setStyleSheet("color: white; font-size: 15px;")

        # 5. Email Label 
        self.email_label = QLabel("📧 zorefbarak@gmail.com", self)
        self.email_label.setGeometry(0, 320, 350, 30)
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_label.setStyleSheet("color: white; font-size: 16px;")

        # 6. LinkedIn Label 
        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/barakzoref/" style="color: lightgreen; text-decoration: none; font-size: 15px;">LinkedIn Profile</a>', self)
        self.linkedin_label.setGeometry(0, 360, 350, 30)
        self.linkedin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkedin_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel(
            '<a href="https://github.com/BarakZoref/IceCreamProject" '
            'style="color: lightgreen; text-decoration: none; font-size: 15px;">'
            'GitHub Project</a>',
            self,
        )
        self.github_label.setGeometry(0, 390, 350, 30)
        self.github_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.github_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.github_label.setOpenExternalLinks(True)

if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()