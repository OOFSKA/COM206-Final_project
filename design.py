# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerPzaNgg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 572)
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.gridLayout = QGridLayout(self.MainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TextAddBar = QTextEdit(self.MainWidget)
        self.TextAddBar.setObjectName(u"TextAddBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextAddBar.sizePolicy().hasHeightForWidth())
        self.TextAddBar.setSizePolicy(sizePolicy)
        self.TextAddBar.setMinimumSize(QSize(100, 50))
        self.TextAddBar.setMaximumSize(QSize(16777215, 50))
        self.TextAddBar.setLineWidth(-1)

        self.gridLayout.addWidget(self.TextAddBar, 0, 1, 1, 2)

        self.ListFrame = QFrame(self.MainWidget)
        self.ListFrame.setObjectName(u"ListFrame")
        sizePolicy.setHeightForWidth(self.ListFrame.sizePolicy().hasHeightForWidth())
        self.ListFrame.setSizePolicy(sizePolicy)
        self.ListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ListFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.ListFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ListItem = QListWidget(self.ListFrame)
        self.ListItem.setObjectName(u"ListItem")
        self.ListItem.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ListItem.sizePolicy().hasHeightForWidth())
        self.ListItem.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ListItem)


        self.gridLayout.addWidget(self.ListFrame, 0, 0, 4, 1)

        self.AddButton = QPushButton(self.MainWidget)
        self.AddButton.setObjectName(u"AddButton")
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setMinimumSize(QSize(50, 50))
        self.AddButton.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.AddButton, 1, 1, 1, 1)

        self.RemoveButton = QPushButton(self.MainWidget)
        self.RemoveButton.setObjectName(u"RemoveButton")
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setMinimumSize(QSize(50, 50))
        self.RemoveButton.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.RemoveButton, 2, 1, 1, 1)

        self.ImagePreview = QLabel(self.MainWidget)
        self.ImagePreview.setObjectName(u"ImagePreview")
        sizePolicy.setHeightForWidth(self.ImagePreview.sizePolicy().hasHeightForWidth())
        self.ImagePreview.setSizePolicy(sizePolicy)
        self.ImagePreview.setMinimumSize(QSize(100, 100))
        self.ImagePreview.setMaximumSize(QSize(500, 500))

        self.gridLayout.addWidget(self.ImagePreview, 3, 1, 1, 1)

        self.AttributeFrame = QFrame(self.MainWidget)
        self.AttributeFrame.setObjectName(u"AttributeFrame")
        sizePolicy.setHeightForWidth(self.AttributeFrame.sizePolicy().hasHeightForWidth())
        self.AttributeFrame.setSizePolicy(sizePolicy)
        self.AttributeFrame.setMaximumSize(QSize(300, 16777215))
        self.AttributeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AttributeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.AttributeFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AttributeText = QTextEdit(self.AttributeFrame)
        self.AttributeText.setObjectName(u"AttributeText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AttributeText.sizePolicy().hasHeightForWidth())
        self.AttributeText.setSizePolicy(sizePolicy1)
        self.AttributeText.setMinimumSize(QSize(200, 50))
        self.AttributeText.setMaximumSize(QSize(100, 50))
        self.AttributeText.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.verticalLayout_2.addWidget(self.AttributeText, 0, Qt.AlignmentFlag.AlignTop)

        self.AttributeList = QListWidget(self.AttributeFrame)
        self.AttributeList.setObjectName(u"AttributeList")
        self.AttributeList.setMinimumSize(QSize(100, 100))
        self.AttributeList.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.AttributeList, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.AttributeFrame, 1, 2, 3, 1)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Item Attribute Lister", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"Add To List", None))
        self.RemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Listed", None))
        self.ImagePreview.setText(QCoreApplication.translate("MainWindow", u"ImageHere", None))
    # retranslateUi

