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

