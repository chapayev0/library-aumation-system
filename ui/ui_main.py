# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainsadyTB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView

from PySide2.QtWidgets import *
import sys
import sqlite3
import os
THIS_DIR = os.path.dirname(__file__)
CODE_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'ui'))
sys.path.append(CODE_DIR)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 642)
        self.root = QWidget(MainWindow)
        self.root.setObjectName(u"root")
        self.frame = QFrame(self.root)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 1292, 635))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.main_stack = QStackedWidget(self.frame)
        self.main_stack.setObjectName(u"main_stack")
        self.main_stack.setStyleSheet(u"border:none;")
        self.reception_page = QWidget()
        self.reception_page.setObjectName(u"reception_page")
        self.horizontalLayout_5 = QHBoxLayout(self.reception_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.roo_top = QFrame(self.reception_page)
        self.roo_top.setObjectName(u"roo_top")
        self.roo_top.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.roo_top.setFrameShape(QFrame.StyledPanel)
        self.roo_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.roo_top)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_side_bar = QFrame(self.roo_top)
        self.left_side_bar.setObjectName(u"left_side_bar")
        self.left_side_bar.setMinimumSize(QSize(200, 0))
        self.left_side_bar.setMaximumSize(QSize(200, 16777215))
        self.left_side_bar.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(24, 58, 86);\n"
"}\n"
"")
        self.left_side_bar.setFrameShape(QFrame.StyledPanel)
        self.left_side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.left_side_bar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_106 = QFrame(self.frame_2)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_106)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))
        self.pushButton.setStyleSheet(u"background-image: url(:/image/assets/system.png);\n"
"background-position: center;\n"
" background-repeat: no-repeat;\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.re_home = QPushButton(self.frame_2)
        self.re_home.setObjectName(u"re_home")
        self.re_home.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(9)
        self.re_home.setFont(font)
        self.re_home.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.re_home)

        self.re_history = QPushButton(self.frame_2)
        self.re_history.setObjectName(u"re_history")
        self.re_history.setMinimumSize(QSize(0, 40))
        self.re_history.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.re_history)

        self.usr_control_btn = QPushButton(self.frame_2)
        self.usr_control_btn.setObjectName(u"usr_control_btn")
        self.usr_control_btn.setMinimumSize(QSize(0, 40))
        self.usr_control_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.usr_control_btn)

        self.re_btn = QPushButton(self.frame_2)
        self.re_btn.setObjectName(u"re_btn")
        self.re_btn.setMinimumSize(QSize(0, 40))
        self.re_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.re_btn)

        self.re_setting = QPushButton(self.frame_2)
        self.re_setting.setObjectName(u"re_setting")
        self.re_setting.setMinimumSize(QSize(0, 40))
        self.re_setting.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.re_setting)

        self.frame_107 = QFrame(self.frame_2)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_107)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.left_side_bar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.about_btn = QPushButton(self.frame_3)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(0, 40))
        self.about_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/icon/assets/c.png);\n"
"	background-color:none;\n"
"\n"
"border-radius:2px;\n"
"background-position: center;\n"
" background-repeat: no-repeat;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.about_btn)

        self.log_out_btn = QPushButton(self.frame_3)
        self.log_out_btn.setObjectName(u"log_out_btn")
        self.log_out_btn.setMinimumSize(QSize(0, 40))
        self.log_out_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:none;\n"
"border:none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"\n"
"background-color:rgb(248, 116, 116);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.log_out_btn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.left_side_bar)

        self.right_root = QFrame(self.roo_top)
        self.right_root.setObjectName(u"right_root")
        self.right_root.setFrameShape(QFrame.StyledPanel)
        self.right_root.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.right_root)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container = QFrame(self.right_root)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(0, 30))
        self.left_container.setMaximumSize(QSize(16777215, 30))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_container)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 2, 5, 0)
        self.horizontalSpacer_3 = QSpacerItem(572, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.frame_4 = QFrame(self.left_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(70, 0))
        self.frame_4.setMaximumSize(QSize(70, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.time_lbl = QLabel(self.frame_4)
        self.time_lbl.setObjectName(u"time_lbl")
        self.time_lbl.setMinimumSize(QSize(0, 10))
        self.time_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.time_lbl)

        self.date_lbl = QLabel(self.frame_4)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setMinimumSize(QSize(0, 10))
        self.date_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.date_lbl)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.notifi_btn = QPushButton(self.left_container)
        self.notifi_btn.setObjectName(u"notifi_btn")
        self.notifi_btn.setMaximumSize(QSize(15, 15))
        self.notifi_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	\n"
"	background-color: rgb(122, 122, 122);\n"
"	border-color: rgb(122, 122, 122);\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(191, 191, 191);\n"
"border-color: rgb(191, 191, 191);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.notifi_btn)

        self.minimize_btn = QPushButton(self.left_container)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMaximumSize(QSize(15, 15))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	\n"
"	background-color: rgb(54, 135, 189);\n"
"	border-color: rgb(54, 135, 189);\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(68, 171, 239);\n"
"border-color: rgb(68, 171, 239);\n"
"}")

        self.horizontalLayout_4.addWidget(self.minimize_btn)

        self.maxmize_btn = QPushButton(self.left_container)
        self.maxmize_btn.setObjectName(u"maxmize_btn")
        self.maxmize_btn.setMaximumSize(QSize(15, 15))
        self.maxmize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	\n"
"	\n"
"\n"
"	background-color: rgb(34, 198, 111);\n"
"	border-color: rgb(34, 198, 111);\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(43, 249, 143);\n"
"	border-color: rgb(43, 249, 143);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.maxmize_btn)

        self.close_btn = QPushButton(self.left_container)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(15, 15))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border:1px solid;\n"
"	;\n"
"	background-color: rgb(217, 54, 57);\n"
"	border-color: rgb(217, 54, 57);\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(250, 97, 100);\n"
"\n"
"border-color: rgb(250, 97, 100);\n"
"}")

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.left_container)

        self.recipt_stack = QStackedWidget(self.right_root)
        self.recipt_stack.setObjectName(u"recipt_stack")
        self.reciption_page = QWidget()
        self.reciption_page.setObjectName(u"reciption_page")
        self.horizontalLayout_11 = QHBoxLayout(self.reciption_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.root1 = QFrame(self.reciption_page)
        self.root1.setObjectName(u"root1")
        self.root1.setFrameShape(QFrame.StyledPanel)
        self.root1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.root1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.re_top_frame = QFrame(self.root1)
        self.re_top_frame.setObjectName(u"re_top_frame")
        self.re_top_frame.setMinimumSize(QSize(250, 0))
        self.re_top_frame.setFrameShape(QFrame.StyledPanel)
        self.re_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.re_top_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.re_top_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(330, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.counter_lbl = QLabel(self.frame_9)
        self.counter_lbl.setObjectName(u"counter_lbl")
        font1 = QFont()
        font1.setPointSize(48)
        self.counter_lbl.setFont(font1)
        self.counter_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.counter_lbl)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.counter_back_btn = QPushButton(self.frame_10)
        self.counter_back_btn.setObjectName(u"counter_back_btn")
        self.counter_back_btn.setMinimumSize(QSize(0, 40))
        self.counter_back_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"background-color: rgb(21, 199, 203);\n"
"}")

        self.horizontalLayout_8.addWidget(self.counter_back_btn)

        self.counter_reset_btn = QPushButton(self.frame_10)
        self.counter_reset_btn.setObjectName(u"counter_reset_btn")
        self.counter_reset_btn.setMinimumSize(QSize(0, 40))
        self.counter_reset_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"background-color: rgb(21, 199, 203);\n"
"}")

        self.horizontalLayout_8.addWidget(self.counter_reset_btn)

        self.counter_next_btn = QPushButton(self.frame_10)
        self.counter_next_btn.setObjectName(u"counter_next_btn")
        self.counter_next_btn.setMinimumSize(QSize(0, 40))
        self.counter_next_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"background-color: rgb(21, 199, 203);\n"
"}")

        self.horizontalLayout_8.addWidget(self.counter_next_btn)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.re_list = QListWidget(self.re_top_frame)
        self.re_list.setObjectName(u"re_list")

        self.horizontalLayout_7.addWidget(self.re_list)


        self.verticalLayout_4.addWidget(self.re_top_frame)

        self.re_down_frame = QFrame(self.root1)
        self.re_down_frame.setObjectName(u"re_down_frame")
        self.re_down_frame.setFrameShape(QFrame.StyledPanel)
        self.re_down_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.re_down_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.left_frm = QFrame(self.re_down_frame)
        self.left_frm.setObjectName(u"left_frm")
        self.left_frm.setFrameShape(QFrame.StyledPanel)
        self.left_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.left_frm)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.left_frm)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_13.addWidget(self.label)

        self.rc_default_price = QLineEdit(self.frame_5)
        self.rc_default_price.setObjectName(u"rc_default_price")
        self.rc_default_price.setMinimumSize(QSize(0, 30))
        self.rc_default_price.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.rc_default_price.setInputMethodHints(Qt.ImhDigitsOnly)
        self.rc_default_price.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.rc_default_price.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.rc_default_price)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_frm)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_14.addWidget(self.label_2)

        self.rc_addtional_price = QLineEdit(self.frame_6)
        self.rc_addtional_price.setObjectName(u"rc_addtional_price")
        self.rc_addtional_price.setMinimumSize(QSize(0, 30))
        self.rc_addtional_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.rc_addtional_price.setInputMethodHints(Qt.ImhNone)
        self.rc_addtional_price.setClearButtonEnabled(True)

        self.horizontalLayout_14.addWidget(self.rc_addtional_price)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_11 = QFrame(self.left_frm)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_15.addWidget(self.label_3)

        self.rc_total_price = QLineEdit(self.frame_11)
        self.rc_total_price.setObjectName(u"rc_total_price")
        self.rc_total_price.setMinimumSize(QSize(0, 30))
        self.rc_total_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.rc_total_price.setReadOnly(True)
        self.rc_total_price.setClearButtonEnabled(True)

        self.horizontalLayout_15.addWidget(self.rc_total_price)


        self.verticalLayout_8.addWidget(self.frame_11)


        self.horizontalLayout_10.addWidget(self.left_frm)

        self.right_frm = QFrame(self.re_down_frame)
        self.right_frm.setObjectName(u"right_frm")
        self.right_frm.setFrameShape(QFrame.StyledPanel)
        self.right_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.right_frm)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_8 = QFrame(self.right_frm)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_18.addWidget(self.label_4)

        self.rc_name = QLineEdit(self.frame_13)
        self.rc_name.setObjectName(u"rc_name")
        self.rc_name.setMinimumSize(QSize(0, 30))
        self.rc_name.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.rc_name.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.rc_name)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_17.addWidget(self.label_5)

        self.rc_age = QLineEdit(self.frame_12)
        self.rc_age.setObjectName(u"rc_age")
        self.rc_age.setMinimumSize(QSize(0, 30))
        self.rc_age.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.rc_age.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.rc_age)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_16.addWidget(self.label_6)

        self.rc_date = QLineEdit(self.frame_14)
        self.rc_date.setObjectName(u"rc_date")
        self.rc_date.setMinimumSize(QSize(0, 30))
        self.rc_date.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.horizontalLayout_16.addWidget(self.rc_date)

        self.rc_time = QLineEdit(self.frame_14)
        self.rc_time.setObjectName(u"rc_time")
        self.rc_time.setMinimumSize(QSize(0, 30))
        self.rc_time.setSizeIncrement(QSize(0, 0))
        self.rc_time.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.horizontalLayout_16.addWidget(self.rc_time)


        self.verticalLayout_9.addWidget(self.frame_14)


        self.horizontalLayout_31.addWidget(self.frame_8)


        self.horizontalLayout_10.addWidget(self.right_frm)


        self.verticalLayout_4.addWidget(self.re_down_frame)

        self.re_bottom_page = QFrame(self.root1)
        self.re_bottom_page.setObjectName(u"re_bottom_page")
        self.re_bottom_page.setMaximumSize(QSize(16777215, 50))
        self.re_bottom_page.setFrameShape(QFrame.StyledPanel)
        self.re_bottom_page.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.re_bottom_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(523, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.re_cancle_btn = QPushButton(self.re_bottom_page)
        self.re_cancle_btn.setObjectName(u"re_cancle_btn")
        self.re_cancle_btn.setMinimumSize(QSize(80, 40))
        self.re_cancle_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_6.addWidget(self.re_cancle_btn)

        self.re_edit_btn = QPushButton(self.re_bottom_page)
        self.re_edit_btn.setObjectName(u"re_edit_btn")
        self.re_edit_btn.setMinimumSize(QSize(80, 40))
        self.re_edit_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_6.addWidget(self.re_edit_btn)

        self.re_ok_btn = QPushButton(self.re_bottom_page)
        self.re_ok_btn.setObjectName(u"re_ok_btn")
        self.re_ok_btn.setMinimumSize(QSize(80, 40))
        self.re_ok_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_6.addWidget(self.re_ok_btn)


        self.verticalLayout_4.addWidget(self.re_bottom_page)


        self.horizontalLayout_11.addWidget(self.root1)

        self.recipt_stack.addWidget(self.reciption_page)
        self.sales_page = QWidget()
        self.sales_page.setObjectName(u"sales_page")
        self.horizontalLayout_106 = QHBoxLayout(self.sales_page)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.frame_172 = QFrame(self.sales_page)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setMaximumSize(QSize(600, 16777215))
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_172)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_173 = QFrame(self.frame_172)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMaximumSize(QSize(16777215, 50))
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_169 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalSpacer_48 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_48)

        self.r_m_srch_3 = QLineEdit(self.frame_173)
        self.r_m_srch_3.setObjectName(u"r_m_srch_3")
        self.r_m_srch_3.setMinimumSize(QSize(200, 30))
        self.r_m_srch_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_169.addWidget(self.r_m_srch_3)

        self.horizontalSpacer_49 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_169.addItem(self.horizontalSpacer_49)


        self.verticalLayout_66.addWidget(self.frame_173)

        self.tableWidget_2 = QTableWidget(self.frame_172)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(116)

        self.verticalLayout_66.addWidget(self.tableWidget_2)

        self.frame_160 = QFrame(self.frame_172)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.label_68 = QLabel(self.frame_160)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_107.addWidget(self.label_68)

        self.r_m_qty_2 = QLineEdit(self.frame_160)
        self.r_m_qty_2.setObjectName(u"r_m_qty_2")
        self.r_m_qty_2.setMinimumSize(QSize(0, 30))
        self.r_m_qty_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_qty_2.setReadOnly(False)
        self.r_m_qty_2.setClearButtonEnabled(True)

        self.horizontalLayout_107.addWidget(self.r_m_qty_2)


        self.verticalLayout_66.addWidget(self.frame_160)

        self.frame_169 = QFrame(self.frame_172)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setMinimumSize(QSize(200, 0))
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_167 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_167.setSpacing(6)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.horizontalLayout_167.setContentsMargins(9, 9, 9, 9)
        self.label_115 = QLabel(self.frame_169)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_167.addWidget(self.label_115)

        self.r_discount_3 = QLineEdit(self.frame_169)
        self.r_discount_3.setObjectName(u"r_discount_3")
        self.r_discount_3.setMinimumSize(QSize(0, 30))
        self.r_discount_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_discount_3.setReadOnly(False)
        self.r_discount_3.setClearButtonEnabled(True)

        self.horizontalLayout_167.addWidget(self.r_discount_3)

        self.r_m_discount_typr_3 = QComboBox(self.frame_169)
        self.r_m_discount_typr_3.setObjectName(u"r_m_discount_typr_3")
        self.r_m_discount_typr_3.setMinimumSize(QSize(200, 30))
        self.r_m_discount_typr_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_167.addWidget(self.r_m_discount_typr_3)


        self.verticalLayout_66.addWidget(self.frame_169)

        self.frame_196 = QFrame(self.frame_172)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(0, 0))
        self.frame_196.setMaximumSize(QSize(16777215, 50))
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_50 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_186.addItem(self.horizontalSpacer_50)

        self.r_add_btn_5 = QPushButton(self.frame_196)
        self.r_add_btn_5.setObjectName(u"r_add_btn_5")
        self.r_add_btn_5.setMinimumSize(QSize(100, 40))
        self.r_add_btn_5.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_186.addWidget(self.r_add_btn_5)


        self.verticalLayout_66.addWidget(self.frame_196)


        self.horizontalLayout_106.addWidget(self.frame_172)

        self.frame_157 = QFrame(self.sales_page)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setMinimumSize(QSize(400, 0))
        self.frame_157.setMaximumSize(QSize(500, 16777215))
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_157)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_165 = QFrame(self.frame_157)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMinimumSize(QSize(200, 0))
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_163.setSpacing(5)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(0, 0, 0, 10)
        self.label_111 = QLabel(self.frame_165)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_163.addWidget(self.label_111)

        self.r_inv_number_2 = QLineEdit(self.frame_165)
        self.r_inv_number_2.setObjectName(u"r_inv_number_2")
        self.r_inv_number_2.setMinimumSize(QSize(0, 30))
        self.r_inv_number_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_inv_number_2.setReadOnly(False)

        self.horizontalLayout_163.addWidget(self.r_inv_number_2)


        self.verticalLayout_62.addWidget(self.frame_165)

        self.tableWidget_3 = QTableWidget(self.frame_157)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(109)

        self.verticalLayout_62.addWidget(self.tableWidget_3)

        self.frame_163 = QFrame(self.frame_157)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(0, 180))
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(0, 0, 0, 0)
        self.frame_164 = QFrame(self.frame_163)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_164)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(-1, 4, -1, 4)
        self.frame_166 = QFrame(self.frame_164)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.frame_166)
        self.horizontalLayout_164.setSpacing(5)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.label_112 = QLabel(self.frame_166)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_164.addWidget(self.label_112)

        self.r_total_2 = QLineEdit(self.frame_166)
        self.r_total_2.setObjectName(u"r_total_2")
        self.r_total_2.setMinimumSize(QSize(0, 30))
        self.r_total_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_total_2.setReadOnly(True)

        self.horizontalLayout_164.addWidget(self.r_total_2)


        self.verticalLayout_65.addWidget(self.frame_166)

        self.frame_167 = QFrame(self.frame_164)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMinimumSize(QSize(200, 0))
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.frame_167)
        self.horizontalLayout_165.setSpacing(5)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.horizontalLayout_165.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.frame_167)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_165.addWidget(self.label_113)

        self.r_discount_2 = QLineEdit(self.frame_167)
        self.r_discount_2.setObjectName(u"r_discount_2")
        self.r_discount_2.setMinimumSize(QSize(0, 30))
        self.r_discount_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_discount_2.setReadOnly(False)
        self.r_discount_2.setClearButtonEnabled(True)

        self.horizontalLayout_165.addWidget(self.r_discount_2)

        self.r_m_discount_typr_2 = QComboBox(self.frame_167)
        self.r_m_discount_typr_2.setObjectName(u"r_m_discount_typr_2")
        self.r_m_discount_typr_2.setMinimumSize(QSize(200, 30))
        self.r_m_discount_typr_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_165.addWidget(self.r_m_discount_typr_2)


        self.verticalLayout_65.addWidget(self.frame_167)

        self.frame_168 = QFrame(self.frame_164)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_166.setSpacing(5)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_114 = QLabel(self.frame_168)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_166.addWidget(self.label_114)

        self.r_afd_price_2 = QLineEdit(self.frame_168)
        self.r_afd_price_2.setObjectName(u"r_afd_price_2")
        self.r_afd_price_2.setMinimumSize(QSize(0, 30))
        self.r_afd_price_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_afd_price_2.setReadOnly(True)

        self.horizontalLayout_166.addWidget(self.r_afd_price_2)


        self.verticalLayout_65.addWidget(self.frame_168)


        self.horizontalLayout_162.addWidget(self.frame_164)


        self.verticalLayout_62.addWidget(self.frame_163)

        self.frame_170 = QFrame(self.frame_157)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setMinimumSize(QSize(0, 0))
        self.frame_170.setMaximumSize(QSize(16777215, 50))
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_46 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_168.addItem(self.horizontalSpacer_46)

        self.r_inv_btn_2 = QPushButton(self.frame_170)
        self.r_inv_btn_2.setObjectName(u"r_inv_btn_2")
        self.r_inv_btn_2.setMinimumSize(QSize(100, 40))
        self.r_inv_btn_2.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_168.addWidget(self.r_inv_btn_2)


        self.verticalLayout_62.addWidget(self.frame_170)


        self.horizontalLayout_106.addWidget(self.frame_157)

        self.recipt_stack.addWidget(self.sales_page)
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.horizontalLayout_109 = QHBoxLayout(self.inventory_page)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.report_page_2 = QTabWidget(self.inventory_page)
        self.report_page_2.setObjectName(u"report_page_2")
        self.report_page_2.setTabPosition(QTabWidget.North)
        self.report_page_2.setTabShape(QTabWidget.Rounded)
        self.report_page_2.setElideMode(Qt.ElideNone)
        self.report_page_2.setTabBarAutoHide(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_104 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.frame_108 = QFrame(self.tab_5)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMaximumSize(QSize(16777215, 16777215))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_108)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.frame_120 = QFrame(self.frame_108)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMaximumSize(QSize(16777215, 50))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalSpacer_43 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_160.addItem(self.horizontalSpacer_43)

        self.r_m_srch_2 = QLineEdit(self.frame_120)
        self.r_m_srch_2.setObjectName(u"r_m_srch_2")
        self.r_m_srch_2.setMinimumSize(QSize(200, 30))
        self.r_m_srch_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_160.addWidget(self.r_m_srch_2)

        self.horizontalSpacer_44 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_160.addItem(self.horizontalSpacer_44)


        self.verticalLayout_59.addWidget(self.frame_120)

        self.frame_158 = QFrame(self.frame_108)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_158)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.frame_158)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_159)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_159)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(197)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(31)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_61.addWidget(self.tableWidget)


        self.verticalLayout_60.addWidget(self.frame_159)


        self.verticalLayout_59.addWidget(self.frame_158)

        self.frame_171 = QFrame(self.frame_108)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setMinimumSize(QSize(0, 0))
        self.frame_171.setMaximumSize(QSize(16777215, 50))
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_45 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_172.addItem(self.horizontalSpacer_45)

        self.r_add_btn_4 = QPushButton(self.frame_171)
        self.r_add_btn_4.setObjectName(u"r_add_btn_4")
        self.r_add_btn_4.setMinimumSize(QSize(100, 40))
        self.r_add_btn_4.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_172.addWidget(self.r_add_btn_4)

        self.r_add_btn_3 = QPushButton(self.frame_171)
        self.r_add_btn_3.setObjectName(u"r_add_btn_3")
        self.r_add_btn_3.setMinimumSize(QSize(100, 40))
        self.r_add_btn_3.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_172.addWidget(self.r_add_btn_3)

        self.r_add_btn_2 = QPushButton(self.frame_171)
        self.r_add_btn_2.setObjectName(u"r_add_btn_2")
        self.r_add_btn_2.setMinimumSize(QSize(100, 40))
        self.r_add_btn_2.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_172.addWidget(self.r_add_btn_2)


        self.verticalLayout_59.addWidget(self.frame_171)


        self.horizontalLayout_104.addWidget(self.frame_108)

        self.report_page_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_105 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.frame_184 = QFrame(self.tab_6)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(400, 400))
        self.frame_184.setMaximumSize(QSize(500, 400))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_184)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMinimumSize(QSize(0, 180))
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_185)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_186 = QFrame(self.frame_185)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_186)
        self.verticalLayout_70.setSpacing(10)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_187 = QFrame(self.frame_186)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.frame_187)
        self.horizontalLayout_181.setSpacing(5)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.label_125 = QLabel(self.frame_187)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_181.addWidget(self.label_125)

        self.ad_m_name_2 = QLineEdit(self.frame_187)
        self.ad_m_name_2.setObjectName(u"ad_m_name_2")
        self.ad_m_name_2.setMinimumSize(QSize(0, 30))
        self.ad_m_name_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_name_2.setReadOnly(False)

        self.horizontalLayout_181.addWidget(self.ad_m_name_2)


        self.verticalLayout_70.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_186)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMinimumSize(QSize(200, 0))
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_182.setSpacing(5)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.label_126 = QLabel(self.frame_188)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_182.addWidget(self.label_126)

        self.ad_m_id_2 = QLineEdit(self.frame_188)
        self.ad_m_id_2.setObjectName(u"ad_m_id_2")
        self.ad_m_id_2.setMinimumSize(QSize(0, 30))
        self.ad_m_id_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_id_2.setReadOnly(False)

        self.horizontalLayout_182.addWidget(self.ad_m_id_2)


        self.verticalLayout_70.addWidget(self.frame_188)

        self.frame_189 = QFrame(self.frame_186)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_110.setSpacing(5)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_127 = QLabel(self.frame_189)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(80, 0))
        self.label_127.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_110.addWidget(self.label_127)

        self.ad_m_id_3 = QLineEdit(self.frame_189)
        self.ad_m_id_3.setObjectName(u"ad_m_id_3")
        self.ad_m_id_3.setMinimumSize(QSize(0, 30))
        self.ad_m_id_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_id_3.setReadOnly(False)

        self.horizontalLayout_110.addWidget(self.ad_m_id_3)


        self.verticalLayout_70.addWidget(self.frame_189)

        self.frame_190 = QFrame(self.frame_186)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_184 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_184.setSpacing(5)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.label_128 = QLabel(self.frame_190)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(80, 0))
        self.label_128.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_184.addWidget(self.label_128)

        self.ad_m_id_5 = QLineEdit(self.frame_190)
        self.ad_m_id_5.setObjectName(u"ad_m_id_5")
        self.ad_m_id_5.setMinimumSize(QSize(0, 30))
        self.ad_m_id_5.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_id_5.setReadOnly(False)

        self.horizontalLayout_184.addWidget(self.ad_m_id_5)


        self.verticalLayout_70.addWidget(self.frame_190)

        self.frame_218 = QFrame(self.frame_186)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_111.setSpacing(5)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_146 = QLabel(self.frame_218)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(80, 0))
        self.label_146.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_111.addWidget(self.label_146)

        self.dateEdit = QDateEdit(self.frame_218)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_111.addWidget(self.dateEdit)


        self.verticalLayout_70.addWidget(self.frame_218)


        self.verticalLayout_69.addWidget(self.frame_186)


        self.verticalLayout_68.addWidget(self.frame_185)

        self.frame_191 = QFrame(self.frame_184)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(0, 0))
        self.frame_191.setMaximumSize(QSize(16777215, 50))
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_185 = QHBoxLayout(self.frame_191)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_47 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_185.addItem(self.horizontalSpacer_47)

        self.ad_add_btn_2 = QPushButton(self.frame_191)
        self.ad_add_btn_2.setObjectName(u"ad_add_btn_2")
        self.ad_add_btn_2.setMinimumSize(QSize(100, 40))
        self.ad_add_btn_2.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_185.addWidget(self.ad_add_btn_2)


        self.verticalLayout_68.addWidget(self.frame_191)


        self.horizontalLayout_105.addWidget(self.frame_184)

        self.report_page_2.addTab(self.tab_6, "")

        self.horizontalLayout_109.addWidget(self.report_page_2)

        self.recipt_stack.addWidget(self.inventory_page)
        self.about_page_2 = QWidget()
        self.about_page_2.setObjectName(u"about_page_2")
        self.recipt_stack.addWidget(self.about_page_2)
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.recipt_stack.addWidget(self.dashboard_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.verticalLayout_38 = QVBoxLayout(self.about_page)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_105 = QFrame(self.about_page)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"QFrame{\n"
"\n"
"}")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_105)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.img_lbl = QLabel(self.frame_105)
        self.img_lbl.setObjectName(u"img_lbl")

        self.verticalLayout_58.addWidget(self.img_lbl)


        self.verticalLayout_38.addWidget(self.frame_105)

        self.recipt_stack.addWidget(self.about_page)
        self.user_control_page = QWidget()
        self.user_control_page.setObjectName(u"user_control_page")
        self.user_control_page.setStyleSheet(u"user_control_page")
        self.verticalLayout_31 = QVBoxLayout(self.user_control_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_70 = QFrame(self.user_control_page)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMaximumSize(QSize(16777215, 50))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalSpacer_27 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_27)

        self.user_search = QLineEdit(self.frame_70)
        self.user_search.setObjectName(u"user_search")
        self.user_search.setMinimumSize(QSize(0, 30))
        self.user_search.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_82.addWidget(self.user_search)

        self.horizontalSpacer_28 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_28)


        self.verticalLayout_31.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.user_control_page)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_71)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.frame_71)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMaximumSize(QSize(16777215, 30))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.label_56 = QLabel(self.frame_74)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_56)

        self.label_52 = QLabel(self.frame_74)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_52)

        self.label_53 = QLabel(self.frame_74)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_53)

        self.label_54 = QLabel(self.frame_74)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_74)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_94.addWidget(self.label_55)


        self.verticalLayout_32.addWidget(self.frame_74)

        self.usr_fm = QFrame(self.frame_71)
        self.usr_fm.setObjectName(u"usr_fm")
        self.usr_fm.setFrameShape(QFrame.StyledPanel)
        self.usr_fm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.usr_fm)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.usr_list = QListWidget(self.usr_fm)
        self.usr_list.setObjectName(u"usr_list")

        self.horizontalLayout_95.addWidget(self.usr_list)


        self.verticalLayout_32.addWidget(self.usr_fm)


        self.verticalLayout_31.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.user_control_page)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 180))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_72)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_76)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.frame_79 = QFrame(self.frame_76)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_84.setSpacing(5)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_79)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_84.addWidget(self.label_38)

        self.usr_name = QLineEdit(self.frame_79)
        self.usr_name.setObjectName(u"usr_name")
        self.usr_name.setMinimumSize(QSize(0, 30))
        self.usr_name.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_84.addWidget(self.usr_name)


        self.verticalLayout_33.addWidget(self.frame_79)

        self.frame_78 = QFrame(self.frame_76)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_86.setSpacing(5)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_78)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_86.addWidget(self.label_45)

        self.usr_phone = QLineEdit(self.frame_78)
        self.usr_phone.setObjectName(u"usr_phone")
        self.usr_phone.setMinimumSize(QSize(0, 30))
        self.usr_phone.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_86.addWidget(self.usr_phone)


        self.verticalLayout_33.addWidget(self.frame_78)

        self.frame_80 = QFrame(self.frame_76)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_87.setSpacing(5)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_80)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_87.addWidget(self.label_46)

        self.usr_mail = QLineEdit(self.frame_80)
        self.usr_mail.setObjectName(u"usr_mail")
        self.usr_mail.setMinimumSize(QSize(0, 30))
        self.usr_mail.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_87.addWidget(self.usr_mail)


        self.verticalLayout_33.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_76)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_88.setSpacing(5)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_81)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_88.addWidget(self.label_47)

        self.usr_nic = QLineEdit(self.frame_81)
        self.usr_nic.setObjectName(u"usr_nic")
        self.usr_nic.setMinimumSize(QSize(0, 30))
        self.usr_nic.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_88.addWidget(self.usr_nic)


        self.verticalLayout_33.addWidget(self.frame_81)


        self.horizontalLayout_83.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_72)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_77)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_82 = QFrame(self.frame_77)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_90.setSpacing(5)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_82)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_90.addWidget(self.label_49)

        self.usr_position = QLineEdit(self.frame_82)
        self.usr_position.setObjectName(u"usr_position")
        self.usr_position.setMinimumSize(QSize(0, 30))
        self.usr_position.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.usr_position.setReadOnly(True)

        self.horizontalLayout_90.addWidget(self.usr_position)

        self.prev_combo = QComboBox(self.frame_82)
        self.prev_combo.addItem("")
        self.prev_combo.addItem("")
        self.prev_combo.addItem("")
        self.prev_combo.addItem("")
        self.prev_combo.setObjectName(u"prev_combo")
        self.prev_combo.setMinimumSize(QSize(120, 30))
        self.prev_combo.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_90.addWidget(self.prev_combo)


        self.verticalLayout_34.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_77)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(200, 0))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_89.setSpacing(5)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_83)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_89.addWidget(self.label_48)

        self.usr_id = QLineEdit(self.frame_83)
        self.usr_id.setObjectName(u"usr_id")
        self.usr_id.setMinimumSize(QSize(0, 30))
        self.usr_id.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.usr_id.setReadOnly(True)

        self.horizontalLayout_89.addWidget(self.usr_id)


        self.verticalLayout_34.addWidget(self.frame_83)

        self.barcodelabel = QLabel(self.frame_77)
        self.barcodelabel.setObjectName(u"barcodelabel")
        self.barcodelabel.setMinimumSize(QSize(0, 50))

        self.verticalLayout_34.addWidget(self.barcodelabel)

        self.frame_84 = QFrame(self.frame_77)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_91.setSpacing(5)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_34.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_77)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_92.setSpacing(5)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_34.addWidget(self.frame_85)


        self.horizontalLayout_83.addWidget(self.frame_77)


        self.verticalLayout_31.addWidget(self.frame_72)

        self.frame_75 = QFrame(self.user_control_page)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 0))
        self.frame_75.setMaximumSize(QSize(16777215, 50))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.new_usr_btn = QPushButton(self.frame_75)
        self.new_usr_btn.setObjectName(u"new_usr_btn")
        self.new_usr_btn.setMinimumSize(QSize(100, 40))
        self.new_usr_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_93.addWidget(self.new_usr_btn)

        self.horizontalSpacer_29 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_93.addItem(self.horizontalSpacer_29)

        self.del_user_btn = QPushButton(self.frame_75)
        self.del_user_btn.setObjectName(u"del_user_btn")
        self.del_user_btn.setMinimumSize(QSize(100, 40))
        self.del_user_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_93.addWidget(self.del_user_btn)

        self.update_user_btn = QPushButton(self.frame_75)
        self.update_user_btn.setObjectName(u"update_user_btn")
        self.update_user_btn.setMinimumSize(QSize(100, 40))
        self.update_user_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_93.addWidget(self.update_user_btn)

        self.add_user_btn = QPushButton(self.frame_75)
        self.add_user_btn.setObjectName(u"add_user_btn")
        self.add_user_btn.setMinimumSize(QSize(100, 40))
        self.add_user_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_93.addWidget(self.add_user_btn)


        self.verticalLayout_31.addWidget(self.frame_75)

        self.recipt_stack.addWidget(self.user_control_page)
        self.re_update_page = QWidget()
        self.re_update_page.setObjectName(u"re_update_page")
        self.horizontalLayout_46 = QHBoxLayout(self.re_update_page)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.root1_4 = QFrame(self.re_update_page)
        self.root1_4.setObjectName(u"root1_4")
        self.root1_4.setFrameShape(QFrame.StyledPanel)
        self.root1_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.root1_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.re_top_frame_4 = QFrame(self.root1_4)
        self.re_top_frame_4.setObjectName(u"re_top_frame_4")
        self.re_top_frame_4.setMinimumSize(QSize(250, 0))
        self.re_top_frame_4.setFrameShape(QFrame.StyledPanel)
        self.re_top_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.re_top_frame_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_55 = QFrame(self.re_top_frame_4)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_36 = QLabel(self.frame_55)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_64.addWidget(self.label_36)

        self.re_up_name = QLineEdit(self.frame_55)
        self.re_up_name.setObjectName(u"re_up_name")
        self.re_up_name.setMinimumSize(QSize(0, 30))
        self.re_up_name.setMaximumSize(QSize(220, 16777215))
        self.re_up_name.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.re_up_name.setReadOnly(True)

        self.horizontalLayout_64.addWidget(self.re_up_name)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_11)


        self.verticalLayout_24.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.re_top_frame_4)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_37 = QLabel(self.frame_56)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_65.addWidget(self.label_37)

        self.re_up_age = QLineEdit(self.frame_56)
        self.re_up_age.setObjectName(u"re_up_age")
        self.re_up_age.setMinimumSize(QSize(0, 30))
        self.re_up_age.setMaximumSize(QSize(220, 16777215))
        self.re_up_age.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.re_up_age.setReadOnly(True)

        self.horizontalLayout_65.addWidget(self.re_up_age)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_12)


        self.verticalLayout_24.addWidget(self.frame_56)


        self.verticalLayout_23.addWidget(self.re_top_frame_4)

        self.re_down_frame_4 = QFrame(self.root1_4)
        self.re_down_frame_4.setObjectName(u"re_down_frame_4")
        self.re_down_frame_4.setMaximumSize(QSize(16777215, 200))
        self.re_down_frame_4.setFrameShape(QFrame.StyledPanel)
        self.re_down_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.re_down_frame_4)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.right_frm_4 = QFrame(self.re_down_frame_4)
        self.right_frm_4.setObjectName(u"right_frm_4")
        self.right_frm_4.setFrameShape(QFrame.StyledPanel)
        self.right_frm_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.right_frm_4)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.right_frm_4)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_58)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_39 = QLabel(self.frame_59)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_69.addWidget(self.label_39)

        self.re_up_num = QLineEdit(self.frame_59)
        self.re_up_num.setObjectName(u"re_up_num")
        self.re_up_num.setMinimumSize(QSize(0, 30))
        self.re_up_num.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.re_up_num.setReadOnly(True)

        self.horizontalLayout_69.addWidget(self.re_up_num)


        self.verticalLayout_25.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_40 = QLabel(self.frame_60)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_70.addWidget(self.label_40)

        self.re_up_date = QLineEdit(self.frame_60)
        self.re_up_date.setObjectName(u"re_up_date")
        self.re_up_date.setMinimumSize(QSize(0, 30))
        self.re_up_date.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.re_up_date.setReadOnly(True)

        self.horizontalLayout_70.addWidget(self.re_up_date)


        self.verticalLayout_25.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_41 = QLabel(self.frame_61)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_71.addWidget(self.label_41)

        self.re_up_time = QLineEdit(self.frame_61)
        self.re_up_time.setObjectName(u"re_up_time")
        self.re_up_time.setMinimumSize(QSize(0, 30))
        self.re_up_time.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.re_up_time.setReadOnly(True)

        self.horizontalLayout_71.addWidget(self.re_up_time)


        self.verticalLayout_25.addWidget(self.frame_61)


        self.horizontalLayout_68.addWidget(self.frame_58)


        self.horizontalLayout_67.addWidget(self.right_frm_4)

        self.left_frm_4 = QFrame(self.re_down_frame_4)
        self.left_frm_4.setObjectName(u"left_frm_4")
        self.left_frm_4.setFrameShape(QFrame.StyledPanel)
        self.left_frm_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.left_frm_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.left_frm_4)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_42 = QLabel(self.frame_62)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_72.addWidget(self.label_42)

        self.re_up_default_price = QLineEdit(self.frame_62)
        self.re_up_default_price.setObjectName(u"re_up_default_price")
        self.re_up_default_price.setMinimumSize(QSize(0, 30))
        self.re_up_default_price.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.re_up_default_price.setReadOnly(True)

        self.horizontalLayout_72.addWidget(self.re_up_default_price)


        self.verticalLayout_26.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.left_frm_4)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_43 = QLabel(self.frame_63)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_73.addWidget(self.label_43)

        self.re_up_addtional_price = QLineEdit(self.frame_63)
        self.re_up_addtional_price.setObjectName(u"re_up_addtional_price")
        self.re_up_addtional_price.setMinimumSize(QSize(0, 30))
        self.re_up_addtional_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")

        self.horizontalLayout_73.addWidget(self.re_up_addtional_price)


        self.verticalLayout_26.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.left_frm_4)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_44 = QLabel(self.frame_64)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_74.addWidget(self.label_44)

        self.re_up_total_price = QLineEdit(self.frame_64)
        self.re_up_total_price.setObjectName(u"re_up_total_price")
        self.re_up_total_price.setMinimumSize(QSize(0, 30))
        self.re_up_total_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.re_up_total_price.setReadOnly(True)

        self.horizontalLayout_74.addWidget(self.re_up_total_price)


        self.verticalLayout_26.addWidget(self.frame_64)


        self.horizontalLayout_67.addWidget(self.left_frm_4)


        self.verticalLayout_23.addWidget(self.re_down_frame_4)

        self.re_bottom_page_4 = QFrame(self.root1_4)
        self.re_bottom_page_4.setObjectName(u"re_bottom_page_4")
        self.re_bottom_page_4.setMaximumSize(QSize(16777215, 50))
        self.re_bottom_page_4.setFrameShape(QFrame.StyledPanel)
        self.re_bottom_page_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.re_bottom_page_4)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalSpacer_14 = QSpacerItem(523, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_14)

        self.re_update_cancle_btn = QPushButton(self.re_bottom_page_4)
        self.re_update_cancle_btn.setObjectName(u"re_update_cancle_btn")
        self.re_update_cancle_btn.setMinimumSize(QSize(80, 40))
        self.re_update_cancle_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_75.addWidget(self.re_update_cancle_btn)

        self.re_update_btn = QPushButton(self.re_bottom_page_4)
        self.re_update_btn.setObjectName(u"re_update_btn")
        self.re_update_btn.setMinimumSize(QSize(80, 40))
        self.re_update_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_75.addWidget(self.re_update_btn)


        self.verticalLayout_23.addWidget(self.re_bottom_page_4)


        self.horizontalLayout_46.addWidget(self.root1_4)

        self.recipt_stack.addWidget(self.re_update_page)
        self.appoinment_page = QWidget()
        self.appoinment_page.setObjectName(u"appoinment_page")
        self.horizontalLayout_30 = QHBoxLayout(self.appoinment_page)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.root1_2 = QFrame(self.appoinment_page)
        self.root1_2.setObjectName(u"root1_2")
        self.root1_2.setFrameShape(QFrame.StyledPanel)
        self.root1_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.root1_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.re_top_frame_2 = QFrame(self.root1_2)
        self.re_top_frame_2.setObjectName(u"re_top_frame_2")
        self.re_top_frame_2.setMinimumSize(QSize(250, 0))
        self.re_top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.re_top_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.re_top_frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_15 = QFrame(self.re_top_frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(330, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.lineEdit = QLineEdit(self.frame_17)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(400, 16777215))
        self.lineEdit.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.horizontalLayout_42.addWidget(self.lineEdit)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.ap_list = QListWidget(self.frame_16)
        self.ap_list.setObjectName(u"ap_list")

        self.horizontalLayout_21.addWidget(self.ap_list)


        self.verticalLayout_11.addWidget(self.frame_16)

        self.frame_37 = QFrame(self.frame_15)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout_11.addWidget(self.frame_37)


        self.horizontalLayout_19.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.re_top_frame_2)

        self.re_down_frame_2 = QFrame(self.root1_2)
        self.re_down_frame_2.setObjectName(u"re_down_frame_2")
        self.re_down_frame_2.setMaximumSize(QSize(16777215, 200))
        self.re_down_frame_2.setFrameShape(QFrame.StyledPanel)
        self.re_down_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.re_down_frame_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.right_frm_2 = QFrame(self.re_down_frame_2)
        self.right_frm_2.setObjectName(u"right_frm_2")
        self.right_frm_2.setFrameShape(QFrame.StyledPanel)
        self.right_frm_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.right_frm_2)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.right_frm_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_22.addWidget(self.label_7)

        self.ap_name = QLineEdit(self.frame_19)
        self.ap_name.setObjectName(u"ap_name")
        self.ap_name.setMinimumSize(QSize(0, 30))
        self.ap_name.setStyleSheet(u"background-color: rgb(220, 220, 220);")

        self.horizontalLayout_22.addWidget(self.ap_name)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_23.addWidget(self.label_8)

        self.ap_age = QLineEdit(self.frame_20)
        self.ap_age.setObjectName(u"ap_age")
        self.ap_age.setMinimumSize(QSize(0, 35))
        self.ap_age.setStyleSheet(u"background-color: rgb(232, 232, 232);")

        self.horizontalLayout_23.addWidget(self.ap_age)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_24.addWidget(self.label_9)

        self.ap_phone_num = QLineEdit(self.frame_21)
        self.ap_phone_num.setObjectName(u"ap_phone_num")
        self.ap_phone_num.setMinimumSize(QSize(0, 35))
        self.ap_phone_num.setStyleSheet(u"background-color: rgb(232, 232, 232);")

        self.horizontalLayout_24.addWidget(self.ap_phone_num)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.horizontalLayout_41.addWidget(self.frame_18)


        self.horizontalLayout_25.addWidget(self.right_frm_2)

        self.left_frm_2 = QFrame(self.re_down_frame_2)
        self.left_frm_2.setObjectName(u"left_frm_2")
        self.left_frm_2.setFrameShape(QFrame.StyledPanel)
        self.left_frm_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.left_frm_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.left_frm_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_13.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.left_frm_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")

        self.verticalLayout_13.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.left_frm_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")

        self.verticalLayout_13.addWidget(self.frame_24)


        self.horizontalLayout_25.addWidget(self.left_frm_2)


        self.verticalLayout_10.addWidget(self.re_down_frame_2)

        self.re_bottom_page_2 = QFrame(self.root1_2)
        self.re_bottom_page_2.setObjectName(u"re_bottom_page_2")
        self.re_bottom_page_2.setMaximumSize(QSize(16777215, 50))
        self.re_bottom_page_2.setFrameShape(QFrame.StyledPanel)
        self.re_bottom_page_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.re_bottom_page_2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_4 = QSpacerItem(523, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_4)

        self.ap_cancle_btn = QPushButton(self.re_bottom_page_2)
        self.ap_cancle_btn.setObjectName(u"ap_cancle_btn")
        self.ap_cancle_btn.setMinimumSize(QSize(80, 40))
        self.ap_cancle_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_29.addWidget(self.ap_cancle_btn)

        self.ap_edit_btn = QPushButton(self.re_bottom_page_2)
        self.ap_edit_btn.setObjectName(u"ap_edit_btn")
        self.ap_edit_btn.setMinimumSize(QSize(80, 40))
        self.ap_edit_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_29.addWidget(self.ap_edit_btn)

        self.ap_ok_btn = QPushButton(self.re_bottom_page_2)
        self.ap_ok_btn.setObjectName(u"ap_ok_btn")
        self.ap_ok_btn.setMinimumSize(QSize(80, 40))
        self.ap_ok_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_29.addWidget(self.ap_ok_btn)


        self.verticalLayout_10.addWidget(self.re_bottom_page_2)


        self.horizontalLayout_30.addWidget(self.root1_2)

        self.recipt_stack.addWidget(self.appoinment_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_7 = QVBoxLayout(self.setting_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_25 = QFrame(self.setting_page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_40 = QFrame(self.frame_25)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_24 = QLabel(self.frame_40)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_47.addWidget(self.label_24)

        self.set_rc_def_price = QLineEdit(self.frame_40)
        self.set_rc_def_price.setObjectName(u"set_rc_def_price")
        self.set_rc_def_price.setMinimumSize(QSize(0, 30))
        self.set_rc_def_price.setMaximumSize(QSize(200, 16777215))
        self.set_rc_def_price.setStyleSheet(u"background-color: rgb(220, 220, 220);")

        self.horizontalLayout_47.addWidget(self.set_rc_def_price)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_16)


        self.verticalLayout_27.addWidget(self.frame_40)

        self.verticalSpacer_2 = QSpacerItem(20, 308, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.frame_25)

        self.frame_32 = QFrame(self.setting_page)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(487, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_15)

        self.set_cancle_btn = QPushButton(self.frame_32)
        self.set_cancle_btn.setObjectName(u"set_cancle_btn")
        self.set_cancle_btn.setMinimumSize(QSize(100, 40))
        self.set_cancle_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_35.addWidget(self.set_cancle_btn)

        self.set_apply_btn = QPushButton(self.frame_32)
        self.set_apply_btn.setObjectName(u"set_apply_btn")
        self.set_apply_btn.setMinimumSize(QSize(100, 40))
        self.set_apply_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_35.addWidget(self.set_apply_btn)


        self.verticalLayout_7.addWidget(self.frame_32)

        self.recipt_stack.addWidget(self.setting_page)
        self.pharmacy_page = QWidget()
        self.pharmacy_page.setObjectName(u"pharmacy_page")
        self.verticalLayout_39 = QVBoxLayout(self.pharmacy_page)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.report_page = QTabWidget(self.pharmacy_page)
        self.report_page.setObjectName(u"report_page")
        self.report_page.setTabPosition(QTabWidget.North)
        self.report_page.setTabShape(QTabWidget.Rounded)
        self.report_page.setElideMode(Qt.ElideNone)
        self.report_page.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_88 = QFrame(self.tab_2)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(600, 16777215))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_88)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_91 = QFrame(self.frame_88)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMaximumSize(QSize(16777215, 50))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalSpacer_36 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_36)

        self.r_m_srch = QLineEdit(self.frame_91)
        self.r_m_srch.setObjectName(u"r_m_srch")
        self.r_m_srch.setMinimumSize(QSize(200, 30))
        self.r_m_srch.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_123.addWidget(self.r_m_srch)

        self.horizontalSpacer_37 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_37)


        self.verticalLayout_46.addWidget(self.frame_91)

        self.frame_154 = QFrame(self.frame_88)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMaximumSize(QSize(16777215, 30))
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_99 = QLabel(self.frame_154)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.label_99)

        self.label_100 = QLabel(self.frame_154)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.label_100)

        self.label_102 = QLabel(self.frame_154)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.label_102)


        self.verticalLayout_46.addWidget(self.frame_154)

        self.frame_92 = QFrame(self.frame_88)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_92)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_94)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_47.addWidget(self.frame_94)

        self.r_m_ad_list = QListWidget(self.frame_92)
        self.r_m_ad_list.setObjectName(u"r_m_ad_list")
        self.r_m_ad_list.setMinimumSize(QSize(0, 200))
        self.r_m_ad_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_47.addWidget(self.r_m_ad_list)


        self.verticalLayout_46.addWidget(self.frame_92)

        self.frame_117 = QFrame(self.frame_88)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setMinimumSize(QSize(0, 180))
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_126.setSpacing(0)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_118)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(9, 9, 9, 9)
        self.frame_119 = QFrame(self.frame_118)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_127.setSpacing(5)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.frame_119)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_127.addWidget(self.label_83)

        self.r_m_name = QLineEdit(self.frame_119)
        self.r_m_name.setObjectName(u"r_m_name")
        self.r_m_name.setMinimumSize(QSize(0, 30))
        self.r_m_name.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_name.setReadOnly(True)

        self.horizontalLayout_127.addWidget(self.r_m_name)


        self.verticalLayout_44.addWidget(self.frame_119)

        self.r_m_brand = QFrame(self.frame_118)
        self.r_m_brand.setObjectName(u"r_m_brand")
        self.r_m_brand.setFrameShape(QFrame.StyledPanel)
        self.r_m_brand.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.r_m_brand)
        self.horizontalLayout_128.setSpacing(5)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.r_m_brand)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_128.addWidget(self.label_84)

        self.r_m_brand_2 = QLineEdit(self.r_m_brand)
        self.r_m_brand_2.setObjectName(u"r_m_brand_2")
        self.r_m_brand_2.setMinimumSize(QSize(0, 30))
        self.r_m_brand_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_brand_2.setReadOnly(True)

        self.horizontalLayout_128.addWidget(self.r_m_brand_2)


        self.verticalLayout_44.addWidget(self.r_m_brand)

        self.frame_121 = QFrame(self.frame_118)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_129.setSpacing(5)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.frame_121)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_129.addWidget(self.label_85)

        self.r_m_exp = QLineEdit(self.frame_121)
        self.r_m_exp.setObjectName(u"r_m_exp")
        self.r_m_exp.setMinimumSize(QSize(0, 30))
        self.r_m_exp.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_exp.setReadOnly(True)

        self.horizontalLayout_129.addWidget(self.r_m_exp)


        self.verticalLayout_44.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.frame_118)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_130.setSpacing(5)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.frame_156 = QFrame(self.frame_122)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_156)
        self.horizontalLayout_159.setSpacing(5)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(0, 0, 0, 0)
        self.label_103 = QLabel(self.frame_156)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_159.addWidget(self.label_103)

        self.r_m_stocks = QLineEdit(self.frame_156)
        self.r_m_stocks.setObjectName(u"r_m_stocks")
        self.r_m_stocks.setMinimumSize(QSize(0, 30))
        self.r_m_stocks.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_stocks.setReadOnly(True)

        self.horizontalLayout_159.addWidget(self.r_m_stocks)


        self.horizontalLayout_130.addWidget(self.frame_156)


        self.verticalLayout_44.addWidget(self.frame_122)


        self.horizontalLayout_126.addWidget(self.frame_118)

        self.frame_123 = QFrame(self.frame_117)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_123)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_124 = QFrame(self.frame_123)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_124)
        self.horizontalLayout_131.setSpacing(5)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_124)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_131.addWidget(self.label_87)

        self.r_m_weight = QLineEdit(self.frame_124)
        self.r_m_weight.setObjectName(u"r_m_weight")
        self.r_m_weight.setMinimumSize(QSize(0, 30))
        self.r_m_weight.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_weight.setReadOnly(True)

        self.horizontalLayout_131.addWidget(self.r_m_weight)


        self.verticalLayout_45.addWidget(self.frame_124)

        self.frame_126 = QFrame(self.frame_123)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_133.setSpacing(5)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.frame_126)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_133.addWidget(self.label_89)

        self.r_m_u_price = QLineEdit(self.frame_126)
        self.r_m_u_price.setObjectName(u"r_m_u_price")
        self.r_m_u_price.setMinimumSize(QSize(0, 30))
        self.r_m_u_price.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_u_price.setReadOnly(True)

        self.horizontalLayout_133.addWidget(self.r_m_u_price)


        self.verticalLayout_45.addWidget(self.frame_126)

        self.frame_125 = QFrame(self.frame_123)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(200, 0))
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_132.setSpacing(5)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_125)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_132.addWidget(self.label_88)

        self.r_m_qty = QLineEdit(self.frame_125)
        self.r_m_qty.setObjectName(u"r_m_qty")
        self.r_m_qty.setMinimumSize(QSize(0, 30))
        self.r_m_qty.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_m_qty.setReadOnly(False)
        self.r_m_qty.setClearButtonEnabled(True)

        self.horizontalLayout_132.addWidget(self.r_m_qty)


        self.verticalLayout_45.addWidget(self.frame_125)

        self.frame_127 = QFrame(self.frame_123)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_134.setSpacing(5)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_45.addWidget(self.frame_127)


        self.horizontalLayout_126.addWidget(self.frame_123)


        self.verticalLayout_46.addWidget(self.frame_117)

        self.frame_90 = QFrame(self.frame_88)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 0))
        self.frame_90.setMaximumSize(QSize(16777215, 50))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_35 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_122.addItem(self.horizontalSpacer_35)

        self.r_add_btn = QPushButton(self.frame_90)
        self.r_add_btn.setObjectName(u"r_add_btn")
        self.r_add_btn.setMinimumSize(QSize(100, 40))
        self.r_add_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_122.addWidget(self.r_add_btn)


        self.verticalLayout_46.addWidget(self.frame_90)


        self.horizontalLayout.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.tab_2)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(400, 0))
        self.frame_89.setMaximumSize(QSize(500, 16777215))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_89)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_128 = QFrame(self.frame_89)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_128)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_134 = QFrame(self.frame_128)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_134)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMaximumSize(QSize(16777215, 30))
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.label_86 = QLabel(self.frame_135)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_86)

        self.label_90 = QLabel(self.frame_135)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_90)

        self.label_67 = QLabel(self.frame_135)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_136.addWidget(self.label_67)

        self.label_101 = QLabel(self.frame_135)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_136.addWidget(self.label_101)


        self.verticalLayout_53.addWidget(self.frame_135)


        self.verticalLayout_52.addWidget(self.frame_134)

        self.r_m_list = QListWidget(self.frame_128)
        self.r_m_list.setObjectName(u"r_m_list")
        self.r_m_list.setMinimumSize(QSize(0, 200))
        self.r_m_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_52.addWidget(self.r_m_list)


        self.verticalLayout_56.addWidget(self.frame_128)

        self.frame_136 = QFrame(self.frame_89)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(0, 180))
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_137.setSpacing(0)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.frame_142 = QFrame(self.frame_136)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_142)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.frame_155 = QFrame(self.frame_142)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMinimumSize(QSize(200, 0))
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_158.setSpacing(5)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.label_110 = QLabel(self.frame_155)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_158.addWidget(self.label_110)

        self.r_inv_number = QLineEdit(self.frame_155)
        self.r_inv_number.setObjectName(u"r_inv_number")
        self.r_inv_number.setMinimumSize(QSize(0, 30))
        self.r_inv_number.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_inv_number.setReadOnly(False)

        self.horizontalLayout_158.addWidget(self.r_inv_number)


        self.verticalLayout_55.addWidget(self.frame_155)

        self.frame_143 = QFrame(self.frame_142)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_142.setSpacing(5)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.frame_143)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_142.addWidget(self.label_107)

        self.r_total = QLineEdit(self.frame_143)
        self.r_total.setObjectName(u"r_total")
        self.r_total.setMinimumSize(QSize(0, 30))
        self.r_total.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_total.setReadOnly(True)

        self.horizontalLayout_142.addWidget(self.r_total)


        self.verticalLayout_55.addWidget(self.frame_143)

        self.frame_144 = QFrame(self.frame_142)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(200, 0))
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_143.setSpacing(5)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.frame_144)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_143.addWidget(self.label_108)

        self.r_discount = QLineEdit(self.frame_144)
        self.r_discount.setObjectName(u"r_discount")
        self.r_discount.setMinimumSize(QSize(0, 30))
        self.r_discount.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_discount.setReadOnly(False)
        self.r_discount.setClearButtonEnabled(True)

        self.horizontalLayout_143.addWidget(self.r_discount)

        self.r_m_discount_typr = QComboBox(self.frame_144)
        self.r_m_discount_typr.setObjectName(u"r_m_discount_typr")
        self.r_m_discount_typr.setMinimumSize(QSize(200, 30))
        self.r_m_discount_typr.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_143.addWidget(self.r_m_discount_typr)


        self.verticalLayout_55.addWidget(self.frame_144)

        self.frame_145 = QFrame(self.frame_142)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_144.setSpacing(5)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_109 = QLabel(self.frame_145)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_144.addWidget(self.label_109)

        self.r_afd_price = QLineEdit(self.frame_145)
        self.r_afd_price.setObjectName(u"r_afd_price")
        self.r_afd_price.setMinimumSize(QSize(0, 30))
        self.r_afd_price.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.r_afd_price.setReadOnly(True)

        self.horizontalLayout_144.addWidget(self.r_afd_price)


        self.verticalLayout_55.addWidget(self.frame_145)

        self.frame_146 = QFrame(self.frame_142)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_145.setSpacing(5)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_55.addWidget(self.frame_146)


        self.horizontalLayout_137.addWidget(self.frame_142)


        self.verticalLayout_56.addWidget(self.frame_136)

        self.frame_147 = QFrame(self.frame_89)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(0, 0))
        self.frame_147.setMaximumSize(QSize(16777215, 50))
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_38 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_38)

        self.r_inv_btn = QPushButton(self.frame_147)
        self.r_inv_btn.setObjectName(u"r_inv_btn")
        self.r_inv_btn.setMinimumSize(QSize(100, 40))
        self.r_inv_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_146.addWidget(self.r_inv_btn)


        self.verticalLayout_56.addWidget(self.frame_147)


        self.horizontalLayout.addWidget(self.frame_89)

        self.report_page.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_99 = QHBoxLayout(self.tab)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.frame_93 = QFrame(self.tab)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(400, 400))
        self.frame_93.setMaximumSize(QSize(500, 400))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_93)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_103 = QFrame(self.frame_93)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 180))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_103)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_109 = QFrame(self.frame_103)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_109)
        self.verticalLayout_42.setSpacing(10)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_117.setSpacing(5)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.frame_110)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_117.addWidget(self.label_74)

        self.ad_m_name = QLineEdit(self.frame_110)
        self.ad_m_name.setObjectName(u"ad_m_name")
        self.ad_m_name.setMinimumSize(QSize(0, 30))
        self.ad_m_name.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_name.setReadOnly(False)

        self.horizontalLayout_117.addWidget(self.ad_m_name)


        self.verticalLayout_42.addWidget(self.frame_110)

        self.frame_111 = QFrame(self.frame_109)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(200, 0))
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_118.setSpacing(5)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.frame_111)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_118.addWidget(self.label_75)

        self.ad_m_id = QLineEdit(self.frame_111)
        self.ad_m_id.setObjectName(u"ad_m_id")
        self.ad_m_id.setMinimumSize(QSize(0, 30))
        self.ad_m_id.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.ad_m_id.setReadOnly(False)

        self.horizontalLayout_118.addWidget(self.ad_m_id)


        self.verticalLayout_42.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_109)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_119.setSpacing(5)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.frame_112)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(80, 0))
        self.label_76.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_119.addWidget(self.label_76)

        self.ad_m_unit_combo = QComboBox(self.frame_112)
        self.ad_m_unit_combo.setObjectName(u"ad_m_unit_combo")
        self.ad_m_unit_combo.setMinimumSize(QSize(0, 30))
        self.ad_m_unit_combo.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_119.addWidget(self.ad_m_unit_combo)


        self.verticalLayout_42.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_109)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_120.setSpacing(5)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_113)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(80, 0))
        self.label_77.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_120.addWidget(self.label_77)

        self.ad_m_foam_combo = QComboBox(self.frame_113)
        self.ad_m_foam_combo.setObjectName(u"ad_m_foam_combo")
        self.ad_m_foam_combo.setMinimumSize(QSize(0, 30))
        self.ad_m_foam_combo.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_120.addWidget(self.ad_m_foam_combo)


        self.verticalLayout_42.addWidget(self.frame_113)


        self.verticalLayout_54.addWidget(self.frame_109)


        self.verticalLayout_36.addWidget(self.frame_103)

        self.frame_114 = QFrame(self.frame_93)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(0, 0))
        self.frame_114.setMaximumSize(QSize(16777215, 50))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_34)

        self.ad_add_btn = QPushButton(self.frame_114)
        self.ad_add_btn.setObjectName(u"ad_add_btn")
        self.ad_add_btn.setMinimumSize(QSize(100, 40))
        self.ad_add_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_121.addWidget(self.ad_add_btn)


        self.verticalLayout_36.addWidget(self.frame_114)


        self.horizontalLayout_99.addWidget(self.frame_93)

        self.report_page.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_100 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.frame_95 = QFrame(self.tab_3)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(400, 450))
        self.frame_95.setMaximumSize(QSize(500, 450))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_95)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_104 = QFrame(self.frame_95)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 180))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_104)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.frame_104)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_115)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_116 = QFrame(self.frame_115)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_124.setSpacing(5)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.frame_116)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(80, 0))
        self.label_78.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_124.addWidget(self.label_78)

        self.pc_m_medicine = QLineEdit(self.frame_116)
        self.pc_m_medicine.setObjectName(u"pc_m_medicine")
        self.pc_m_medicine.setMinimumSize(QSize(0, 30))
        self.pc_m_medicine.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_124.addWidget(self.pc_m_medicine)


        self.verticalLayout_43.addWidget(self.frame_116)

        self.pc_m_list = QListWidget(self.frame_115)
        self.pc_m_list.setObjectName(u"pc_m_list")
        self.pc_m_list.setDragEnabled(True)
        self.pc_m_list.setViewMode(QListView.IconMode)

        self.verticalLayout_43.addWidget(self.pc_m_list)

        self.frame_129 = QFrame(self.frame_115)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(200, 0))
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_125.setSpacing(5)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.frame_129)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_125.addWidget(self.label_79)

        self.pc_m_brand = QLineEdit(self.frame_129)
        self.pc_m_brand.setObjectName(u"pc_m_brand")
        self.pc_m_brand.setMinimumSize(QSize(0, 30))
        self.pc_m_brand.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_brand.setReadOnly(False)
        self.pc_m_brand.setClearButtonEnabled(True)

        self.horizontalLayout_125.addWidget(self.pc_m_brand)


        self.verticalLayout_43.addWidget(self.frame_129)

        self.frame_130 = QFrame(self.frame_115)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_135.setSpacing(5)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.frame_130)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_135.addWidget(self.label_80)

        self.pc_m_company = QLineEdit(self.frame_130)
        self.pc_m_company.setObjectName(u"pc_m_company")
        self.pc_m_company.setMinimumSize(QSize(0, 30))
        self.pc_m_company.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_company.setClearButtonEnabled(True)

        self.horizontalLayout_135.addWidget(self.pc_m_company)


        self.verticalLayout_43.addWidget(self.frame_130)

        self.frame_133 = QFrame(self.frame_115)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_140.setSpacing(5)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.frame_133)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_140.addWidget(self.label_82)

        self.pc_m_qty = QLineEdit(self.frame_133)
        self.pc_m_qty.setObjectName(u"pc_m_qty")
        self.pc_m_qty.setMinimumSize(QSize(0, 30))
        self.pc_m_qty.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_qty.setClearButtonEnabled(True)

        self.horizontalLayout_140.addWidget(self.pc_m_qty)


        self.verticalLayout_43.addWidget(self.frame_133)

        self.frame_149 = QFrame(self.frame_115)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_152.setSpacing(5)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_149)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_152.addWidget(self.label_98)

        self.pc_m_u_discount = QLineEdit(self.frame_149)
        self.pc_m_u_discount.setObjectName(u"pc_m_u_discount")
        self.pc_m_u_discount.setMinimumSize(QSize(0, 30))
        self.pc_m_u_discount.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_u_discount.setClearButtonEnabled(True)

        self.horizontalLayout_152.addWidget(self.pc_m_u_discount)

        self.pc_m_discount_typr = QComboBox(self.frame_149)
        self.pc_m_discount_typr.setObjectName(u"pc_m_discount_typr")
        self.pc_m_discount_typr.setMinimumSize(QSize(200, 30))
        self.pc_m_discount_typr.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_152.addWidget(self.pc_m_discount_typr)


        self.verticalLayout_43.addWidget(self.frame_149)

        self.frame_131 = QFrame(self.frame_115)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_131)
        self.horizontalLayout_138.setSpacing(5)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.frame_131)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_138.addWidget(self.label_81)

        self.pc_m_u_price = QLineEdit(self.frame_131)
        self.pc_m_u_price.setObjectName(u"pc_m_u_price")
        self.pc_m_u_price.setMinimumSize(QSize(0, 30))
        self.pc_m_u_price.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_u_price.setClearButtonEnabled(True)

        self.horizontalLayout_138.addWidget(self.pc_m_u_price)

        self.label_64 = QLabel(self.frame_131)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_138.addWidget(self.label_64)

        self.pc_m_total = QLineEdit(self.frame_131)
        self.pc_m_total.setObjectName(u"pc_m_total")
        self.pc_m_total.setMinimumSize(QSize(0, 30))
        self.pc_m_total.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.pc_m_total.setReadOnly(True)

        self.horizontalLayout_138.addWidget(self.pc_m_total)


        self.verticalLayout_43.addWidget(self.frame_131)

        self.frame_137 = QFrame(self.frame_115)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_141.setSpacing(5)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.frame_137)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(80, 0))
        self.label_91.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_141.addWidget(self.label_91)


        self.verticalLayout_43.addWidget(self.frame_137)


        self.verticalLayout_57.addWidget(self.frame_115)


        self.verticalLayout_37.addWidget(self.frame_104)

        self.frame_132 = QFrame(self.frame_95)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 0))
        self.frame_132.setMaximumSize(QSize(16777215, 50))
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_39 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_139.addItem(self.horizontalSpacer_39)

        self.update_user_btn_4 = QPushButton(self.frame_132)
        self.update_user_btn_4.setObjectName(u"update_user_btn_4")
        self.update_user_btn_4.setMinimumSize(QSize(100, 40))
        self.update_user_btn_4.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_139.addWidget(self.update_user_btn_4)

        self.pc_prch_btn = QPushButton(self.frame_132)
        self.pc_prch_btn.setObjectName(u"pc_prch_btn")
        self.pc_prch_btn.setMinimumSize(QSize(100, 40))
        self.pc_prch_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_139.addWidget(self.pc_prch_btn)


        self.verticalLayout_37.addWidget(self.frame_132)


        self.horizontalLayout_100.addWidget(self.frame_95)

        self.report_page.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_101 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.frame_96 = QFrame(self.tab_4)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMaximumSize(QSize(16777215, 16777215))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_96)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(16777215, 50))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalSpacer_40 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_40)

        self.m_store_srch = QLineEdit(self.frame_97)
        self.m_store_srch.setObjectName(u"m_store_srch")
        self.m_store_srch.setMinimumSize(QSize(200, 30))
        self.m_store_srch.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_147.addWidget(self.m_store_srch)

        self.horizontalSpacer_41 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_41)


        self.verticalLayout_48.addWidget(self.frame_97)

        self.frame_101 = QFrame(self.frame_96)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMaximumSize(QSize(16777215, 30))
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_57 = QLabel(self.frame_101)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_101)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_58)

        self.label_59 = QLabel(self.frame_101)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_101)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_60)

        self.label_61 = QLabel(self.frame_101)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_101)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_62)

        self.label_66 = QLabel(self.frame_101)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_102.addWidget(self.label_66)


        self.verticalLayout_48.addWidget(self.frame_101)

        self.frame_98 = QFrame(self.frame_96)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_98)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_99)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_49.addWidget(self.frame_99)

        self.m_store_list = QListWidget(self.frame_98)
        self.m_store_list.setObjectName(u"m_store_list")
        self.m_store_list.setMinimumSize(QSize(0, 200))
        self.m_store_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_49.addWidget(self.m_store_list)


        self.verticalLayout_48.addWidget(self.frame_98)

        self.frame_138 = QFrame(self.frame_96)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 180))
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_139)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.frame_139)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_149.setSpacing(5)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_140)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_149.addWidget(self.label_92)

        self.m_store_name = QLineEdit(self.frame_140)
        self.m_store_name.setObjectName(u"m_store_name")
        self.m_store_name.setMinimumSize(QSize(0, 30))
        self.m_store_name.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_name.setInputMethodHints(Qt.ImhNone)
        self.m_store_name.setClearButtonEnabled(True)

        self.horizontalLayout_149.addWidget(self.m_store_name)


        self.verticalLayout_50.addWidget(self.frame_140)

        self.frame_141 = QFrame(self.frame_139)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_150.setSpacing(5)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.frame_141)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_150.addWidget(self.label_93)

        self.m_store_brand = QLineEdit(self.frame_141)
        self.m_store_brand.setObjectName(u"m_store_brand")
        self.m_store_brand.setMinimumSize(QSize(0, 30))
        self.m_store_brand.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_brand.setClearButtonEnabled(True)

        self.horizontalLayout_150.addWidget(self.m_store_brand)

        self.label_63 = QLabel(self.frame_141)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_150.addWidget(self.label_63)

        self.m_store_company = QLineEdit(self.frame_141)
        self.m_store_company.setObjectName(u"m_store_company")
        self.m_store_company.setMinimumSize(QSize(0, 30))
        self.m_store_company.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_company.setClearButtonEnabled(True)

        self.horizontalLayout_150.addWidget(self.m_store_company)


        self.verticalLayout_50.addWidget(self.frame_141)

        self.frame_148 = QFrame(self.frame_139)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_151.setSpacing(5)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.label_94 = QLabel(self.frame_148)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(80, 0))
        self.label_94.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_151.addWidget(self.label_94)

        self.m_store_exp = QLineEdit(self.frame_148)
        self.m_store_exp.setObjectName(u"m_store_exp")
        self.m_store_exp.setMinimumSize(QSize(0, 30))
        self.m_store_exp.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_exp.setClearButtonEnabled(True)

        self.horizontalLayout_151.addWidget(self.m_store_exp)


        self.verticalLayout_50.addWidget(self.frame_148)


        self.horizontalLayout_148.addWidget(self.frame_139)

        self.frame_150 = QFrame(self.frame_138)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_150)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_153.setSpacing(5)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.label_95 = QLabel(self.frame_151)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(80, 0))
        self.label_95.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_153.addWidget(self.label_95)

        self.m_store_unit = QComboBox(self.frame_151)
        self.m_store_unit.setObjectName(u"m_store_unit")
        self.m_store_unit.setMinimumSize(QSize(0, 30))
        self.m_store_unit.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.horizontalLayout_153.addWidget(self.m_store_unit)


        self.verticalLayout_51.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_150)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(200, 0))
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_154.setSpacing(5)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.label_96 = QLabel(self.frame_152)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_154.addWidget(self.label_96)

        self.m_store_qty = QLineEdit(self.frame_152)
        self.m_store_qty.setObjectName(u"m_store_qty")
        self.m_store_qty.setMinimumSize(QSize(0, 30))
        self.m_store_qty.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_qty.setReadOnly(False)
        self.m_store_qty.setClearButtonEnabled(True)

        self.horizontalLayout_154.addWidget(self.m_store_qty)


        self.verticalLayout_51.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_150)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_155.setSpacing(5)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.frame_153)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_155.addWidget(self.label_97)

        self.m_store_u_price = QLineEdit(self.frame_153)
        self.m_store_u_price.setObjectName(u"m_store_u_price")
        self.m_store_u_price.setMinimumSize(QSize(0, 30))
        self.m_store_u_price.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.m_store_u_price.setClearButtonEnabled(True)

        self.horizontalLayout_155.addWidget(self.m_store_u_price)


        self.verticalLayout_51.addWidget(self.frame_153)


        self.horizontalLayout_148.addWidget(self.frame_150)


        self.verticalLayout_48.addWidget(self.frame_138)

        self.frame_100 = QFrame(self.frame_96)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 0))
        self.frame_100.setMaximumSize(QSize(16777215, 50))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157.addItem(self.horizontalSpacer_42)

        self.m_store_delete = QPushButton(self.frame_100)
        self.m_store_delete.setObjectName(u"m_store_delete")
        self.m_store_delete.setMinimumSize(QSize(100, 40))
        self.m_store_delete.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_157.addWidget(self.m_store_delete)

        self.m_store_update = QPushButton(self.frame_100)
        self.m_store_update.setObjectName(u"m_store_update")
        self.m_store_update.setMinimumSize(QSize(100, 40))
        self.m_store_update.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_157.addWidget(self.m_store_update)


        self.verticalLayout_48.addWidget(self.frame_100)


        self.horizontalLayout_101.addWidget(self.frame_96)

        self.report_page.addTab(self.tab_4, "")
        self.Report = QWidget()
        self.Report.setObjectName(u"Report")
        self.report_page.addTab(self.Report, "")

        self.verticalLayout_39.addWidget(self.report_page)

        self.recipt_stack.addWidget(self.pharmacy_page)
        self.ap_update_page = QWidget()
        self.ap_update_page.setObjectName(u"ap_update_page")
        self.horizontalLayout_58 = QHBoxLayout(self.ap_update_page)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.root1_3 = QFrame(self.ap_update_page)
        self.root1_3.setObjectName(u"root1_3")
        self.root1_3.setFrameShape(QFrame.StyledPanel)
        self.root1_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.root1_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.re_top_frame_3 = QFrame(self.root1_3)
        self.re_top_frame_3.setObjectName(u"re_top_frame_3")
        self.re_top_frame_3.setMinimumSize(QSize(250, 0))
        self.re_top_frame_3.setFrameShape(QFrame.StyledPanel)
        self.re_top_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.re_top_frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_50 = QFrame(self.re_top_frame_3)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_28 = QLabel(self.frame_50)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_59.addWidget(self.label_28)

        self.ap_up_doc = QLineEdit(self.frame_50)
        self.ap_up_doc.setObjectName(u"ap_up_doc")
        self.ap_up_doc.setMinimumSize(QSize(100, 30))
        self.ap_up_doc.setMaximumSize(QSize(220, 16777215))
        self.ap_up_doc.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_doc.setReadOnly(True)

        self.horizontalLayout_59.addWidget(self.ap_up_doc)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_6)


        self.verticalLayout_20.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.re_top_frame_3)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_30 = QLabel(self.frame_51)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_60.addWidget(self.label_30)

        self.ap_up_num = QLineEdit(self.frame_51)
        self.ap_up_num.setObjectName(u"ap_up_num")
        self.ap_up_num.setMinimumSize(QSize(0, 30))
        self.ap_up_num.setMaximumSize(QSize(220, 16777215))
        self.ap_up_num.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_num.setReadOnly(True)

        self.horizontalLayout_60.addWidget(self.ap_up_num)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_7)


        self.verticalLayout_20.addWidget(self.frame_51)

        self.frame_53 = QFrame(self.re_top_frame_3)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_34 = QLabel(self.frame_53)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_62.addWidget(self.label_34)

        self.ap_up_date = QLineEdit(self.frame_53)
        self.ap_up_date.setObjectName(u"ap_up_date")
        self.ap_up_date.setMinimumSize(QSize(0, 30))
        self.ap_up_date.setMaximumSize(QSize(220, 16777215))
        self.ap_up_date.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_date.setReadOnly(True)

        self.horizontalLayout_62.addWidget(self.ap_up_date)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_8)


        self.verticalLayout_20.addWidget(self.frame_53)

        self.frame_52 = QFrame(self.re_top_frame_3)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_33 = QLabel(self.frame_52)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_61.addWidget(self.label_33)

        self.ap_up_time = QLineEdit(self.frame_52)
        self.ap_up_time.setObjectName(u"ap_up_time")
        self.ap_up_time.setMinimumSize(QSize(0, 30))
        self.ap_up_time.setMaximumSize(QSize(220, 16777215))
        self.ap_up_time.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_time.setReadOnly(True)

        self.horizontalLayout_61.addWidget(self.ap_up_time)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_9)


        self.verticalLayout_20.addWidget(self.frame_52)


        self.verticalLayout_19.addWidget(self.re_top_frame_3)

        self.re_down_frame_3 = QFrame(self.root1_3)
        self.re_down_frame_3.setObjectName(u"re_down_frame_3")
        self.re_down_frame_3.setMaximumSize(QSize(16777215, 200))
        self.re_down_frame_3.setFrameShape(QFrame.StyledPanel)
        self.re_down_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.re_down_frame_3)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.right_frm_3 = QFrame(self.re_down_frame_3)
        self.right_frm_3.setObjectName(u"right_frm_3")
        self.right_frm_3.setFrameShape(QFrame.StyledPanel)
        self.right_frm_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.right_frm_3)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.right_frm_3)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_43)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_13 = QLabel(self.frame_44)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_51.addWidget(self.label_13)

        self.ap_up_name = QLineEdit(self.frame_44)
        self.ap_up_name.setObjectName(u"ap_up_name")
        self.ap_up_name.setMinimumSize(QSize(0, 30))
        self.ap_up_name.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_name.setReadOnly(True)

        self.horizontalLayout_51.addWidget(self.ap_up_name)


        self.verticalLayout_21.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_14 = QLabel(self.frame_45)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_52.addWidget(self.label_14)

        self.ap_up_age = QLineEdit(self.frame_45)
        self.ap_up_age.setObjectName(u"ap_up_age")
        self.ap_up_age.setMinimumSize(QSize(0, 30))
        self.ap_up_age.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_age.setReadOnly(True)

        self.horizontalLayout_52.addWidget(self.ap_up_age)


        self.verticalLayout_21.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_15 = QLabel(self.frame_46)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_53.addWidget(self.label_15)

        self.ap_up_phone = QLineEdit(self.frame_46)
        self.ap_up_phone.setObjectName(u"ap_up_phone")
        self.ap_up_phone.setMinimumSize(QSize(0, 30))
        self.ap_up_phone.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.ap_up_phone.setReadOnly(True)

        self.horizontalLayout_53.addWidget(self.ap_up_phone)


        self.verticalLayout_21.addWidget(self.frame_46)


        self.horizontalLayout_50.addWidget(self.frame_43)


        self.horizontalLayout_49.addWidget(self.right_frm_3)

        self.left_frm_3 = QFrame(self.re_down_frame_3)
        self.left_frm_3.setObjectName(u"left_frm_3")
        self.left_frm_3.setFrameShape(QFrame.StyledPanel)
        self.left_frm_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.left_frm_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.left_frm_3)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_16 = QLabel(self.frame_47)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_54.addWidget(self.label_16)

        self.ap_up_default_price = QLineEdit(self.frame_47)
        self.ap_up_default_price.setObjectName(u"ap_up_default_price")
        self.ap_up_default_price.setMinimumSize(QSize(0, 30))
        self.ap_up_default_price.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.ap_up_default_price.setReadOnly(True)

        self.horizontalLayout_54.addWidget(self.ap_up_default_price)


        self.verticalLayout_22.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.left_frm_3)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_31 = QLabel(self.frame_48)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_55.addWidget(self.label_31)

        self.ap_up_addtional_price = QLineEdit(self.frame_48)
        self.ap_up_addtional_price.setObjectName(u"ap_up_addtional_price")
        self.ap_up_addtional_price.setMinimumSize(QSize(0, 30))
        self.ap_up_addtional_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")

        self.horizontalLayout_55.addWidget(self.ap_up_addtional_price)


        self.verticalLayout_22.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.left_frm_3)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_32 = QLabel(self.frame_49)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_56.addWidget(self.label_32)

        self.ap_up_total_price = QLineEdit(self.frame_49)
        self.ap_up_total_price.setObjectName(u"ap_up_total_price")
        self.ap_up_total_price.setMinimumSize(QSize(0, 30))
        self.ap_up_total_price.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.ap_up_total_price.setReadOnly(True)

        self.horizontalLayout_56.addWidget(self.ap_up_total_price)


        self.verticalLayout_22.addWidget(self.frame_49)


        self.horizontalLayout_49.addWidget(self.left_frm_3)


        self.verticalLayout_19.addWidget(self.re_down_frame_3)

        self.re_bottom_page_3 = QFrame(self.root1_3)
        self.re_bottom_page_3.setObjectName(u"re_bottom_page_3")
        self.re_bottom_page_3.setMaximumSize(QSize(16777215, 50))
        self.re_bottom_page_3.setFrameShape(QFrame.StyledPanel)
        self.re_bottom_page_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.re_bottom_page_3)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer_5 = QSpacerItem(523, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_5)

        self.ap_update_cancle_btn = QPushButton(self.re_bottom_page_3)
        self.ap_update_cancle_btn.setObjectName(u"ap_update_cancle_btn")
        self.ap_update_cancle_btn.setMinimumSize(QSize(80, 40))
        self.ap_update_cancle_btn.setStyleSheet(u"background-color: rgb(232, 57, 63);")

        self.horizontalLayout_57.addWidget(self.ap_update_cancle_btn)

        self.ap_update_btn = QPushButton(self.re_bottom_page_3)
        self.ap_update_btn.setObjectName(u"ap_update_btn")
        self.ap_update_btn.setMinimumSize(QSize(80, 40))
        self.ap_update_btn.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_57.addWidget(self.ap_update_btn)


        self.verticalLayout_19.addWidget(self.re_bottom_page_3)


        self.horizontalLayout_58.addWidget(self.root1_3)

        self.recipt_stack.addWidget(self.ap_update_page)
        self.history_page = QWidget()
        self.history_page.setObjectName(u"history_page")
        self.verticalLayout_15 = QVBoxLayout(self.history_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_26 = QFrame(self.history_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 100))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 50))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.history_cat_combo = QComboBox(self.frame_29)
        self.history_cat_combo.setObjectName(u"history_cat_combo")
        self.history_cat_combo.setMinimumSize(QSize(150, 25))
        self.history_cat_combo.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.history_cat_combo.setMaxCount(2147483645)
        self.history_cat_combo.setModelColumn(0)

        self.horizontalLayout_33.addWidget(self.history_cat_combo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer)

        self.rc_radio = QRadioButton(self.frame_29)
        self.rc_radio.setObjectName(u"rc_radio")

        self.horizontalLayout_33.addWidget(self.rc_radio)

        self.ap_radio = QRadioButton(self.frame_29)
        self.ap_radio.setObjectName(u"ap_radio")

        self.horizontalLayout_33.addWidget(self.ap_radio)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_13)

        self.hostory_search = QLineEdit(self.frame_29)
        self.hostory_search.setObjectName(u"hostory_search")
        self.hostory_search.setMinimumSize(QSize(200, 25))
        self.hostory_search.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.hostory_search.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.hostory_search)


        self.verticalLayout_16.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 50))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.history_doc_combo = QComboBox(self.frame_30)
        self.history_doc_combo.setObjectName(u"history_doc_combo")
        self.history_doc_combo.setMinimumSize(QSize(150, 25))
        self.history_doc_combo.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.history_doc_combo.setEditable(False)
        self.history_doc_combo.setMaxCount(2147483645)

        self.horizontalLayout_32.addWidget(self.history_doc_combo)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.h_date_lbl = QLabel(self.frame_31)
        self.h_date_lbl.setObjectName(u"h_date_lbl")
        self.h_date_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.h_date_lbl)


        self.horizontalLayout_32.addWidget(self.frame_31)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.h_limit_lbl = QLabel(self.frame_33)
        self.h_limit_lbl.setObjectName(u"h_limit_lbl")
        self.h_limit_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.h_limit_lbl)

        self.history_limit_edit = QSpinBox(self.frame_33)
        self.history_limit_edit.setObjectName(u"history_limit_edit")
        self.history_limit_edit.setMinimumSize(QSize(0, 20))
        self.history_limit_edit.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.history_limit_edit.setMinimum(1)
        self.history_limit_edit.setMaximum(200)
        self.history_limit_edit.setValue(10)

        self.horizontalLayout_36.addWidget(self.history_limit_edit)


        self.horizontalLayout_32.addWidget(self.frame_33)


        self.verticalLayout_16.addWidget(self.frame_30)


        self.verticalLayout_15.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.history_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_27)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 40))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_17 = QLabel(self.frame_34)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_34)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_34)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_34)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_20)

        self.label_22 = QLabel(self.frame_34)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_22)

        self.label_21 = QLabel(self.frame_34)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_21)

        self.label_35 = QLabel(self.frame_34)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_35)


        self.verticalLayout_17.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_27)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_35)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea = QScrollArea(self.frame_35)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1044, 355))
        self.horizontalLayout_40 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.patient_history_list = QListWidget(self.scrollAreaWidgetContents)
        self.patient_history_list.setObjectName(u"patient_history_list")

        self.horizontalLayout_40.addWidget(self.patient_history_list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.frame_28 = QFrame(self.frame_35)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 30))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_23 = QLabel(self.frame_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_39.addWidget(self.label_23)

        self.history_cnt = QLabel(self.frame_28)
        self.history_cnt.setObjectName(u"history_cnt")
        self.history_cnt.setMinimumSize(QSize(0, 25))
        self.history_cnt.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.history_cnt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.history_cnt)

        self.label_25 = QLabel(self.frame_28)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_25)

        self.history_income = QLabel(self.frame_28)
        self.history_income.setObjectName(u"history_income")
        self.history_income.setMinimumSize(QSize(0, 25))
        self.history_income.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.history_income.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.history_income)


        self.verticalLayout_18.addWidget(self.frame_28)


        self.verticalLayout_17.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_27)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_10)

        self.pushButton_9 = QPushButton(self.frame_36)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 40))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(216, 216, 216);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(21, 199, 203);\n"
"\n"
"}")

        self.horizontalLayout_38.addWidget(self.pushButton_9)


        self.verticalLayout_17.addWidget(self.frame_36)


        self.verticalLayout_15.addWidget(self.frame_27)

        self.recipt_stack.addWidget(self.history_page)
        self.web_page = QWidget()
        self.web_page.setObjectName(u"web_page")
        self.verticalLayout_14 = QVBoxLayout(self.web_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_38 = QFrame(self.web_page)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_2 = QWebEngineView(self.frame_39)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_43.addWidget(self.widget_2)


        self.horizontalLayout_45.addWidget(self.frame_39)


        self.verticalLayout_14.addWidget(self.frame_38)

        self.rc_print_cancle = QFrame(self.web_page)
        self.rc_print_cancle.setObjectName(u"rc_print_cancle")
        self.rc_print_cancle.setMaximumSize(QSize(16777215, 50))
        self.rc_print_cancle.setFrameShape(QFrame.StyledPanel)
        self.rc_print_cancle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.rc_print_cancle)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.rc_cancl_print = QPushButton(self.rc_print_cancle)
        self.rc_cancl_print.setObjectName(u"rc_cancl_print")
        self.rc_cancl_print.setMinimumSize(QSize(0, 40))
        self.rc_cancl_print.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(234, 48, 119);\n"
"}")

        self.horizontalLayout_44.addWidget(self.rc_cancl_print)

        self.rc_print = QPushButton(self.rc_print_cancle)
        self.rc_print.setObjectName(u"rc_print")
        self.rc_print.setMinimumSize(QSize(0, 40))
        self.rc_print.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(130, 130, 130);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(12, 204, 108);\n"
"\n"
"}")

        self.horizontalLayout_44.addWidget(self.rc_print)


        self.verticalLayout_14.addWidget(self.rc_print_cancle)

        self.recipt_stack.addWidget(self.web_page)

        self.verticalLayout.addWidget(self.recipt_stack)


        self.horizontalLayout_3.addWidget(self.right_root)


        self.horizontalLayout_5.addWidget(self.roo_top)

        self.main_stack.addWidget(self.reception_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.horizontalLayout_63 = QHBoxLayout(self.login_page)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(300, 100, 300, 100)
        self.login_stack = QStackedWidget(self.login_page)
        self.login_stack.setObjectName(u"login_stack")
        self.login_stack.setStyleSheet(u"background-color: rgb(24, 58, 86);")
        self.login_window = QWidget()
        self.login_window.setObjectName(u"login_window")
        self.login_window.setStyleSheet(u"background-color: rgb(24, 58, 86);")
        self.verticalLayout_28 = QVBoxLayout(self.login_window)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_4)

        self.frame_161 = QFrame(self.login_window)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMinimumSize(QSize(160, 200))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_108.setSpacing(0)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_161)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(150, 150))
        self.label_50.setMaximumSize(QSize(100, 100))
        self.label_50.setStyleSheet(u"background-image: url(:/image/C:/Users/Dilhara/Downloads/New Project.jpg);")

        self.horizontalLayout_108.addWidget(self.label_50)


        self.verticalLayout_28.addWidget(self.frame_161)

        self.frame_54 = QFrame(self.login_window)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_54)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(20, -1, 20, -1)
        self.frame_66 = QFrame(self.frame_54)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_21)

        self.user_name = QLineEdit(self.frame_66)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setMinimumSize(QSize(250, 30))
        self.user_name.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.user_name.setAlignment(Qt.AlignCenter)
        self.user_name.setClearButtonEnabled(True)

        self.horizontalLayout_77.addWidget(self.user_name)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_20)


        self.verticalLayout_29.addWidget(self.frame_66)

        self.frame_65 = QFrame(self.frame_54)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_22)

        self.user_password = QLineEdit(self.frame_65)
        self.user_password.setObjectName(u"user_password")
        self.user_password.setMinimumSize(QSize(250, 30))
        self.user_password.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.user_password.setEchoMode(QLineEdit.Password)
        self.user_password.setAlignment(Qt.AlignCenter)
        self.user_password.setClearButtonEnabled(True)

        self.horizontalLayout_76.addWidget(self.user_password)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_23)


        self.verticalLayout_29.addWidget(self.frame_65)

        self.froget_pass_btn = QPushButton(self.frame_54)
        self.froget_pass_btn.setObjectName(u"froget_pass_btn")
        self.froget_pass_btn.setCursor(QCursor(Qt.OpenHandCursor))
        self.froget_pass_btn.setStyleSheet(u"color: rgb(48, 158, 255);")

        self.verticalLayout_29.addWidget(self.froget_pass_btn)


        self.verticalLayout_28.addWidget(self.frame_54)

        self.frame_57 = QFrame(self.login_window)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(20, -1, 20, -1)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_18)

        self.lodin_exit_btn = QPushButton(self.frame_57)
        self.lodin_exit_btn.setObjectName(u"lodin_exit_btn")
        self.lodin_exit_btn.setMinimumSize(QSize(120, 40))
        self.lodin_exit_btn.setStyleSheet(u"background-color: rgb(255, 94, 94);")

        self.horizontalLayout_66.addWidget(self.lodin_exit_btn)

        self.login_btn = QPushButton(self.frame_57)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(120, 40))
        self.login_btn.setStyleSheet(u"background-color: rgb(49, 234, 255);")

        self.horizontalLayout_66.addWidget(self.login_btn)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_19)


        self.verticalLayout_28.addWidget(self.frame_57)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_3)

        self.login_stack.addWidget(self.login_window)
        self.pass_inc_page = QWidget()
        self.pass_inc_page.setObjectName(u"pass_inc_page")
        self.verticalLayout_30 = QVBoxLayout(self.pass_inc_page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 20, -1, -1)
        self.frame_69 = QFrame(self.pass_inc_page)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_25)

        self.pushButton_2 = QPushButton(self.frame_69)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 100))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icon/assets/failed.png);")

        self.horizontalLayout_81.addWidget(self.pushButton_2)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_26)


        self.verticalLayout_30.addWidget(self.frame_69)

        self.frame_67 = QFrame(self.pass_inc_page)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.plainTextEdit = QPlainTextEdit(self.frame_67)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font2 = QFont()
        font2.setFamily(u"Segoe MDL2 Assets")
        font2.setPointSize(11)
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"color: rgb(255, 74, 101);")
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_80.addWidget(self.plainTextEdit)


        self.verticalLayout_30.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.pass_inc_page)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalSpacer_24 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_24)

        self.login_try_btn = QPushButton(self.frame_68)
        self.login_try_btn.setObjectName(u"login_try_btn")
        self.login_try_btn.setMinimumSize(QSize(100, 40))
        self.login_try_btn.setStyleSheet(u"background-color: rgb(49, 234, 255);")

        self.horizontalLayout_79.addWidget(self.login_try_btn)


        self.verticalLayout_30.addWidget(self.frame_68)

        self.login_stack.addWidget(self.pass_inc_page)
        self.try_again_page = QWidget()
        self.try_again_page.setObjectName(u"try_again_page")
        self.verticalLayout_35 = QVBoxLayout(self.try_again_page)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_73 = QFrame(self.try_again_page)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 125))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.pushButton_5 = QPushButton(self.frame_73)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 100))
        self.pushButton_5.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_98.addWidget(self.pushButton_5)


        self.verticalLayout_35.addWidget(self.frame_73)

        self.frame_86 = QFrame(self.try_again_page)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.textEdit = QTextEdit(self.frame_86)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_97.addWidget(self.textEdit)


        self.verticalLayout_35.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.try_again_page)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 0))
        self.frame_87.setMaximumSize(QSize(16777215, 40))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_30 = QSpacerItem(217, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_30)

        self.req_pass_reset = QPushButton(self.frame_87)
        self.req_pass_reset.setObjectName(u"req_pass_reset")
        self.req_pass_reset.setMinimumSize(QSize(100, 40))
        self.req_pass_reset.setStyleSheet(u"background-color: rgb(38, 223, 125);")

        self.horizontalLayout_96.addWidget(self.req_pass_reset)


        self.verticalLayout_35.addWidget(self.frame_87)

        self.login_stack.addWidget(self.try_again_page)

        self.horizontalLayout_63.addWidget(self.login_stack)

        self.main_stack.addWidget(self.login_page)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.horizontalLayout_85 = QHBoxLayout(self.admin_page)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.main_stack.addWidget(self.admin_page)

        self.horizontalLayout_12.addWidget(self.main_stack)

        MainWindow.setCentralWidget(self.root)

        self.retranslateUi(MainWindow)

        self.main_stack.setCurrentIndex(0)
        self.recipt_stack.setCurrentIndex(9)
        self.report_page_2.setCurrentIndex(1)
        self.report_page.setCurrentIndex(0)
        self.history_cat_combo.setCurrentIndex(-1)
        self.login_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.re_home.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.re_history.setText(QCoreApplication.translate("MainWindow", u"Add user", None))
        self.usr_control_btn.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.re_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.re_setting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_btn.setText("")
        self.log_out_btn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.time_lbl.setText(QCoreApplication.translate("MainWindow", u"7:49 AM", None))
        self.date_lbl.setText(QCoreApplication.translate("MainWindow", u"12/17/2021", None))
        self.notifi_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maxmize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maxmize", None))
#endif // QT_CONFIG(tooltip)
        self.maxmize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.counter_lbl.setText(QCoreApplication.translate("MainWindow", u"000", None))
#if QT_CONFIG(tooltip)
        self.counter_back_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Decrease number", None))
#endif // QT_CONFIG(tooltip)
        self.counter_back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(tooltip)
        self.counter_reset_btn.setToolTip(QCoreApplication.translate("MainWindow", u"reset counter", None))
#endif // QT_CONFIG(tooltip)
        self.counter_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.counter_next_btn.setToolTip(QCoreApplication.translate("MainWindow", u"increase number", None))
#endif // QT_CONFIG(tooltip)
        self.counter_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Default Fee", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Addtional Fee", None))
        self.rc_addtional_price.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Fee", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Date / Time", None))
        self.re_cancle_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.re_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.re_ok_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Qty", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Qty", None))
        self.r_m_qty_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity need to release", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.r_discount_3.setPlaceholderText("")
        self.r_add_btn_5.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        self.r_inv_number_2.setPlaceholderText("")
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.r_total_2.setPlaceholderText("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.r_discount_2.setPlaceholderText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Discount added price", None))
        self.r_inv_btn_2.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Qty", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Discount(%)", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"sss", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"j6", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"20 000", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"5", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.r_add_btn_4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.r_add_btn_3.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.r_add_btn_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.report_page_2.setTabText(self.report_page_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Item List", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Boook Name", None))
        self.ad_m_name_2.setPlaceholderText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Book ID", None))
        self.ad_m_id_2.setPlaceholderText("")
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Student Name", None))
        self.ad_m_id_3.setPlaceholderText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Student ID", None))
        self.ad_m_id_5.setPlaceholderText("")
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Return Date", None))
        self.ad_add_btn_2.setText(QCoreApplication.translate("MainWindow", u"Borrow", None))
        self.report_page_2.setTabText(self.report_page_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Add New Item", None))
        self.img_lbl.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Book Name", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Author Name", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Book Name", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Author Name", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.usr_position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select from list", None))
        self.prev_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"History", None))
        self.prev_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Literature", None))
        self.prev_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Relgion", None))
        self.prev_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Math", None))

        self.prev_combo.setProperty("placeholderText", "")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.usr_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a Category from list", None))
        self.barcodelabel.setText("")
        self.new_usr_btn.setText(QCoreApplication.translate("MainWindow", u"Borrow Books", None))
        self.del_user_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.update_user_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Number Token", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Default Fee", None))
        self.re_up_default_price.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Addtional Fee", None))
        self.re_up_addtional_price.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Total Fee", None))
        self.re_update_cancle_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.re_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Number", None))
#if QT_CONFIG(tooltip)
        self.ap_cancle_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Cancle apoinment", None))
#endif // QT_CONFIG(tooltip)
        self.ap_cancle_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.ap_edit_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Edit previous bills", None))
#endif // QT_CONFIG(tooltip)
        self.ap_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.ap_ok_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add apoinment", None))
#endif // QT_CONFIG(tooltip)
        self.ap_ok_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Student Number", None))
        self.set_cancle_btn.setText(QCoreApplication.translate("MainWindow", u"Cancle", None))
        self.set_apply_btn.setText(QCoreApplication.translate("MainWindow", u"release", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Medicine Brand", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Medicine Brand", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Expire date", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Avalible Stocks", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.r_m_weight.setPlaceholderText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"QTY", None))
        self.r_m_qty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity need to release", None))
        self.r_add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"QTY", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        self.r_inv_number.setPlaceholderText("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.r_total.setPlaceholderText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.r_discount.setPlaceholderText("")
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Discount added price", None))
        self.r_inv_btn.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.report_page.setTabText(self.report_page.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Release Medicine", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.ad_m_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select from list", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Medicine ID", None))
        self.ad_m_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a Position from list", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.ad_m_unit_combo.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Select a Unit", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Foam", None))
        self.ad_m_foam_combo.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Select a medicine foam", None))
        self.ad_add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.report_page.setTabText(self.report_page.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Add a new Medicine", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Medicine Brand", None))
        self.pc_m_brand.setPlaceholderText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Qty", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"EXP Date", None))
        # self.pc_m_exp.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.update_user_btn_4.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pc_prch_btn.setText(QCoreApplication.translate("MainWindow", u"Purchase", None))
        self.report_page.setTabText(self.report_page.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Purchace Medicine", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Medicine Brand", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Qty", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Exp Date", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Medicine Name", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Medecine Brand", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Expire date", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"QTY", None))
        self.m_store_qty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a Position from list", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Price of 1", None))
        self.m_store_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.m_store_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.report_page.setTabText(self.report_page.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Manage Medicine", None))
        self.report_page.setTabText(self.report_page.indexOf(self.Report), QCoreApplication.translate("MainWindow", u"Report", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Channled Doctor", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Number Token", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Default Fee", None))
        self.ap_up_default_price.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Addtional Fee", None))
        self.ap_up_addtional_price.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Total Fee", None))
        self.ap_update_cancle_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.ap_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.history_cat_combo.setCurrentText("")
        self.history_cat_combo.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Select a Categery", None))
        self.rc_radio.setText(QCoreApplication.translate("MainWindow", u"Reciption", None))
        self.ap_radio.setText(QCoreApplication.translate("MainWindow", u"Appoinment", None))
        self.hostory_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here", None))
        self.history_doc_combo.setCurrentText("")
        self.history_doc_combo.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Select a Doctor", None))
        self.h_date_lbl.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        # self.history_date_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.h_limit_lbl.setText(QCoreApplication.translate("MainWindow", u"Result Limit", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Position Num", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"OPD Issued NUmber", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Patient Age", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total Patients", None))
        self.history_cnt.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Total Income  Rs.", None))
        self.history_income.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.rc_cancl_print.setText(QCoreApplication.translate("MainWindow", u"Cancle", None))
        self.rc_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_50.setText("")
        self.user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter username", None))
        self.user_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter password", None))
        self.froget_pass_btn.setText(QCoreApplication.translate("MainWindow", u"Froget Password ?", None))
        self.lodin_exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\n"
"Username or password incorrect. Please check and try again !", None))
        self.login_try_btn.setText(QCoreApplication.translate("MainWindow", u"Try Again", None))
        self.pushButton_5.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e72774;\">Did you froget your password? Please contact system administrator!</span></p></body></html>", None))
        self.req_pass_reset.setText(QCoreApplication.translate("MainWindow", u"Request Reset", None))
    # retranslateUi

