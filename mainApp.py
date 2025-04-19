from mainWidgetApp.controller import MainHandle
from PySide6.QtWidgets import QApplication
import sys

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.main_window = MainHandle()
        self.main_window.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())
