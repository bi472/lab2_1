import json
import test
from bottle import post, request
from datetime import date



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
    file.write(json.dumps(orders))
    file.close()


@post('/feedback', method='post')
def prepare_review():
    text = request.forms.get('FEEDBACK')
    email = request.forms.get('EMAIL')
    phone = request.forms.get('PHONE')
    author = request.forms.get('AUTHOR')
    if not text:
        return "enter feedback"
    review = {
    "feedback": text,
    "email": email,
    "phone": phone,
    "author": author,
    "date": date.today().strftime('%Y/%m/%d')
    }
    create_review(review)
    return "Your review was created"

