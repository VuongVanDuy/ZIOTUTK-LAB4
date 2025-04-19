from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Signal
from .view import Ui_Form
from config import DATA_SAMPLE_DIR, GENDER, LANGUAGES
import os
import random

class QCustomWidget(Ui_Form, QWidget):
    accepted = Signal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_list = []
        # Kết nối tín hiệu
        self.selectPathButton.clicked.connect(self.select_path)
        self.addButton.clicked.connect(self.add_file)
        self.removeButton.clicked.connect(self.remove_file)
        self.acceptButton.clicked.connect(self.accept_files)
        self.cancelButton.clicked.connect(self.close)
        self.autoSelectButton.clicked.connect(self.auto_select_files)

    def select_path(self):
        # Mở hộp thoại chọn file trong thư mục trong folder data_samples
        folder_path = DATA_SAMPLE_DIR
        selected_path = QFileDialog.getOpenFileNames(self, "Select Folder", folder_path, "All Files (*)")[0]
        if selected_path:
            self.pathLineEdit.setText(selected_path[0])
        else:
            QMessageBox.warning(self, "Warning", "No folder selected.")

    def random_select_file(self, gender, language):
        folder_path = os.path.join(DATA_SAMPLE_DIR, gender, language)
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            QMessageBox.warning(self, "Warning", "Files not found in required folders.")
            return

        try:
            selected_file = random.choice(files)
            full_path_file = os.path.join(folder_path, selected_file)
            self.fileListWidget.addItem(full_path_file)
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Error selecting files: " + str(e))

    def auto_select_files(self):
        self.random_select_file(GENDER[0], LANGUAGES[0])
        self.random_select_file(GENDER[0], LANGUAGES[1])
        self.random_select_file(GENDER[1], LANGUAGES[2])
        self.random_select_file(GENDER[1], LANGUAGES[3])


    def add_file(self):
        name = self.pathLineEdit.text().strip()
        if name:
            self.fileListWidget.addItem(name)
            self.pathLineEdit.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a file name to add.")

    def remove_file(self):
        idx = self.fileListWidget.currentRow()
        if idx >= 0:
            self.fileListWidget.takeItem(idx)
        else:
            QMessageBox.warning(self, "Warning", "Please select a file to remove.")

    def accept_files(self):
        if not self.fileListWidget.count():
            QMessageBox.critical(self, "Error", "No file to choose.")
            return

        self.file_list = [self.fileListWidget.item(i).text() for i in range(self.fileListWidget.count())]
        self.accepted.emit(self.file_list)
        self.close()

    def close(self):
        self.deleteLater()
        super().close()


if __name__ == "__main__":
    app = QApplication([])
    window = QCustomWidget()
    window.show()
    app.exec()
