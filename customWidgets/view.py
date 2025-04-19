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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(496, 475)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pathLayout = QHBoxLayout()
        self.pathLayout.setObjectName(u"pathLayout")
        self.selectPathButton = QPushButton(Form)
        self.selectPathButton.setObjectName(u"selectPathButton")

        self.pathLayout.addWidget(self.selectPathButton)

        self.pathLineEdit = QLineEdit(Form)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setReadOnly(True)

        self.pathLayout.addWidget(self.pathLineEdit)

        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")

        self.pathLayout.addWidget(self.addButton)


        self.verticalLayout.addLayout(self.pathLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.autoSelectButton = QPushButton(Form)
        self.autoSelectButton.setObjectName(u"autoSelectButton")
        self.autoSelectButton.setMinimumSize(QSize(150, 0))
        self.autoSelectButton.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.autoSelectButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.listLabel = QLabel(Form)
        self.listLabel.setObjectName(u"listLabel")

        self.verticalLayout.addWidget(self.listLabel)

        self.fileListWidget = QListWidget(Form)
        self.fileListWidget.setObjectName(u"fileListWidget")

        self.verticalLayout.addWidget(self.fileListWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.removeButton = QPushButton(Form)
        self.removeButton.setObjectName(u"removeButton")

        self.buttonLayout.addWidget(self.removeButton)

        self.acceptButton = QPushButton(Form)
        self.acceptButton.setObjectName(u"acceptButton")

        self.buttonLayout.addWidget(self.acceptButton)

        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Create new files", None))
        self.selectPathButton.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.autoSelectButton.setText(QCoreApplication.translate("Form", u"Auto select", None))
        self.listLabel.setText(QCoreApplication.translate("Form", u"List files:", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.acceptButton.setText(QCoreApplication.translate("Form", u"Accept", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

