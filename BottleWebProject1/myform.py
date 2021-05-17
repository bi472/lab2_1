from bottle import post, request
from re import *
import pdb
import json

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    questions = {}
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(mail)
    if not (mail == '' or quest == ''):
        if is_valid:
            questions[mail].append = quest
            return "Спасибо! Мы ответим вам по адресу %s" % mail
        else:
            return "Пожалуйста, введите правильный email. Иначе мы не сможем с вами связаться и не сможем сделать наш сайт чуточку лучше. :)"
    else:
        return "Пожалуйста, введите все поля. Похоже некоторые вы забыли ..."
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

    

    