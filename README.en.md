# Wildboost
## Изменить язык: [Русский](README.md)
***
A bidder program that automatically manages bids at the Wildberries advertising auction. The program determines the real rates (for advertising in search / advertising in the product card). And it keeps the user-specified position or range of positions without exceeding the specified budget.
## [DEMO](README.demo.md)
## Functionality:
1. Registration, authorization, related operations (e-mail confirmation, password recovery and change, etc.)
2. Paid subscription
3. Parsing the real rates of the Wildberries auction
4. Change the bids of the selected campaigns according to the specified settings
5. Start and stop selected campaigns
## Installation and use:
- Deploy [API](https://github.com/dyanashek/Wildboost-api) on server or locally
- Create an .env file containing the following variables:
> the file is created in the root folder of the project
   - **ACCOUNT_ID** - account ID [Yukassa](https://yookassa.ru/my/payments)
   - **SECRET_KEY_PAYMENT** - secret key of Yukass
   - **ADDRESS** - fully qualified domain name of your server, without / at the end
   - **EMAIL_KEY** - secret key of the [mailgun](https://app.mailgun.com/mg/dashboard) service for sending e-mail
   - **EMAIL_URL** - url of your mailgun service account
   - **EMAIL_FROM** - the address that will be indicated in "from" when sending an e-mail with a verification code
- Install the virtual environment and activate it (if necessary):
> Installation and activation in the root folder of the project
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Install dependencies:
```sh
pip install -r requirements.txt
```
- Run project:
```sh
python3 main.py
```
- Optionally compile to an executable using pyinstaller