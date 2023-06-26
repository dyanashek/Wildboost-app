# WildBoost
## Change language: [English](README.en.md)
***
Программа-биддер, в автоматическом режиме управляющая ставками на рекламном аукционе Wildberries. Программа определяет реальные ставки (для рекламы в поиске / рекламы в карточке товара). И удерживает заданную пользователем позицию или диапазон позиций, не превышая заданный бюджет.
## [DEMO](README.demo.md)
## Функционал:
1. Регистрация, авторизация, связанные операции (подтверждение e-mail, восстановление и смена пароля и пр.)
2. Платная подписка
3. Парсинг реальных ставок аукциона Wildberries
4. Изменение ставок выбранных кампаний в соответствии с заданными настройками
5. Запуск и остановка выбранных кампаний
## Установка и использование:
- Разверните [API](https://github.com/dyanashek/Wildboost-api) на сервере или локально
- Создайте файл .env, содержащий следующие переменные:
> файл создается в корневой папке проекта
  - **ACCOUNT_ID** - ID аккаунта [Юкасса](https://yookassa.ru/my/payments)
  - **SECRET_KEY_PAYMENT** - секретный ключ Юкасса
  - **ADDRESS** - полное доменное имя вашего сервера, без / в окончании
  - **EMAIL_KEY** - секретный ключ сервиса [mailgun](https://app.mailgun.com/mg/dashboard) для рассылки e-mail
  - **EMAIL_URL** - url вашего аккаунта сервиса mailgun
  - **EMAIL_FROM** - адрес, который будет указывать в "from" при отправке e-mail с кодом верификации
- Установить виртуальное окружение и активировать его (при необходимости):
> Установка и активация в корневой папке проекта
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Установить зависимости:
```sh
pip install -r requirements.txt
```
- Запустить проект:
```sh
python3 main.py
```
- При необходимости скомпилировать в исполняемый файл с помощью pyinstaller