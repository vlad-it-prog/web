import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import JsonResponse
from app.models import Client
from random import randint
import os
import os.path
import pandas
from app import pandas_dataframes
from django.contrib.auth.models import User
import requests
import json
from django.utils.translation import ugettext as _


import random
from datetime import datetime
from app.models import Person


from app.models import *


def index(request):
    ls = Songs.objects.all()
    result = ""
    for x in ls:
        result = result + " " + x.song
    return HttpResponse(result)


def main_page(request):
    key_tracklist = ''
    x = request.POST
    for p in x:
        key_tracklist = key_tracklist + x[p]
    print(key_tracklist)
    df_track_list = pandas.read_csv("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\track_list.csv")
    ls_main = []
    q = 0
    for y in df_track_list['artist']:
          for z in df_track_list['song']:
                ls_main.append([str(q), df_track_list['artist'][q], df_track_list['song'][q]])
                q = q + 1
                break

    if key_tracklist == 'artist':
          ls_main = sorted(ls_main, key=lambda artist: artist[1])
    else:
        ls_main = sorted(ls_main, key=lambda song: song[2])


    #elif key_tracklist != 'song':
       #   ls_main = sorted(ls_main, key=lambda song: song[2])

    df_bands = pandas.read_csv("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\band_list.csv")
    menu_items = df_bands['cover bands']
    menu_head = str(df_bands.keys()[1])


  #  response = requests.get(
  #      'https://www.nbrb.by/api/exrates/rates?periodicity=0'
  #  )
   # data = json.loads(response.text)

    context = {
        #'exchange rates': data,
        'cover_bands': menu_items,
        'table': ls_main,
        'table_1': [],
        'loged': request.user.is_authenticated,
        'username_loged': request.user.username
    }
    #print(data)

    return render(request, 'page_1.html', context)



def main_page_2(request):

    context = {'loged': request.user.is_authenticated,
               'username_loged': request.user.username
    }
    return render(request, 'page_1.html', context)


def main(request):
    context = {'loged_2': request.user.is_authenticated,
    }
    return render(request, 'main.html', context)


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'main.html', {'msg': True})
    else:
        login(request, user)
        return HttpResponseRedirect('/page_1')


def test(request):
    return render(request, 'test.html')


def logout_page(request):
    return render(request, 'logout_page.html')


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/main')
    else:
        return HttpResponseRedirect('/page_1')


def registration_form(request):
    return render(request, 'registration.html', {})

def register(request):
    user = User.objects.create_user(request.POST['login'],
                                    password=request.POST['password'],
                                    first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email']
                                    )
    client = Client(user=user, address='Minsk')
    client.save()
    #return HttpResponse('OK'),
    return HttpResponseRedirect('/main')


def ajax_path(request):
    a = str(randint(1, 100))
    response = {
        'message': request.POST['a'] + a
    }
    return JsonResponse(response)


def ajax_valid(request):
    x = User.objects.filter(username=request.POST['a'])

    if len(x) == 0:
        response = {
            'user_exist': False
        }
    else:
        response = {
            'user_exist': True
        }
    return JsonResponse(response)


def ajax_cb(request):
    x = request.POST['a']
    print(x)
    alph_ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', ' ']
    if x[-1] in alph_ls:
        ls_list = []
        ls_str = ''
        for root, dirs, files in os.walk("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands"):
            for file in files:
                if file.endswith(".csv"):
                    path_file = os.path.join(file)
                    ls_list.append(path_file)
        for _ in ls_list:
            if x in _[0:len(x)]:
                ls_str = ls_str + _ + ', \n'

        response = {
            'message': ls_str
        }
        return JsonResponse(response)
    else:
        response = {
            'message': 'ты нажал не на ту клавишу'
        }
        return JsonResponse(response)


def button_ok(request, x):
    creat_file = open("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\privet.csv", 'w')
    creat_file.write('artist,song')
    creat_file.close()


def band_list(request):
    df = pandas.read_csv("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\band_list.csv")
    menu_items = df['cover bands']
    menu_head = str(df.keys()[1])
    context = {
        'cover_bands': menu_items
    }
    print(sorted(menu_items))
    print(df.loc[5])
    return render(request, 'page_1.html', context)


def exchange_rates(request):
    response = requests.get(
        'http://www.nbrb.by/api/exrates/rates/145?startDate=2020-10-14&endDate=2020-10-20'
    )
    #z = 0
    #for _ in range(7):

    data = json.loads(response.text)
    context = {
        'exchange_rates': data

    }

    return render(request, 'page_2.html', context)


def experiment(request):
    size = 1
    slice_size = 500
    Person.objects.all().delete()
    for _ in range(int(size / slice_size)):
        slice = []
        for _ in range(slice_size):
            slice.append(
                Person(
                    name=str(random.randint(1, 1000)),
                    credit_card_number=str(
                        random.randint(10**70, 10**80)
                    )
                )
            )
        Person.objects.bulk_create(slice, slice_size)

    sum = 0
    for _ in range(100):
        start = datetime.now()
        list(Person.objects.filter(
            credit_card_number=random.randint(
                10**70, 10**80
            )
        ))
        delta = (datetime.now() - start).total_seconds()
        sum = sum + delta
    print("Время выполнения 100 запрсосов: " + str(sum) + ' секунд')
   # return render(request,'\page_3.html', {"Время выполнения 100 запрсосов: " + str(sum) + ' секунд'})
  #  print()


def main(request):
    return render(request,
                  'page_1.html', {'title': _('Пожалуйста')}
                  )


def page_3(request):
    return render(request, 'page_3.html', {})


def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name'])
    persons = Person.objects.filter(
        id__gt=int(request.GET['start']),
        id__lt=int(request.GET['finish'])
    )
    for person in persons:
        writer.writerow([person.id, person.name])
#    return response
