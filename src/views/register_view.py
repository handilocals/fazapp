import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout

class GalleryManagementWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Gallery Management")

        # Create layout
        layout = QVBoxLayout()

        # Add gallery list
        gallery_label = QLabel("Galleries:")
        self.gallery_list = QListWidget()
        layout.addWidget(gallery_label)
        layout.addWidget(self.gallery_list)

        # Add buttons
        add_gallery_button = QPushButton("Add Gallery")
        delete_gallery_button = QPushButton("Delete Gallery")
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_gallery_button)
        button_layout.addWidget(delete_gallery_button)
        layout.addLayout(button_layout)

        # Set window layout
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GalleryManagementWindow()
    window.show()
    sys.exit(app.exec_())