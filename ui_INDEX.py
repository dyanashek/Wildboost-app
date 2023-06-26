# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_INDECvlgEhk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)
import prices_rc
import prices_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1135, 783)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u".SF NS Text"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/prices/Mail-image.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"QMainWindow {\n"
"     background:white;\n"
"     color:black;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #C02C70;\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #2F4FBB;\n"
"    color:white;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::flat {\n"
"    border:none;\n"
"    background-color:transparent;\n"
"}\n"
"QPushButton::flat:hover {\n"
"    border:none;\n"
"    background-color: white;\n"
"    color: #2F4FBB\n"
"}\n"
""
                        "QPushButton::flat:pressed {\n"
"    border:none;\n"
"    background-color: white;\n"
"    color: #0D31A6;\n"
"}\n"
"QLabel {\n"
"    color:black;\n"
"}\n"
"QCheckBox {\n"
"   color:black;\n"
"}\n"
"QRadioButton {\n"
"    color:black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled {\n"
"    color: #a3a3a3;\n"
"    background-color: #f2f2f2;\n"
"}\n"
"\n"
"QPushButton:focus, QToolButton:focus, QCommandLinkButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit, QSpinBox {\n"
"    border: 1px solid #B4B5B8;\n"
"    background-color: #fff;\n"
"    color: #333;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QLineEdit:focus, QSpinBox::focus {\n"
"    border: 2px solid #2F4FBB;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.IndexWindow = QStackedWidget(self.centralwidget)
        self.IndexWindow.setObjectName(u"IndexWindow")
        self.IndexWindow.setToolTipDuration(-1)
        self.IndexWindow.setAutoFillBackground(False)
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.LoginPage.setFont(font)
        self.verticalLayout = QVBoxLayout(self.LoginPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout_2.setSpacing(-1)
#endif
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_37 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_37, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 12, 1, 1, 1)

        self.verticalSpacer_53 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_53, 9, 3, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_59, 4, 2, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_16, 13, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.forgot_password_button_loginpage = QPushButton(self.LoginPage)
        self.forgot_password_button_loginpage.setObjectName(u"forgot_password_button_loginpage")
        font1 = QFont()
        font1.setFamilies([u".SF NS Text"])
        font1.setUnderline(True)
        self.forgot_password_button_loginpage.setFont(font1)
        self.forgot_password_button_loginpage.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgot_password_button_loginpage.setFocusPolicy(Qt.NoFocus)
        self.forgot_password_button_loginpage.setStyleSheet(u"")
        self.forgot_password_button_loginpage.setAutoRepeat(False)
        self.forgot_password_button_loginpage.setFlat(True)

        self.horizontalLayout_6.addWidget(self.forgot_password_button_loginpage)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 10, 3, 1, 1)

        self.password_input_loginpage = QLineEdit(self.LoginPage)
        self.password_input_loginpage.setObjectName(u"password_input_loginpage")
        self.password_input_loginpage.setMinimumSize(QSize(200, 30))
        self.password_input_loginpage.setFocusPolicy(Qt.StrongFocus)
        self.password_input_loginpage.setEchoMode(QLineEdit.Password)
        self.password_input_loginpage.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.password_input_loginpage, 6, 3, 1, 1)

        self.error_messages_LoginPage = QStackedWidget(self.LoginPage)
        self.error_messages_LoginPage.setObjectName(u"error_messages_LoginPage")
        self.error_messages_LoginPage.setMinimumSize(QSize(310, 39))
        self.error_messages_LoginPage.setMaximumSize(QSize(16777215, 39))
        self.message_wrong_data_LoginPage = QWidget()
        self.message_wrong_data_LoginPage.setObjectName(u"message_wrong_data_LoginPage")
        self.message_wrong_data_LoginPage.setMinimumSize(QSize(0, 39))
        self.horizontalLayout_46 = QHBoxLayout(self.message_wrong_data_LoginPage)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.message_wrong_data_LoginPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(310, 39))
        self.label_17.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u".SF NS Text"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setOpenExternalLinks(False)

        self.horizontalLayout_46.addWidget(self.label_17)

        self.error_messages_LoginPage.addWidget(self.message_wrong_data_LoginPage)
        self.message_no_connection_LoginPage = QWidget()
        self.message_no_connection_LoginPage.setObjectName(u"message_no_connection_LoginPage")
        self.horizontalLayout_21 = QHBoxLayout(self.message_no_connection_LoginPage)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.message_no_connection_LoginPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 39))
        self.label_18.setMaximumSize(QSize(16777215, 39))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setOpenExternalLinks(False)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.error_messages_LoginPage.addWidget(self.message_no_connection_LoginPage)
        self.message_empty_LoginPage = QWidget()
        self.message_empty_LoginPage.setObjectName(u"message_empty_LoginPage")
        self.error_messages_LoginPage.addWidget(self.message_empty_LoginPage)

        self.gridLayout_2.addWidget(self.error_messages_LoginPage, 2, 1, 1, 3)

        self.email_input_loginpage = QLineEdit(self.LoginPage)
        self.email_input_loginpage.setObjectName(u"email_input_loginpage")
        self.email_input_loginpage.setMinimumSize(QSize(200, 30))
        self.email_input_loginpage.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.email_input_loginpage.setDragEnabled(False)
        self.email_input_loginpage.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.email_input_loginpage.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.email_input_loginpage, 4, 3, 1, 1)

        self.password_label_loginpage = QLabel(self.LoginPage)
        self.password_label_loginpage.setObjectName(u"password_label_loginpage")
        self.password_label_loginpage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.password_label_loginpage, 6, 1, 1, 1)

        self.email_label_loginpage = QLabel(self.LoginPage)
        self.email_label_loginpage.setObjectName(u"email_label_loginpage")
        self.email_label_loginpage.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.email_label_loginpage, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.enter_button_loginpage = QPushButton(self.LoginPage)
        self.enter_button_loginpage.setObjectName(u"enter_button_loginpage")
        self.enter_button_loginpage.setMinimumSize(QSize(100, 30))
        self.enter_button_loginpage.setFont(font)
        self.enter_button_loginpage.setCursor(QCursor(Qt.PointingHandCursor))
        self.enter_button_loginpage.setFocusPolicy(Qt.NoFocus)
        self.enter_button_loginpage.setCheckable(False)
        self.enter_button_loginpage.setChecked(False)
        self.enter_button_loginpage.setAutoDefault(False)
        self.enter_button_loginpage.setFlat(False)

        self.horizontalLayout_2.addWidget(self.enter_button_loginpage)

        self.horizontalSpacer_54 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_54)

        self.signup_button_loginpage = QPushButton(self.LoginPage)
        self.signup_button_loginpage.setObjectName(u"signup_button_loginpage")
        self.signup_button_loginpage.setMinimumSize(QSize(100, 30))
        self.signup_button_loginpage.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_button_loginpage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.signup_button_loginpage)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 3, 1, 1)

        self.verticalSpacer_56 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_56, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label_6 = QLabel(self.LoginPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_38, 5, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 6, 0, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_39, 7, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.IndexWindow.addWidget(self.LoginPage)
        self.ChangeEmailPage = QWidget()
        self.ChangeEmailPage.setObjectName(u"ChangeEmailPage")
        self.verticalLayout_4 = QVBoxLayout(self.ChangeEmailPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_42 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_42, 6, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 5, 0, 1, 1)

        self.label_8 = QLabel(self.ChangeEmailPage)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 5, 1, 1, 1)

        self.label_10 = QLabel(self.ChangeEmailPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_10.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_4.addWidget(self.label_10, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.confirm_button_ChangeEmailPage = QPushButton(self.ChangeEmailPage)
        self.confirm_button_ChangeEmailPage.setObjectName(u"confirm_button_ChangeEmailPage")
        self.confirm_button_ChangeEmailPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_ChangeEmailPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_ChangeEmailPage.setFocusPolicy(Qt.NoFocus)
        self.confirm_button_ChangeEmailPage.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.confirm_button_ChangeEmailPage)

        self.horizontalSpacer_55 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_55)

        self.cancle_button_ChangeEmailPage = QPushButton(self.ChangeEmailPage)
        self.cancle_button_ChangeEmailPage.setObjectName(u"cancle_button_ChangeEmailPage")
        self.cancle_button_ChangeEmailPage.setMinimumSize(QSize(100, 30))
        self.cancle_button_ChangeEmailPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancle_button_ChangeEmailPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.cancle_button_ChangeEmailPage)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 9, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 11, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 5, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 10, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.email_input_ChangeEmailPage = QLineEdit(self.ChangeEmailPage)
        self.email_input_ChangeEmailPage.setObjectName(u"email_input_ChangeEmailPage")
        self.email_input_ChangeEmailPage.setMinimumSize(QSize(200, 30))
        self.email_input_ChangeEmailPage.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.email_input_ChangeEmailPage.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.email_input_ChangeEmailPage, 7, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_41, 4, 1, 1, 1)

        self.verticalSpacer_43 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_43, 8, 1, 1, 1)

        self.error_messages_ChangeEmailPage = QStackedWidget(self.ChangeEmailPage)
        self.error_messages_ChangeEmailPage.setObjectName(u"error_messages_ChangeEmailPage")
        self.error_messages_ChangeEmailPage.setMinimumSize(QSize(0, 39))
        self.error_messages_ChangeEmailPage.setMaximumSize(QSize(16777215, 39))
        self.message_invalid_email_ChangeEmailPage = QWidget()
        self.message_invalid_email_ChangeEmailPage.setObjectName(u"message_invalid_email_ChangeEmailPage")
        self.horizontalLayout_22 = QHBoxLayout(self.message_invalid_email_ChangeEmailPage)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.message_invalid_email_ChangeEmailPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(215, 39))
        self.label_19.setMaximumSize(QSize(215, 39))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setOpenExternalLinks(False)

        self.horizontalLayout_22.addWidget(self.label_19)

        self.error_messages_ChangeEmailPage.addWidget(self.message_invalid_email_ChangeEmailPage)
        self.message_empty_ChangeEmailPage = QWidget()
        self.message_empty_ChangeEmailPage.setObjectName(u"message_empty_ChangeEmailPage")
        self.error_messages_ChangeEmailPage.addWidget(self.message_empty_ChangeEmailPage)
        self.message_no_connection_ChangeEmailPage = QWidget()
        self.message_no_connection_ChangeEmailPage.setObjectName(u"message_no_connection_ChangeEmailPage")
        self.horizontalLayout_23 = QHBoxLayout(self.message_no_connection_ChangeEmailPage)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.message_no_connection_ChangeEmailPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(260, 39))
        self.label_20.setMaximumSize(QSize(260, 39))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setOpenExternalLinks(False)

        self.horizontalLayout_23.addWidget(self.label_20)

        self.error_messages_ChangeEmailPage.addWidget(self.message_no_connection_ChangeEmailPage)

        self.gridLayout_4.addWidget(self.error_messages_ChangeEmailPage, 3, 1, 1, 1)

        self.verticalSpacer_55 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_55, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.IndexWindow.addWidget(self.ChangeEmailPage)
        self.EnterEmailPage = QWidget()
        self.EnterEmailPage.setObjectName(u"EnterEmailPage")
        self.verticalLayout_5 = QVBoxLayout(self.EnterEmailPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_45 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_45, 6, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 3, 0, 1, 1)

        self.email_input_EnterEmailPage = QLineEdit(self.EnterEmailPage)
        self.email_input_EnterEmailPage.setObjectName(u"email_input_EnterEmailPage")
        self.email_input_EnterEmailPage.setMinimumSize(QSize(200, 30))
        self.email_input_EnterEmailPage.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.email_input_EnterEmailPage.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.email_input_EnterEmailPage, 5, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.confirm_button_EnterEmailPage = QPushButton(self.EnterEmailPage)
        self.confirm_button_EnterEmailPage.setObjectName(u"confirm_button_EnterEmailPage")
        self.confirm_button_EnterEmailPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_EnterEmailPage.setFont(font)
        self.confirm_button_EnterEmailPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_EnterEmailPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.confirm_button_EnterEmailPage)

        self.horizontalSpacer_56 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_56)

        self.cancle_button_EnterEmailPage = QPushButton(self.EnterEmailPage)
        self.cancle_button_EnterEmailPage.setObjectName(u"cancle_button_EnterEmailPage")
        self.cancle_button_EnterEmailPage.setMinimumSize(QSize(100, 30))
        self.cancle_button_EnterEmailPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancle_button_EnterEmailPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_7.addWidget(self.cancle_button_EnterEmailPage)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 7, 1, 1, 1)

        self.label_14 = QLabel(self.EnterEmailPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_14.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_5.addWidget(self.label_14, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 8, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.label_9 = QLabel(self.EnterEmailPage)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 3, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 3, 2, 1, 1)

        self.verticalSpacer_44 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_44, 4, 1, 1, 1)

        self.verticalSpacer_54 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_54, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.IndexWindow.addWidget(self.EnterEmailPage)
        self.SignupPage = QWidget()
        self.SignupPage.setObjectName(u"SignupPage")
        self.verticalLayout_2 = QVBoxLayout(self.SignupPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_47 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_47, 6, 3, 1, 1)

        self.password_input_SignupPage = QLineEdit(self.SignupPage)
        self.password_input_SignupPage.setObjectName(u"password_input_SignupPage")
        self.password_input_SignupPage.setMinimumSize(QSize(200, 30))
        self.password_input_SignupPage.setFocusPolicy(Qt.StrongFocus)
        self.password_input_SignupPage.setStyleSheet(u"")
        self.password_input_SignupPage.setEchoMode(QLineEdit.Password)
        self.password_input_SignupPage.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.password_input_SignupPage, 7, 3, 1, 1)

        self.verticalSpacer_49 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_49, 10, 3, 1, 1)

        self.password_repeat_input_SignupPage = QLineEdit(self.SignupPage)
        self.password_repeat_input_SignupPage.setObjectName(u"password_repeat_input_SignupPage")
        self.password_repeat_input_SignupPage.setMinimumSize(QSize(200, 30))
        self.password_repeat_input_SignupPage.setFocusPolicy(Qt.StrongFocus)
        self.password_repeat_input_SignupPage.setEchoMode(QLineEdit.Password)
        self.password_repeat_input_SignupPage.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.password_repeat_input_SignupPage, 9, 3, 1, 1)

        self.email_input_SignupPage = QLineEdit(self.SignupPage)
        self.email_input_SignupPage.setObjectName(u"email_input_SignupPage")
        self.email_input_SignupPage.setMinimumSize(QSize(200, 30))
        self.email_input_SignupPage.setFocusPolicy(Qt.StrongFocus)
        self.email_input_SignupPage.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.email_input_SignupPage.setFrame(True)
        self.email_input_SignupPage.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.email_input_SignupPage, 5, 3, 1, 1)

        self.label_5 = QLabel(self.SignupPage)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_15, 13, 3, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_48, 8, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.confirm_button_SiqnupPage = QPushButton(self.SignupPage)
        self.confirm_button_SiqnupPage.setObjectName(u"confirm_button_SiqnupPage")
        self.confirm_button_SiqnupPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_SiqnupPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_SiqnupPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.confirm_button_SiqnupPage)

        self.horizontalSpacer_57 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_57)

        self.cancle_button_SignupPage = QPushButton(self.SignupPage)
        self.cancle_button_SignupPage.setObjectName(u"cancle_button_SignupPage")
        self.cancle_button_SignupPage.setMinimumSize(QSize(100, 30))
        self.cancle_button_SignupPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancle_button_SignupPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.cancle_button_SignupPage)


        self.gridLayout.addLayout(self.horizontalLayout_3, 11, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 12, 3, 1, 1)

        self.label_4 = QLabel(self.SignupPage)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_58, 5, 2, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_46, 4, 1, 1, 1)

        self.label_3 = QLabel(self.SignupPage)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 4, 1, 1)

        self.label_15 = QLabel(self.SignupPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_15.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_15, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.verticalSpacer_57 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_57, 2, 3, 1, 1)

        self.error_messages_SignupPage = QStackedWidget(self.SignupPage)
        self.error_messages_SignupPage.setObjectName(u"error_messages_SignupPage")
        self.error_messages_SignupPage.setMinimumSize(QSize(0, 39))
        self.error_messages_SignupPage.setMaximumSize(QSize(16777215, 39))
        self.message_empty_SignupPage = QWidget()
        self.message_empty_SignupPage.setObjectName(u"message_empty_SignupPage")
        self.error_messages_SignupPage.addWidget(self.message_empty_SignupPage)
        self.message_no_connection_SignupPage = QWidget()
        self.message_no_connection_SignupPage.setObjectName(u"message_no_connection_SignupPage")
        self.horizontalLayout_30 = QHBoxLayout(self.message_no_connection_SignupPage)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.message_no_connection_SignupPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(260, 39))
        self.label_27.setMaximumSize(QSize(260, 39))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_27.setScaledContents(False)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setOpenExternalLinks(False)

        self.horizontalLayout_30.addWidget(self.label_27)

        self.error_messages_SignupPage.addWidget(self.message_no_connection_SignupPage)
        self.message_email_exists_SignupPage = QWidget()
        self.message_email_exists_SignupPage.setObjectName(u"message_email_exists_SignupPage")
        self.horizontalLayout_18 = QHBoxLayout(self.message_email_exists_SignupPage)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.message_email_exists_SignupPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(350, 39))
        self.label_2.setMaximumSize(QSize(350, 39))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)

        self.horizontalLayout_18.addWidget(self.label_2)

        self.error_messages_SignupPage.addWidget(self.message_email_exists_SignupPage)
        self.message_different_passwords_SignupPage = QWidget()
        self.message_different_passwords_SignupPage.setObjectName(u"message_different_passwords_SignupPage")
        self.horizontalLayout_17 = QHBoxLayout(self.message_different_passwords_SignupPage)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.message_different_passwords_SignupPage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(350, 39))
        self.label.setMaximumSize(QSize(350, 39))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout_17.addWidget(self.label)

        self.error_messages_SignupPage.addWidget(self.message_different_passwords_SignupPage)
        self.message_invalid_email_SignupPage = QWidget()
        self.message_invalid_email_SignupPage.setObjectName(u"message_invalid_email_SignupPage")
        self.horizontalLayout_19 = QHBoxLayout(self.message_invalid_email_SignupPage)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.message_invalid_email_SignupPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(350, 39))
        self.label_16.setMaximumSize(QSize(350, 39))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setOpenExternalLinks(False)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.error_messages_SignupPage.addWidget(self.message_invalid_email_SignupPage)

        self.gridLayout.addWidget(self.error_messages_SignupPage, 3, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.IndexWindow.addWidget(self.SignupPage)
        self.ChangPasswordPage = QWidget()
        self.ChangPasswordPage.setObjectName(u"ChangPasswordPage")
        self.verticalLayout_7 = QVBoxLayout(self.ChangPasswordPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout_7.setSpacing(-1)
#endif
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_12 = QLabel(self.ChangPasswordPage)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 5, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_19, 11, 3, 1, 1)

        self.password_repeat_ChangePasswordPage = QLineEdit(self.ChangPasswordPage)
        self.password_repeat_ChangePasswordPage.setObjectName(u"password_repeat_ChangePasswordPage")
        self.password_repeat_ChangePasswordPage.setMinimumSize(QSize(300, 30))
        self.password_repeat_ChangePasswordPage.setMaximumSize(QSize(300, 16777215))
        self.password_repeat_ChangePasswordPage.setFocusPolicy(Qt.StrongFocus)
        self.password_repeat_ChangePasswordPage.setEchoMode(QLineEdit.Password)
        self.password_repeat_ChangePasswordPage.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.password_repeat_ChangePasswordPage, 7, 3, 1, 1)

        self.label_13 = QLabel(self.ChangPasswordPage)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 7, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_17, 5, 0, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(15, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_27, 6, 3, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_18, 5, 4, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_13, 1, 1, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_50, 7, 2, 1, 1)

        self.new_password_input_ChangePasswordPage = QLineEdit(self.ChangPasswordPage)
        self.new_password_input_ChangePasswordPage.setObjectName(u"new_password_input_ChangePasswordPage")
        self.new_password_input_ChangePasswordPage.setMinimumSize(QSize(200, 30))
        self.new_password_input_ChangePasswordPage.setMaximumSize(QSize(300, 16777215))
        self.new_password_input_ChangePasswordPage.setFocusPolicy(Qt.StrongFocus)
        self.new_password_input_ChangePasswordPage.setEchoMode(QLineEdit.Password)
        self.new_password_input_ChangePasswordPage.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.new_password_input_ChangePasswordPage, 5, 3, 1, 1)

        self.error_messages_ChangePasswordPage = QStackedWidget(self.ChangPasswordPage)
        self.error_messages_ChangePasswordPage.setObjectName(u"error_messages_ChangePasswordPage")
        self.error_messages_ChangePasswordPage.setMinimumSize(QSize(0, 39))
        self.error_messages_ChangePasswordPage.setMaximumSize(QSize(300, 39))
        self.message_different_passwords_ChangePasswordPage = QWidget()
        self.message_different_passwords_ChangePasswordPage.setObjectName(u"message_different_passwords_ChangePasswordPage")
        self.horizontalLayout_24 = QHBoxLayout(self.message_different_passwords_ChangePasswordPage)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.message_different_passwords_ChangePasswordPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(300, 39))
        self.label_21.setMaximumSize(QSize(300, 39))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_21.setScaledContents(False)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setOpenExternalLinks(False)

        self.horizontalLayout_24.addWidget(self.label_21)

        self.error_messages_ChangePasswordPage.addWidget(self.message_different_passwords_ChangePasswordPage)
        self.message_empty_ChangePasswordPage = QWidget()
        self.message_empty_ChangePasswordPage.setObjectName(u"message_empty_ChangePasswordPage")
        self.error_messages_ChangePasswordPage.addWidget(self.message_empty_ChangePasswordPage)
        self.message_no_connection_ChangePasswordPage = QWidget()
        self.message_no_connection_ChangePasswordPage.setObjectName(u"message_no_connection_ChangePasswordPage")
        self.horizontalLayout_25 = QHBoxLayout(self.message_no_connection_ChangePasswordPage)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.message_no_connection_ChangePasswordPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(300, 39))
        self.label_22.setMaximumSize(QSize(200, 39))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setOpenExternalLinks(False)

        self.horizontalLayout_25.addWidget(self.label_22)

        self.error_messages_ChangePasswordPage.addWidget(self.message_no_connection_ChangePasswordPage)

        self.gridLayout_7.addWidget(self.error_messages_ChangePasswordPage, 3, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_14, 10, 3, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_13.setSpacing(-1)
#endif
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_19 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.confirm_button_ChangePasswordPage = QPushButton(self.ChangPasswordPage)
        self.confirm_button_ChangePasswordPage.setObjectName(u"confirm_button_ChangePasswordPage")
        self.confirm_button_ChangePasswordPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_ChangePasswordPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_ChangePasswordPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.confirm_button_ChangePasswordPage)

        self.horizontalSpacer_51 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_51)

        self.cancle_button_ChangePasswordPage = QPushButton(self.ChangPasswordPage)
        self.cancle_button_ChangePasswordPage.setObjectName(u"cancle_button_ChangePasswordPage")
        self.cancle_button_ChangePasswordPage.setMinimumSize(QSize(100, 30))
        self.cancle_button_ChangePasswordPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancle_button_ChangePasswordPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.cancle_button_ChangePasswordPage)

        self.horizontalSpacer_20 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 9, 3, 1, 1)

        self.label_29 = QLabel(self.ChangPasswordPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_29.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_7.addWidget(self.label_29, 1, 3, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_29, 8, 3, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_30, 4, 3, 1, 1)

        self.verticalSpacer_58 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_58, 2, 3, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_7)

        self.IndexWindow.addWidget(self.ChangPasswordPage)
        self.IndexPage = QWidget()
        self.IndexPage.setObjectName(u"IndexPage")
        self.verticalLayout_8 = QVBoxLayout(self.IndexPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 2)
        self.profile_button_IndexPage = QToolButton(self.IndexPage)
        self.profile_button_IndexPage.setObjectName(u"profile_button_IndexPage")
        self.profile_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.profile_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #A8B8F0;\n"
"    border-right: none;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"QToolButton:pressed {\n"
"    color: white;\n"
"    background: #2F4FBB;\n"
"}")

        self.horizontalLayout_16.addWidget(self.profile_button_IndexPage)

        self.search_button_IndexPage = QToolButton(self.IndexPage)
        self.search_button_IndexPage.setObjectName(u"search_button_IndexPage")
        self.search_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.search_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #A8B8F0;\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"QToolButton:pressed {\n"
"    color: white;\n"
"    background: #2F4FBB;\n"
"}")
        self.search_button_IndexPage.setCheckable(False)
        self.search_button_IndexPage.setAutoRaise(False)

        self.horizontalLayout_16.addWidget(self.search_button_IndexPage)

        self.product_button_IndexPage = QToolButton(self.IndexPage)
        self.product_button_IndexPage.setObjectName(u"product_button_IndexPage")
        self.product_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.product_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.product_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #A8B8F0;\n"
"    border-left: none;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"QToolButton:pressed {\n"
"    color: white;\n"
"    background: #2F4FBB;\n"
"}")

        self.horizontalLayout_16.addWidget(self.product_button_IndexPage)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_21)

        self.how_to_use_button_IndexPage = QToolButton(self.IndexPage)
        self.how_to_use_button_IndexPage.setObjectName(u"how_to_use_button_IndexPage")
        self.how_to_use_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.how_to_use_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.how_to_use_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #2F4FBB;\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #2F4FBB;\n"
"    color:white;\n"
"}")

        self.horizontalLayout_16.addWidget(self.how_to_use_button_IndexPage)

        self.horizontalSpacer_76 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_76)

        self.update_button_IndexPage = QToolButton(self.IndexPage)
        self.update_button_IndexPage.setObjectName(u"update_button_IndexPage")
        self.update_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.update_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #2F4FBB;\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #2F4FBB;\n"
"    color:white;\n"
"}\n"
"\n"
"QToolButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.update_button_IndexPage)

        self.horizontalSpacer_75 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_75)

        self.exit_button_IndexPage = QToolButton(self.IndexPage)
        self.exit_button_IndexPage.setObjectName(u"exit_button_IndexPage")
        self.exit_button_IndexPage.setMinimumSize(QSize(0, 25))
        self.exit_button_IndexPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button_IndexPage.setStyleSheet(u"QToolButton {\n"
"    border: 1px solid #C02C70;\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #C02C70;\n"
"    color:white;\n"
"}")

        self.horizontalLayout_16.addWidget(self.exit_button_IndexPage)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.AlgoritmWindow = QStackedWidget(self.IndexPage)
        self.AlgoritmWindow.setObjectName(u"AlgoritmWindow")
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.verticalLayout_22 = QVBoxLayout(self.ProfilePage)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_9 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout_9.setSpacing(-1)
#endif
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_26 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_26, 8, 2, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_33)

        self.label_32 = QLabel(self.ProfilePage)
        self.label_32.setObjectName(u"label_32")
        font4 = QFont()
        font4.setBold(True)
        self.label_32.setFont(font4)
#if QT_CONFIG(whatsthis)
        self.label_32.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)

        self.horizontalLayout_39.addWidget(self.label_32)

        self.horizontalSpacer_22 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_22)

        self.key_input_ProfilePage = QLineEdit(self.ProfilePage)
        self.key_input_ProfilePage.setObjectName(u"key_input_ProfilePage")
        self.key_input_ProfilePage.setMinimumSize(QSize(350, 37))
        self.key_input_ProfilePage.setClearButtonEnabled(True)

        self.horizontalLayout_39.addWidget(self.key_input_ProfilePage)

        self.horizontalSpacer_23 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_23)

        self.confirm_key_button_ProfilePage = QPushButton(self.ProfilePage)
        self.confirm_key_button_ProfilePage.setObjectName(u"confirm_key_button_ProfilePage")
        self.confirm_key_button_ProfilePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_key_button_ProfilePage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_39.addWidget(self.confirm_key_button_ProfilePage)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_40)


        self.gridLayout_9.addLayout(self.horizontalLayout_39, 3, 0, 1, 4)

        self.verticalSpacer_21 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_9.addItem(self.verticalSpacer_21, 10, 2, 1, 1)

        self.widget = QWidget(self.ProfilePage)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius: 6px;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
#ifndef Q_OS_MAC
        self.horizontalLayout_11.setSpacing(-1)
#endif
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_24, 3, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_23, 5, 0, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setFont(font4)

        self.gridLayout_11.addWidget(self.label_28, 2, 0, 1, 1)

        self.email_label_ProfilePage = QLabel(self.widget)
        self.email_label_ProfilePage.setObjectName(u"email_label_ProfilePage")
        self.email_label_ProfilePage.setMaximumSize(QSize(16777215, 20))
        self.email_label_ProfilePage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.email_label_ProfilePage, 0, 2, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_25, 1, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_24, 4, 1, 1, 1)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font4)
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_30, 4, 0, 1, 1)

        self.subscribtion_plan_label_ProfilePage = QLabel(self.widget)
        self.subscribtion_plan_label_ProfilePage.setObjectName(u"subscribtion_plan_label_ProfilePage")
        self.subscribtion_plan_label_ProfilePage.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_11.addWidget(self.subscribtion_plan_label_ProfilePage, 2, 2, 1, 1)

        self.expire_date_label_ProfilePage = QLabel(self.widget)
        self.expire_date_label_ProfilePage.setObjectName(u"expire_date_label_ProfilePage")
        self.expire_date_label_ProfilePage.setMaximumSize(QSize(16777215, 20))
        self.expire_date_label_ProfilePage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.expire_date_label_ProfilePage, 4, 2, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)

        self.refresh_button_ProfilePage = QPushButton(self.widget)
        self.refresh_button_ProfilePage.setObjectName(u"refresh_button_ProfilePage")
        self.refresh_button_ProfilePage.setFont(font)
        self.refresh_button_ProfilePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_button_ProfilePage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_10.addWidget(self.refresh_button_ProfilePage)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_41)


        self.gridLayout_11.addLayout(self.horizontalLayout_10, 6, 0, 1, 3)


        self.horizontalLayout_11.addLayout(self.gridLayout_11)


        self.gridLayout_9.addWidget(self.widget, 1, 2, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_34)

        self.pay_199_button_ProfilePage = QPushButton(self.ProfilePage)
        self.pay_199_button_ProfilePage.setObjectName(u"pay_199_button_ProfilePage")
        self.pay_199_button_ProfilePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pay_199_button_ProfilePage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #BA45B7;\n"
"    color: white;\n"
"    background-color: #BA45B7;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #8A2487;\n"
"    border: 1px solid #8A2487;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #8A2487;\n"
"    border: 1px solid #8A2487;\n"
"}")

        self.horizontalLayout_36.addWidget(self.pay_199_button_ProfilePage)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_35)


        self.gridLayout_12.addLayout(self.horizontalLayout_36, 2, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.verticalSpacer_28, 1, 1, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_43, 0, 0, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_44, 0, 2, 1, 1)

        self.label_36 = QLabel(self.ProfilePage)
        self.label_36.setObjectName(u"label_36")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QSize(212, 350))
        self.label_36.setMaximumSize(QSize(212, 350))
        self.label_36.setPixmap(QPixmap(u":/prices/profi.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_36, 0, 5, 1, 1)

        self.label_35 = QLabel(self.ProfilePage)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QSize(212, 350))
        self.label_35.setMaximumSize(QSize(212, 350))
        self.label_35.setPixmap(QPixmap(u":/prices/standart.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_35, 0, 3, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_36)

        self.pay_349_button_ProfilePage = QPushButton(self.ProfilePage)
        self.pay_349_button_ProfilePage.setObjectName(u"pay_349_button_ProfilePage")
        self.pay_349_button_ProfilePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pay_349_button_ProfilePage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}")

        self.horizontalLayout_37.addWidget(self.pay_349_button_ProfilePage)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_37)


        self.gridLayout_12.addLayout(self.horizontalLayout_37, 2, 3, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_45, 0, 4, 1, 1)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_38)

        self.pay_499_button_ProfilePage = QPushButton(self.ProfilePage)
        self.pay_499_button_ProfilePage.setObjectName(u"pay_499_button_ProfilePage")
        self.pay_499_button_ProfilePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pay_499_button_ProfilePage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}")

        self.horizontalLayout_38.addWidget(self.pay_499_button_ProfilePage)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_39)


        self.gridLayout_12.addLayout(self.horizontalLayout_38, 2, 5, 1, 1)

        self.label_34 = QLabel(self.ProfilePage)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QSize(212, 350))
        self.label_34.setMaximumSize(QSize(212, 350))
        font5 = QFont()
        font5.setBold(False)
        self.label_34.setFont(font5)
        self.label_34.setPixmap(QPixmap(u":/prices/basic.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_34, 0, 1, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_46, 0, 6, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_12, 4, 0, 1, 4)

        self.about_subscribe_ProfilePage = QStackedWidget(self.ProfilePage)
        self.about_subscribe_ProfilePage.setObjectName(u"about_subscribe_ProfilePage")
        self.free_subscribe_ProfilePage = QWidget()
        self.free_subscribe_ProfilePage.setObjectName(u"free_subscribe_ProfilePage")
        self.horizontalLayout_40 = QHBoxLayout(self.free_subscribe_ProfilePage)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 15, 0, 0)
        self.label_33 = QLabel(self.free_subscribe_ProfilePage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(620, 160))
        self.label_33.setMaximumSize(QSize(620, 160))
        self.label_33.setPixmap(QPixmap(u":/prices/about_trial.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_33)

        self.about_subscribe_ProfilePage.addWidget(self.free_subscribe_ProfilePage)
        self.standart_subscribe_ProfilePage = QWidget()
        self.standart_subscribe_ProfilePage.setObjectName(u"standart_subscribe_ProfilePage")
        self.horizontalLayout_42 = QHBoxLayout(self.standart_subscribe_ProfilePage)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.standart_subscribe_ProfilePage)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(620, 160))
        self.label_38.setMaximumSize(QSize(620, 160))
        self.label_38.setPixmap(QPixmap(u":/prices/about_standart.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_38)

        self.about_subscribe_ProfilePage.addWidget(self.standart_subscribe_ProfilePage)
        self.profi_subscribe_ProfilePage = QWidget()
        self.profi_subscribe_ProfilePage.setObjectName(u"profi_subscribe_ProfilePage")
        self.horizontalLayout_43 = QHBoxLayout(self.profi_subscribe_ProfilePage)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_47)

        self.label_39 = QLabel(self.profi_subscribe_ProfilePage)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(620, 160))
        self.label_39.setMaximumSize(QSize(620, 160))
        self.label_39.setPixmap(QPixmap(u":/prices/about_profi.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_39)

        self.about_subscribe_ProfilePage.addWidget(self.profi_subscribe_ProfilePage)
        self.base_subscribe_ProfilePage = QWidget()
        self.base_subscribe_ProfilePage.setObjectName(u"base_subscribe_ProfilePage")
        self.horizontalLayout_41 = QHBoxLayout(self.base_subscribe_ProfilePage)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, -1, 0)
        self.label_37 = QLabel(self.base_subscribe_ProfilePage)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(620, 160))
        self.label_37.setMaximumSize(QSize(620, 160))
        self.label_37.setPixmap(QPixmap(u":/prices/about_basic.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setIndent(-1)

        self.horizontalLayout_41.addWidget(self.label_37)

        self.about_subscribe_ProfilePage.addWidget(self.base_subscribe_ProfilePage)

        self.gridLayout_9.addWidget(self.about_subscribe_ProfilePage, 0, 0, 3, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_22, 0, 2, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(15, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_32, 1, 1, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_42, 1, 3, 1, 1)

        self.verticalSpacer_61 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_61, 2, 2, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_9)

        self.AlgoritmWindow.addWidget(self.ProfilePage)
        self.SearchPage = QWidget()
        self.SearchPage.setObjectName(u"SearchPage")
        self.verticalLayout_13 = QVBoxLayout(self.SearchPage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_product = QScrollArea(self.SearchPage)
        self.scrollArea_product.setObjectName(u"scrollArea_product")
        self.scrollArea_product.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"    background: #F5F5F5;\n"
"}")
        self.scrollArea_product.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 369, 310))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.product_layout_SearchPage = QVBoxLayout()
        self.product_layout_SearchPage.setSpacing(10)
        self.product_layout_SearchPage.setObjectName(u"product_layout_SearchPage")
        self.product_layout_SearchPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_18.addLayout(self.product_layout_SearchPage)

        self.scrollArea_product.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_8.addWidget(self.scrollArea_product, 0, 1, 1, 1)

        self.scrollArea_log = QScrollArea(self.SearchPage)
        self.scrollArea_log.setObjectName(u"scrollArea_log")
        self.scrollArea_log.setAutoFillBackground(False)
        self.scrollArea_log.setStyleSheet(u"QScrollArea {\n"
"    background: #F5F5F5;\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"}")
        self.scrollArea_log.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1119, 310))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"QWidget{\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.log_layout_SearchPage = QVBoxLayout()
        self.log_layout_SearchPage.setSpacing(10)
        self.log_layout_SearchPage.setObjectName(u"log_layout_SearchPage")
        self.log_layout_SearchPage.setContentsMargins(10, 10, 10, 10)
        self.label_logo_SearchPage = QLabel(self.scrollAreaWidgetContents_5)
        self.label_logo_SearchPage.setObjectName(u"label_logo_SearchPage")
        self.label_logo_SearchPage.setMinimumSize(QSize(0, 90))
        self.label_logo_SearchPage.setMaximumSize(QSize(16777215, 90))
        self.label_logo_SearchPage.setLayoutDirection(Qt.LeftToRight)
        self.label_logo_SearchPage.setAutoFillBackground(False)
        self.label_logo_SearchPage.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_logo_SearchPage.setAlignment(Qt.AlignCenter)

        self.log_layout_SearchPage.addWidget(self.label_logo_SearchPage)


        self.verticalLayout_21.addLayout(self.log_layout_SearchPage)

        self.scrollArea_log.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_8.addWidget(self.scrollArea_log, 4, 0, 1, 3)

        self.scrollArea_seattings = QScrollArea(self.SearchPage)
        self.scrollArea_seattings.setObjectName(u"scrollArea_seattings")
        self.scrollArea_seattings.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"    background: #F5F5F5;\n"
"}")
        self.scrollArea_seattings.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 370, 310))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"QWidget{\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.settings_layout_SearchPage = QVBoxLayout()
        self.settings_layout_SearchPage.setSpacing(10)
        self.settings_layout_SearchPage.setObjectName(u"settings_layout_SearchPage")
        self.settings_layout_SearchPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_19.addLayout(self.settings_layout_SearchPage)

        self.scrollArea_seattings.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_8.addWidget(self.scrollArea_seattings, 0, 2, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(10, 2, 10, 5)
        self.start_companies_button_SearchPage = QPushButton(self.SearchPage)
        self.start_companies_button_SearchPage.setObjectName(u"start_companies_button_SearchPage")
        self.start_companies_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_companies_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_51.addWidget(self.start_companies_button_SearchPage)

        self.horizontalSpacer_77 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_77)

        self.stop_companies_button_SearchPage = QPushButton(self.SearchPage)
        self.stop_companies_button_SearchPage.setObjectName(u"stop_companies_button_SearchPage")
        self.stop_companies_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_companies_button_SearchPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_51.addWidget(self.stop_companies_button_SearchPage)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_63)

        self.reset_button_SearchPage = QPushButton(self.SearchPage)
        self.reset_button_SearchPage.setObjectName(u"reset_button_SearchPage")
        self.reset_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_button_SearchPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_51.addWidget(self.reset_button_SearchPage)


        self.gridLayout_8.addLayout(self.horizontalLayout_51, 5, 0, 1, 3)

        self.menu_SearchPage = QStackedWidget(self.SearchPage)
        self.menu_SearchPage.setObjectName(u"menu_SearchPage")
        self.menu_SearchPage.setMinimumSize(QSize(0, 30))
        self.menu_SearchPage.setMaximumSize(QSize(16777215, 34))
        self.menu_buttons_SearchPage = QWidget()
        self.menu_buttons_SearchPage.setObjectName(u"menu_buttons_SearchPage")
        self.horizontalLayout_33 = QHBoxLayout(self.menu_buttons_SearchPage)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu_adverts_setup_SearchPage = QStackedWidget(self.menu_buttons_SearchPage)
        self.menu_adverts_setup_SearchPage.setObjectName(u"menu_adverts_setup_SearchPage")
        self.menu_adverts_setup_confirm_SearchPage = QWidget()
        self.menu_adverts_setup_confirm_SearchPage.setObjectName(u"menu_adverts_setup_confirm_SearchPage")
        self.horizontalLayout_44 = QHBoxLayout(self.menu_adverts_setup_confirm_SearchPage)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_26)

        self.menu_search_setup_refresh_button_SearchPage = QPushButton(self.menu_adverts_setup_confirm_SearchPage)
        self.menu_search_setup_refresh_button_SearchPage.setObjectName(u"menu_search_setup_refresh_button_SearchPage")
        self.menu_search_setup_refresh_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_search_setup_refresh_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_search_setup_refresh_button_SearchPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_44.addWidget(self.menu_search_setup_refresh_button_SearchPage)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_61)

        self.menu_adverts_setup_confirm_button_SearchPage = QPushButton(self.menu_adverts_setup_confirm_SearchPage)
        self.menu_adverts_setup_confirm_button_SearchPage.setObjectName(u"menu_adverts_setup_confirm_button_SearchPage")
        self.menu_adverts_setup_confirm_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_adverts_setup_confirm_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_adverts_setup_confirm_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_44.addWidget(self.menu_adverts_setup_confirm_button_SearchPage)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_27)

        self.menu_adverts_setup_SearchPage.addWidget(self.menu_adverts_setup_confirm_SearchPage)
        self.menu_adverts_setup_amount_error_SearchPage = QWidget()
        self.menu_adverts_setup_amount_error_SearchPage.setObjectName(u"menu_adverts_setup_amount_error_SearchPage")
        self.horizontalLayout_48 = QHBoxLayout(self.menu_adverts_setup_amount_error_SearchPage)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.menu_adverts_setup_amount_error_SearchPage)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font4)
        self.label_46.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_46)

        self.horizontalSpacer_78 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_78)

        self.menu_adverts_setup_amount_error_ok_button_SearchPage = QPushButton(self.menu_adverts_setup_amount_error_SearchPage)
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setObjectName(u"menu_adverts_setup_amount_error_ok_button_SearchPage")
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setMaximumSize(QSize(40, 16777215))
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_48.addWidget(self.menu_adverts_setup_amount_error_ok_button_SearchPage)

        self.menu_adverts_setup_SearchPage.addWidget(self.menu_adverts_setup_amount_error_SearchPage)
        self.menu_adverts_setup_empty_SearchPage = QWidget()
        self.menu_adverts_setup_empty_SearchPage.setObjectName(u"menu_adverts_setup_empty_SearchPage")
        self.menu_adverts_setup_SearchPage.addWidget(self.menu_adverts_setup_empty_SearchPage)

        self.horizontalLayout.addWidget(self.menu_adverts_setup_SearchPage)

        self.menu_product_setup_SearchPage = QStackedWidget(self.menu_buttons_SearchPage)
        self.menu_product_setup_SearchPage.setObjectName(u"menu_product_setup_SearchPage")
        self.menu_product_setup_confirm_SearchPage = QWidget()
        self.menu_product_setup_confirm_SearchPage.setObjectName(u"menu_product_setup_confirm_SearchPage")
        self.horizontalLayout_34 = QHBoxLayout(self.menu_product_setup_confirm_SearchPage)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_28)

        self.menu_product_setup_refresh_button_SearchPage = QPushButton(self.menu_product_setup_confirm_SearchPage)
        self.menu_product_setup_refresh_button_SearchPage.setObjectName(u"menu_product_setup_refresh_button_SearchPage")
        self.menu_product_setup_refresh_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_refresh_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_refresh_button_SearchPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_34.addWidget(self.menu_product_setup_refresh_button_SearchPage)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_60)

        self.menu_product_setup_confirm_button_SearchPage = QPushButton(self.menu_product_setup_confirm_SearchPage)
        self.menu_product_setup_confirm_button_SearchPage.setObjectName(u"menu_product_setup_confirm_button_SearchPage")
        self.menu_product_setup_confirm_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_confirm_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_confirm_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_34.addWidget(self.menu_product_setup_confirm_button_SearchPage)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_29)

        self.menu_product_setup_SearchPage.addWidget(self.menu_product_setup_confirm_SearchPage)
        self.menu_product_setup_amount_error_SearchPage = QWidget()
        self.menu_product_setup_amount_error_SearchPage.setObjectName(u"menu_product_setup_amount_error_SearchPage")
        self.horizontalLayout_47 = QHBoxLayout(self.menu_product_setup_amount_error_SearchPage)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.menu_product_setup_amount_error_SearchPage)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font4)
        self.label_45.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_45)

        self.horizontalSpacer_79 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_79)

        self.menu_product_setup_amount_error_ok_button_SearchPage = QPushButton(self.menu_product_setup_amount_error_SearchPage)
        self.menu_product_setup_amount_error_ok_button_SearchPage.setObjectName(u"menu_product_setup_amount_error_ok_button_SearchPage")
        self.menu_product_setup_amount_error_ok_button_SearchPage.setMaximumSize(QSize(40, 16777215))
        self.menu_product_setup_amount_error_ok_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_amount_error_ok_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_amount_error_ok_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_47.addWidget(self.menu_product_setup_amount_error_ok_button_SearchPage)

        self.menu_product_setup_SearchPage.addWidget(self.menu_product_setup_amount_error_SearchPage)
        self.menu_product_setup_empty_SearchPage = QWidget()
        self.menu_product_setup_empty_SearchPage.setObjectName(u"menu_product_setup_empty_SearchPage")
        self.menu_product_setup_SearchPage.addWidget(self.menu_product_setup_empty_SearchPage)

        self.horizontalLayout.addWidget(self.menu_product_setup_SearchPage)

        self.menu_settings_SearchPage = QStackedWidget(self.menu_buttons_SearchPage)
        self.menu_settings_SearchPage.setObjectName(u"menu_settings_SearchPage")
        self.menu_settings_start_SearchPage = QWidget()
        self.menu_settings_start_SearchPage.setObjectName(u"menu_settings_start_SearchPage")
        self.horizontalLayout_35 = QHBoxLayout(self.menu_settings_start_SearchPage)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_30)

        self.menu_settings_start_button_SearchPage = QPushButton(self.menu_settings_start_SearchPage)
        self.menu_settings_start_button_SearchPage.setObjectName(u"menu_settings_start_button_SearchPage")
        self.menu_settings_start_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_start_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_settings_start_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_35.addWidget(self.menu_settings_start_button_SearchPage)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_31)

        self.menu_settings_SearchPage.addWidget(self.menu_settings_start_SearchPage)
        self.menu_settings_stop_SearchPage = QWidget()
        self.menu_settings_stop_SearchPage.setObjectName(u"menu_settings_stop_SearchPage")
        self.horizontalLayout_45 = QHBoxLayout(self.menu_settings_stop_SearchPage)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_48)

        self.menu_settings_stop_button_SearchPage = QPushButton(self.menu_settings_stop_SearchPage)
        self.menu_settings_stop_button_SearchPage.setObjectName(u"menu_settings_stop_button_SearchPage")
        self.menu_settings_stop_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_stop_button_SearchPage.setFocusPolicy(Qt.NoFocus)
        self.menu_settings_stop_button_SearchPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_45.addWidget(self.menu_settings_stop_button_SearchPage)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_49)

        self.menu_settings_SearchPage.addWidget(self.menu_settings_stop_SearchPage)
        self.menu_settings_empty_SearchPage = QWidget()
        self.menu_settings_empty_SearchPage.setObjectName(u"menu_settings_empty_SearchPage")
        self.menu_settings_SearchPage.addWidget(self.menu_settings_empty_SearchPage)
        self.menu_settings_error_SearchPage = QWidget()
        self.menu_settings_error_SearchPage.setObjectName(u"menu_settings_error_SearchPage")
        self.horizontalLayout_50 = QHBoxLayout(self.menu_settings_error_SearchPage)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.error_label_settings_SearchPage = QLabel(self.menu_settings_error_SearchPage)
        self.error_label_settings_SearchPage.setObjectName(u"error_label_settings_SearchPage")
        self.error_label_settings_SearchPage.setFont(font4)
        self.error_label_settings_SearchPage.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}\n"
"")
        self.error_label_settings_SearchPage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.error_label_settings_SearchPage)

        self.horizontalSpacer_80 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_80)

        self.menu_settings_error_ok_button_SearchPage = QPushButton(self.menu_settings_error_SearchPage)
        self.menu_settings_error_ok_button_SearchPage.setObjectName(u"menu_settings_error_ok_button_SearchPage")
        self.menu_settings_error_ok_button_SearchPage.setMaximumSize(QSize(40, 16777215))
        self.menu_settings_error_ok_button_SearchPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_error_ok_button_SearchPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_50.addWidget(self.menu_settings_error_ok_button_SearchPage)

        self.menu_settings_SearchPage.addWidget(self.menu_settings_error_SearchPage)

        self.horizontalLayout.addWidget(self.menu_settings_SearchPage)


        self.horizontalLayout_33.addLayout(self.horizontalLayout)

        self.menu_SearchPage.addWidget(self.menu_buttons_SearchPage)
        self.menu_subscribe_error_SearchPage = QWidget()
        self.menu_subscribe_error_SearchPage.setObjectName(u"menu_subscribe_error_SearchPage")
        self.verticalLayout_24 = QVBoxLayout(self.menu_subscribe_error_SearchPage)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.menu_subscribe_error_SearchPage)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font4)
        self.label_44.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}\n"
"")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_44)

        self.menu_SearchPage.addWidget(self.menu_subscribe_error_SearchPage)
        self.menu_key_error_SearchPage = QWidget()
        self.menu_key_error_SearchPage.setObjectName(u"menu_key_error_SearchPage")
        self.verticalLayout_20 = QVBoxLayout(self.menu_key_error_SearchPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, 0, 0)
        self.label_43 = QLabel(self.menu_key_error_SearchPage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font4)
        self.label_43.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}\n"
"")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_43)

        self.menu_SearchPage.addWidget(self.menu_key_error_SearchPage)

        self.gridLayout_8.addWidget(self.menu_SearchPage, 2, 0, 1, 3)

        self.scrollArea_adverts = QScrollArea(self.SearchPage)
        self.scrollArea_adverts.setObjectName(u"scrollArea_adverts")
        self.scrollArea_adverts.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"    background: #F5F5F5;\n"
"}")
        self.scrollArea_adverts.setFrameShape(QFrame.StyledPanel)
        self.scrollArea_adverts.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_adverts.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 370, 310))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
#ifndef Q_OS_MAC
        self.verticalLayout_15.setSpacing(-1)
#endif
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.adverts_layout_SearchPage = QVBoxLayout()
        self.adverts_layout_SearchPage.setSpacing(10)
        self.adverts_layout_SearchPage.setObjectName(u"adverts_layout_SearchPage")
        self.adverts_layout_SearchPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_15.addLayout(self.adverts_layout_SearchPage)

        self.scrollArea_adverts.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_8.addWidget(self.scrollArea_adverts, 0, 0, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_40, 1, 0, 1, 1)

        self.verticalSpacer_50 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_50, 3, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_8)

        self.AlgoritmWindow.addWidget(self.SearchPage)
        self.ProductPage = QWidget()
        self.ProductPage.setObjectName(u"ProductPage")
        self.verticalLayout_11 = QVBoxLayout(self.ProductPage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_51 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_51, 3, 0, 1, 1)

        self.verticalSpacer_52 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_52, 1, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(10, 2, 10, 5)
        self.start_companies_button_ProductPage = QPushButton(self.ProductPage)
        self.start_companies_button_ProductPage.setObjectName(u"start_companies_button_ProductPage")
        self.start_companies_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_companies_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_60.addWidget(self.start_companies_button_ProductPage)

        self.horizontalSpacer_81 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_81)

        self.stop_companies_button_ProductPage = QPushButton(self.ProductPage)
        self.stop_companies_button_ProductPage.setObjectName(u"stop_companies_button_ProductPage")
        self.stop_companies_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_companies_button_ProductPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_60.addWidget(self.stop_companies_button_ProductPage)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_74)

        self.reset_button_ProductPage = QPushButton(self.ProductPage)
        self.reset_button_ProductPage.setObjectName(u"reset_button_ProductPage")
        self.reset_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_button_ProductPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_60.addWidget(self.reset_button_ProductPage)


        self.gridLayout_10.addLayout(self.horizontalLayout_60, 5, 0, 1, 3)

        self.menu_ProductPage = QStackedWidget(self.ProductPage)
        self.menu_ProductPage.setObjectName(u"menu_ProductPage")
        self.menu_ProductPage.setMinimumSize(QSize(0, 30))
        self.menu_ProductPage.setMaximumSize(QSize(16777215, 34))
        self.menu_buttons_ProductPage = QWidget()
        self.menu_buttons_ProductPage.setObjectName(u"menu_buttons_ProductPage")
        self.horizontalLayout_52 = QHBoxLayout(self.menu_buttons_ProductPage)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.menu_adverts_setup_ProductPage = QStackedWidget(self.menu_buttons_ProductPage)
        self.menu_adverts_setup_ProductPage.setObjectName(u"menu_adverts_setup_ProductPage")
        self.menu_adverts_setup_confirm_ProductPage = QWidget()
        self.menu_adverts_setup_confirm_ProductPage.setObjectName(u"menu_adverts_setup_confirm_ProductPage")
        self.horizontalLayout_53 = QHBoxLayout(self.menu_adverts_setup_confirm_ProductPage)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_64)

        self.menu_search_setup_refresh_button_ProductPage = QPushButton(self.menu_adverts_setup_confirm_ProductPage)
        self.menu_search_setup_refresh_button_ProductPage.setObjectName(u"menu_search_setup_refresh_button_ProductPage")
        self.menu_search_setup_refresh_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_search_setup_refresh_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_search_setup_refresh_button_ProductPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_53.addWidget(self.menu_search_setup_refresh_button_ProductPage)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_65)

        self.menu_adverts_setup_confirm_button_ProductPage = QPushButton(self.menu_adverts_setup_confirm_ProductPage)
        self.menu_adverts_setup_confirm_button_ProductPage.setObjectName(u"menu_adverts_setup_confirm_button_ProductPage")
        self.menu_adverts_setup_confirm_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_adverts_setup_confirm_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_adverts_setup_confirm_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}\n"
"QPushButton::disabled {\n"
"    border: 1px solid #B4B5B8;\n"
"    color: black;\n"
"    background-color: #F5F5F5;\n"
"    border-radius: 6px;\n"
"}")

        self.horizontalLayout_53.addWidget(self.menu_adverts_setup_confirm_button_ProductPage)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_66)

        self.menu_adverts_setup_ProductPage.addWidget(self.menu_adverts_setup_confirm_ProductPage)
        self.menu_adverts_setup_amount_error_ProductPage = QWidget()
        self.menu_adverts_setup_amount_error_ProductPage.setObjectName(u"menu_adverts_setup_amount_error_ProductPage")
        self.horizontalLayout_54 = QHBoxLayout(self.menu_adverts_setup_amount_error_ProductPage)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.menu_adverts_setup_amount_error_ProductPage)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font4)
        self.label_48.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_48)

        self.horizontalSpacer_82 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_82)

        self.menu_adverts_setup_amount_error_ok_button_ProductPage = QPushButton(self.menu_adverts_setup_amount_error_ProductPage)
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setObjectName(u"menu_adverts_setup_amount_error_ok_button_ProductPage")
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setMaximumSize(QSize(40, 16777215))
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_54.addWidget(self.menu_adverts_setup_amount_error_ok_button_ProductPage)

        self.menu_adverts_setup_ProductPage.addWidget(self.menu_adverts_setup_amount_error_ProductPage)
        self.menu_adverts_setup_empty_ProductPage = QWidget()
        self.menu_adverts_setup_empty_ProductPage.setObjectName(u"menu_adverts_setup_empty_ProductPage")
        self.menu_adverts_setup_ProductPage.addWidget(self.menu_adverts_setup_empty_ProductPage)

        self.horizontalLayout_9.addWidget(self.menu_adverts_setup_ProductPage)

        self.menu_product_setup_ProductPage = QStackedWidget(self.menu_buttons_ProductPage)
        self.menu_product_setup_ProductPage.setObjectName(u"menu_product_setup_ProductPage")
        self.menu_product_setup_confirm_ProductPage = QWidget()
        self.menu_product_setup_confirm_ProductPage.setObjectName(u"menu_product_setup_confirm_ProductPage")
        self.horizontalLayout_55 = QHBoxLayout(self.menu_product_setup_confirm_ProductPage)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_67)

        self.menu_product_setup_refresh_button_ProductPage = QPushButton(self.menu_product_setup_confirm_ProductPage)
        self.menu_product_setup_refresh_button_ProductPage.setObjectName(u"menu_product_setup_refresh_button_ProductPage")
        self.menu_product_setup_refresh_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_refresh_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_refresh_button_ProductPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_55.addWidget(self.menu_product_setup_refresh_button_ProductPage)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_68)

        self.menu_product_setup_confirm_button_ProductPage = QPushButton(self.menu_product_setup_confirm_ProductPage)
        self.menu_product_setup_confirm_button_ProductPage.setObjectName(u"menu_product_setup_confirm_button_ProductPage")
        self.menu_product_setup_confirm_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_confirm_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_confirm_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_55.addWidget(self.menu_product_setup_confirm_button_ProductPage)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_69)

        self.menu_product_setup_ProductPage.addWidget(self.menu_product_setup_confirm_ProductPage)
        self.menu_product_setup_amount_error_ProductPage = QWidget()
        self.menu_product_setup_amount_error_ProductPage.setObjectName(u"menu_product_setup_amount_error_ProductPage")
        self.horizontalLayout_56 = QHBoxLayout(self.menu_product_setup_amount_error_ProductPage)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.menu_product_setup_amount_error_ProductPage)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font4)
        self.label_49.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_49)

        self.horizontalSpacer_83 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_83)

        self.menu_product_setup_amount_error_ok_button_ProductPage = QPushButton(self.menu_product_setup_amount_error_ProductPage)
        self.menu_product_setup_amount_error_ok_button_ProductPage.setObjectName(u"menu_product_setup_amount_error_ok_button_ProductPage")
        self.menu_product_setup_amount_error_ok_button_ProductPage.setMaximumSize(QSize(40, 16777215))
        self.menu_product_setup_amount_error_ok_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_product_setup_amount_error_ok_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_product_setup_amount_error_ok_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_56.addWidget(self.menu_product_setup_amount_error_ok_button_ProductPage)

        self.menu_product_setup_ProductPage.addWidget(self.menu_product_setup_amount_error_ProductPage)
        self.menu_product_setup_empty_ProductPage = QWidget()
        self.menu_product_setup_empty_ProductPage.setObjectName(u"menu_product_setup_empty_ProductPage")
        self.menu_product_setup_ProductPage.addWidget(self.menu_product_setup_empty_ProductPage)

        self.horizontalLayout_9.addWidget(self.menu_product_setup_ProductPage)

        self.menu_settings_ProductPage = QStackedWidget(self.menu_buttons_ProductPage)
        self.menu_settings_ProductPage.setObjectName(u"menu_settings_ProductPage")
        self.menu_settings_start_ProductPage = QWidget()
        self.menu_settings_start_ProductPage.setObjectName(u"menu_settings_start_ProductPage")
        self.horizontalLayout_57 = QHBoxLayout(self.menu_settings_start_ProductPage)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_70)

        self.menu_settings_start_button_ProductPage = QPushButton(self.menu_settings_start_ProductPage)
        self.menu_settings_start_button_ProductPage.setObjectName(u"menu_settings_start_button_ProductPage")
        self.menu_settings_start_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_start_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_settings_start_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_57.addWidget(self.menu_settings_start_button_ProductPage)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_71)

        self.menu_settings_ProductPage.addWidget(self.menu_settings_start_ProductPage)
        self.menu_settings_stop_ProductPage = QWidget()
        self.menu_settings_stop_ProductPage.setObjectName(u"menu_settings_stop_ProductPage")
        self.horizontalLayout_58 = QHBoxLayout(self.menu_settings_stop_ProductPage)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_72)

        self.menu_settings_stop_button_ProductPage = QPushButton(self.menu_settings_stop_ProductPage)
        self.menu_settings_stop_button_ProductPage.setObjectName(u"menu_settings_stop_button_ProductPage")
        self.menu_settings_stop_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_stop_button_ProductPage.setFocusPolicy(Qt.NoFocus)
        self.menu_settings_stop_button_ProductPage.setStyleSheet(u"QPushButton {\n"
"    padding: 8px 16px;\n"
"    border: 1px solid #C02C70;\n"
"    color: white;\n"
"    background-color: #C02C70;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #B50959;\n"
"    border: 1px solid #B50959;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #C02C70;\n"
"    border: 1px solid #C02C70;\n"
"}")

        self.horizontalLayout_58.addWidget(self.menu_settings_stop_button_ProductPage)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_73)

        self.menu_settings_ProductPage.addWidget(self.menu_settings_stop_ProductPage)
        self.menu_settings_empty_ProductPage = QWidget()
        self.menu_settings_empty_ProductPage.setObjectName(u"menu_settings_empty_ProductPage")
        self.menu_settings_ProductPage.addWidget(self.menu_settings_empty_ProductPage)
        self.menu_settings_error_ProductPage = QWidget()
        self.menu_settings_error_ProductPage.setObjectName(u"menu_settings_error_ProductPage")
        self.horizontalLayout_59 = QHBoxLayout(self.menu_settings_error_ProductPage)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.error_label_settings_ProductPage = QLabel(self.menu_settings_error_ProductPage)
        self.error_label_settings_ProductPage.setObjectName(u"error_label_settings_ProductPage")
        self.error_label_settings_ProductPage.setFont(font4)
        self.error_label_settings_ProductPage.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.error_label_settings_ProductPage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.error_label_settings_ProductPage)

        self.horizontalSpacer_84 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_84)

        self.menu_settings_error_ok_button_ProductPage = QPushButton(self.menu_settings_error_ProductPage)
        self.menu_settings_error_ok_button_ProductPage.setObjectName(u"menu_settings_error_ok_button_ProductPage")
        self.menu_settings_error_ok_button_ProductPage.setMaximumSize(QSize(40, 16777215))
        self.menu_settings_error_ok_button_ProductPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_settings_error_ok_button_ProductPage.setStyleSheet(u"QPushButton::default {\n"
"    padding: 8px 4px;\n"
"    border: 1px solid #2F4FBB;\n"
"    color: white;\n"
"    background-color: #2F4FBB;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton::default:hover {\n"
"    background-color: #0D31A6;\n"
"    border: 1px solid #0D31A6;\n"
"}\n"
"QPushButton::default:pressed {\n"
"    background-color: #2F4FBB;\n"
"    border: 1px solid #2F4FBB;\n"
"}")

        self.horizontalLayout_59.addWidget(self.menu_settings_error_ok_button_ProductPage)

        self.menu_settings_ProductPage.addWidget(self.menu_settings_error_ProductPage)

        self.horizontalLayout_9.addWidget(self.menu_settings_ProductPage)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_9)

        self.menu_ProductPage.addWidget(self.menu_buttons_ProductPage)
        self.menu_subscribe_error_ProductPage = QWidget()
        self.menu_subscribe_error_ProductPage.setObjectName(u"menu_subscribe_error_ProductPage")
        self.verticalLayout_25 = QVBoxLayout(self.menu_subscribe_error_ProductPage)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.menu_subscribe_error_ProductPage)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"}")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_50)

        self.menu_ProductPage.addWidget(self.menu_subscribe_error_ProductPage)
        self.menu_key_error_ProductPage = QWidget()
        self.menu_key_error_ProductPage.setObjectName(u"menu_key_error_ProductPage")
        self.verticalLayout_26 = QVBoxLayout(self.menu_key_error_ProductPage)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, 0, 0)
        self.label_51 = QLabel(self.menu_key_error_ProductPage)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font4)
        self.label_51.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_51)

        self.menu_ProductPage.addWidget(self.menu_key_error_ProductPage)

        self.gridLayout_10.addWidget(self.menu_ProductPage, 2, 0, 1, 3)

        self.scrollArea_log_ProductPage = QScrollArea(self.ProductPage)
        self.scrollArea_log_ProductPage.setObjectName(u"scrollArea_log_ProductPage")
        self.scrollArea_log_ProductPage.setStyleSheet(u"QScrollArea {\n"
"    background: #F5F5F5;\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"}")
        self.scrollArea_log_ProductPage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1119, 310))
        self.scrollAreaWidgetContents_8.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.log_layout_ProductPage = QVBoxLayout()
        self.log_layout_ProductPage.setSpacing(10)
        self.log_layout_ProductPage.setObjectName(u"log_layout_ProductPage")
        self.log_layout_ProductPage.setContentsMargins(10, 10, 10, 10)
        self.label_logo_ProductPage = QLabel(self.scrollAreaWidgetContents_8)
        self.label_logo_ProductPage.setObjectName(u"label_logo_ProductPage")
        self.label_logo_ProductPage.setMinimumSize(QSize(0, 90))
        self.label_logo_ProductPage.setMaximumSize(QSize(16777215, 90))
        self.label_logo_ProductPage.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_logo_ProductPage.setAlignment(Qt.AlignCenter)

        self.log_layout_ProductPage.addWidget(self.label_logo_ProductPage)


        self.verticalLayout_27.addLayout(self.log_layout_ProductPage)

        self.scrollArea_log_ProductPage.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_10.addWidget(self.scrollArea_log_ProductPage, 4, 0, 1, 3)

        self.scrollArea_product_ProductPage = QScrollArea(self.ProductPage)
        self.scrollArea_product_ProductPage.setObjectName(u"scrollArea_product_ProductPage")
        self.scrollArea_product_ProductPage.setStyleSheet(u"QScrollArea {\n"
"    background: #F5F5F5;\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"}")
        self.scrollArea_product_ProductPage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 369, 310))
        self.scrollAreaWidgetContents_9.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.product_layout_ProductPage = QVBoxLayout()
        self.product_layout_ProductPage.setSpacing(10)
        self.product_layout_ProductPage.setObjectName(u"product_layout_ProductPage")
        self.product_layout_ProductPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_28.addLayout(self.product_layout_ProductPage)

        self.scrollArea_product_ProductPage.setWidget(self.scrollAreaWidgetContents_9)

        self.gridLayout_10.addWidget(self.scrollArea_product_ProductPage, 0, 1, 1, 1)

        self.scrollArea_seattings_ProductPage = QScrollArea(self.ProductPage)
        self.scrollArea_seattings_ProductPage.setObjectName(u"scrollArea_seattings_ProductPage")
        self.scrollArea_seattings_ProductPage.setStyleSheet(u"QScrollArea {\n"
"    background: #F5F5F5;\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"}")
        self.scrollArea_seattings_ProductPage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 370, 310))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.settings_layout_ProductPage = QVBoxLayout()
        self.settings_layout_ProductPage.setSpacing(10)
        self.settings_layout_ProductPage.setObjectName(u"settings_layout_ProductPage")
        self.settings_layout_ProductPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_23.addLayout(self.settings_layout_ProductPage)

        self.scrollArea_seattings_ProductPage.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_10.addWidget(self.scrollArea_seattings_ProductPage, 0, 2, 1, 1)

        self.scrollArea_adverts_ProductPage = QScrollArea(self.ProductPage)
        self.scrollArea_adverts_ProductPage.setObjectName(u"scrollArea_adverts_ProductPage")
        self.scrollArea_adverts_ProductPage.setStyleSheet(u"QScrollArea {\n"
"    background: #F5F5F5;\n"
"    border: 1px solid #B4B5B8;\n"
"    border-radius:6px;\n"
"}")
        self.scrollArea_adverts_ProductPage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 370, 310))
        self.scrollAreaWidgetContents_7.setStyleSheet(u"QWidget {\n"
"    border-radius:6px;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_7)
#ifndef Q_OS_MAC
        self.verticalLayout_16.setSpacing(-1)
#endif
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.adverts_layout_ProductPage = QVBoxLayout()
        self.adverts_layout_ProductPage.setSpacing(10)
        self.adverts_layout_ProductPage.setObjectName(u"adverts_layout_ProductPage")
        self.adverts_layout_ProductPage.setContentsMargins(10, 10, 10, 10)

        self.verticalLayout_16.addLayout(self.adverts_layout_ProductPage)

        self.scrollArea_adverts_ProductPage.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_10.addWidget(self.scrollArea_adverts_ProductPage, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_10)

        self.AlgoritmWindow.addWidget(self.ProductPage)

        self.verticalLayout_10.addWidget(self.AlgoritmWindow)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        self.IndexWindow.addWidget(self.IndexPage)
        self.ConfirmPasswordChangePage = QWidget()
        self.ConfirmPasswordChangePage.setObjectName(u"ConfirmPasswordChangePage")
        self.verticalLayout_6 = QVBoxLayout(self.ConfirmPasswordChangePage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_32 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_32, 8, 1, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_31, 6, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_13, 5, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_33, 4, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_12, 15, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_11, 1, 0, 1, 1)

        self.label_31 = QLabel(self.ConfirmPasswordChangePage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_31.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_6.addWidget(self.label_31, 1, 1, 1, 1)

        self.error_messages_ConfirmPasswordChangePage = QStackedWidget(self.ConfirmPasswordChangePage)
        self.error_messages_ConfirmPasswordChangePage.setObjectName(u"error_messages_ConfirmPasswordChangePage")
        self.error_messages_ConfirmPasswordChangePage.setMinimumSize(QSize(0, 39))
        self.error_messages_ConfirmPasswordChangePage.setMaximumSize(QSize(16777215, 39))
        self.error_messages_ConfirmPasswordChangePage.setLineWidth(0)
        self.message_no_connection_ConfirmPasswordChangePage = QWidget()
        self.message_no_connection_ConfirmPasswordChangePage.setObjectName(u"message_no_connection_ConfirmPasswordChangePage")
        self.horizontalLayout_26 = QHBoxLayout(self.message_no_connection_ConfirmPasswordChangePage)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.message_no_connection_ConfirmPasswordChangePage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(312, 39))
        self.label_23.setMaximumSize(QSize(312, 39))
        self.label_23.setFont(font3)
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_23.setFrameShadow(QFrame.Plain)
        self.label_23.setTextFormat(Qt.AutoText)
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setIndent(0)
        self.label_23.setOpenExternalLinks(False)

        self.horizontalLayout_26.addWidget(self.label_23)

        self.error_messages_ConfirmPasswordChangePage.addWidget(self.message_no_connection_ConfirmPasswordChangePage)
        self.message_empty_ConfirmPasswordChangePage = QWidget()
        self.message_empty_ConfirmPasswordChangePage.setObjectName(u"message_empty_ConfirmPasswordChangePage")
        self.error_messages_ConfirmPasswordChangePage.addWidget(self.message_empty_ConfirmPasswordChangePage)
        self.message_wrong_code_ConfirmPasswordChangePage = QWidget()
        self.message_wrong_code_ConfirmPasswordChangePage.setObjectName(u"message_wrong_code_ConfirmPasswordChangePage")
        self.horizontalLayout_27 = QHBoxLayout(self.message_wrong_code_ConfirmPasswordChangePage)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.message_wrong_code_ConfirmPasswordChangePage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(350, 39))
        self.label_24.setMaximumSize(QSize(350, 39))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setOpenExternalLinks(False)

        self.horizontalLayout_27.addWidget(self.label_24)

        self.error_messages_ConfirmPasswordChangePage.addWidget(self.message_wrong_code_ConfirmPasswordChangePage)

        self.gridLayout_6.addWidget(self.error_messages_ConfirmPasswordChangePage, 3, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_14, 5, 2, 1, 1)

        self.verticalSpacer_62 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_62, 10, 1, 1, 1)

        self.verticalSpacer_59 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_59, 2, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_62)

        self.send_again_button_ConfirmPasswordChangePage = QPushButton(self.ConfirmPasswordChangePage)
        self.send_again_button_ConfirmPasswordChangePage.setObjectName(u"send_again_button_ConfirmPasswordChangePage")
        self.send_again_button_ConfirmPasswordChangePage.setEnabled(False)
        self.send_again_button_ConfirmPasswordChangePage.setMinimumSize(QSize(243, 0))
        self.send_again_button_ConfirmPasswordChangePage.setMaximumSize(QSize(243, 16777215))
        font6 = QFont()
        font6.setUnderline(True)
        self.send_again_button_ConfirmPasswordChangePage.setFont(font6)
        self.send_again_button_ConfirmPasswordChangePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_again_button_ConfirmPasswordChangePage.setStyleSheet(u"")
        self.send_again_button_ConfirmPasswordChangePage.setFlat(True)

        self.horizontalLayout_12.addWidget(self.send_again_button_ConfirmPasswordChangePage)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_85)


        self.gridLayout_6.addLayout(self.horizontalLayout_12, 11, 1, 1, 1)

        self.verification_code_input_ConfirnChangePasswordPage = QLineEdit(self.ConfirmPasswordChangePage)
        self.verification_code_input_ConfirnChangePasswordPage.setObjectName(u"verification_code_input_ConfirnChangePasswordPage")
        self.verification_code_input_ConfirnChangePasswordPage.setMinimumSize(QSize(200, 30))
        self.verification_code_input_ConfirnChangePasswordPage.setInputMethodHints(Qt.ImhDigitsOnly)
        self.verification_code_input_ConfirnChangePasswordPage.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.verification_code_input_ConfirnChangePasswordPage, 7, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_18, 16, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.confirm_button_ConfirmChangePasswordPage = QPushButton(self.ConfirmPasswordChangePage)
        self.confirm_button_ConfirmChangePasswordPage.setObjectName(u"confirm_button_ConfirmChangePasswordPage")
        self.confirm_button_ConfirmChangePasswordPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_ConfirmChangePasswordPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_ConfirmChangePasswordPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.confirm_button_ConfirmChangePasswordPage)

        self.horizontalSpacer_52 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_52)

        self.cancel_button_ConfirmChangePasswordPage = QPushButton(self.ConfirmPasswordChangePage)
        self.cancel_button_ConfirmChangePasswordPage.setObjectName(u"cancel_button_ConfirmChangePasswordPage")
        self.cancel_button_ConfirmChangePasswordPage.setMinimumSize(QSize(100, 30))
        self.cancel_button_ConfirmChangePasswordPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button_ConfirmChangePasswordPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.cancel_button_ConfirmChangePasswordPage)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 9, 1, 1, 1)

        self.label_email_ConfirmChangePasswordPage = QLabel(self.ConfirmPasswordChangePage)
        self.label_email_ConfirmChangePasswordPage.setObjectName(u"label_email_ConfirmChangePasswordPage")
        self.label_email_ConfirmChangePasswordPage.setAlignment(Qt.AlignCenter)
        self.label_email_ConfirmChangePasswordPage.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_email_ConfirmChangePasswordPage, 5, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_6)

        self.IndexWindow.addWidget(self.ConfirmPasswordChangePage)
        self.EmailComfirmPage = QWidget()
        self.EmailComfirmPage.setObjectName(u"EmailComfirmPage")
        self.verticalLayout_3 = QVBoxLayout(self.EmailComfirmPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.confirm_button_EmailConfirmPage = QPushButton(self.EmailComfirmPage)
        self.confirm_button_EmailConfirmPage.setObjectName(u"confirm_button_EmailConfirmPage")
        self.confirm_button_EmailConfirmPage.setMinimumSize(QSize(100, 30))
        self.confirm_button_EmailConfirmPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_button_EmailConfirmPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.confirm_button_EmailConfirmPage)

        self.horizontalSpacer_53 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_53)

        self.changeemail_button_EmailConfirmPage = QPushButton(self.EmailComfirmPage)
        self.changeemail_button_EmailConfirmPage.setObjectName(u"changeemail_button_EmailConfirmPage")
        self.changeemail_button_EmailConfirmPage.setMinimumSize(QSize(100, 30))
        self.changeemail_button_EmailConfirmPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeemail_button_EmailConfirmPage.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.changeemail_button_EmailConfirmPage)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 10, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 14, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 6, 0, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_35, 9, 1, 1, 1)

        self.label_40 = QLabel(self.EmailComfirmPage)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setPixmap(QPixmap(u":/prices/WildBoost_logo.png"))
        self.label_40.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_3.addWidget(self.label_40, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 6, 2, 1, 1)

        self.verticalSpacer_60 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_60, 2, 1, 1, 1)

        self.error_messages_EmailConfirmPage = QStackedWidget(self.EmailComfirmPage)
        self.error_messages_EmailConfirmPage.setObjectName(u"error_messages_EmailConfirmPage")
        self.error_messages_EmailConfirmPage.setMinimumSize(QSize(0, 39))
        self.error_messages_EmailConfirmPage.setMaximumSize(QSize(16777215, 30))
        self.message_wrong_code_EmailConfirmPage = QWidget()
        self.message_wrong_code_EmailConfirmPage.setObjectName(u"message_wrong_code_EmailConfirmPage")
        self.horizontalLayout_28 = QHBoxLayout(self.message_wrong_code_EmailConfirmPage)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.message_wrong_code_EmailConfirmPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(230, 39))
        self.label_25.setMaximumSize(QSize(230, 39))
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_25.setScaledContents(False)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setOpenExternalLinks(False)

        self.horizontalLayout_28.addWidget(self.label_25)

        self.error_messages_EmailConfirmPage.addWidget(self.message_wrong_code_EmailConfirmPage)
        self.message_empty_EmailConfirmPage = QWidget()
        self.message_empty_EmailConfirmPage.setObjectName(u"message_empty_EmailConfirmPage")
        self.error_messages_EmailConfirmPage.addWidget(self.message_empty_EmailConfirmPage)
        self.message_no_connection_EmailConfirmPage = QWidget()
        self.message_no_connection_EmailConfirmPage.setObjectName(u"message_no_connection_EmailConfirmPage")
        self.horizontalLayout_29 = QHBoxLayout(self.message_no_connection_EmailConfirmPage)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.message_no_connection_EmailConfirmPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(260, 39))
        self.label_26.setMaximumSize(QSize(260, 39))
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"QLabel {\n"
"    border:1px solid #C02C70;\n"
"    border-radius:6px;\n"
"    color:#C02C70;\n"
"};")
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setOpenExternalLinks(False)

        self.horizontalLayout_29.addWidget(self.label_26)

        self.error_messages_EmailConfirmPage.addWidget(self.message_no_connection_EmailConfirmPage)

        self.gridLayout_3.addWidget(self.error_messages_EmailConfirmPage, 3, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_20, 15, 1, 1, 1)

        self.label_email_EmailConfirmPage = QLabel(self.EmailComfirmPage)
        self.label_email_EmailConfirmPage.setObjectName(u"label_email_EmailConfirmPage")
        self.label_email_EmailConfirmPage.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_email_EmailConfirmPage, 6, 1, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_36, 4, 1, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_34, 7, 1, 1, 1)

        self.verification_code__input_EmailConfirmPage = QLineEdit(self.EmailComfirmPage)
        self.verification_code__input_EmailConfirmPage.setObjectName(u"verification_code__input_EmailConfirmPage")
        self.verification_code__input_EmailConfirmPage.setMinimumSize(QSize(200, 30))
        self.verification_code__input_EmailConfirmPage.setInputMethodHints(Qt.ImhDigitsOnly)
        self.verification_code__input_EmailConfirmPage.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.verification_code__input_EmailConfirmPage, 8, 1, 1, 1)

        self.label_7 = QLabel(self.EmailComfirmPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 5, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_86)

        self.send_again_button_EmailConfirmPage = QPushButton(self.EmailComfirmPage)
        self.send_again_button_EmailConfirmPage.setObjectName(u"send_again_button_EmailConfirmPage")
        self.send_again_button_EmailConfirmPage.setEnabled(False)
        self.send_again_button_EmailConfirmPage.setFont(font6)
        self.send_again_button_EmailConfirmPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_again_button_EmailConfirmPage.setFlat(True)

        self.horizontalLayout_14.addWidget(self.send_again_button_EmailConfirmPage)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_87)


        self.gridLayout_3.addLayout(self.horizontalLayout_14, 12, 1, 1, 1)

        self.verticalSpacer_63 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_63, 11, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.IndexWindow.addWidget(self.EmailComfirmPage)

        self.verticalLayout_9.addWidget(self.IndexWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet(u"QStatusBar {\n"
"    border: 1px solid #B4B5B8;\n"
"    background: #F5F5F5;\n"
"    color:black;\n"
"}")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.IndexWindow.setCurrentIndex(5)
        self.error_messages_LoginPage.setCurrentIndex(2)
        self.enter_button_loginpage.setDefault(True)
        self.confirm_button_ChangeEmailPage.setDefault(True)
        self.error_messages_ChangeEmailPage.setCurrentIndex(1)
        self.confirm_button_EnterEmailPage.setDefault(True)
        self.confirm_button_SiqnupPage.setDefault(True)
        self.error_messages_SignupPage.setCurrentIndex(0)
        self.error_messages_ChangePasswordPage.setCurrentIndex(1)
        self.confirm_button_ChangePasswordPage.setDefault(True)
        self.AlgoritmWindow.setCurrentIndex(2)
        self.confirm_key_button_ProfilePage.setDefault(True)
        self.about_subscribe_ProfilePage.setCurrentIndex(2)
        self.start_companies_button_SearchPage.setDefault(True)
        self.menu_SearchPage.setCurrentIndex(0)
        self.menu_adverts_setup_SearchPage.setCurrentIndex(0)
        self.menu_adverts_setup_confirm_button_SearchPage.setDefault(True)
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setDefault(True)
        self.menu_product_setup_SearchPage.setCurrentIndex(2)
        self.menu_product_setup_confirm_button_SearchPage.setDefault(True)
        self.menu_product_setup_amount_error_ok_button_SearchPage.setDefault(True)
        self.menu_settings_start_button_SearchPage.setDefault(True)
        self.menu_settings_error_ok_button_SearchPage.setDefault(True)
        self.start_companies_button_ProductPage.setDefault(True)
        self.menu_ProductPage.setCurrentIndex(0)
        self.menu_adverts_setup_ProductPage.setCurrentIndex(0)
        self.menu_adverts_setup_confirm_button_ProductPage.setDefault(True)
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setDefault(True)
        self.menu_product_setup_ProductPage.setCurrentIndex(2)
        self.menu_product_setup_confirm_button_ProductPage.setDefault(True)
        self.menu_product_setup_amount_error_ok_button_ProductPage.setDefault(True)
        self.menu_settings_start_button_ProductPage.setDefault(True)
        self.menu_settings_error_ok_button_ProductPage.setDefault(True)
        self.error_messages_ConfirmPasswordChangePage.setCurrentIndex(1)
        self.confirm_button_ConfirmChangePasswordPage.setDefault(True)
        self.confirm_button_EmailConfirmPage.setDefault(True)
        self.error_messages_EmailConfirmPage.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WildBoost", None))
        self.forgot_password_button_loginpage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u044b \u043d\u0435\u0432\u0435\u0440\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435!", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.email_input_loginpage.setText("")
        self.password_label_loginpage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.email_label_loginpage.setText(QCoreApplication.translate("MainWindow", u"E-mail:     ", None))
        self.enter_button_loginpage.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.enter_button_loginpage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.signup_button_loginpage.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 e-mail:", None))
        self.label_10.setText("")
        self.confirm_button_ChangeEmailPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_ChangeEmailPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancle_button_ChangeEmailPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.cancle_button_ChangeEmailPage.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 e-mail!", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.confirm_button_EnterEmailPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_EnterEmailPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancle_button_EnterEmailPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.cancle_button_EnterEmailPage.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_14.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448 e-mail:", None))
        self.email_input_SignupPage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c gmail \u0438\u043b\u0438 yandex", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:  ", None))
        self.confirm_button_SiqnupPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_SiqnupPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancle_button_SignupPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
#if QT_CONFIG(shortcut)
        self.cancle_button_SignupPage.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.label_15.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0441 \u0442\u0430\u043a\u0438\u043c e-mail \u0443\u0436\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438 \u043d\u0435 \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442!", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0439 e-mail!", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u043e\u043b\u0438 \u043d\u0435 \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442!", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.confirm_button_ChangePasswordPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_ChangePasswordPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancle_button_ChangePasswordPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.cancle_button_ChangePasswordPage.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_29.setText("")
        self.profile_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.search_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043b\u0430\u043c\u0430 \u0432 \u043f\u043e\u0438\u0441\u043a\u0435", None))
        self.product_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043b\u0430\u043c\u0430 \u0432 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435", None))
        self.how_to_use_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f?", None))
        self.update_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0439 \u043d\u0435\u0442", None))
        self.exit_button_IndexPage.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d \u043e\u0442 \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u0433\u043e \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430:", None))
#if QT_CONFIG(whatsthis)
        self.key_input_ProfilePage.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.confirm_key_button_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_key_button_ProfilePage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0440\u0438\u0444\u043d\u044b\u0439 \u043f\u043b\u0430\u043d:", None))
        self.email_label_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"tesing_pretty_long_email@gmail.com", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430 \u0438\u0441\u0442\u0435\u043a\u0430\u0435\u0442:", None))
        self.subscribtion_plan_label_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.expire_date_label_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.refresh_button_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.refresh_button_ProfilePage.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.pay_199_button_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.label_36.setText("")
        self.label_35.setText("")
        self.pay_349_button_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.pay_499_button_ProfilePage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.label_34.setText("")
        self.label_33.setText("")
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_37.setText("")
        self.label_logo_SearchPage.setText("")
        self.start_companies_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.stop_companies_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.reset_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.menu_search_setup_refresh_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.menu_adverts_setup_confirm_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0439!", None))
        self.menu_adverts_setup_amount_error_ok_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.menu_product_setup_refresh_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.menu_product_setup_confirm_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432!", None))
        self.menu_product_setup_amount_error_ok_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.menu_settings_start_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.menu_settings_stop_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.error_label_settings_SearchPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0445!", None))
        self.menu_settings_error_ok_button_SearchPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u0435\u043a \u0441\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438. \u041f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0438\u0442\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0443 \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \"\u043f\u0440\u043e\u0444\u0438\u043b\u044c\"!", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u043e\u0442 \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u0433\u043e \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430 Wildberries \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \"\u043f\u0440\u043e\u0444\u0438\u043b\u044c\"!", None))
        self.start_companies_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.stop_companies_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.reset_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.menu_search_setup_refresh_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.menu_adverts_setup_confirm_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0439!", None))
        self.menu_adverts_setup_amount_error_ok_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.menu_product_setup_refresh_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.menu_product_setup_confirm_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0432\u0430\u0440\u043e\u0432!", None))
        self.menu_product_setup_amount_error_ok_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.menu_settings_start_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.menu_settings_stop_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.error_label_settings_ProductPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0445!", None))
        self.menu_settings_error_ok_button_ProductPage.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u0435\u043a \u0441\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0438. \u041f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0438\u0442\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u043a\u0443 \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \"\u043f\u0440\u043e\u0444\u0438\u043b\u044c\"!", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u043e\u0442 \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u043e\u0433\u043e \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430 Wildberries \u0432\u043e \u0432\u043a\u043b\u0430\u0434\u043a\u0435 \"\u043f\u0440\u043e\u0444\u0438\u043b\u044c\"!", None))
        self.label_logo_ProductPage.setText("")
        self.label_31.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f!", None))
        self.send_again_button_ConfirmPasswordChangePage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e \u0447\u0435\u0440\u0435\u0437 02:00", None))
        self.verification_code_input_ConfirnChangePasswordPage.setText("")
        self.verification_code_input_ConfirnChangePasswordPage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0441\u044c\u043c\u043e \u043c\u043e\u0433\u043b\u043e \u043f\u043e\u043f\u0430\u0441\u0442\u044c \u0432 \"\u0441\u043f\u0430\u043c\".", None))
        self.confirm_button_ConfirmChangePasswordPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_ConfirmChangePasswordPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancel_button_ConfirmChangePasswordPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.cancel_button_ConfirmChangePasswordPage.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_email_ConfirmChangePasswordPage.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u044f \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f, \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u0412\u0430\u0448 e-mail.", None))
        self.confirm_button_EmailConfirmPage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.confirm_button_EmailConfirmPage.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.changeemail_button_EmailConfirmPage.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c e-mail", None))
        self.label_40.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f!", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435!", None))
        self.label_email_EmailConfirmPage.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u0412\u0430\u0448 e-mail.", None))
        self.verification_code__input_EmailConfirmPage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0441\u044c\u043c\u043e \u043c\u043e\u0433\u043b\u043e \u043f\u043e\u043f\u0430\u0441\u0442\u044c \u0432 \"\u0441\u043f\u0430\u043c\".", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f,", None))
        self.send_again_button_EmailConfirmPage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u043d\u043e \u0447\u0435\u0440\u0435\u0437 02:00", None))
#if QT_CONFIG(tooltip)
        self.statusBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.statusBar.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.statusBar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

