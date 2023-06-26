from ui_INDEX import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThreadPool, QRunnable, Slot, QThread, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget, QRadioButton, QButtonGroup, 
    QCheckBox, QHBoxLayout, QSpinBox, QWidgetItem, QAbstractSpinBox)

from yookassa import Configuration, Payment
from aiohttp import ClientSession

import sys
import json
import requests
import datetime
import asyncio
import time
import threading
import webbrowser
import re
import ssl
import certifi
import uuid
from copy import copy

import config

from verification import send_email, send_recovery_email
from style import (menu_button_left, menu_active_button_left, menu_button_mid,
                   menu_active_button_mid, menu_button_right, menu_active_button_right)

Configuration.account_id = config.ACCOUNT_ID
Configuration.secret_key = config.SECRET_KEY

app = QApplication(sys.argv)
Form = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()

subscribtion_plan = {
    1 : {'name' : 'пробный', 'adverts' : 1, 'products' : 1, 'renew' : 15, 'price' : 0},
    2 : {'name' : 'базовый', 'adverts' : 1, 'products' : 1, 'renew' : 10, 'price' : 5},
    3 : {'name' : 'стандарт', 'adverts' : 3, 'products' : 5, 'renew' : 5, 'price' : 449},
    4 : {'name' : 'профи', 'adverts' : 10, 'products' : 30, 'renew' : 3, 'price' : 599},
    } # словарь с параметрами подписок

button_group_search_adverts = QButtonGroup() # группа радио-кнопок для определения активной (кампании в поиске)
checkboxes_search_adverts = [] # список чекбоксов, для определения активных (кампании в поиске)'
search_adverts_ids = [] # список id кампаний для рекламы в поиске

button_group_product_adverts = QButtonGroup() # группа радио-кнопок для определения активной (кампании в карточке)
checkboxes_product_adverts = [] # список чекбоксов, для определения активных (кампании в карточке)
product_adverts_ids = [] # список id кампаний для рекламы в карточке

button_group_search_products = QButtonGroup() # группа радио-кнопок для определения активной (продукты в кампаниях для поиска)
checkboxes_search_products = [] # список чекбоксов, для определения активных (продукты в кампаниях для поиска)

button_group_product_products = QButtonGroup() # группа радио-кнопок для определения активной (продукты в кампаниях в карточке)
checkboxes_product_products = [] # список чекбоксов, для определения активных (продукты в кампаниях в карточке)

product_group_settings = []
max_price_settings = []
key_word_settings = []
place_max_settings = []
place_min_settings = []

product_group_settings_product = []
max_price_settings_product = []
place_max_settings_product = []
place_min_settings_product = []

stop_search_events = []
stop_product_events = []
reset_timer_password_events = []
reset_timer_verify_events = []

verification_code = 0
VERSION = 1
TOKEN = ''
KEY = ''
VERIFIED = ''
EXPIRE_DATE = ''
SUBSCRIBE_PLAN = ''
EMAIL = ''
UPDATE_URL = ''

class LayoutSignals(QObject):
    result = Signal(tuple)
    result_wrong = Signal(tuple)
    result_error = Signal(tuple)
    result_product = Signal(tuple)
    result_wrong_product = Signal(tuple)
    result_error_product = Signal(tuple)
    start_or_stop = Signal(str)
    start_or_stop_product = Signal(str)
    subscription_expired = Signal()
    status_bar_info = Signal(bool)
    button_disable = Signal(object)

    @Slot()
    def add_log(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:green; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log.verticalScrollBar()
        
        ui.log_layout_SearchPage.addWidget(log)
        ui.log_layout_SearchPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log.verticalScrollBar().setValue(ui.scrollArea_log.verticalScrollBar().maximum())

    @Slot()
    def add_log_wrong(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:#E6925D; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log.verticalScrollBar()
        
        ui.log_layout_SearchPage.addWidget(log)
        ui.log_layout_SearchPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log.verticalScrollBar().setValue(ui.scrollArea_log.verticalScrollBar().maximum())

    @Slot()
    def add_log_error(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:red; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log.verticalScrollBar()
        
        ui.log_layout_SearchPage.addWidget(log)
        ui.log_layout_SearchPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log.verticalScrollBar().setValue(ui.scrollArea_log.verticalScrollBar().maximum())

    @Slot()
    def add_log_product(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:green; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log_ProductPage.verticalScrollBar()
        
        ui.log_layout_ProductPage.addWidget(log)
        ui.log_layout_ProductPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log_ProductPage.verticalScrollBar().setValue(ui.scrollArea_log_ProductPage.verticalScrollBar().maximum())

    @Slot()
    def add_log_wrong_product(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:#E6925D; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log_ProductPage.verticalScrollBar()
        
        ui.log_layout_ProductPage.addWidget(log)
        ui.log_layout_ProductPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log_ProductPage.verticalScrollBar().setValue(ui.scrollArea_log_ProductPage.verticalScrollBar().maximum())

    @Slot()
    def add_log_error_product(self, data):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setWordWrap(True)
        log.setMaximumHeight(data[1])
        log.setText(data[0])
        log.setStyleSheet('QLabel{color:red; opacity:.7;}')

        line = QFrame()
        line.setFrameStyle(QFrame.HLine)
        line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
        line.setMaximumHeight(1)

        scrollbar = ui.scrollArea_log_ProductPage.verticalScrollBar()
        
        ui.log_layout_ProductPage.addWidget(log)
        ui.log_layout_ProductPage.addWidget(line)
        
        if (scrollbar.value() >= scrollbar.maximum() - 100) or (scrollbar.value() == 0):
            ui.scrollArea_log_ProductPage.verticalScrollBar().setValue(ui.scrollArea_log_ProductPage.verticalScrollBar().maximum())

    @Slot()
    def start_stop_message(self, text):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        log.setWordWrap(False)
        log.setMaximumHeight(15)
        log.setStyleSheet('QLabel{color:green; opacity:.7;}')
        log.setText(text)

        ui.log_layout_SearchPage.addWidget(log)
        
    @Slot()
    def start_stop_message_product(self, text):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        log.setWordWrap(False)
        log.setMaximumHeight(15)
        log.setStyleSheet('QLabel{color:green; opacity:.7;}')
        log.setText(text)

        ui.log_layout_ProductPage.addWidget(log)

    @Slot()
    def sub_expired(self):
        log = QLabel()
        log.setAlignment(Qt.AlignmentFlag.AlignTop)
        log.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        log.setWordWrap(False)
        log.setMaximumHeight(15)
        log.setStyleSheet('QLabel{color:red; opacity:.7;}')
        log.setText(f'''Истек срок действия подписки. WildBoost остановлен ({time.strftime('%d %B %H:%M:%S', time.localtime())}).''')

        ui.menu_SearchPage.setCurrentWidget(ui.menu_subscribe_error_SearchPage)
        ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_start_SearchPage)
        ui.log_layout_SearchPage.addWidget(log)

        log_product = QLabel()
        log_product.setAlignment(Qt.AlignmentFlag.AlignTop)
        log_product.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        log_product.setWordWrap(False)
        log_product.setMaximumHeight(15)
        log_product.setStyleSheet('QLabel{color:red; opacity:.7;}')
        log_product.setText(f'''Истек срок действия подписки. WildBoost остановлен ({time.strftime('%d %B %H:%M:%S', time.localtime())}).''')

        ui.menu_ProductPage.setCurrentWidget(ui.menu_subscribe_error_ProductPage)
        ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_start_ProductPage)
        ui.log_layout_ProductPage.addWidget(log_product)
    
    @Slot()
    def update_status_bar_info(self, is_important):
        ui.statusBar.clearMessage()

        if is_important:
            ui.statusBar.showMessage('ВАЖНО: установите обновление для корректной работы приложения! По всем вопросам обращайтесь по почте: support@wildboost.ru')
        else:
            ui.statusBar.showMessage('По всем вопросам обращайтесь по почте: support@wildboost.ru')

signal = LayoutSignals()
signal.result.connect(signal.add_log)
signal.result_wrong.connect(signal.add_log_wrong)
signal.result_error.connect(signal.add_log_error)
signal.result_product.connect(signal.add_log_product)
signal.result_wrong_product.connect(signal.add_log_wrong_product)
signal.result_error_product.connect(signal.add_log_error_product)
signal.start_or_stop.connect(signal.start_stop_message)
signal.start_or_stop_product.connect(signal.start_stop_message_product)
signal.subscription_expired.connect(signal.sub_expired)
signal.status_bar_info.connect(signal.update_status_bar_info)

# чистим данные, сбрасываем ошибки
def clear_LoginPage():
    ui.email_input_loginpage.setText('')
    ui.password_input_loginpage.setText('')
    ui.error_messages_LoginPage.setCurrentWidget(ui.message_empty_LoginPage)

def clear_SignupPage():
    ui.email_input_SignupPage.setText("")
    ui.password_input_SignupPage.setText("")
    ui.password_repeat_input_SignupPage.setText("")
    ui.error_messages_SignupPage.setCurrentWidget(ui.message_empty_SignupPage)

def clear_adverts_menu_SearchPage():
    search_adverts_amount = ui.adverts_layout_SearchPage.count()
    search_adverts_ids.clear()
    if search_adverts_amount != 0:
        for i in range(search_adverts_amount):
            ui.adverts_layout_SearchPage.itemAt(i).widget().deleteLater()
        checkboxes_search_adverts.clear()
        for button in button_group_search_adverts.buttons():
            button_group_search_adverts.removeButton(button)

def clear_products_menu_SearchPage():
    search_adverts_products_amount = ui.product_layout_SearchPage.count()
    if search_adverts_products_amount != 0:
        for i in range(search_adverts_products_amount):
            ui.product_layout_SearchPage.itemAt(i).widget().deleteLater()
        checkboxes_search_products.clear()
        for button in button_group_search_products.buttons():
            button_group_search_products.removeButton(button)

def clear_settings_SearchPage():
    search_settings_amount = ui.settings_layout_SearchPage.count()

    product_group_settings.clear()
    max_price_settings.clear()
    key_word_settings.clear()
    place_max_settings.clear()
    place_min_settings.clear()

    if search_settings_amount != 0:
        for i in range(search_settings_amount):
                item = ui.settings_layout_SearchPage.itemAt(i)
                if isinstance(item, QHBoxLayout):
                    for i in range(item.count()):
                        item.itemAt(i).widget().deleteLater()
                        item.layout().deleteLater()
                elif isinstance(item, QWidgetItem):
                    item.widget().deleteLater()
                elif item is None:
                    clear_settings_SearchPage()

def clear_log_SearchPage():
    search_log_amount = ui.log_layout_SearchPage.count()
    if search_log_amount != 0:
        for i in range(search_log_amount):
            if ui.log_layout_SearchPage.itemAt(i).widget().objectName() != 'label_logo_SearchPage':
                ui.log_layout_SearchPage.itemAt(i).widget().deleteLater()

def clear_adverts_menu_ProductPage():
    product_adverts_ids.clear()
    product_adverts_amount = ui.adverts_layout_ProductPage.count()
    if product_adverts_amount != 0:
        for i in range(product_adverts_amount):
            ui.adverts_layout_ProductPage.itemAt(i).widget().deleteLater()
        checkboxes_product_adverts.clear()
        for button in button_group_product_adverts.buttons():
            button_group_product_adverts.removeButton(button)

def clear_products_menu_ProductPage():
    product_adverts_products_amount = ui.product_layout_ProductPage.count()
    if product_adverts_products_amount != 0:
        for i in range(product_adverts_products_amount):
            ui.product_layout_ProductPage.itemAt(i).widget().deleteLater()
        checkboxes_product_products.clear()
        for button in button_group_product_products.buttons():
            button_group_product_products.removeButton(button)

def clear_settings_ProductPage():
    product_settings_amount = ui.settings_layout_ProductPage.count()

    product_group_settings_product.clear()
    max_price_settings_product.clear()
    place_max_settings_product.clear()
    place_min_settings_product.clear()

    if product_settings_amount != 0:
        for i in range(product_settings_amount):
                item = ui.settings_layout_ProductPage.itemAt(i)
                if isinstance(item, QHBoxLayout):
                    for i in range(item.count()):
                        item.itemAt(i).widget().deleteLater()
                        item.layout().deleteLater()
                elif isinstance(item, QWidgetItem):
                    item.widget().deleteLater()
                elif item is None:
                    clear_settings_ProductPage()

def clear_log_ProductPage():
    product_log_amount = ui.log_layout_ProductPage.count()
    if product_log_amount != 0:
        for i in range(product_log_amount):
            if ui.log_layout_ProductPage.itemAt(i).widget().objectName() != 'label_logo_ProductPage':
                ui.log_layout_ProductPage.itemAt(i).widget().deleteLater()

# проверяем тарифный план, срок действия подписки; устаналиваем соответсвующие данные на странице профиля
def check_subscribtion_params():
    if TOKEN != '':
        headers = {
        'Authorization': f'Token {TOKEN}'
        }
        try:
            response = requests.get(f'{config.ADDRESS}/api/subscription/', headers=headers)
            if response.status_code == 200:
                response = response.json()

                global EXPIRE_DATE
                EXPIRE_DATE = response.get('expire_date')
                global SUBSCRIBE_PLAN
                SUBSCRIBE_PLAN = response.get('subscribe_plan')

                if SUBSCRIBE_PLAN == 1:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.free_subscribe_ProfilePage)
                elif SUBSCRIBE_PLAN == 2:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.base_subscribe_ProfilePage)
                elif SUBSCRIBE_PLAN == 3:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.standart_subscribe_ProfilePage)    
                elif SUBSCRIBE_PLAN == 4:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.profi_subscribe_ProfilePage)

                ui.subscribtion_plan_label_ProfilePage.setText(subscribtion_plan[SUBSCRIBE_PLAN]['name'].upper())
                ui.expire_date_label_ProfilePage.setText(EXPIRE_DATE)

        except:
            pass

# получаем токен на основании введенных данных,
# устанавливаем константы
def get_token(email, password):
    data = {
    'username' : email,
    'password' : password
    }
    try:
        response = requests.post(f'{config.ADDRESS}/api/token-auth/', data=data)
    except:
        return 'connection error'

    if response.status_code == 200:
        global TOKEN
        TOKEN = response.json().get('token')

        headers = {
            'Authorization': f'Token {TOKEN}'
        }
        try:
            response = requests.get(f'{config.ADDRESS}/api/subscription/', headers=headers)
        except:
            return 'connection error'

        if response.status_code == 200:

            global VERIFIED
            VERIFIED = response.json().get('verified')
            global EXPIRE_DATE
            EXPIRE_DATE = response.json().get('expire_date')
            global SUBSCRIBE_PLAN
            SUBSCRIBE_PLAN = response.json().get('subscribe_plan')
            global EMAIL
            EMAIL = response.json().get('email')

            if SUBSCRIBE_PLAN == 1:
                ui.about_subscribe_ProfilePage.setCurrentWidget(ui.free_subscribe_ProfilePage)
            elif SUBSCRIBE_PLAN == 2:
                ui.about_subscribe_ProfilePage.setCurrentWidget(ui.base_subscribe_ProfilePage)
            elif SUBSCRIBE_PLAN == 3:
                ui.about_subscribe_ProfilePage.setCurrentWidget(ui.standart_subscribe_ProfilePage)    
            elif SUBSCRIBE_PLAN == 4:
                ui.about_subscribe_ProfilePage.setCurrentWidget(ui.profi_subscribe_ProfilePage)

            ui.subscribtion_plan_label_ProfilePage.setText(subscribtion_plan[SUBSCRIBE_PLAN]['name'].upper())
            ui.email_label_ProfilePage.setText(EMAIL)
            ui.expire_date_label_ProfilePage.setText(EXPIRE_DATE)
    else:
        return 'data error'
    return response

# авторизуемся, получаем константы, проверяем верифицирован ли пользователь
# если да - перенаправляем на главную страницу, если нет - на страницу верификации
def login():
    email = ui.email_input_loginpage.text().lower().strip()
    password = ui.password_input_loginpage.text()
    
    response = get_token(email, password)

    if response == 'connection error':
        ui.error_messages_LoginPage.setCurrentWidget(ui.message_no_connection_LoginPage)

    elif response == 'data error':
        ui.error_messages_LoginPage.setCurrentWidget(ui.message_wrong_data_LoginPage)

    elif response.status_code == 200:

        clear_LoginPage()

        if VERIFIED is True:
            ui.IndexWindow.setCurrentWidget(ui.IndexPage)
            
            ui.profile_button_IndexPage.setStyleSheet(menu_active_button_left)
            ui.search_button_IndexPage.setStyleSheet(menu_button_mid)
            ui.product_button_IndexPage.setStyleSheet(menu_button_right)

            ui.AlgoritmWindow.setCurrentWidget(ui.ProfilePage)

        elif VERIFIED is False:

            global verification_code
            verification_code = send_email(email)

            global EMAIL
            EMAIL = email

            ui.label_email_ConfirmChangePasswordPage.setText(f'Для восстановления пароля введите код потверждения, отправленный на Ваш e-mail: {EMAIL}.')
            ui.label_email_EmailConfirmPage.setText(f'отправленный на Ваш e-mail: {EMAIL}.')

            threading.Thread(daemon=True, target=timer_EmailConfirmPage).start()

            ui.IndexWindow.setCurrentWidget(ui.EmailComfirmPage)

# регистрация. если введенные пароли совпадают: создается новый пользователь
# отправляет письмо для верификации, перенаправляется на страницу верификации
def signup():
    email = ui.email_input_SignupPage.text().lower().strip()
    password = ui.password_input_SignupPage.text()
    password2 = ui.password_repeat_input_SignupPage.text()

    if password == password2:
        data = {
        'username' : email,
        'email' : email,
        'password' : password,
        }

        try:
            response = requests.post(f'{config.ADDRESS}/api/signup/', data=data)
        except:
            ui.error_messages_SignupPage.setCurrentWidget(ui.message_no_connection_SignupPage)
            return None
        
        if response.status_code == 201:
            response = get_token(email, password)
            
            if response == 'connection error':
                ui.error_messages_SignupPage.setCurrentWidget(ui.message_no_connection_SignupPage)

            elif response.status_code == 200:
                clear_SignupPage()

                global verification_code
                verification_code = send_email(email)

                global EMAIL
                EMAIL = email
                
                ui.label_email_ConfirmChangePasswordPage.setText(f'Для восстановления пароля введите код потверждения, отправленный на Ваш e-mail: {EMAIL}.')
                ui.label_email_EmailConfirmPage.setText(f'отправленный на Ваш e-mail: {EMAIL}.')

                threading.Thread(daemon=True, target=timer_EmailConfirmPage).start()

                ui.IndexWindow.setCurrentWidget(ui.EmailComfirmPage)

        elif 'username' in response.text:
            if response.json().get('username') == ["A user with that username already exists."]:
                ui.error_messages_SignupPage.setCurrentWidget(ui.message_email_exists_SignupPage)
            elif response.json().get('username') == ["This field may not be blank."]:
                ui.error_messages_SignupPage.setCurrentWidget(ui.message_invalid_email_SignupPage)

        elif 'email' in response.text:
            ui.error_messages_SignupPage.setCurrentWidget(ui.message_invalid_email_SignupPage)

    else:
        ui.error_messages_SignupPage.setCurrentWidget(ui.message_different_passwords_SignupPage)

# проверяет корректность введенного кода, в случае успеха пускает на главную страницу
# вносит изменения в БД, помечая аккаунт как верифицированный
def email_verify():
    input_code = ui.verification_code__input_EmailConfirmPage.text().strip()

    if input_code == str(verification_code):
        headers = {
            'Authorization': f'Token {TOKEN}'
        }
        data={
            'verified' : True
        }

        try:
            response = requests.patch(f'{config.ADDRESS}/api/subscription/change/', headers=headers, data=data)
        except:
            ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_no_connection_EmailConfirmPage)
            return None

        if response.status_code == 200:

            ui.verification_code__input_EmailConfirmPage.setText('')
            ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_empty_EmailConfirmPage)

            ui.IndexWindow.setCurrentWidget(ui.IndexPage)  
            ui.profile_button_IndexPage.setStyleSheet(menu_active_button_left)
            ui.search_button_IndexPage.setStyleSheet(menu_button_mid)
            ui.product_button_IndexPage.setStyleSheet(menu_button_right)

            reset_timer_verify()
            ui.AlgoritmWindow.setCurrentWidget(ui.ProfilePage)

        # на всякий случай (по идее, если нет ошибки соединения, то ответ всегда 200)
        else:
            ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_no_connection_EmailConfirmPage)

    else:
        ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_wrong_code_EmailConfirmPage)

# меняет e-mail, если такой еще не зарегистрирован в БД, отправляет на него код верификации
# перекидывает на страницу верификации электронной почты
def change_email():
    email = ui.email_input_ChangeEmailPage.text().lower().strip()
    headers = {
            'Authorization': f'Token {TOKEN}'
        }
    data={
        'email' : email,
        'username' : email
    }

    try:
        response = requests.patch(f'{config.ADDRESS}/api/subscription/change/', headers=headers, data=data)
    except:
        ui.error_messages_ChangeEmailPage.setCurrentWidget(ui.message_no_connection_ChangeEmailPage)
        return None

    if response.status_code == 200:
        global verification_code
        verification_code = send_email(email)

        global EMAIL
        EMAIL = email

        ui.label_email_ConfirmChangePasswordPage.setText(f'Для восстановления пароля введите код потверждения, отправленный на Ваш e-mail: {EMAIL}.')
        ui.label_email_EmailConfirmPage.setText(f'отправленный на Ваш e-mail: {EMAIL}.')

        ui.email_input_ChangeEmailPage.setText('')
        ui.error_messages_ChangeEmailPage.setCurrentWidget(ui.message_empty_ChangeEmailPage)
        
        ui.IndexWindow.setCurrentWidget(ui.EmailComfirmPage)
    elif response.status_code == 406:
        ui.error_messages_ChangeEmailPage.setCurrentWidget(ui.message_email_exists_ChangeEmailPage)
    else:
        ui.error_messages_ChangeEmailPage.setCurrentWidget(ui.message_invalid_email_ChangeEmailPage)
        
# отправляет код для сброса пароля на указанный адрес
# перенаправляет на страницу для валидации кода
def change_password_verify():
    global EMAIL
    EMAIL = ui.email_input_EnterEmailPage.text().lower().strip()
    global verification_code
    verification_code = send_recovery_email(EMAIL)

    ui.label_email_ConfirmChangePasswordPage.setText(f'Для восстановления пароля введите код потверждения, отправленный на Ваш e-mail: {EMAIL}.')
    ui.label_email_EmailConfirmPage.setText(f'отправленный на Ваш e-mail: {EMAIL}.')

    ui.email_input_EnterEmailPage.setText('')

    threading.Thread(daemon=True, target=timer_ConfirmPasswordChangePage).start()
    ui.new_password_input_ChangePasswordPage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.ConfirmPasswordChangePage)

# повторно отправляем e-mail для сброса пароля
def send_again_ChangePassword():
    global verification_code
    verification_code = send_recovery_email(EMAIL)

    ui.send_again_button_ConfirmPasswordChangePage.setDisabled(True)
    threading.Thread(daemon=True, target=timer_ConfirmPasswordChangePage).start()

def send_again_verify():
    global verification_code
    verification_code = send_email(EMAIL)

    ui.send_again_button_EmailConfirmPage.setDisabled(True)
    threading.Thread(daemon=True, target=timer_EmailConfirmPage).start()

# запускает таймер для повторной отправки e-mail при восстановлении пароля
def timer_ConfirmPasswordChangePage():
    reset_event = threading.Event()
    reset_timer_password_events.append(reset_event)
    for num in range(120,0,-1):
        if reset_event.is_set():
            return None
        minutes = num // 60
        seconds = str(num - minutes*60)
        if len(seconds) == 1:
            seconds = f'0{seconds}'
        ui.send_again_button_ConfirmPasswordChangePage.setText(f'Отправить повторно через 0{minutes}:{seconds}')
        time.sleep(1)

    reset_timer_password_events.pop()
    ui.send_again_button_ConfirmPasswordChangePage.setText('Отправить повторно') 
    ui.send_again_button_ConfirmPasswordChangePage.setEnabled(True)

# запускает таймер для повторной отправки e-mail при верификации
def timer_EmailConfirmPage():
    reset_event = threading.Event()
    reset_timer_verify_events.append(reset_event)
    for num in range(120,0,-1):
        if reset_event.is_set():
            return None
        minutes = num // 60
        seconds = str(num - minutes*60)
        if len(seconds) == 1:
            seconds = f'0{seconds}'
        ui.send_again_button_EmailConfirmPage.setText(f'Отправить повторно через 0{minutes}:{seconds}')
        time.sleep(1)

    reset_timer_verify_events.pop()
    ui.send_again_button_EmailConfirmPage.setText('Отправить повторно') 
    ui.send_again_button_EmailConfirmPage.setEnabled(True)

# валидирует код, отправленный для сброса пароля
# перенаправляет на страницу установки нового пароля
def recovery_email_verify():
    input_code = ui.verification_code_input_ConfirnChangePasswordPage.text().strip()
    if input_code == str(verification_code):
        ui.verification_code_input_ConfirnChangePasswordPage.setText('')
        ui.error_messages_ConfirmPasswordChangePage.setCurrentWidget(ui.message_empty_ConfirmPasswordChangePage)
        reset_timer_ChangePassword()
        ui.IndexWindow.setCurrentWidget(ui.ChangPasswordPage)
    else:
        ui.error_messages_ConfirmPasswordChangePage.setCurrentWidget(ui.message_wrong_code_ConfirmPasswordChangePage)

# меняет пароль, если введенные совпадают. помечает пользователя как верифицированного
# перенаправляет на главную страницу
def change_password():
    password = ui.new_password_input_ChangePasswordPage.text()
    password2 = ui.password_repeat_ChangePasswordPage.text()

    if password == password2:
        data={
            'password' : password,
            'email' : EMAIL
        }

        try:
            response = requests.patch(f'{config.ADDRESS}/api/change-password/', data=data)
        except:
            ui.error_messages_ChangePasswordPage.setCurrentWidget(ui.message_no_connection_ChangePasswordPage)
            return None

        if response.status_code == 200:
            response = get_token(EMAIL, password)

            if response == 'connection error':
                ui.error_messages_SignupPage.setCurrentWidget(ui.message_no_connection_SignupPage)

            else:
                headers = {
                'Authorization': f'Token {TOKEN}'
                }
                data={
                    'verified' : True
                }

                try:
                    response = requests.patch(f'{config.ADDRESS}/api/subscription/change/', headers=headers, data=data)
                except:
                    ui.error_messages_SignupPage.setCurrentWidget(ui.message_no_connection_SignupPage)
                    return None

                if response.status_code == 200:
                    ui.new_password_input_ChangePasswordPage.setText('')
                    ui.password_repeat_ChangePasswordPage.setText('')
                    ui.error_messages_ChangePasswordPage.setCurrentWidget(ui.message_empty_ChangePasswordPage)

                    ui.IndexWindow.setCurrentWidget(ui.IndexPage)

                    ui.profile_button_IndexPage.setStyleSheet(menu_active_button_left)
                    ui.search_button_IndexPage.setStyleSheet(menu_button_mid)
                    ui.product_button_IndexPage.setStyleSheet(menu_button_right)


                    ui.AlgoritmWindow.setCurrentWidget(ui.ProfilePage)

                # на всякий случай (по идее, если нет ошибки соединения, то ответ всегда 200)
                else:
                    ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_no_connection_ChangePasswordPage)

        # перестраховка - если нет ошибки соединения, то ответ всегда должен быть 200
        else:
            ui.error_messages_ChangePasswordPage.setCurrentWidget(ui.message_no_connection_ChangePasswordPage)
    else:
        ui.error_messages_ChangePasswordPage.setCurrentWidget(ui.message_different_passwords_ChangePasswordPage)

# переход на страницу регистрации: чистим введенные данные и сбрасываем сообщения об ошибках
def proceed_to_SignupPage():
    clear_LoginPage()
    ui.email_input_SignupPage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.SignupPage)

# переход на страницу восстановления пароля: чистим данные, сбрасывме ошибки
def proceed_to_EnterEmailPage():
    clear_LoginPage()
    ui.email_input_EnterEmailPage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.EnterEmailPage)

# переход на страницу профиля:
def proceed_to_ProfilePage():
    ui.profile_button_IndexPage.setStyleSheet(menu_active_button_left)
    ui.search_button_IndexPage.setStyleSheet(menu_button_mid)
    ui.product_button_IndexPage.setStyleSheet(menu_button_right)
    ui.key_input_ProfilePage.setFocus()
    ui.AlgoritmWindow.setCurrentWidget(ui.ProfilePage)

# переход на страницу с рекламными кампаниями для поиска
def proceed_to_SearchPage():
    ui.profile_button_IndexPage.setStyleSheet(menu_button_left)
    ui.search_button_IndexPage.setStyleSheet(menu_active_button_mid)
    ui.product_button_IndexPage.setStyleSheet(menu_button_right)

    if datetime.datetime.strptime(EXPIRE_DATE, '%Y-%m-%d').date() < datetime.date.today():
        ui.menu_SearchPage.setCurrentWidget(ui.menu_subscribe_error_SearchPage)
    elif KEY == '':
        ui.menu_SearchPage.setCurrentWidget(ui.menu_key_error_SearchPage)
    else:
        ui.menu_SearchPage.setCurrentWidget(ui.menu_buttons_SearchPage)

    if len(button_group_search_products.buttons()) == 0 and checkboxes_search_products == []:
        ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_empty_SearchPage)
        ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)
    elif ui.settings_layout_SearchPage.count() == 0:
        ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)
    ui.AlgoritmWindow.setCurrentWidget(ui.SearchPage)

# переход на страницу с рекламными кампаниями для карточек товара
def proceed_to_ProductPage():
    ui.profile_button_IndexPage.setStyleSheet(menu_button_left)
    ui.search_button_IndexPage.setStyleSheet(menu_button_mid)
    ui.product_button_IndexPage.setStyleSheet(menu_active_button_right)

    if datetime.datetime.strptime(EXPIRE_DATE, '%Y-%m-%d').date() < datetime.date.today():
        ui.menu_ProductPage.setCurrentWidget(ui.menu_subscribe_error_ProductPage)
    elif KEY == '':
        ui.menu_ProductPage.setCurrentWidget(ui.menu_key_error_ProductPage)
    else:
        ui.menu_ProductPage.setCurrentWidget(ui.menu_buttons_ProductPage)

    if len(button_group_product_products.buttons()) == 0 and checkboxes_product_products == []:
        ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_empty_ProductPage)
        ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)
    elif ui.settings_layout_ProductPage.count() == 0:
        ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)
    ui.AlgoritmWindow.setCurrentWidget(ui.ProductPage)

# переход на страницу с изменением e-mail
def proceed_to_ChangeEmailPage():
    ui.verification_code__input_EmailConfirmPage.setText('')
    ui.error_messages_EmailConfirmPage.setCurrentWidget(ui.message_empty_EmailConfirmPage)
    reset_timer_verify()
    ui.email_input_ChangeEmailPage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.ChangeEmailPage)

# выходим на страницу входа (начальная страница приложения)
# отчищаем заполненные поля, обнуляем сообщения об ошибках
def exit_EnterEmailPage():
    ui.email_input_EnterEmailPage.setText('')
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)

def exit_SignupPage():
    ui.email_input_SignupPage.setText('')
    ui.password_input_SignupPage.setText('')
    ui.password_repeat_input_SignupPage.setText('')
    ui.error_messages_SignupPage.setCurrentWidget(ui.message_empty_SignupPage)
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)
  
def exit_ChangeEmailPage():
    ui.email_input_ChangeEmailPage.setText('')
    ui.error_messages_ChangeEmailPage.setCurrentWidget(ui.message_empty_ChangeEmailPage)
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)

def exit_ChangePasswordPage():
    ui.new_password_input_ChangePasswordPage.setText('')
    ui.password_repeat_ChangePasswordPage.setText('')
    ui.error_messages_ChangePasswordPage.setCurrentWidget(ui.message_empty_ChangePasswordPage)
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)
 
def exit_ConfirmChangePasswordPage():
    ui.verification_code_input_ConfirnChangePasswordPage.setText('')
    ui.error_messages_ConfirmPasswordChangePage.setCurrentWidget(ui.message_empty_ConfirmPasswordChangePage)
    reset_timer_ChangePassword()
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)

def logout():
    global KEY
    KEY=''
    
    clear_adverts_menu_SearchPage()
    clear_products_menu_SearchPage()
    clear_settings_SearchPage()
    clear_log_SearchPage()

    ui.key_input_ProfilePage.setPlaceholderText('')
    ui.email_input_loginpage.setFocus()
    ui.IndexWindow.setCurrentWidget(ui.LoginPage)

# функция, отвечающая за платеж - откомментировать!
def payment(amount, subscribe_plan):
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url" : "https://wildboost.ru"
        },
        "capture": True,
        "description": f"Оплата подписки с тарифом {subscribtion_plan[subscribe_plan]['name'].upper()}, на 1 месяц",
        "receipt": {
        "customer": {"email": EMAIL},
        "items":
            [{
              "description": f"Подписка WildBoost, тариф {subscribtion_plan[subscribe_plan]['name'].upper()}, 1 месяц",
              "quantity": "1",
              "amount": {
                "value": amount,
                "currency": "RUB"
              },
              "vat_code": "1"
            }]
        },
    }, uuid.uuid4())
    try:
        payment_url = payment.confirmation.confirmation_url
        payment_id = payment.id
    except:
        return 'Не удалось сгенерировать платеж'

    if payment_url and payment_id:
        headers = {
        'Authorization': f'Token {TOKEN}'
        }
        data={
            'payment_id' : payment_id,
            'payment_amount' : amount,
            'expire_date' : datetime.date.today() + datetime.timedelta(days = 31),
            'subscribe_plan' : subscribe_plan
        }
        threading.Thread(daemon=True, target=update_payment_status, args=(headers,data)).start()
        webbrowser.open_new_tab(payment_url)

def update_payment_status(headers, data):
    try:
        requests.post(f'{config.ADDRESS}/api/payment-status/', headers=headers, data=data)
    except:
        return None

# получение списка рекламных кампаний при вводе ключа
def get_adverts():
    # обновляем параметры подписки, задаем введенный ключ
    check_subscribtion_params()
    global KEY
    KEY = ui.key_input_ProfilePage.text().strip()

    # обнуляем сформированные ранее списки кампаний, удаляем их из виджета на странице поисковых кампаний
    clear_adverts_menu_SearchPage()
    
    # обнуляем свормированные ранее списки продуктов, удаляем их из виджета на странице поисковых кампаний
    clear_products_menu_SearchPage()

    # обнуляем сформированные ранее настройки, удаляем их из виджета на странтце поисковых кампаний
    clear_settings_SearchPage()

    # обнуляем сформированные ранее списки кампаний, удаляем их из виджета на странице кампаний в карточке
    clear_adverts_menu_ProductPage()
    
    # обнуляем свормированные ранее списки продуктов, удаляем их из виджета на странице кампаний в карточке
    clear_products_menu_ProductPage()

    # обнуляем сформированные ранее настройки, удаляем их из виджета на странцие кампаний в карточке
    clear_settings_ProductPage()

    # останавливаем рекламу в поиске
    stop_search_advert()

    stop_product_advert()

    # если введено значение ключа, стараемся подключиться по нему к WB
    if KEY != '':
        regex = r'[а-яА-Я]'
        symbols = re.findall(regex, KEY)
        # проверяем на отсутствие кириллицы (с ней падает)
        if symbols == []:
            ui.key_input_ProfilePage.setPlaceholderText('')
            headers_wb = {
                'Authorization': KEY,
            }
            params = {
                'order' : 'create',
            }
            url_wb = 'https://advert-api.wb.ru/adv/v0/adverts'

            
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params)
            # при ошибке соединения присваиваем ключу пустое значение, выводим сообщение об ошибке
            except requests.ConnectionError:
                KEY = ''
                ui.key_input_ProfilePage.setText('')
                ui.key_input_ProfilePage.setPlaceholderText('Ошибка соединения!')
                return None
            except:
                KEY = ''
                ui.key_input_ProfilePage.setText('')
                ui.key_input_ProfilePage.setPlaceholderText('Ошибка!')
                return None

            # если соединение установлено
            if response.status_code == 200:
                # и получен список кампаний, выдаем сообщение об успешной обработке ключа
                if response.json():
                    ui.key_input_ProfilePage.setText('')
                    ui.key_input_ProfilePage.setPlaceholderText('Токен сохранен до следующей авторизации!')
                    
                    # циклом обрабатываем каждую кампанию из списка
                    for advert in response.json():

                        advert_type = advert['type']
                        advert_id = advert['advertId']
                        advert_create = advert['createTime'][:10]
                        advert_status = advert['status']
                        advert_name = advert['name']

                        if advert_status == 11:
                            advert_word_status = 'приостановлена'
                        elif advert_status == 9:
                            advert_word_status = 'активна'
                        
                        # кампании для рекламы в поиске добавляем в соответствующие списки,
                        # учитываем тип подписки для выбора отображения чекбокса или "радио-кнопки"
                        if advert_type == 6 and (advert_status == 9 or advert_status == 11):
                            search_adverts_ids.append(advert_id)

                            if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
                                if len(button_group_search_adverts.buttons()) == 0:
                                    title = QLabel()
                                    title.setText('Выберите рекламную кампанию:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_SearchPage.addWidget(title)

                                radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), cоздана  {advert_create}, {advert_word_status}')
                                radio_button.setChecked(False)
                                radio_button.setObjectName(str(advert_name))
                                button_group_search_adverts.addButton(radio_button)
                                ui.adverts_layout_SearchPage.addWidget(radio_button)

                            else:
                                if checkboxes_search_adverts == []:
                                    title = QLabel()
                                    title.setText('Выберите рекламные кампании:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_SearchPage.addWidget(title)

                                checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                                checkbox.setChecked(False)
                                checkbox.setObjectName(str(advert_name))
                                checkboxes_search_adverts.append(checkbox)
                                ui.adverts_layout_SearchPage.addWidget(checkbox)

                        elif advert_type == 5 and (advert_status == 9 or advert_status == 11):
                            product_adverts_ids.append(advert_id)

                            if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
                                if len(button_group_product_adverts.buttons()) == 0:
                                    title = QLabel()
                                    title.setText('Выберите рекламную кампанию:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_ProductPage.addWidget(title)

                                radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                                radio_button.setChecked(False)
                                radio_button.setObjectName(str(advert_name))
                                button_group_product_adverts.addButton(radio_button)
                                ui.adverts_layout_ProductPage.addWidget(radio_button)

                            else:
                                if checkboxes_product_adverts == []:
                                    title = QLabel()
                                    title.setText('Выберите рекламные кампании:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_ProductPage.addWidget(title)

                                checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                                checkbox.setChecked(False)
                                checkbox.setObjectName(str(advert_name))
                                checkboxes_product_adverts.append(checkbox)
                                ui.adverts_layout_ProductPage.addWidget(checkbox)
                    
                    # если кампаний для рекламы в поиске не обнаружена - предупредим об этом пользователя
                    if checkboxes_search_adverts == [] and len(button_group_search_adverts.buttons()) == 0:
                        no_company_label = QLabel()
                        no_company_label.setText('Нет рекламных кампаний для поиска!')
                        no_company_label.setAlignment(Qt.AlignCenter)
                        ui.adverts_layout_SearchPage.addWidget(no_company_label)
                    
                    if checkboxes_product_adverts == [] and len(button_group_product_adverts.buttons()) == 0:
                        no_company_label = QLabel()
                        no_company_label.setText('Нет рекламных кампаний для карточки товара!')
                        no_company_label.setAlignment(Qt.AlignCenter)
                        ui.adverts_layout_ProductPage.addWidget(no_company_label) 

                # если json() пустой - значит, рекламных кампаний не создано, ставим пользователя в известность
                else:
                    ui.key_input_ProfilePage.setText('')
                    ui.key_input_ProfilePage.setPlaceholderText('   Cоздайте рекламную кампанию!')

                    no_company_label = QLabel()
                    no_company_label.setText('Нет рекламных кампаний для поиска!')
                    no_company_label.setAlignment(Qt.AlignCenter)
                    ui.adverts_layout_SearchPage.addWidget(no_company_label)
                    
                    no_company_label_product = QLabel()
                    no_company_label_product.setText('Нет рекламных кампаний для карточки товара!')
                    no_company_label_product.setAlignment(Qt.AlignCenter)
                    ui.adverts_layout_ProductPage.addWidget(no_company_label_product)

            #  если ответ не 200, значит ключ неверный, перезапишем его значение на пустую строку, уведоми пользователя
            else:
                KEY = ''
                ui.key_input_ProfilePage.setText('')
                ui.key_input_ProfilePage.setPlaceholderText('Введен неверный токен!')
                return None

        # если введенный ключ содержит кириллицу
        else:
            KEY = ''
            ui.key_input_ProfilePage.setText('')
            ui.key_input_ProfilePage.setPlaceholderText('Введен неверный токен!')
            return None

    # если поле для ввода ключа пустое, выводим сообщение о том, что его необходимо заполнить       
    else:
        ui.key_input_ProfilePage.setPlaceholderText('Введите токен от рекламного кабинета!')
        return None

# обновляем список рекламных кампаний для рекламы в поиске
def refresh_search_adverts():
    # обнуляем сформированные ранее списки кампаний, удаляем их из виджета на странице поисковых кампаний
    clear_adverts_menu_SearchPage()
    
    # обнуляем сформированные ранее списки продуктов, удаляем их из виджета на странице поисковых кампаний
    clear_products_menu_SearchPage()

    clear_settings_SearchPage()

    # останавливаем рекламу в поиске
    stop_search_advert()
    
    # убираем кнопки из под окна с продуктами и настройками
    ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_empty_SearchPage)
    ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)

    # если введено значение ключа, стараемся подключиться по нему к WB
    if KEY != '':
        ui.key_input_ProfilePage.setPlaceholderText('')
        headers_wb = {
            'Authorization': KEY,
        }
        params = {
            'order' : 'create',
        }
        url_wb = 'https://advert-api.wb.ru/adv/v0/adverts'

        
        try:
            response = requests.get(url_wb, headers=headers_wb, params=params)
        # при ошибке соединения предлагаем обновить повторно
        except:
            no_connection_label = QLabel()
            no_connection_label.setText('Не удалось установить соединение!')
            no_connection_label.setAlignment(Qt.AlignCenter)
            clear_adverts_menu_SearchPage()
            ui.adverts_layout_SearchPage.addWidget(no_connection_label)
            return None

        # если соединение установлено
        if response.status_code == 200:
            # и получен список кампаний
            if response.json():
                # циклом обрабатываем каждую кампанию из списка
                for advert in response.json():

                    advert_type = advert['type']
                    advert_id = advert['advertId']
                    advert_create = advert['createTime'][:10]
                    advert_status = advert['status']
                    advert_name = advert['name']

                    if advert_status == 11:
                        advert_word_status = 'приостановлена'
                    elif advert_status == 9:
                        advert_word_status = 'активна'
                    
                    # кампании для рекламы в поиске добавляем в соответствующие списки,
                    # учитываем тип подписки для выбора отображения чекбокса или "радио-кнопки"
                    if advert_type == 6  and (advert_status == 9 or advert_status == 11):
                        search_adverts_ids.append(advert_id)
                        if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
                            if len(button_group_search_adverts.buttons()) == 0:
                                    title = QLabel()
                                    title.setText('Выберите рекламную кампанию:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_SearchPage.addWidget(title)

                            radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                            radio_button.setChecked(False)
                            radio_button.setObjectName(str(advert_name))
                            button_group_search_adverts.addButton(radio_button)
                            ui.adverts_layout_SearchPage.addWidget(radio_button)
                        else:
                            if checkboxes_search_adverts == []:
                                    title = QLabel()
                                    title.setText('Выберите рекламные кампании:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_SearchPage.addWidget(title)

                            checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                            checkbox.setChecked(False)
                            checkbox.setObjectName(str(advert_name))
                            checkboxes_search_adverts.append(checkbox)
                            ui.adverts_layout_SearchPage.addWidget(checkbox)
                
                # если кампаний для рекламы в поиске не обнаружена - предупредим об этом пользователя
                if checkboxes_search_adverts == [] and len(button_group_search_adverts.buttons()) == 0:
                    no_company_label = QLabel()
                    no_company_label.setText('Нет рекламных кампаний для поиска!')
                    no_company_label.setAlignment(Qt.AlignCenter)
                    ui.adverts_layout_SearchPage.addWidget(no_company_label)

            # если json() пустой - значит, рекламных кампаний не создано, ставим пользователя в известность
            else:
                no_company_label = QLabel()
                no_company_label.setText('Нет рекламных кампаний для поиска!')
                no_company_label.setAlignment(Qt.AlignCenter)
                ui.adverts_layout_SearchPage.addWidget(no_company_label)
                ui.menu_adverts_setup_SearchPage.setCurrentWidget(ui.menu_adverts_setup_empty_SearchPage)

# обновляем список рекламных кампаний для рекламы в карточке
def refresh_product_adverts():
    # обнуляем сформированные ранее списки кампаний, удаляем их из виджета на странице поисковых кампаний
    clear_adverts_menu_ProductPage()
    
    # обнуляем сформированные ранее списки продуктов, удаляем их из виджета на странице поисковых кампаний
    clear_products_menu_ProductPage()

    clear_settings_ProductPage()

    stop_product_advert()
    
    # убираем кнопки из под окна с продуктами и настройками
    ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_empty_ProductPage)
    ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)

    # если введено значение ключа, стараемся подключиться по нему к WB
    if KEY != '':
        ui.key_input_ProfilePage.setPlaceholderText('')
        headers_wb = {
            'Authorization': KEY,
        }
        params = {
            'order' : 'create',
        }
        url_wb = 'https://advert-api.wb.ru/adv/v0/adverts'

        
        try:
            response = requests.get(url_wb, headers=headers_wb, params=params)
        # при ошибке соединения предлагаем обновить повторно
        except:
            no_connection_label = QLabel()
            no_connection_label.setText('Не удалось установить соединение!')
            no_connection_label.setAlignment(Qt.AlignCenter)
            clear_adverts_menu_ProductPage()
            ui.adverts_layout_ProductPage.addWidget(no_connection_label)
            return None

        # если соединение установлено
        if response.status_code == 200:
            # и получен список кампаний
            if response.json():
                # циклом обрабатываем каждую кампанию из списка
                for advert in response.json():

                    advert_type = advert['type']
                    advert_id = advert['advertId']
                    advert_create = advert['createTime'][:10]
                    advert_status = advert['status']
                    advert_name = advert['name']

                    if advert_status == 11:
                        advert_word_status = 'приостановлена'
                    elif advert_status == 9:
                        advert_word_status = 'активна'
                    
                    # кампании для рекламы в поиске добавляем в соответствующие списки,
                    # учитываем тип подписки для выбора отображения чекбокса или "радио-кнопки"
                    if advert_type == 5  and (advert_status == 9 or advert_status == 11):
                        product_adverts_ids.append(advert_id)
                        if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
                            if len(button_group_product_adverts.buttons()) == 0:
                                    title = QLabel()
                                    title.setText('Выберите рекламную кампанию:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_ProductPage.addWidget(title)

                            radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                            radio_button.setChecked(False)
                            radio_button.setObjectName(str(advert_name))
                            button_group_product_adverts.addButton(radio_button)
                            ui.adverts_layout_ProductPage.addWidget(radio_button)
                        else:
                            if checkboxes_product_adverts == []:
                                    title = QLabel()
                                    title.setText('Выберите рекламные кампании:')
                                    title.setAlignment(Qt.AlignmentFlag.AlignTop)
                                    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                    title.setMaximumHeight(15)
                                    ui.adverts_layout_ProductPage.addWidget(title)

                            checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {advert_word_status}')
                            checkbox.setChecked(False)
                            checkbox.setObjectName(str(advert_name))
                            checkboxes_product_adverts.append(checkbox)
                            ui.adverts_layout_ProductPage.addWidget(checkbox)
                
                # если кампаний для рекламы в поиске не обнаружена - предупредим об этом пользователя
                if checkboxes_product_adverts == [] and len(button_group_product_adverts.buttons()) == 0:
                    no_company_label = QLabel()
                    no_company_label.setText('Нет рекламных кампаний для рекламы в карточке товара!')
                    no_company_label.setAlignment(Qt.AlignCenter)
                    ui.adverts_layout_ProductPage.addWidget(no_company_label)

            # если json() пустой - значит, рекламных кампаний не создано, ставим пользователя в известность
            else:
                no_company_label = QLabel()
                no_company_label.setText('Нет рекламных кампаний для рекламы в карточке товара!')
                no_company_label.setAlignment(Qt.AlignCenter)
                ui.adverts_layout_ProductPage.addWidget(no_company_label)
                ui.menu_adverts_setup_ProductPage.setCurrentWidget(ui.menu_adverts_setup_empty_ProductPage)

# получаем список товаров для выбранных рекламных кампаний в поиске
def get_search_adverts_products():
    # обнуляем свормированные ранее списки продуктов, удаляем их из виджета на странице поисковых кампаний
    clear_products_menu_SearchPage()

    clear_settings_SearchPage()

    # останавливаем рекламу в поиске
    stop_search_advert()

    ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)

    regex = r'(?<=:)[0-9]*'
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_search_adverts.checkedButton()
        
        if checked_button:
            ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_confirm_SearchPage)
            advert_id = int(re.search(regex, checked_button.text()).group())
            advert_name = checked_button.objectName()

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)
            except:
                no_connection_label = QLabel()
                no_connection_label.setText('Не удалось установить соединение!')
                no_connection_label.setAlignment(Qt.AlignCenter)
                clear_products_menu_SearchPage()
                ui.product_layout_SearchPage.addWidget(no_connection_label)
                return None

            if response.status_code == 200:
                title = QLabel()
                title.setText('Выберите товарную группу:')
                title.setAlignment(Qt.AlignmentFlag.AlignTop)
                title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                title.setMaximumHeight(15)
                ui.product_layout_SearchPage.addWidget(title)

                products = response.json().get('params')
                for product in products:
                    product_id = product.get('subjectId')
                    product_name = product.get('subjectName')

                    radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), {product_name}')
                    radio_button.setChecked(False)
                    radio_button.setObjectName(str(product_id))
                    button_group_search_products.addButton(radio_button)
                    ui.product_layout_SearchPage.addWidget(radio_button)
            
            else:
                return None
                    
        else:
            ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_empty_SearchPage)
            return None

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_search_adverts if checkbox.isChecked()]

        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_empty_SearchPage)
            ui.menu_adverts_setup_SearchPage.setCurrentWidget(ui.menu_adverts_setup_amount_error_SearchPage)
            return None

        if checked_boxes != []:
            ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_confirm_SearchPage)
            for num, checkbox in enumerate(checked_boxes):
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_name = checkbox.objectName()

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)
                except:
                    no_connection_label = QLabel()
                    no_connection_label.setText('Не удалось установить соединение!')
                    no_connection_label.setAlignment(Qt.AlignCenter)
                    clear_products_menu_SearchPage()
                    ui.product_layout_SearchPage.addWidget(no_connection_label)
                    return None

                if response.status_code == 200:
                    if num == 0:
                        title = QLabel()
                        title.setText('Выберите товарные группы:')
                        title.setAlignment(Qt.AlignmentFlag.AlignTop)
                        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        title.setMaximumHeight(15)
                        ui.product_layout_SearchPage.addWidget(title)

                    products = response.json().get('params')
                    for product in products:
                        product_id = product.get('subjectId')
                        product_name = product.get('subjectName')

                        checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {product_name}')
                        checkbox.setChecked(False)
                        checkbox.setObjectName(str(product_id))
                        checkboxes_search_products.append(checkbox)
                        ui.product_layout_SearchPage.addWidget(checkbox)
            
                else:
                    return None
                
                
        else:
            ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_empty_SearchPage)
            return None

# получаем список товаров для выбранных рекламных кампаний в карточке
def get_product_adverts_products():

    # обнуляем свормированные ранее списки продуктов, удаляем их из виджета на странице поисковых кампаний
    clear_products_menu_ProductPage()

    clear_settings_ProductPage()

    stop_product_advert()

    ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)

    regex = r'(?<=:)[0-9]*'
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_product_adverts.checkedButton()
        
        if checked_button:
            ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_confirm_ProductPage)
            advert_id = int(re.search(regex, checked_button.text()).group())
            advert_name = checked_button.objectName()

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)
            except:
                return None

            if response.status_code == 200:
                title = QLabel()
                title.setText('Выберите товарную группу:')
                title.setAlignment(Qt.AlignmentFlag.AlignTop)
                title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                title.setMaximumHeight(15)
                ui.product_layout_ProductPage.addWidget(title)

                products = response.json().get('params')
                for product in products:
                    product_id = product.get('setId')
                    product_name = product.get('setName').lower()
                    product_article = product.get('nms')[0].get('nm')

                    radio_button = QRadioButton(f'{advert_name} (ID:{advert_id}), {product_name}')
                    radio_button.setChecked(False)
                    radio_button.setObjectName(f'{product_id}, {product_article}')
                    button_group_product_products.addButton(radio_button)
                    ui.product_layout_ProductPage.addWidget(radio_button)
            
            else:
                no_connection_label = QLabel()
                no_connection_label.setText('Не удалось установить соединение!')
                no_connection_label.setAlignment(Qt.AlignCenter)
                clear_products_menu_ProductPage()
                ui.product_layout_ProductPage.addWidget(no_connection_label)
                return None
                    
        else:
            ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_empty_ProductPage)
            return None

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_product_adverts if checkbox.isChecked()]

        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_empty_ProductPage)
            ui.menu_adverts_setup_ProductPage.setCurrentWidget(ui.menu_adverts_setup_amount_error_ProductPage)
            return None

        if checked_boxes != []:
            ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_confirm_ProductPage)
            for num, checkbox in enumerate(checked_boxes):
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_name = checkbox.objectName()

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)
                except:
                    no_connection_label = QLabel()
                    no_connection_label.setText('Не удалось установить соединение!')
                    no_connection_label.setAlignment(Qt.AlignCenter)
                    clear_products_menu_ProductPage()
                    ui.product_layout_ProductPage.addWidget(no_connection_label)
                    return None

                if response.status_code == 200:
                    if num == 0:
                        title = QLabel()
                        title.setText('Выберите товарные группы:')
                        title.setAlignment(Qt.AlignmentFlag.AlignTop)
                        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        title.setMaximumHeight(15)
                        ui.product_layout_ProductPage.addWidget(title)

                    products = response.json().get('params')
                    for product in products:
                        product_id = product.get('setId')
                        product_name = product.get('setName').lower()
                        product_article = product.get('nms')[0].get('nm')

                        checkbox = QCheckBox(f'{advert_name} (ID:{advert_id}), {product_name}')
                        checkbox.setChecked(False)
                        checkbox.setObjectName(f'{product_id}, {product_article}')
                        checkboxes_product_products.append(checkbox)
                        ui.product_layout_ProductPage.addWidget(checkbox)
            
                else:
                    return None
                
                
        else:
            ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_empty_ProductPage)
            return None

# формируем экран настроек программы для рекламной кампании в поиске
def get_search_settings():

    clear_settings_SearchPage()

    # останавливаем рекламу в поиске
    stop_search_advert()

    regex = r'(?<=:)[0-9]*'
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_search_products.checkedButton()
        if checked_button:
            ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_start_SearchPage)
            advert_id = re.search(regex, checked_button.text()).group()
            product_group_id = checked_button.objectName()

            title = QLabel()
            title.setText('Задайте настройки:')
            title.setAlignment(Qt.AlignmentFlag.AlignTop)
            title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title.setMaximumHeight(15)
            ui.settings_layout_SearchPage.addWidget(title)

            layout_name = QHBoxLayout()

            name = QLabel()
            name.setText(checked_button.text())
            name.setObjectName(product_group_id)
            product_group_settings.append(name)

            max_price = QSpinBox()
            max_price.setMinimum(40)
            max_price.setMaximum(10000)
            max_price.setMinimumHeight(37)
            max_price.setSingleStep(10)
            max_price.setPrefix('₽')
            max_price.setSuffix(' макс. цена')
            max_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            max_price_settings.append(max_price)

            layout_name.addWidget(name)
            layout_name.addWidget(max_price)

            key_word = QLineEdit()
            key_word.setPlaceholderText('Введите ключевое слово для группы товаров.')
            key_word.setMinimumHeight(37)
            key_word_settings.append(key_word)

            layout_MaxMinPlace = QHBoxLayout()
            text_max = QLabel()
            text_max.setText('Макс. место')

            place_max = QSpinBox()
            place_max.setMaximum(10)
            place_max.setMinimum(1)
            place_max.setMinimumHeight(37)
            place_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            place_max_settings.append(place_max)

            text_min = QLabel()
            text_min.setText('Мин. место')

            place_min = QSpinBox()
            place_min.setMaximum(10)
            place_min.setMinimum(1)
            place_min.setValue(10)
            place_min.setMinimumHeight(37)
            place_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            place_min_settings.append(place_min)

            layout_MaxMinPlace.addWidget(text_max)
            layout_MaxMinPlace.addWidget(place_max)
            layout_MaxMinPlace.addWidget(text_min)
            layout_MaxMinPlace.addWidget(place_min)

            ui.settings_layout_SearchPage.addLayout(layout_name)
            ui.settings_layout_SearchPage.addWidget(key_word)
            ui.settings_layout_SearchPage.addLayout(layout_MaxMinPlace)
                    
        else:
            ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)
            return None

    else:

        checkbox_dict = {}
        for checkbox in checkboxes_search_products:
            advert_id = re.search(regex, checkbox.text()).group()
            product_group_id = checkbox.objectName()
            if advert_id not in checkbox_dict:
                checkbox_dict[advert_id] = [product_group_id]
            else:
                checkbox_dict[advert_id].append(product_group_id)
        
        for value in checkbox_dict.values():
            if len(value) > subscribtion_plan[SUBSCRIBE_PLAN]['products']:
                ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)
                ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_amount_error_SearchPage)
                return None
            else:
                pass

        checked_boxes = [checkbox for checkbox in checkboxes_search_products if checkbox.isChecked()]

        if checked_boxes != []:
            title = QLabel()
            title.setText('Задайте настройки:')
            title.setAlignment(Qt.AlignmentFlag.AlignTop)
            title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title.setMaximumHeight(15)
            ui.settings_layout_SearchPage.addWidget(title)

            for num, checkbox in enumerate(checked_boxes):

                ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_start_SearchPage)
                product_group_id = checkbox.objectName()

                layout_name = QHBoxLayout()
                name = QLabel()
                name.setText(f'{num +1}. {checkbox.text()}')
                name.setObjectName(product_group_id)
                product_group_settings.append(name)

                max_price = QSpinBox()
                max_price.setMinimum(40)
                max_price.setMaximum(10000)
                max_price.setMinimumHeight(37)
                max_price.setSingleStep(10)
                max_price.setPrefix('₽')
                max_price.setSuffix(' макс. цена')
                max_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                max_price_settings.append(max_price)

                layout_name.addWidget(name)
                layout_name.addWidget(max_price)

                key_word = QLineEdit()
                key_word.setPlaceholderText('Введите ключевое слово для группы товаров.')
                key_word.setMinimumHeight(37)
                key_word_settings.append(key_word)

                layout_MaxMinPlace = QHBoxLayout()
                text_max = QLabel()
                text_max.setText('Макс. место')
                place_max = QSpinBox()
                place_max.setMaximum(10)
                place_max.setMinimum(1)
                place_max.setMinimumHeight(37)
                place_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                place_max_settings.append(place_max)

                text_min = QLabel()
                text_min.setText('Мин. место')
                place_min = QSpinBox()
                place_min.setMaximum(10)
                place_min.setMinimum(1)
                place_min.setMinimumHeight(37)
                place_min.setValue(10)
                place_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                place_min_settings.append(place_min)

                layout_MaxMinPlace.addWidget(text_max)
                layout_MaxMinPlace.addWidget(place_max)
                layout_MaxMinPlace.addWidget(text_min)
                layout_MaxMinPlace.addWidget(place_min)

                line = QFrame()
                line.setFrameStyle(QFrame.HLine)
                line.setStyleSheet('QFrame {background:#B4B5B8; border:none;}')
                line.setMaximumHeight(1)

                ui.settings_layout_SearchPage.addLayout(layout_name)
                ui.settings_layout_SearchPage.addWidget(key_word)
                ui.settings_layout_SearchPage.addLayout(layout_MaxMinPlace)
                ui.settings_layout_SearchPage.addWidget(line)
                           
        else:
            ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_empty_SearchPage)
            return None

# формируем экран настроек программы для рекламной кампании в карточке
def get_product_settings():

    clear_settings_ProductPage()

    stop_product_advert()

    regex = r'(?<=:)[0-9]*'
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_product_products.checkedButton()
        if checked_button:
            ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_start_ProductPage)
            advert_id = re.search(regex, checked_button.text()).group()
            product_group_id = checked_button.objectName().split(', ')[0]

            title = QLabel()
            title.setText('Задайте настройки:')
            title.setAlignment(Qt.AlignmentFlag.AlignTop)
            title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title.setMaximumHeight(15)
            ui.settings_layout_ProductPage.addWidget(title)

            layout_name = QHBoxLayout()

            name = QLabel()
            name.setText(checked_button.text())
            name.setObjectName(checked_button.objectName())
            product_group_settings_product.append(name)

            max_price = QSpinBox()
            max_price.setMinimum(40)
            max_price.setMaximum(10000)
            max_price.setMinimumHeight(37)
            max_price.setSingleStep(10)
            max_price.setPrefix('₽')
            max_price.setSuffix(' макс. цена')
            max_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            max_price_settings_product.append(max_price)

            layout_name.addWidget(name)
            layout_name.addWidget(max_price)

            layout_MaxMinPlace = QHBoxLayout()
            text_max = QLabel()
            text_max.setText('Макс. место')

            place_max = QSpinBox()
            place_max.setMaximum(10)
            place_max.setMinimum(1)
            place_max.setMinimumHeight(37)
            place_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            place_max_settings_product.append(place_max)

            text_min = QLabel()
            text_min.setText('Мин. место')

            place_min = QSpinBox()
            place_min.setMaximum(10)
            place_min.setMinimum(1)
            place_min.setValue(10)
            place_min.setMinimumHeight(37)
            place_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            place_min_settings_product.append(place_min)

            layout_MaxMinPlace.addWidget(text_max)
            layout_MaxMinPlace.addWidget(place_max)
            layout_MaxMinPlace.addWidget(text_min)
            layout_MaxMinPlace.addWidget(place_min)

            ui.settings_layout_ProductPage.addLayout(layout_name)
            ui.settings_layout_ProductPage.addLayout(layout_MaxMinPlace)
                    
        else:
            ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)
            return None

    else:

        checkbox_dict = {}
        for checkbox in checkboxes_product_products:
            advert_id = re.search(regex, checkbox.text()).group()
            product_group_id = checkbox.objectName().split(', ')[0]
            if advert_id not in checkbox_dict:
                checkbox_dict[advert_id] = [product_group_id]
            else:
                checkbox_dict[advert_id].append(product_group_id)
        
        for value in checkbox_dict.values():
            if len(value) > subscribtion_plan[SUBSCRIBE_PLAN]['products']:
                ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)
                ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_amount_error_ProductPage)
                return None
            else:
                pass

        checked_boxes = [checkbox for checkbox in checkboxes_product_products if checkbox.isChecked()]

        if checked_boxes != []:
            title = QLabel()
            title.setText('Задайте настройки:')
            title.setAlignment(Qt.AlignmentFlag.AlignTop)
            title.setAlignment(Qt.AlignmentFlag.AlignCenter)
            title.setMaximumHeight(15)
            ui.settings_layout_ProductPage.addWidget(title)

            for num, checkbox in enumerate(checked_boxes):

                ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_start_ProductPage)
                product_group_id = checkbox.objectName().split(', ')[0]

                layout_name = QHBoxLayout()
                name = QLabel()
                name.setText(f'{num +1}. {checkbox.text()}')
                name.setObjectName(checkbox.objectName())
                product_group_settings_product.append(name)

                max_price = QSpinBox()
                max_price.setMinimum(40)
                max_price.setMaximum(10000)
                max_price.setMinimumHeight(37)
                max_price.setSingleStep(10)
                max_price.setPrefix('₽')
                max_price.setSuffix(' макс. цена')
                max_price.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                max_price_settings_product.append(max_price)

                layout_name.addWidget(name)
                layout_name.addWidget(max_price)

                layout_MaxMinPlace = QHBoxLayout()
                text_max = QLabel()
                text_max.setText('Макс. место')
                place_max = QSpinBox()
                place_max.setMaximum(10)
                place_max.setMinimum(1)
                place_max.setMinimumHeight(37)
                place_max.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                place_max_settings_product.append(place_max)

                text_min = QLabel()
                text_min.setText('Мин. место')
                place_min = QSpinBox()
                place_min.setMaximum(10)
                place_min.setMinimum(1)
                place_min.setMinimumHeight(37)
                place_min.setValue(10)
                place_min.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                place_min_settings_product.append(place_min)

                layout_MaxMinPlace.addWidget(text_max)
                layout_MaxMinPlace.addWidget(place_max)
                layout_MaxMinPlace.addWidget(text_min)
                layout_MaxMinPlace.addWidget(place_min)

                line = QFrame()
                line.setFrameStyle(QFrame.HLine)
                line.setStyleSheet('QFrame {background:#B4B5B8; border: none;}')
                line.setMaximumHeight(1)

                ui.settings_layout_ProductPage.addLayout(layout_name)
                ui.settings_layout_ProductPage.addLayout(layout_MaxMinPlace)
                ui.settings_layout_ProductPage.addWidget(line)
                
        else:
            ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_empty_ProductPage)
            return None

# получаем информацию по промо-товарам, в соответствии с запросом
async def get_advertisers(request):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    async with ClientSession() as session:
        url = f'https://catalog-ads.wildberries.ru/api/v5/search?keyword={request}'
        try:
            async with session.get(url=url, headers=headers, ssl=ssl_context) as response:
                response = await response.json()
        except:
            advertisers = 'connection error'
            return advertisers

        try:
            result = response['adverts']
            position_on_page = response['pages'][0]['positions']
        except:
            advertisers = 'not valid search'
            return advertisers

        if result and position_on_page:
            advertisers = []
            for position, product in enumerate(result):
                if position <= 9:
                    advertisers.append([product['advertId'], product['cpm'], position_on_page[position]])
                else:
                    advertisers.append([product['advertId'], product['cpm']])
            return advertisers
        else:
            advertisers = 'not valid search'
            return advertisers

# получаем текущую ставку по группе товаро
async def get_current_price(advert_id, sub_id):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
    params_wb = {
        'id' : advert_id
    }
    headers_wb = {
        'Authorization': KEY,
    }
    async with ClientSession() as session:
        try:
            async with session.get(url=url_wb, headers=headers_wb, params=params_wb, ssl=ssl_context) as response:
                response = await response.json()
        except:
            current_price = 'connection error'
            return current_price

        try:
            response = response['params']
        except:
            current_price = 'failed to get price'
            return current_price
        
        for subId in response:
            if subId['subjectId'] == sub_id:
                current_price = subId['price']
                return current_price
        current_price = 'failed to get price'
        return current_price

# меняем цену
async def change_price_wb(advert_id, sub_id, new_price):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    headers_wb = {
        'Authorization': KEY,
    }
    url_wb = 'https://advert-api.wb.ru/adv/v0/cpm'
    params_wb = {
        "advertId" : advert_id,
        "type" : 6,
        "cpm" : new_price,
        "param" : sub_id,
    }
    async with ClientSession() as session:
        try:
            async with session.post(url=url_wb, headers=headers_wb, json=params_wb, ssl=ssl_context) as response:
                result = await response.text()
        except:
            result = 'connection error'
            return result

        if response.status == 200:
            return 200
        else:
            return 'error'

# собираем информацию для принятия решения о смене цены, обрабатываем результаты
async def change_price(advert_data):
    name = advert_data[0]
    advert_id = advert_data[1]
    sub_id = advert_data[2]
    key_word = advert_data[3]
    group_name = advert_data[4]
    place_max = advert_data[5]
    place_min = advert_data[6]
    price_max = advert_data[7]
    using_key_word = False
    if key_word != '':
        using_key_word = True
        task_adv = asyncio.create_task(get_advertisers(key_word))
        advertisers = await asyncio.gather(task_adv)

        if not isinstance(advertisers[0], list):
            using_key_word = False
            task_adv = asyncio.create_task(get_advertisers(group_name))
            advertisers = await asyncio.gather(task_adv)

    else:
        task_adv = asyncio.create_task(get_advertisers(group_name))
        advertisers = await asyncio.gather(task_adv)

    task_price = asyncio.create_task(get_current_price(advert_id, sub_id))
    current_price = await asyncio.gather(task_price)

    advertisers = advertisers[0]
    current_price = current_price[0]

    if isinstance(advertisers, list) and isinstance(current_price, int):
        only_prices = []
        pages_positions = []

        for advertiser in advertisers:
            if advertiser[0] not in search_adverts_ids:
                only_prices.append(int(advertiser[1]))
            if len(advertiser) > 2:
                pages_positions.append(advertiser[2])
        new_price = 0
        page_position = 0
        for position, price in enumerate(only_prices):
            position += 1
            if (place_max <= position <= place_min) and (price + 1 <= price_max):
                new_price = price + 1
                try:
                    page_position = pages_positions[position - 1]
                except:
                    page_position = 0
                break
        
        if new_price == 0:
            new_price = 40
            position = len(only_prices)
            if position > 10:
                page_position = 0
            else:
                try:
                    page_position = pages_positions[position - 1]
                except:
                    page_position = 0
        
        prices = copy(only_prices)
        prices.append(current_price)
        prev_position = sorted(prices, reverse=True).index(current_price) + 1

        if page_position != 0:
            position_text = f'позиция на первой странице: {page_position}'
        else:
            position_text = 'позиция за пределами первой страницы'

        if using_key_word:
            query_text = f'Поиск по ключевому слову: "{key_word}"'
        else:
            query_text = f'Поиск по названию группы товаров: "{group_name}"'

        if new_price != current_price:

            task = asyncio.create_task(change_price_wb(advert_id, sub_id, new_price))
            result = await asyncio.gather(task)
            result = result[0]

            if isinstance(result, int):
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}). {query_text}.\
                              \n\
                              \nНовая цена: {new_price}, позиция в аукционе: {position}, {position_text}.\
                              \nПредыдущая цена: {current_price}, предыдущая позиция в аукционе: {prev_position}.\
                              \nАукцион (первые 10 ставок): {only_prices[:10]}'''

                signal.result.emit((log_text, 90))
   
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}). {query_text}.\
                                \n\
                                \nНе удалось изменить цену на: {new_price} - сбой в подключении к Wildberries.\
                                \nЦена не изменена: {current_price}, текущая позиция в аукционе: {prev_position}.\
                                \nАукцион (первые 10 ставок): {only_prices[:10]}'''

                signal.result_wrong.emit((log_text, 90))

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}). {query_text}.\
                            \n\
                            \nЦена не изменена: {current_price}, текущая позиция: {prev_position}, {position_text}.\
                            \nАукцион (первые 10 ставок): {only_prices[:10]}'''
            
            signal.result.emit((log_text, 70))

    else:
        if ('connection' in advertisers):
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nСбой подключения к серверу - проверьте интернет соединение. Если Ваше интернет соединение активно - сбой на стороне Wildberries.'''
            signal.result_error.emit((log_text, 55))
            
        elif 'not valid' in advertisers:
            
            if key_word == '':
                error_text = f'''Не удалось определить ставки аукциона по названию группы товаров: "{group_name}".\
                            \nКлючевое слово указано не было. Если проблема повторяется, укажите ключево слово для группы товаров.'''
            else:
                error_text = f'''Не удалось определить ставки аукциона по названию группы товаров: "{group_name}" и ключевому слову "{key_word}".\
                            \nЕсли проблема повторяется, проверьте корректность введенного ключевого слова.'''

            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \n{error_text}'''

            signal.result_wrong.emit((log_text, 70))
            
        elif 'failed' in current_price:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nНе удалось определить текущую ставку по группе товаров. Если проблема носит регулярный характер - перезапустите программу.'''

            signal.result_wrong.emit((log_text, 55))
            
        elif 'connection' in current_price:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nСбой подключения к серверу - проверьте интернет соединение. Если Ваше интернет соединение активно - сбой на стороне Wildberries.'''

            signal.result_error.emit((log_text, 55))     

# формируем задачи для выполнения запросов
async def run_settings(requests_search):
    tasks = []
    for request in requests_search:
        tasks.append(asyncio.create_task(change_price(request)))

    for task in tasks:
        await task

def func_wrap(settings):
    exit_event = threading.Event()
    stop_search_events.append(exit_event)

    start_date = ''

    while True:
        if start_date != datetime.date.today() or start_date == '':
            check_subscribtion_params()
            start_date = datetime.date.today()

        if datetime.datetime.strptime(EXPIRE_DATE, '%Y-%m-%d').date() < datetime.date.today():
            signal.subscription_expired.emit()
            break

        if exit_event.is_set():
            break

        asyncio.run(run_settings(settings))

        if exit_event.is_set():
            break

        time.sleep(subscribtion_plan[SUBSCRIBE_PLAN]['renew']*60)

# стартуем настройку аукциона для рекламной кампании в поиске
def start_search_advert():

    place_max_clear = []
    place_min_clear = []
    for num in range(len(place_max_settings)):
        place_max = place_max_settings[num].value()
        place_min = place_min_settings[num].value()
        if place_max <= place_min:
            place_max_clear.append(place_max)
            place_min_clear.append(place_min)
        else:
            ui.error_label_settings_SearchPage.setText(f'Ошибка в диапазоне мест, пункт {num+1}')
            ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_error_SearchPage)
            return None

    max_price_clear = []
    for max_price in max_price_settings:
        max_price_clear.append(max_price.value())

    key_word_clear = []
    regex = r'[а-яА-Я|\s|-]*'
    for key_word in key_word_settings:
        key_word = re.fullmatch(regex, key_word.text())
        if key_word:
            key_word = ' '.join(key_word.group().strip(' ').split()).lower().replace('ё ', 'е')
            key_word_clear.append(key_word)
        else:
            key_word_clear.append('')
    
    advert_id_clear = []
    product_group_id_clear = []
    product_group_name_clear = []
    name_clear = []
    regex = r'(?<=:)[0-9]*'
    for product_group in product_group_settings:
        name_clear.append(product_group.text())
        product_group_id_clear.append(int(product_group.objectName()))
        advert_id = int(re.search(regex, product_group.text()).group())
        advert_id_clear.append(advert_id)
        product_name = product_group.text().split(', ')[1]
        product_group_name_clear.append(product_name)

    bidder_settings_search = []
    for num in range(len(advert_id_clear)):
            bidder_settings_search.append(
                (name_clear[num], 
                advert_id_clear[num],
                product_group_id_clear[num],
                key_word_clear[num],
                product_group_name_clear[num],
                place_max_clear[num],
                place_min_clear[num],
                max_price_clear[num])
                )

    signal.start_or_stop.emit(f'''WildBoost запущен ({time.strftime('%d %B %H:%M:%S', time.localtime())}):''')
    ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_stop_SearchPage)
    ui.scrollArea_log.setStyleSheet('''QScrollArea {
                                background: white;
                                border: 1px solid #B4B5B8;
                                border-radius:6px;
                                }'''
                                )
    
    threading.Thread(daemon=True, target=func_wrap, args=(bidder_settings_search,)).start()

# получаем информацию по товарам, рекламирующимся в карточке
async def get_advertisers_product(article):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    async with ClientSession() as session:
        url = f'https://carousel-ads.wildberries.ru/api/v4/carousel?nm={article}'
        try:
            async with session.get(url=url, headers=headers, ssl=ssl_context) as response:
                response = await response.json()
        except:
            advertisers = 'connection error'
            return advertisers

        try:
            advertisers = []
            for product in response:
                advertisers.append([product['advertId'], product['cpm']])
            return advertisers
        except:
            return 'not valid search'

# получаем текущую ставку по группе товаров (реклама в карточке)
async def get_current_price_product(advert_id, sub_id):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    url_wb = 'https://advert-api.wb.ru/adv/v0/advert'
    params_wb = {
        'id' : advert_id
    }
    headers_wb = {
        'Authorization': KEY,
    }
    async with ClientSession() as session:
        try:
            async with session.get(url=url_wb, headers=headers_wb, params=params_wb, ssl=ssl_context) as response:
                response = await response.json()
        except:
            current_price = 'connection error'
            return current_price

        try:
            response = response['params']
        except:
            current_price = 'failed to get price'
            return current_price
        
        for subId in response:
            if subId['setId'] == sub_id:
                current_price = subId['price']
                return current_price
        current_price = 'failed to get price'
        return current_price

# меняем цену
async def change_price_wb_product(advert_id, sub_id, new_price):
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(certifi.where())
    headers_wb = {
        'Authorization': KEY,
    }
    url_wb = 'https://advert-api.wb.ru/adv/v0/cpm'
    params_wb = {
        "advertId" : advert_id,
        "type" : 5,
        "cpm" : new_price,
        "param" : sub_id,
    }
    async with ClientSession() as session:
        try:
            async with session.post(url=url_wb, headers=headers_wb, json=params_wb, ssl=ssl_context) as response:
                result = await response.text()
        except:
            result = 'connection error'
            return result

        if response.status == 200:
            return 200
        else:
            return 'error'

# собираем информацию для принятия решения о смене цены, обрабатываем результаты
async def change_price_product(advert_data):
    name = advert_data[0]
    advert_id = advert_data[1]
    sub_id = advert_data[2]
    article = advert_data[3]
    place_max = advert_data[4]
    place_min = advert_data[5]
    price_max = advert_data[6]

    task_adv = asyncio.create_task(get_advertisers_product(article))
    advertisers = await asyncio.gather(task_adv)

    task_price = asyncio.create_task(get_current_price_product(advert_id, sub_id))
    current_price = await asyncio.gather(task_price)

    advertisers = advertisers[0]
    current_price = current_price[0]

    if isinstance(advertisers, list) and isinstance(current_price, int):
        only_prices = []

        for advertiser in advertisers:
            if advertiser[0] not in product_adverts_ids:
                only_prices.append(int(advertiser[1]))
        
        new_price = 0
        for position, price in enumerate(only_prices):
            position += 1
            if (place_max <= position <= place_min) and (price + 1 <= price_max):
                new_price = price + 1
                break

        
        if new_price == 0:
            new_price = 40
            prices_now = copy(only_prices)
            prices_now.append(new_price)
            position = sorted(prices_now, reverse=True).index(new_price) + 1

        
        prices = copy(only_prices)
        prices.append(current_price)
        prev_position = sorted(prices, reverse=True).index(current_price) + 1

        if new_price != current_price:

            task = asyncio.create_task(change_price_wb_product(advert_id, sub_id, new_price))
            result = await asyncio.gather(task)
            result = result[0]

            if isinstance(result, int):
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                              \n\
                              \nНовая цена: {new_price}, позиция в аукционе: {position}.\
                              \nПредыдущая цена: {current_price}, предыдущая позиция в аукционе: {prev_position}.\
                              \nАукцион: {only_prices[:10]}'''

                signal.result_product.emit((log_text, 90))
   
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                                \n\
                                \nНе удалось изменить цену на: {new_price} - сбой в подключении к Wildberries.\
                                \nЦена не изменена: {current_price}, текущая позиция в аукционе: {prev_position}.\
                                \nАукцион: {only_prices[:10]}'''

                signal.result_wrong_product.emit((log_text, 90))

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nЦена не изменена: {current_price}, текущая позиция: {prev_position}.\
                            \nАукцион: {only_prices[:10]}'''
            
            signal.result_product.emit((log_text, 70))

    else:
        if ('connection' in advertisers):
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nСбой подключения к серверу - проверьте интернет соединение. Если Ваше интернет соединение активно - сбой на стороне Wildberries.'''
            signal.result_error_product.emit((log_text, 55))
            
        elif 'not valid' in advertisers:

            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nНе удалось определить ставки аукциона по артикулу: {article}. Если проблема повторяется - проверьте корректность введеного артикула.'''

            signal.result_wrong_product.emit((log_text, 55))
            
        elif 'failed' in current_price:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nНе удалось определить текущую ставку по группе товаров. Если проблема носит регулярный характер - перезапустите программу.'''

            signal.result_wrong_product.emit((log_text, 55))
            
        elif 'connection' in current_price:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())} ({name}).\
                            \n\
                            \nСбой подключения к серверу - проверьте интернет соединение. Если Ваше интернет соединение активно - сбой на стороне Wildberries.'''

            signal.result_error_product.emit((log_text, 55)) 

# формируем задачи для выполнения запросов
async def run_settings_product(requests_search):
    tasks = []
    for request in requests_search:
        tasks.append(asyncio.create_task(change_price_product(request)))

    for task in tasks:
        await task

def func_wrap_product(settings):
    exit_event = threading.Event()
    stop_product_events.append(exit_event)

    start_date = ''

    while True:
        if start_date != datetime.date.today() or start_date == '':
            check_subscribtion_params()
            start_date = datetime.date.today()

        if datetime.datetime.strptime(EXPIRE_DATE, '%Y-%m-%d').date() < datetime.date.today():
            signal.subscription_expired.emit()
            break

        if exit_event.is_set():
            break

        asyncio.run(run_settings_product(settings))

        if exit_event.is_set():
            break

        time.sleep(subscribtion_plan[SUBSCRIBE_PLAN]['renew']*60)

# стартуем настройку аукциона для рекламной кампании в карточке
def start_product_advert():

    place_max_clear = []
    place_min_clear = []
    for num in range(len(place_max_settings_product)):
        place_max = place_max_settings_product[num].value()
        place_min = place_min_settings_product[num].value()
        if place_max <= place_min:
            place_max_clear.append(place_max)
            place_min_clear.append(place_min)
        else:
            ui.error_label_settings_ProductPage.setText(f'Ошибка в диапазоне мест, пункт {num+1}')
            ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_error_ProductPage)
            return None

    max_price_clear = []
    for max_price in max_price_settings_product:
        max_price_clear.append(max_price.value())
    
    advert_id_clear = []
    product_group_id_clear = []
    name_clear = []
    articles_clear = []
    regex = r'(?<=:)[0-9]*'
    for product_group in product_group_settings_product:
        name_clear.append(product_group.text())

        product_group_id_clear.append(int(product_group.objectName().split(', ')[0]))
        articles_clear.append(int(product_group.objectName().split(', ')[1]))

        advert_id = int(re.search(regex, product_group.text()).group())
        advert_id_clear.append(advert_id)

    bidder_settings_product = []
    for num in range(len(advert_id_clear)):
            bidder_settings_product.append(
                (name_clear[num], 
                advert_id_clear[num],
                product_group_id_clear[num],
                articles_clear[num],
                place_max_clear[num],
                place_min_clear[num],
                max_price_clear[num],)
                )

    signal.start_or_stop_product.emit(f'''WildBoost запущен ({time.strftime('%d %B %H:%M:%S', time.localtime())}):''')
    ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_stop_ProductPage)
    ui.scrollArea_log_ProductPage.setStyleSheet('''QScrollArea {
                                background: white;
                                border: 1px solid #B4B5B8;
                                border-radius:6px;
                                }'''
                                )

    threading.Thread(daemon=True, target=func_wrap_product, args=(bidder_settings_product,)).start()

# останавливаем программу для установки цен в рекламных кампаниях поиска
def stop_search_advert():
    if stop_search_events != []:
        stop_search_events[-1].set()
        stop_search_events.pop()
        signal.start_or_stop.emit(f'''WildBoost остановлен ({time.strftime('%d %B %H:%M:%S', time.localtime())}).''')
        ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_start_SearchPage)

        ui.scrollArea_log.setStyleSheet('''QScrollArea {
                                background: #F5F5F5;
                                border: 1px solid #B4B5B8;
                                border-radius:6px;
                                }'''
                                )

# обновляет таймер повторной отправки e-mail при восстановлении пароля        
def reset_timer_ChangePassword():
    ui.send_again_button_ConfirmPasswordChangePage.setDisabled(True)
    if reset_timer_password_events != []:
        reset_timer_password_events[-1].set()
        reset_timer_password_events.pop()

# обновляет таймер повторной отправки e-mail при верификации
def reset_timer_verify():
    ui.send_again_button_EmailConfirmPage.setDisabled(True)
    if reset_timer_verify_events != []:
        reset_timer_verify_events[-1].set()
        reset_timer_verify_events.pop()

# останавливаем программу для установки цен в рекламных кампаниях поиска
def stop_product_advert():
    if stop_product_events != []:
        stop_product_events[-1].set()
        stop_product_events.pop()
        signal.start_or_stop_product.emit(f'''WildBoost остановлен ({time.strftime('%d %B %H:%M:%S', time.localtime())}).''')
        ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_start_ProductPage)

        ui.scrollArea_log_ProductPage.setStyleSheet('''QScrollArea {
                                background: #F5F5F5;
                                border: 1px solid #B4B5B8;
                                border-radius:6px;
                                }'''
                                )

# запускаем все выбранные кампании в поиске
def start_all_search_companies():
    regex = r'(?<=:)[0-9]*'
    
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_search_adverts.checkedButton()
        
        if checked_button:
            ui.start_companies_button_SearchPage.setDisabled(True)
            advert_id = int(re.search(regex, checked_button.text()).group())

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/start'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)
            except:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}.'''
                signal.result_error.emit((log_text, 15))
                ui.start_companies_button_SearchPage.setEnabled(True)
                return None

            if response.status_code == 200:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: кампания ID:{advert_id} активирована.'''
                checked_button.setText(checked_button.text().replace('приостановлена', 'активна'))
                signal.result.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}.'''
                signal.result_error.emit((log_text, 15))
            
            ui.start_companies_button_SearchPage.setEnabled(True)

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error.emit((log_text, 15))

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_search_adverts if checkbox.isChecked()]
        
        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: превышение доступного лимита рекламных кампаний.'''
            signal.result_error.emit((log_text, 15))
            return None
        advert_ids = []
        if checked_boxes != []:
            ui.start_companies_button_SearchPage.setDisabled(True)
            activated=[]
            for checkbox in checked_boxes:
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_ids.append(advert_id)

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/start'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)

                except:
                    log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}.'''
                    signal.result_error.emit((log_text, 15))
                    return None

                if response.status_code == 200:
                    checkbox.setText(checkbox.text().replace('приостановлена', 'активна'))
                    activated.append(advert_id)

            not_activated = set(advert_ids) - set(activated)
            if not_activated == set():
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{activated} активированы.'''.replace('[', '').replace(']', '')
                signal.result.emit((log_text, 15))
            elif activated != []:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{activated} активированы, {not_activated} - активировать не удалось.'''.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
                signal.result_wrong.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{not_activated} - активировать не удалось.'''.replace('{', '').replace('}', '')
                signal.result_error.emit((log_text, 15))
            ui.start_companies_button_SearchPage.setEnabled(True)

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error.emit((log_text, 15))

def start_all_search_companies_thread():
    threading.Thread(daemon=True, target=start_all_search_companies).start()

# останавливаем все выбранные кампании в поиске
def stop_all_search_companies():
    regex = r'(?<=:)[0-9]*'
    
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_search_adverts.checkedButton()
        
        if checked_button:
            ui.stop_companies_button_SearchPage.setDisabled(True)
            advert_id = int(re.search(regex, checked_button.text()).group())

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/pause'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)
            except:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось остановить кампанию ID:{advert_id}.'''
                signal.result_error.emit((log_text, 15))
                ui.stop_companies_button_SearchPage.setEnabled(True)
                return None

            if response.status_code == 200:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: кампания ID:{advert_id} приостановлена.'''

                checked_button.setText(checked_button.text().replace('активна', 'приостановлена'))

                signal.result.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось остановить кампанию ID:{advert_id}.'''
                signal.result_error.emit((log_text, 15))

            ui.stop_companies_button_SearchPage.setEnabled(True)
        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error.emit((log_text, 15))

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_search_adverts if checkbox.isChecked()]
        
        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: превышение доступного лимита рекламных кампаний.'''
            signal.result_error.emit((log_text, 15))
            return None

        advert_ids = []
        if checked_boxes != []:
            ui.stop_companies_button_SearchPage.setDisabled(True)
            stopped = []
            for checkbox in checked_boxes:
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_ids.append(advert_id)

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/pause'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)

                except:
                    log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось приостановить кампанию ID:{advert_id}.'''
                    signal.result_error.emit((log_text, 15))
                    ui.stop_companies_button_SearchPage.setEnabled(True)
                    return None
                
                if response.status_code == 200:
                    checkbox.setText(checkbox.text().replace('активна', 'приостановлена'))
                    stopped.append(advert_id)
                
            not_stopped = set(advert_ids) - set(stopped)
            if not_stopped == set():
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{stopped} приостановлены.'''.replace('[', '').replace(']', '')
                signal.result.emit((log_text, 15))
            elif stopped != []:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{stopped} приостановлены, {not_stopped} - остановить не удалось.'''.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
                signal.result_wrong.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{not_stopped} - остановить не удалось.'''.replace('{', '').replace('}', '')
                signal.result_error.emit((log_text, 15)) 
            ui.stop_companies_button_SearchPage.setEnabled(True)

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error.emit((log_text, 15))

def stop_all_search_companies_thread():
    threading.Thread(daemon=True, target=stop_all_search_companies).start()

# запускаем все выбранные кампании в карточке
def start_all_product_companies():
    regex = r'(?<=:)[0-9]*'
    
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_product_adverts.checkedButton()
        
        if checked_button:
            ui.start_companies_button_ProductPage.setDisabled(True)
            advert_id = int(re.search(regex, checked_button.text()).group())

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/start'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)

            except:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}.'''
                signal.result_error_product.emit((log_text, 15))
                ui.start_companies_button_ProductPage.setEnabled(True)
                return None

            if response.status_code == 200:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: кампания ID:{advert_id} активирована.'''

                checked_button.setText(checked_button.text().replace('приостановлена', 'активна'))
                
                signal.result_product.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}.'''
                signal.result_error_product.emit((log_text, 15))
            
            ui.start_companies_button_ProductPage.setEnabled(True)

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error_product.emit((log_text, 15))

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_product_adverts if checkbox.isChecked()]
        
        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: превышение доступного лимита рекламных кампаний. '''
            signal.result_error_product.emit((log_text, 15))
            return None
        advert_ids = []
        if checked_boxes != []:
            ui.start_companies_button_ProductPage.setDisabled(True)
            activated = []
            for checkbox in checked_boxes:
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_ids.append(advert_id)

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/start'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)

                except:
                    log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось активировать кампанию ID:{advert_id}'''
                    signal.result_error_product.emit((log_text, 15))
                    ui.start_companies_button_ProductPage.setEnabled(True)
                    return None
                
                if response.status_code == 200:
                    checkbox.setText(checkbox.text().replace('приостановлена', 'активна'))
                    activated.append(advert_id)
            not_activated = set(advert_ids) - set(activated)
            if not_activated == set():
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{activated} активированы.'''.replace('[', '').replace(']', '')
                signal.result_product.emit((log_text, 15))
            elif activated != []:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{activated} активированы, {not_activated} - активировать не удалось.'''.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
                signal.result_wrong_product.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{not_activated} - активировать не удалось.'''.replace('{', '').replace('}', '')
                signal.result_error_product.emit((log_text, 15))
            ui.start_companies_button_ProductPage.setEnabled(True)
                        
        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error_product.emit((log_text, 15))

def start_all_product_companies_thread():
    threading.Thread(daemon=True, target=start_all_product_companies).start()

# останавливаем все выбранные кампании в поиске
def stop_all_product_companies():
    regex = r'(?<=:)[0-9]*'
    
    if (SUBSCRIBE_PLAN == 1) or (SUBSCRIBE_PLAN == 2):
        checked_button = button_group_product_adverts.checkedButton()
        
        if checked_button:
            ui.stop_companies_button_ProductPage.setDisabled(True)
            advert_id = int(re.search(regex, checked_button.text()).group())

            headers_wb = {
            'Authorization': KEY,
            }    
            url_wb = 'https://advert-api.wb.ru/adv/v0/pause'
            params_wb = {
                'id' : advert_id
            }
            try:
                response = requests.get(url_wb, headers=headers_wb, params=params_wb)

            except:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось остановить кампанию ID:{advert_id}.'''
                signal.result_error_product.emit((log_text, 15))
                ui.stop_companies_button_ProductPage.setEnabled(True)
                return None

            if response.status_code == 200:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: кампания ID:{advert_id} приостановлена.'''

                checked_button.setText(checked_button.text().replace('активна', 'приостановлена'))

                signal.result_product.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось остановить кампанию ID:{advert_id}.'''
                signal.result_error_product.emit((log_text, 15))
            ui.stop_companies_button_ProductPage.setEnabled(True)

        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error_product.emit((log_text, 15))

    else:
        checked_boxes = [checkbox for checkbox in checkboxes_product_adverts if checkbox.isChecked()]
        
        if len(checked_boxes) > subscribtion_plan[SUBSCRIBE_PLAN]['adverts']:
            
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: превышение доступного лимита рекламных кампаний.'''
            signal.result_error_product.emit((log_text, 15))
            return None
        advert_ids = []
        if checked_boxes != []:
            ui.stop_companies_button_ProductPage.setDisabled(True)
            stopped = []
            for checkbox in checked_boxes:
                advert_id = int(re.search(regex, checkbox.text()).group())
                advert_ids.append(advert_id)

                headers_wb = {
                'Authorization': KEY,
                }    
                url_wb = 'https://advert-api.wb.ru/adv/v0/pause'
                params_wb = {
                    'id' : advert_id
                }

                try:
                    response = requests.get(url_wb, headers=headers_wb, params=params_wb)

                except:
                    log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не удалось приостановить кампанию ID:{advert_id}.'''
                    signal.result_error_product.emit((log_text, 15))
                    ui.stop_companies_button_ProductPage.setEnabled(True)
                    return None

                if response.status_code == 200:
                    checkbox.setText(checkbox.text().replace('активна', 'приостановлена'))
                    stopped.append(advert_id)
            not_stopped = set(advert_ids) - set(stopped)
            if not_stopped == set():
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{stopped} приостановлены.'''.replace('[', '').replace(']', '')
                signal.result_product.emit((log_text, 15))
            elif stopped != []:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{stopped} приостановлены, {not_stopped} - остановить не удалось.'''.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
                signal.result_wrong_product.emit((log_text, 15))
            else:
                log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: рекламные кампании ID:{not_stopped} - остановить не удалось.'''.replace('{', '').replace('}', '')
                signal.result_error_product.emit((log_text, 15))
            ui.stop_companies_button_ProductPage.setEnabled(True)
                    
        else:
            log_text = f'''{time.strftime('%d %B %H:%M:%S', time.localtime())}: не выбрано ни одной кампании.'''
            signal.result_error_product.emit((log_text, 15))

def stop_all_product_companies_thread():
    threading.Thread(daemon=True, target=stop_all_product_companies).start()

# переходим по ссылке для установки обновления
def proceed_update_url():
    if UPDATE_URL != '':
        webbrowser.open_new_tab(UPDATE_URL)

# переходим по ссылке с инструкцией
def proceed_how_to_use():
    webbrowser.open_new_tab('https://wildboost.ru/how_to_use/')

# получаем сервисную информацию о параметрах подписок и наличии обновлений при нажатии кнопки "обновить"
def get_service_info():
    while True:
        try:
            response = requests.get(f'{config.ADDRESS}/api/subscriptions-info/')
        except:
            signal.status_bar_info.emit(False)
            ui.update_button_IndexPage.setDisabled(True)
            return None

        if response.status_code == 200:
            sub_info = {}
            info = json.loads(response.json())
            for sub in info:
                sub_info[sub['id']] = {
                    'name' : sub['name'], 
                    'adverts' : sub['adverts'], 
                    'products' : sub['products'], 
                    'renew' : sub['renew'], 
                    'price' : sub['price']
                    }
            global subscribtion_plan
            subscribtion_plan = sub_info

        try:
            response = requests.get(f'{config.ADDRESS}/api/update/')
        except:
            signal.status_bar_info.emit(False)
            ui.update_button_IndexPage.setEnabled(False)
            return None

        if response.status_code == 200:
            last_update = json.loads(response.json())
            if VERSION != last_update['id']:
                ui.update_button_IndexPage.setText('Обновить приложение')
                ui.update_button_IndexPage.setEnabled(True)
                global UPDATE_URL
                UPDATE_URL = last_update['url']

                if last_update['important']:
                    signal.status_bar_info.emit(True)
                else:
                    signal.status_bar_info.emit(False)
            else:
                ui.update_button_IndexPage.setEnabled(False)
                signal.status_bar_info.emit(False)
        else:
            ui.update_button_IndexPage.setEnabled(False)
            signal.status_bar_info.emit(False)

        time.sleep(10800)

threading.Thread(daemon=True, target=get_service_info).start()

def refresh_subscribtion_params():
    if TOKEN != '':
        ui.refresh_button_ProfilePage.setDisabled(True)
        headers = {
        'Authorization': f'Token {TOKEN}'
        }
        try:
            response = requests.get(f'{config.ADDRESS}/api/subscription/', headers=headers)
            if response.status_code == 200:
                response = response.json()

                global EXPIRE_DATE
                EXPIRE_DATE = response.get('expire_date')
                global SUBSCRIBE_PLAN
                SUBSCRIBE_PLAN = response.get('subscribe_plan')

                if SUBSCRIBE_PLAN == 1:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.free_subscribe_ProfilePage)
                elif SUBSCRIBE_PLAN == 2:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.base_subscribe_ProfilePage)
                elif SUBSCRIBE_PLAN == 3:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.standart_subscribe_ProfilePage)    
                elif SUBSCRIBE_PLAN == 4:
                    ui.about_subscribe_ProfilePage.setCurrentWidget(ui.profi_subscribe_ProfilePage)

                ui.subscribtion_plan_label_ProfilePage.setText(subscribtion_plan[SUBSCRIBE_PLAN]['name'].upper())
                ui.expire_date_label_ProfilePage.setText(EXPIRE_DATE)
                ui.refresh_button_ProfilePage.setEnabled(True)

        except:
            pass

def refresh_button_pressed():
    threading.Thread(daemon=True, target=refresh_subscribtion_params).start()

# наводит фокус при открытии приложения, задает нужную страницу
ui.email_input_loginpage.setFocus()
ui.IndexWindow.setCurrentWidget(ui.LoginPage)

# кнопки, расположенные на странице вход
ui.enter_button_loginpage.clicked.connect(login)
ui.signup_button_loginpage.clicked.connect(proceed_to_SignupPage)
ui.forgot_password_button_loginpage.clicked.connect(proceed_to_EnterEmailPage)

# отправка формы регистрации
ui.confirm_button_SiqnupPage.clicked.connect(signup)

# верификация e-mail при регистрации
ui.confirm_button_EmailConfirmPage.clicked.connect(email_verify)

# направляет на страницу изменения адреса электронной почты
ui.changeemail_button_EmailConfirmPage.clicked.connect(proceed_to_ChangeEmailPage)

# меняет привязанный адрес электронной почты, направляет на страницу верфикации
ui.confirm_button_ChangeEmailPage.clicked.connect(change_email)

# отправляет письмо с кодом для изменения пароля
ui.confirm_button_EnterEmailPage.clicked.connect(change_password_verify)

# проверяет код, присланный для изменения пароля, перенаправляет на страницу для ввода нового пароля
ui.confirm_button_ConfirmChangePasswordPage.clicked.connect(recovery_email_verify)

# переустанавливает пароль и направляет на страницу входа
ui.confirm_button_ChangePasswordPage.clicked.connect(change_password)

# повторно отправляет e-mail для смены пароля
ui.send_again_button_ConfirmPasswordChangePage.clicked.connect(send_again_ChangePassword)

# повторно отправляет e-mail для верификации
ui.send_again_button_EmailConfirmPage.clicked.connect(send_again_verify)

# переключается на настройку рекламы в поиске
ui.search_button_IndexPage.clicked.connect(proceed_to_SearchPage)
# переключается на настройку рекламы в карточке товара
ui.product_button_IndexPage.clicked.connect(proceed_to_ProductPage)
# переключается на профиль
ui.profile_button_IndexPage.clicked.connect(proceed_to_ProfilePage)

# кнопки выхода и отмены (переводят на начальную страницу входа)
ui.cancle_button_EnterEmailPage.clicked.connect(exit_EnterEmailPage)
ui.cancle_button_SignupPage.clicked.connect(exit_SignupPage)
ui.cancle_button_ChangeEmailPage.clicked.connect(exit_ChangeEmailPage)
ui.cancle_button_ChangePasswordPage.clicked.connect(exit_ChangePasswordPage)
ui.cancel_button_ConfirmChangePasswordPage.clicked.connect(exit_ConfirmChangePasswordPage) 
ui.exit_button_IndexPage.clicked.connect(logout)

# кнопка подтверждения введеного ключа
ui.confirm_key_button_ProfilePage.clicked.connect(get_adverts)

# кнопки оплаты тарифов
ui.pay_199_button_ProfilePage.clicked.connect(lambda: payment(subscribtion_plan[2]['price'], 2))
ui.pay_349_button_ProfilePage.clicked.connect(lambda: payment(subscribtion_plan[3]['price'], 3))
ui.pay_499_button_ProfilePage.clicked.connect(lambda: payment(subscribtion_plan[4]['price'], 4))

# кнопка обновления статуса подписки
ui.refresh_button_ProfilePage.clicked.connect(refresh_button_pressed)

# 1. кнопки на странице настройки рекламы в поиске:
# 1.1 кнопки под графой с рекламными кампаниями
ui.menu_search_setup_refresh_button_SearchPage.clicked.connect(refresh_search_adverts)
ui.menu_adverts_setup_confirm_button_SearchPage.clicked.connect(get_search_adverts_products)
ui.menu_adverts_setup_amount_error_ok_button_SearchPage.clicked.connect(lambda: ui.menu_adverts_setup_SearchPage.setCurrentWidget(ui.menu_adverts_setup_confirm_SearchPage))
# 1.2 кнопки под графой товарных групп
ui.menu_product_setup_refresh_button_SearchPage.clicked.connect(get_search_adverts_products)
ui.menu_product_setup_confirm_button_SearchPage.clicked.connect(get_search_settings)
ui.menu_product_setup_amount_error_ok_button_SearchPage.clicked.connect(lambda: ui.menu_product_setup_SearchPage.setCurrentWidget(ui.menu_product_setup_confirm_SearchPage))
# 1.3 кнопки под графой настроек
ui.menu_settings_start_button_SearchPage.clicked.connect(start_search_advert)
ui.menu_settings_error_ok_button_SearchPage.clicked.connect(lambda: ui.menu_settings_SearchPage.setCurrentWidget(ui.menu_settings_start_SearchPage))
ui.menu_settings_stop_button_SearchPage.clicked.connect(stop_search_advert)
#1.4 кнопки под окном логов
ui.reset_button_SearchPage.clicked.connect(clear_log_SearchPage)
ui.start_companies_button_SearchPage.clicked.connect(start_all_search_companies_thread)
ui.stop_companies_button_SearchPage.clicked.connect(stop_all_search_companies_thread)

# 2. кнопки на странице настройки рекламы в карточке товара:
# 2.1 кнопки под графой с рекламными кампаниями
ui.menu_search_setup_refresh_button_ProductPage.clicked.connect(refresh_product_adverts)
ui.menu_adverts_setup_confirm_button_ProductPage.clicked.connect(get_product_adverts_products)
ui.menu_adverts_setup_amount_error_ok_button_ProductPage.clicked.connect(lambda: ui.menu_adverts_setup_ProductPage.setCurrentWidget(ui.menu_adverts_setup_confirm_ProductPage))
# 2.2 кнопки под графой товарных групп
ui.menu_product_setup_refresh_button_ProductPage.clicked.connect(get_product_adverts_products)
ui.menu_product_setup_confirm_button_ProductPage.clicked.connect(get_product_settings)
ui.menu_product_setup_amount_error_ok_button_ProductPage.clicked.connect(lambda: ui.menu_product_setup_ProductPage.setCurrentWidget(ui.menu_product_setup_confirm_ProductPage))
# 2.3 кнопки под графой настроек
ui.menu_settings_start_button_ProductPage.clicked.connect(start_product_advert)
ui.menu_settings_error_ok_button_ProductPage.clicked.connect(lambda: ui.menu_settings_ProductPage.setCurrentWidget(ui.menu_settings_start_ProductPage))
ui.menu_settings_stop_button_ProductPage.clicked.connect(stop_product_advert)
#2.4 кнопки под окном логов
ui.reset_button_ProductPage.clicked.connect(clear_log_ProductPage)
ui.start_companies_button_ProductPage.clicked.connect(start_all_product_companies_thread)
ui.stop_companies_button_ProductPage.clicked.connect(stop_all_product_companies_thread)

# кнопка для установки обновлений (активна в случае наличия обновлений)
ui.update_button_IndexPage.clicked.connect(proceed_update_url)

# кнопка со ссылкой на инструкцию
ui.how_to_use_button_IndexPage.clicked.connect(proceed_how_to_use)

sys.exit(app.exec())