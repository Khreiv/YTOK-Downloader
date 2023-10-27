from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit, QProgressBar, QPushButton, QRadioButton, QWidget)


class UiMainWindow(object):
    def __init__(self):
        self.label = None
        self.progress_bar = None
        self.download_button = None
        self.mp4_select = None
        self.mp3_select = None
        self.mode_title_text = None
        self.mode_title = None
        self.url_title_text = None
        self.url_title = None
        self.insert_url_text = None
        self.insert_url_frame = None
        self.centralwidget = None

    def setup_ui(self, main_window):

        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(500, 100)

        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")

        # URL INPUT FRAME
        self.insert_url_frame = QFrame(self.centralwidget)
        self.insert_url_frame.setObjectName(u"insert_url_frame")
        self.insert_url_frame.setGeometry(QRect(104, 15, 380, 30))
        self.insert_url_frame.setStyleSheet(u"background: \"black\";\n"
                                            "border: 2px solid grey;\n"
                                            "border-radius: 15px;")
        self.insert_url_frame.setFrameShape(QFrame.StyledPanel)
        self.insert_url_frame.setFrameShadow(QFrame.Raised)

        # URL INPUT TEXT
        self.insert_url_text = QLineEdit(self.insert_url_frame)
        self.insert_url_text.setObjectName(u"insert_url_text")
        self.insert_url_text.setGeometry(QRect(9, 0, 361, 30))
        self.insert_url_text.setStyleSheet(u"background: \"transparent\";\n"
                                           "color: \"white\";\n"
                                           "border: 0px;\n"
                                           "font: 11pt Arial;")

        # URL TITLE FRAME
        self.url_title = QFrame(self.centralwidget)
        self.url_title.setObjectName(u"url_title")
        self.url_title.setGeometry(QRect(15, 15, 80, 30))
        self.url_title.setStyleSheet(u"background: \"transparent\";\n"
                                     "border: 2px solid black;\n"
                                     "border-radius: 15px;")
        self.url_title.setFrameShape(QFrame.StyledPanel)
        self.url_title.setFrameShadow(QFrame.Raised)

        # URL TITLE TEXT
        self.url_title_text = QLabel(self.url_title)
        self.url_title_text.setObjectName(u"url_title_text")
        self.url_title_text.setGeometry(QRect(0, 0, 80, 30))
        self.url_title_text.setStyleSheet(u"background: \"transparent\";\n"
                                          "color: \"black\";\n"
                                          "border: 0px;\n"
                                          "font: 13pt Arial;")
        self.url_title_text.setAlignment(Qt.AlignCenter)

        # MODE TITLE FRAME
        self.mode_title = QFrame(self.centralwidget)
        self.mode_title.setObjectName(u"mode_title")
        self.mode_title.setGeometry(QRect(15, 55, 80, 30))
        self.mode_title.setStyleSheet(u"background: \"transparent\";\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 15px;")
        self.mode_title.setFrameShape(QFrame.StyledPanel)
        self.mode_title.setFrameShadow(QFrame.Raised)

        # MODE TITLE TEXT
        self.mode_title_text = QLabel(self.mode_title)
        self.mode_title_text.setObjectName(u"mode_title_text")
        self.mode_title_text.setGeometry(QRect(0, 0, 80, 30))
        self.mode_title_text.setStyleSheet(u"background: \"transparent\";\n"
                                           "color: \"black\";\n"
                                           "border: 0px;\n"
                                           "font: 13pt Arial;")
        self.mode_title_text.setAlignment(Qt.AlignCenter)

        # MP3 RADIO BUTTON
        self.mp3_select = QRadioButton(self.centralwidget)
        self.mp3_select.setObjectName(u"mp3_select")
        self.mp3_select.setGeometry(QRect(115, 63, 60, 17))
        self.mp3_select.setStyleSheet(u"font: 10pt;")
        self.mp3_select.setChecked(True)

        # MP4 RADIO BUTTON
        self.mp4_select = QRadioButton(self.centralwidget)
        self.mp4_select.setObjectName(u"mp4_select")
        self.mp4_select.setGeometry(QRect(180, 63, 60, 17))
        self.mp4_select.setStyleSheet(u"font: 10pt;")

        # DOWNLOAD BUTTON
        self.download_button = QPushButton(self.centralwidget)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(400, 55, 75, 30))
        self.download_button.setStyleSheet(u"QPushButton{\n"
                                           "background: \"black\";\n"
                                           "border: 2px solid grey;\n"
                                           "border-radius: 15px;\n"
                                           "color: \"white\";\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "background: \"grey\";\n"
                                           "border: 2px solid black;\n"
                                           "border-radius: 15px;\n"
                                           "color: \"black\";\n}")

        # PROGRESS BAR
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(250, 64, 130, 20))
        self.progress_bar.setValue(0)

        # PROGRESS BAR TEXT
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(251, 63, 91, 20))
        self.label.setAlignment(Qt.AlignCenter)

        # CENTRAL WIDGET
        main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui(main_window)
        QMetaObject.connectSlotsByName(main_window)

    # setupUi
    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"YTOK Downloader", None))
        self.insert_url_text.setText("")
        self.url_title_text.setText(QCoreApplication.translate("MainWindow", u"Url", None))
        self.mode_title_text.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.mp3_select.setText(QCoreApplication.translate("MainWindow", u"MP3", None))
        self.mp4_select.setText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
    # retranslateUi
