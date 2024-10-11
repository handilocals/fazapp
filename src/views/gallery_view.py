import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Login")

        # Create layout
        layout = QVBoxLayout()

        # Add logo and title
        logo_label = QLabel("Face.ai Logo")  # Replace with your logo
        layout.addWidget(logo_label)

        title_label = QLabel("Welcome to face.ai")
        title_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        layout.addWidget(title_label)

        # Add username and password fields
        username_label = QLabel("Username:")
        self.username_edit = QLineEdit()
        username_layout = QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_edit)
        layout.addLayout(username_layout)

        password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_edit)
        layout.addLayout(password_layout)

        # Add sign in button
        sign_in_button = QPushButton("Sign In")
        layout.addWidget(sign_in_button)

        # Set window layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())