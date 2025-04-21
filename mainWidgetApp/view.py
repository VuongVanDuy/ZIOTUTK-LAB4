# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 517)
        icon = QIcon()
        icon.addFile(u":/icons/iconsApp/generator_noise_app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnChooseFile = QPushButton(self.centralwidget)
        self.btnChooseFile.setObjectName(u"btnChooseFile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChooseFile.sizePolicy().hasHeightForWidth())
        self.btnChooseFile.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.btnChooseFile.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/iconsApp/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnChooseFile.setIcon(icon1)
        self.btnChooseFile.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btnChooseFile, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.generateButton.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/iconsApp/Generator.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generateButton.setIcon(icon2)
        self.generateButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.generateButton, 1, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(500, 0))
        self.listWidget.setViewMode(QListView.ViewMode.ListMode)

        self.gridLayout.addWidget(self.listWidget, 0, 1, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setStyleSheet(u"/* Bi\u1ec3u qu\u00e9t n\u1ec1n c\u1ee7a progress bar */\n"
"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 10px;\n"
"    background-color: #eee;\n"
"    text-align: center;\n"
"    padding: 2px;\n"
"    font: 14px \"Segoe UI\", sans-serif;\n"
"    color: #555;\n"
"}\n"
"\n"
"/* Ph\u1ea7n fill c\u1ee7a progress bar */\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #6a9ef7, stop:0.5 #4a7cf3, stop:1 #3362dd\n"
"    );\n"
"    margin: 0px 1px;    /* kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c chunk \u0111\u1ec3 t\u1ea1o hi\u1ec7u \u1ee9ng v\u00e2n s\u00f3ng */\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi hover l\u00ean bar */\n"
"QProgressBar:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi progress \u0111\u1ea1t 100% */\n"
"QProgressBar[maximum=\"100\"][value=\"100\"]::chunk {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        sto"
                        "p:0 #61d742, stop:0.5 #4fb73a, stop:1 #3da832\n"
"    );\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.sliderLayout = QVBoxLayout()
        self.sliderLayout.setObjectName(u"sliderLayout")
        self.voiceVolumeLayout = QHBoxLayout()
        self.voiceVolumeLayout.setObjectName(u"voiceVolumeLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/iconsApp/volume-2.png"))
        self.label.setScaledContents(True)

        self.voiceVolumeLayout.addWidget(self.label)

        self.voiceVolumeLabel = QLabel(self.centralwidget)
        self.voiceVolumeLabel.setObjectName(u"voiceVolumeLabel")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        self.voiceVolumeLabel.setFont(font3)
        self.voiceVolumeLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.voiceVolumeLabel.setScaledContents(False)

        self.voiceVolumeLayout.addWidget(self.voiceVolumeLabel)

        self.voiceVolumeSlider = QSlider(self.centralwidget)
        self.voiceVolumeSlider.setObjectName(u"voiceVolumeSlider")
        self.voiceVolumeSlider.setStyleSheet(u"\n"
"                        QSlider::groove:horizontal { height: 8px; margin: 0px; background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff8c00, stop:1 #ffd700); border-radius: 4px; }\n"
"                        QSlider::handle:horizontal { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #cccccc); border: 1px solid #888; width: 16px; margin: -4px 0; border-radius: 8px; }\n"
"                      ")
        self.voiceVolumeSlider.setMinimum(1)
        self.voiceVolumeSlider.setMaximum(100)
        self.voiceVolumeSlider.setValue(40)
        self.voiceVolumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.voiceVolumeLayout.addWidget(self.voiceVolumeSlider)


        self.sliderLayout.addLayout(self.voiceVolumeLayout)

        self.noiseVolumeLayout = QHBoxLayout()
        self.noiseVolumeLayout.setObjectName(u"noiseVolumeLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/iconsApp/volume-2.png"))
        self.label_2.setScaledContents(True)

        self.noiseVolumeLayout.addWidget(self.label_2)

        self.noiseVolumeLabel = QLabel(self.centralwidget)
        self.noiseVolumeLabel.setObjectName(u"noiseVolumeLabel")
        self.noiseVolumeLabel.setFont(font3)

        self.noiseVolumeLayout.addWidget(self.noiseVolumeLabel)

        self.noiseVolumeSlider = QSlider(self.centralwidget)
        self.noiseVolumeSlider.setObjectName(u"noiseVolumeSlider")
        self.noiseVolumeSlider.setStyleSheet(u"\n"
"                        QSlider::groove:horizontal { height: 8px; margin: 0px; background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00bfff, stop:1 #1e90ff); border-radius: 4px; }\n"
"                        QSlider::handle:horizontal { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #cccccc); border: 1px solid #888; width: 16px; margin: -4px 0; border-radius: 8px; }\n"
"                      ")
        self.noiseVolumeSlider.setMinimum(1)
        self.noiseVolumeSlider.setMaximum(100)
        self.noiseVolumeSlider.setValue(10)
        self.noiseVolumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.noiseVolumeLayout.addWidget(self.noiseVolumeSlider)


        self.sliderLayout.addLayout(self.noiseVolumeLayout)


        self.verticalLayout_2.addLayout(self.sliderLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.playNoiseButton = QPushButton(self.centralwidget)
        self.playNoiseButton.setObjectName(u"playNoiseButton")
        self.playNoiseButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.playNoiseButton.sizePolicy().hasHeightForWidth())
        self.playNoiseButton.setSizePolicy(sizePolicy)
        self.playNoiseButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/iconsApp/play-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playNoiseButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.playNoiseButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.showSpectrumButton = QPushButton(self.centralwidget)
        self.showSpectrumButton.setObjectName(u"showSpectrumButton")
        self.showSpectrumButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.showSpectrumButton.sizePolicy().hasHeightForWidth())
        self.showSpectrumButton.setSizePolicy(sizePolicy)
        self.showSpectrumButton.setFont(font2)

        self.horizontalLayout.addWidget(self.showSpectrumButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButtonRecord = QRadioButton(self.centralwidget)
        self.radioButtonRecord.setObjectName(u"radioButtonRecord")
        self.radioButtonRecord.setFont(font1)
        self.radioButtonRecord.setChecked(True)

        self.verticalLayout.addWidget(self.radioButtonRecord)

        self.radioButtonChoose = QRadioButton(self.centralwidget)
        self.radioButtonChoose.setObjectName(u"radioButtonChoose")
        self.radioButtonChoose.setFont(font1)

        self.verticalLayout.addWidget(self.radioButtonChoose)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.btnChoose = QPushButton(self.centralwidget)
        self.btnChoose.setObjectName(u"btnChoose")
        self.btnChoose.setEnabled(False)
        self.btnChoose.setFont(font1)
        self.btnChoose.setIcon(icon1)
        self.btnChoose.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnChoose)

        self.btnRecord = QPushButton(self.centralwidget)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setFont(font1)
        self.btnRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"    min-width: 30px;\n"
"    min-height: 30px;\n"
"    max-width: 30px;\n"
"    max-height: 30px;\n"
"    background-color:#ef4927;\n"
"    color: #333;\n"
"    border: 1px solid #bbb;\n"
"}\n"
"\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi r\u00ea chu\u1ed9t v\u00e0o */\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    color: #000;\n"
"    border: 1px solid #888;\n"
"}\n"
"\n"
"/* Hi\u1ec7u \u1ee9ng khi nh\u1ea5n gi\u1eef */\n"
"QPushButton:pressed {\n"
"    background-color: #d0d0d0;\n"
"    border: 1px solid #666;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/iconsApp/disc.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRecord.setIcon(icon4)
        self.btnRecord.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnRecord)

        self.btnPlayVoice = QPushButton(self.centralwidget)
        self.btnPlayVoice.setObjectName(u"btnPlayVoice")
        self.btnPlayVoice.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/iconsApp/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPlayVoice.setIcon(icon5)
        self.btnPlayVoice.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnPlayVoice)

        self.pathSaveVoice = QLineEdit(self.centralwidget)
        self.pathSaveVoice.setObjectName(u"pathSaveVoice")
        self.pathSaveVoice.setFont(font1)
        self.pathSaveVoice.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.pathSaveVoice)

        self.compareButton = QPushButton(self.centralwidget)
        self.compareButton.setObjectName(u"compareButton")
        self.compareButton.setEnabled(False)
        self.compareButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.compareButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Speech Noise Generator", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Speech Noise Generator", None))
        self.btnChooseFile.setText(QCoreApplication.translate("MainWindow", u"Choose file", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate Noise", None))
        self.label.setText("")
        self.voiceVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"(voice):", None))
        self.label_2.setText("")
        self.noiseVolumeLabel.setText(QCoreApplication.translate("MainWindow", u"(noise):", None))
        self.playNoiseButton.setText(QCoreApplication.translate("MainWindow", u"Play result noise", None))
        self.showSpectrumButton.setText(QCoreApplication.translate("MainWindow", u"Amplitude spectrum", None))
        self.radioButtonRecord.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.radioButtonChoose.setText(QCoreApplication.translate("MainWindow", u"Choose file", None))
        self.btnChoose.setText("")
        self.btnRecord.setText("")
        self.btnPlayVoice.setText("")
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Compare with My Voice", None))
    # retranslateUi

