from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox, QFileDialog
from PySide6.QtCore import QTimer, QThread, Signal
from .view import Ui_MainWindow
from customWidgets.controller import QCustomWidget
from model.generator import GeneratorNoise
from config import FREQ, DURATION, DIR
import os
import sys
import soundfile as sf
import sounddevice as sd
import time
import numpy as np

class GeneratorThread(QThread):
    finished = Signal()

    def __init__(self, generator):
        super().__init__()
        self.generator = generator

    def run(self):
        self.generator.generate()
        self.finished.emit()

class MainHandle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Noise Generator")

        # Initialize variables
        self.output_file_noise = None
        self.generator = None
        self.thread = None

        # Button connections
        self.btnChooseFile.clicked.connect(self.show_custom_widget)
        self.generateButton.clicked.connect(self.generate_noise)
        self.playNoiseButton.clicked.connect(self.on_play_noise)
        self.showSpectrumButton.clicked.connect(self.show_spectrum)
        self.compareButton.clicked.connect(self.show_compare_with_user_voice)
        self.btnRecord.clicked.connect(self.start_recording)
        self.btnChoose.clicked.connect(self.choose_file_voice_user)
        self.btnPlayVoice.clicked.connect(self.play_voice)
        self.radioButtonRecord.toggled.connect(self.changeRadioBtnRecord)
        self.pathSaveVoice.textChanged.connect(self.changeLabelPathVoice)

    def show_custom_widget(self):
        self.custom_widget = QCustomWidget()
        self.custom_widget.show()
        self.custom_widget.accepted.connect(self.set_list_widget)

    def set_list_widget(self, file_list):
        if not file_list:
            QMessageBox.warning(self, "Warning", "No files selected.")
            return
        self.listWidget.clear()
        self.set_sate_btns([self.playNoiseButton, self.showSpectrumButton], False)
        # set 0 for progress bar
        self.progressBar.setValue(0)
        # quit thread if it is running
        if isinstance(self.thread, QThread):
            del self.thread
            self.thread = None
        if isinstance(self.generator, GeneratorNoise):
            del self.generator
            self.generator = None

        for file in file_list:
            item = QListWidgetItem(file)
            self.listWidget.addItem(item)

    def update_progress(self, start_time):
        elapsed = time.time() - start_time
        progress = min(int((elapsed / 10) * 100), 100)
        self.progressBar.setValue(progress)
        QApplication.processEvents()
        return progress < 100

    def generate_noise(self):
        # Get selected voice files
        voices_path = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        if not voices_path:
            return

        # Read slider values
        volume_voice = self.voiceVolumeSlider.value() / 100.0
        volume_noise = self.noiseVolumeSlider.value() / 100.0

        # Generate noise
        self.generator = GeneratorNoise(voices_path=voices_path, fs=None,
                                        volume_voice=volume_voice, volume_noise=volume_noise)

        start_time = time.time()

        # Update progress while generating
        timer = QTimer()
        timer.timeout.connect(lambda: self.update_progress(start_time))
        timer.start(100)  # Update every 100ms

        # Run the generator in a separate thread
        self.thread = GeneratorThread(self.generator)
        self.thread.finished.connect(lambda: timer.stop())
        self.thread.finished.connect(lambda: self.progressBar.setValue(100))
        self.thread.finished.connect(lambda: self.set_sate_btns(
            [self.playNoiseButton, self.showSpectrumButton, self.compareButton], True))
        self.output_file_noise = os.path.join(DIR, 'output_noise.wav')
        self.thread.finished.connect(lambda: self.generator.save_to_file(
            self.output_file_noise, self.generator.noise))
        self.thread.start()

    def on_play_noise(self):
        if self.output_file_noise:
            self.play_noise_media(self.output_file_noise)
        else:
            print("No output file to play.")

    def play_noise_media(self, file_path):
        # Absolute path & existence
        abs_path = os.path.abspath(file_path)
        if not os.path.exists(abs_path):
            print(f"File not found: {abs_path}")
            return

        print(f"Attempting to play file: {abs_path}")

        try:
            data, samplerate = sf.read(abs_path)
            print("▶️ Playing audio...")
            sd.play(data, samplerate)
            sd.wait()  # Wait until playback is finished
        except Exception as e:
            print(f"Error playing audio: {e}")

    def show_spectrum(self):
        if self.generator:
            self.generator.amplitude_spectrum()

    def show_compare_with_user_voice(self):
        # Open the image file and set to page_1 of stack widget
        if self.generator:
            voice_file = self.pathSaveVoice.text().strip()
            self.generator.compare_with_user_voice(voice_file=voice_file)
        else:
            QMessageBox.warning(self, "Warning", "No generated noise to compare with.")

    def changeRadioBtnRecord(self):
        if self.radioButtonRecord.isChecked():
            self.btnRecord.setEnabled(True)
            self.btnChoose.setEnabled(False)
        else:
            self.btnRecord.setEnabled(False)
            self.btnChoose.setEnabled(True)

    def changeLabelPathVoice(self):
        if not self.pathSaveVoice.text():
            self.compareButton.setEnabled(False)
            self.btnPlayVoice.setEnabled(False)
        else:
            self.compareButton.setEnabled(True)
            self.btnPlayVoice.setEnabled(True)

    def start_recording(self):
        try:
            self.statusBar().showMessage("Start recording ...")
            # Show a message box to indicate recording has started
            recording_message = QMessageBox(self)
            recording_message.setWindowTitle("Recording")
            recording_message.setText("Recording in progress... Close this window to stop.")
            recording_message.setStandardButtons(QMessageBox.Ok)
            recording_message.show()

            # Start recording audio
            recording = []
            stream = sd.InputStream(samplerate=FREQ, channels=1, callback=lambda indata, frames, time, status: recording.append(indata.copy()))
            with stream:
                while recording_message.isVisible():
                    QApplication.processEvents()
                    sd.sleep(100)
            # Close the message box
            recording_message.close()

            # Stop recording and process the data
            self.statusBar().showMessage("Recording finished.")
            recording = np.concatenate(recording, axis=0)

            # Open a dialog for the user to choose a save location
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Recording", DIR, "WAV Files (*.wav)")
            if file_path:
                sf.write(file_path, recording, FREQ)
                self.pathSaveVoice.setText(file_path)
                QMessageBox.information(self, "Success", f"Recording saved to `{file_path}`")
            else:
                QMessageBox.information(self, "Cancelled", "Save operation cancelled.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Recording error: {e}")

    def choose_file_voice_user(self):
        folder_path = DIR
        selected_path = QFileDialog.getOpenFileName(self, "Select File", folder_path, "WAV Files (*.wav)")[0]
        if selected_path:
            self.pathSaveVoice.setText(selected_path)
        else:
            QMessageBox.warning(self, "Warning", "No file selected.")

    def play_voice(self):
        path_file = self.pathSaveVoice.text().strip()
        if not path_file:
            QMessageBox.warning(self, "Warning", "No file to play.")
            return

        abs_path = os.path.abspath(path_file)
        if not os.path.exists(path_file):
            print(f"File not found: {abs_path}")
            return

        print(f"Attempting to play file: {abs_path}")

        try:
            data, samplerate = sf.read(abs_path)
            print("▶️ Playing audio...")
            sd.play(data, samplerate)
            sd.wait()  # Wait until playback is finished
        except Exception as e:
            print(f"Error playing audio: {e}")

    def set_sate_btns(self, list_btns, state=True):
        for btn in list_btns:
            btn.setEnabled(state)

    def reset_app(self):
        self.listWidget.clear()
        self.pathSaveVoice.clear()
        self.set_sate_btns([self.playNoiseButton, self.showSpectrumButton, self.compareButton], False)
        self.progressBar.setValue(0)
        self.voiceVolumeSlider.setValue(40)
        self.noiseVolumeSlider.setValue(10)
        if isinstance(self.thread, QThread):
            del self.thread
            self.thread = None
        if isinstance(self.generator, GeneratorNoise):
            del self.generator
            self.generator = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainHandle()
    window.show()
    sys.exit(app.exec())
