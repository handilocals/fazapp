import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

class EnrollmentWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Enrollment")

        # Create layout
        layout = QVBoxLayout()

        # Add instructions
        instructions_label = QLabel("Enter your name and select a photo to enroll.")
        layout.addWidget(instructions_label)

        # Add name input
        name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_edit)
        layout.addLayout(name_layout)

        # Add photo selection
        photo_label = QLabel("Photo:")
        self.photo_path_edit = QLineEdit()
        select_photo_button = QPushButton("Select Photo")

        select_photo_button.clicked.connect(self.select_photo)

        photo_layout = QHBoxLayout()
        photo_layout.addWidget(photo_label)
        photo_layout.addWidget(self.photo_path_edit)
        photo_layout.addWidget(select_photo_button)
        layout.addLayout(photo_layout)

        # Add enroll button
        enroll_button = QPushButton("Enroll")
        layout.addWidget(enroll_button)

        # Set window layout
        self.setLayout(layout)

    def select_photo(self):
        # Implement logic to open file dialog and get photo path
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", "Image Files (*.jpg; *.png)")
        if file_name:
            self.photo_path_edit.setText(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnrollmentWindow()
    window.show()
    sys.exit(app.exec_())