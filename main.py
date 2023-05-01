from widgets.MainWindow import MainWindow
from ui.ui_MainWindow import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())