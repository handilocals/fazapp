import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Dashboard")

        # Create layout
        layout = QVBoxLayout()

        # Add welcome message
        welcome_label = QLabel("Welcome to the Dashboard")
        layout.addWidget(welcome_label)

        # Add buttons for navigation
        enroll_button = QPushButton("Enroll")
        recognize_button = QPushButton("Recognize")
        gallery_button = QPushButton("Gallery")
        settings_button = QPushButton("Settings")

        button_layout = QHBoxLayout()
        button_layout.addWidget(enroll_button)
        button_layout.addWidget(recognize_button)
        button_layout.addWidget(gallery_button)
        button_layout.addWidget(settings_button)

        layout.addLayout(button_layout)

        # Set window layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())