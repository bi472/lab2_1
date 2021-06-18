from bottle import post, request
from re import *
import pdb
import json
import myform_mail
from datetime import date
import test
questions = {}

def get_all_reviews():
    reviews = []
    with open('reviews.json') as f: # Получение данных из json файла
        file_content = f.read()
        reviews = json.loads(file_content)
    return reviews

def create_review(rev): 
    reviews = []
    try:
        with open('reviews.json') as f: # Получение данных из json файла
            file_content = f.read()
            reviews = json.loads(file_content)
    except Exception:
        reviews = []
    reviews.append(rev) 
    file = open("reviews.json", 'w') # Запись в файл
    file.write(json.dumps(reviews))
    file.close()

@post('/home', method='post')
def prepare_review():
    text = request.forms.get('FEEDBACK')
    email = request.forms.get('EMAIL')
    phone = request.forms.get('PHONE')
    author = request.forms.get('AUTHOR')
    if not (test.check_mail(email)):
        return "Введите email правильно."
    if not (test.check_phone(phone)):
        return "Введите номер телефона правильно."
    if not text:
        return "Пожалуйста, введите отзыв."
    review = {
    "feedback": text,
    "email": email,
    "phone": phone,
    "author": author,
    "date": date.today().strftime('%Y/%m/%d')
    }
    create_review(review)
    return "Your review was created"
    

    