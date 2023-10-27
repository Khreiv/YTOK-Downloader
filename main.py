from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import QCoreApplication
import sys
import os

from gui import UiMainWindow
from engine import Downloader


class MainClass(QMainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        # GUI INSTANCE
        self.interface = UiMainWindow()
        self.interface.setup_ui(self)
        # ABSOLUTE PATH FOR APP ICON
        abs_path = os.path.abspath('src\\icon.png')
        app_icon = QIcon(abs_path)
        self.setWindowIcon(app_icon)
        # INSTANCE OF DOWNLOADER
        self.downloader = Downloader()
        # CONNECT DOWNLOADER PROCESS
        self.downloader.progress_signal.connect(self.update_progress)
        # CONNECT DOWNLOAD BUTTON
        self.interface.download_button.clicked.connect(self.download)

    # DIRECTORY FOR SAVING
    def set_directory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Seleccionar directorio de descarga')
        if directory:
            return directory
        else:
            return 0000

    # CHECK FILE FORMAT
    def check_mode(self):
        if self.interface.mp3_select.isChecked():
            return False
        elif self.interface.mp4_select.isChecked():
            return True

    # DOWNLOAD PROCESS
    def download(self):
        # PROGRESS BAR TEXT DOWNLOADING
        self.interface.label.setText(QCoreApplication.translate("MainWindow", u"Downloading...", None))
        # PROGRESS BAR STATUS 0
        self.interface.progress_bar.setValue(0)
        # DOWNLOAD PROCESS
        self.downloader.download(self.interface.insert_url_text.text(), self.check_mode(), self.set_directory())
        # CLEAN URL
        self.interface.insert_url_text.clear()
        # PROGRESS BAR TEXT COMPLETE
        self.interface.label.setText(QCoreApplication.translate("MainWindow", u"Completed!", None))

    # SET PROGRESS BAR PROCESS
    def update_progress(self, percent):
        self.interface.progress_bar.setValue(percent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec())
