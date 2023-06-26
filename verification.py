import requests
import random
import json

import config

def randomizer():
    num = random.choice(range(10000, 100000))
    return num

def send_email(email):
    num = randomizer()
    requests.post(
		config.EMAIL_URL,
		auth=("api", config.EMAIL_KEY),
		data={"from": config.EMAIL_FROM,
			"to": [email],
			"subject": "Верификация e-mail",
			"template": "validation_letter",
			"t:variables": json.dumps({"verify": num})})
    return num

def send_recovery_email(email):
    num = randomizer()
    requests.post(
		config.EMAIL_URL,
		auth=("api", config.EMAIL_KEY),
		data={"from": config.EMAIL_FROM,
			"to": [email],
			"subject": "Запрос на сброс пароля",
			"template": "password_recovery",
			"t:variables": json.dumps({"verify": num})})
    return num
