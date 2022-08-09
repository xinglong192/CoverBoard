# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CusTDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CusTDialog(object):
    def setupUi(self, CusTDialog):
        if not CusTDialog.objectName():
            CusTDialog.setObjectName(u"CusTDialog")
        CusTDialog.resize(139, 145)
        self.gridLayout = QGridLayout(CusTDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tvSlider = QSlider(CusTDialog)
        self.tvSlider.setObjectName(u"tvSlider")
        self.tvSlider.setMinimumSize(QSize(20, 0))
        self.tvSlider.setMaximumSize(QSize(20, 16777215))
        self.tvSlider.setMaximum(255)
        self.tvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.tvSlider)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnOk = QPushButton(CusTDialog)
        self.btnOk.setObjectName(u"btnOk")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOk.sizePolicy().hasHeightForWidth())
        self.btnOk.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btnOk)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnCancel = QPushButton(CusTDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btnCancel)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(CusTDialog)

        QMetaObject.connectSlotsByName(CusTDialog)
    # setupUi

    def retranslateUi(self, CusTDialog):
        CusTDialog.setWindowTitle(QCoreApplication.translate("CusTDialog", u"\u900f\u660e\u5ea6", None))
        self.btnOk.setText(QCoreApplication.translate("CusTDialog", u"\u786e\u5b9a", None))
        self.btnCancel.setText(QCoreApplication.translate("CusTDialog", u"\u53d6\u6d88", None))
    # retranslateUi

