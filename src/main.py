import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FAZES")

        # Create menu bar
        self.menubar = self.menuBar()

        # Create file menu
        file_menu = self.menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create view menu
        view_menu = self.menubar.addMenu("View")

        # ... (add more menu items as needed)

        # Set central widget (placeholder)
        self.setCentralWidget(QWidget())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())