from PySide6.QtWidgets import QMessageBox
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from PySide6.QtCore import QObject, Signal


# WRONG LINK ERROR MESSAGE
def show_error_message(title, message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()


class Downloader(QObject):
    # SIGNAL FOR PROGRESS BAR
    progress_signal = Signal(int)

    # DOWNLOADER METHOD
    def download(self, url, video, path):
        try:
            source = YouTube(url)

            # IF CORRECT LINK CHOOSE MP3 OR MP4 MODES
            if path != 0000:
                if video:
                    stream = source.streams.get_highest_resolution()
                    stream.download(output_path=path, filename=f'{source.title}.mp4')
                else:
                    stream = source.streams.get_audio_only()
                    stream.download(output_path=path, filename=f'{source.title}.mp3')

                # SIGNAL FOR PROGRESS BAR
                self.progress_signal.emit(100)

        except RegexMatchError:
            error_message = "URL de YouTube no válida. Por favor, ingrese una URL de video de YouTube válida."
            show_error_message("Error", error_message)
