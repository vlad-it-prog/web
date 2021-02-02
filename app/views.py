import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import JsonResponse
from random import randint
import os
import os.path
import pandas
from app import pandas_dataframes
from django.contrib.auth.models import User
import requests
import json
from django.utils.translation import ugettext as _, activate
import re
import random
from datetime import time
from datetime import datetime
from app.models import Track, Band, Client, Person, Person, Cash, Images, Song, ExportFolderName, ExportFileName, History, ImportFolderName
import requests
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings


def language(request):

    """ URL:
        Function:
        File:  """

    try:
        lang = request.POST['language']
    except MultiValueDictKeyError:
        lang = False

    activate(lang)
    response = HttpResponseRedirect(request.COOKIES["path_name"])

    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)

    return response


def start_page(request):

    """ URL: help_page
        Function: help_page
        File: help_page.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        return HttpResponseRedirect('/main_page')


def help_page(request):

    """ URL: help_page
        Function: help_page
        File: help_page.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        response = render(request, "help_page.html", {})
        response.set_cookie(key="path_name", value="help_page")
        return response


# ______________________________________________________________________________________________________________________


def add_new_cover_band_to_band_list(request):

    """ URL:
        Function:
        File: .html """

    response = {
        'message': request.POST['a']
    }

    return JsonResponse(response.message)
# ______________________________________________________________________________________________________________________


def login_page(request):

    """ URL: login_page
        Function: login_page
        File: login_page.html """

    if request.user.is_authenticated:
        return HttpResponseRedirect('/main_page')
    else:
        response = render(request, "login_page.html", {})
        response.set_cookie(key="path_name", value="login_page")
        return response
# ______________________________________________________________________________________________________________________


def main_page(request):

    """ URL: main_page
        Function: main_page
        File: main_page.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        all_songs = len(Track.objects.values('song_name'))
        all_bands = len(Band.objects.values('band_name'))
        all_bands_list = []
        cover_bands = []
        for band in range(len(Band.objects.values('band_name'))):
            all_bands_list.append([band + 1, Band.objects.order_by('band_name').values()[band]['band_name']])
            cover_bands.append(Band.objects.order_by('band_name').values()[band]['band_name'])

        table = []
        for track in range(len(Track.objects.values())):
            table.append([track + 1, Track.objects.order_by("artist_name").values()[track]['artist_name'], Track.objects.order_by("artist_name").values()[track]['song_name']])

        dir_name = ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name']

        if dir_name not in os.listdir():
            os.makedirs(os.path.split(os.path.abspath(os.listdir()[0]))[0] + "\\" + dir_name)
        else:
            pass
        export_path = os.path.abspath(ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name'] + "\\")


        import_dir_name = ImportFolderName.objects.values('name')[len(ImportFolderName.objects.values('name')) - 1]['name']
        if import_dir_name not in os.listdir():
            os.makedirs(os.path.split(os.path.abspath(os.listdir()[0]))[0] + "\\" + import_dir_name)
        else:
            pass
        # print(os.listdir())
        # import_path = os.path.abspath(ImportFolderName.objects.values('name')[len(ImportFolderName.objects.values('name')) - 1]['name'] + "\\")


        # print(os.path.basename('C:\\Users\\User\\PycharmProjects\\test_python\\test_1'))

        # key_tracklist = ''
        # x = request.POST
        # for p in x:
        #     key_tracklist = key_tracklist + x[p]
        # print(key_tracklist)
        # df_track_list = pandas.read_csv("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\track_list.csv")


        # df_bands = pandas.read_csv("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\band_list.csv")
        # menu_items = df_bands['cover bands']
        # menu_head = str(df_bands.keys()[1])


        # response = requests.get(
        #     'https://www.nbrb.by/api/exrates/rates?periodicity=0'
        # )
        # data = json.loads(response.text)

        history_dict = []
        num = 0
        history_all = History.objects.all()
        for history_time in history_all:
            history_dict.append([str(history_time), str(history_all[num].event) + "_" + str(num + 1), history_all[num].user])
            num = num + 1
        # print(history_dict)


        context = {
            # 'exchange rates': data,
            # 'cover_bands': menu_items,
            'table': table,
            "dir_name": dir_name,
            "export_path": export_path,
            "import_dir_name": import_dir_name,
            # "import_path": import_path,
            "all_songs": all_songs,
            "all_bands": all_bands,
            "all_bands_list": all_bands_list,
            "cover_bands": cover_bands,
            'table_1': [],
            'loged': request.user.is_authenticated,
            'username_loged': request.user.username,
            'title': _('Пожалуйста'),
            'song': Song.objects.all()[0],
            "history_dict": history_dict
        }
        # print(type(request.LANGUAGE_CODE))
        # print()
        # from django.views

        # for p in request.COOKIES:
        #     print(p)

        response = render(request, 'main_page.html', context)
        response.set_cookie(key="path_name", value="main_page")
        return response
# ______________________________________________________________________________________________________________________


def main_page_2(request):

    """ URL:
        Function:
        File: .html """

    context = {'loged': request.user.is_authenticated,
               'username_loged': request.user.username}

    return render(request, 'main_page.html', context)
# ______________________________________________________________________________________________________________________


# def main(request):
#
#     """ URL:
#         Function:
#         File: .html """
#
#     context = {'loged_2': request.user.is_authenticated,
#     }
#     return render(request, 'main.html', context)
# ______________________________________________________________________________________________________________________


def login_user(request):

    """ URL:
        Function:
        File: .html """

    if request.user.is_authenticated:
        return HttpResponseRedirect('/main_page')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
        except MultiValueDictKeyError:
            username = False
            password = 'False'

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            response = render(request, 'login_page.html', {'msg': True})
            response.set_cookie(key="path_name", value="login_user")
            return response
        else:
            login(request, user)
            return HttpResponseRedirect('/main_page')
# ______________________________________________________________________________________________________________________


def test(request):

    """ URL:
        Function:
        File: .html """

    return render(request, 'test.html', {"title": _("Новости")})
# ______________________________________________________________________________________________________________________


def do_logout(request):

    """ URL: do_logout
        Function: do_logout
        File: .html """

    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login_page')
    else:
        return HttpResponse('You Are Not Log In')
# ______________________________________________________________________________________________________________________


def registration(request):

    """ URL:
        Function:
        File: .html """

    if request.user.is_authenticated:
        return HttpResponseRedirect('/main_page')
    else:
        response = render(request, 'registration.html', {})
        response.set_cookie(key="path_name", value="registration")
        return response

# ______________________________________________________________________________________________________________________


def register(request):

    """ URL:
        Function:
        File: .html """

    user = User.objects.create_user(request.POST['login'],
                                    password=request.POST['password'],
                                    first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email']
                                    )
    client = Client(user=user, address='Minsk')
    client.save()
    return HttpResponseRedirect('/login_page')
# ______________________________________________________________________________________________________________________


def ajax_path(request):

    """ URL:
        Function:
        File: .html """

    a = str(randint(1, 100))
    response = {
        'message': request.POST['a'] + a
    }
    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def ajax_valid(request):

    """ URL:
        Function:
        File: .html """

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
# ______________________________________________________________________________________________________________________


def ajax_cb(request):

    """ URL:
        Function:
        File: .html """

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
# ______________________________________________________________________________________________________________________


def button_ok(request, x):

    """ URL:
        Function:
        File: .html """

    creat_file = open("C:\\Users\\pc1\\PycharmProjects\\untitled1\\cover_bands\\privet.csv", 'w')
    creat_file.write('artist,song')
    creat_file.close()
# ______________________________________________________________________________________________________________________


def band_list(request):

    """ URL:
        Function:
        File: .html """

    # df = pandas.read_csv("C:\\Users\\User\\PycharmProjects\\web\\cover_bands.csv")
    # menu_items = df['cover band']
    # menu_head = str(df.keys()[1])
    # context = {
    #     'cover_bands': menu_items
    # }
    # print(sorted(menu_items))
    # print(df.loc[5])
    if request.GET['button'] == 'yes':
        print(os.getcwd())
        os.chdir("C:\\Users\\User\\PycharmProjects\\web\\" + request.GET['import_folder_name'])
        print(os.getcwd())
        # db = pandas.read_csv()
    return HttpResponseRedirect("song_list_page")
# ______________________________________________________________________________________________________________________


def exchange_rates(request):

    """ URL:
        Function:
        File: .html """

    response = requests.get(
        'http://www.nbrb.by/api/exrates/rates/145?startDate=2020-10-14&endDate=2020-10-20'
    )
    # z = 0
    # for _ in range(7):

    data = json.loads(response.text)
    context = {
        'exchange_rates': data

    }

    return render(request, 'page_2.html', context)
# ______________________________________________________________________________________________________________________


def experiment(request):

    """ URL:
        Function:
        File: .html """

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

# ______________________________________________________________________________________________________________________


def page_3(request):

    """ URL:
        Function:
        File: .html """

    return render(request, 'page_3.html', {})
# ______________________________________________________________________________________________________________________


def get_csv(request):

    """ URL:
        Function:
        File: .html """

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
# ______________________________________________________________________________________________________________________


def ajax_path(request):

    """ URL: ajax_clock
        Function: ajax_clock
        File: .html """

    a = str(randint(1, 100))
    response = {
        'message': request.POST['a'] + a
    }
    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def main_test_cash(request):

    """ URL:
        Function:
        File: .html """

    return
# ______________________________________________________________________________________________________________________


def test_html(request):

    """ URL:
        Function:
        File: .html """

    return
# ______________________________________________________________________________________________________________________


def delete_cover_band(request):

    """ URL: delete_cover_band
        Function: delete_cover_band
        File: main_page.html
        Element path (web/html): "MAIN MENU" button --> "Delete Cover Band" button --> "Delete Cover Band Modal Window"
        --> "Export Files Folder
        Name:..." input + "Delete" button
        JS path: """

    band_delete = request.GET['select_to_delete_cover_band']

    band_name_list = []
    for x in range(len(Band.objects.values("band_name"))):
        band_name_list.append(Band.objects.values()[x]["band_name"])
    print(band_name_list)

    if len(request.GET['select_to_delete_cover_band']) == 0:
        response = {
            'message': "Nothing was ever done!"
        }
    elif band_delete not in band_name_list and band_delete != "":
        response = {
            'message': "This Cover Band does not exist in the band list!"
        }
    else:
        response = {
            'message': ""
        }
        Band.objects.filter(band_name=request.GET['select_to_delete_cover_band']).delete()
    print(request.GET['select_to_delete_cover_band'])

    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def add_cover_band(request):

    """ URL:
        Function:
        File: .html """

    band = request.GET['select_to_add_cover_band']

    band_name_list = []
    for x in range(len(Band.objects.values("band_name"))):
        band_name_list.append(Band.objects.values()[x]["band_name"])
    print(band_name_list)

    if len(request.GET['select_to_add_cover_band']) == 0:
        response = {
            'message': "Nothing was ever done!"
        }
    elif band in band_name_list:
        response = {
            'message': "This Cover Band is already exist!"
        }
    else:
        response = {
            'message': ''
        }
        Band.objects.create(band_name=request.GET['select_to_add_cover_band'])
    print(request.GET['select_to_add_cover_band'])

    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def cover_bands_details(request):

    """ URL:
        Function:
        File: .html """

    # response = {
    #     'message': request.GET['cover_band_1_details']
    # }
    print(request.GET['cover_band_1_details'])
    print(request.GET['cover_band_2_details'])

    return JsonResponse()# (response)
# ______________________________________________________________________________________________________________________


def rename_export_folder(request):

    """ URL: rename_export_folder
        Function: rename_export_folder
        File: main_page.html
        Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
        Name:..." input + "Save Changes" button
        JS path: """

    current_dir_name = ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name']
    if len(request.GET['new_export_folder_name']) == 0:
        response = {
            'message': "don't alert"
        }
    elif request.GET['new_export_folder_name'] == current_dir_name:
        response = {
            'message': "don't alert"
        }
    else:
        response = {
            'message': ""
        }
        os.rename(current_dir_name, request.GET['new_export_folder_name'])
        ExportFolderName.objects.filter(subject='export folder').update(name=request.GET['new_export_folder_name'])

    # print(ExportFolderName.objects.values())

    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def rename_import_folder(request):

    """ URL: rename_export_folder
        Function: rename_export_folder
        File: main_page.html
        Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
        Name:..." input + "Save Changes" button
        JS path: """

    current_dir_name = ImportFolderName.objects.values('name')[len(ImportFolderName.objects.values('name')) - 1]['name']
    if len(request.GET['new_import_folder_name']) == 0:
        response = {
            'message': "don't alert"
        }
    elif request.GET['new_import_folder_name'] == current_dir_name:
        response = {
            'message': "don't alert"
        }
    else:
        response = {
            'message': ""
        }
        os.rename(current_dir_name, request.GET['new_import_folder_name'])
        ImportFolderName.objects.filter(subject='import folder').update(name=request.GET['new_import_folder_name'])

    print(ImportFolderName.objects.values())

    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def name_export_file(request):

    """ URL: name_export_file
        Function: name_export_file
        File: main_page.html
        Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
        Name:..." input + "Save Changes" button
        JS path: """

    other_file_name_list = []
    export_file_name = request.GET["new_export_file_name"]

    for y in range(len(Band.objects.values('band_name'))):
        other_file_name_list.append(Band.objects.values()[y]['band_name'])

    if export_file_name in other_file_name_list:
        for dir_content_name in os.path.abspath(ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name'] + "\\"):
            if re.match(export_file_name + "^\s\d+$", dir_content_name) is not None:
                creat_file = open((os.path.abspath(ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name'] + "\\") + export_file_name + " 1.csv"), 'w')
                # creat_file.write('artist,song')
                creat_file.close()
            else:
                creat_file = open((os.path.abspath(
                    ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1][
                        'name'] + "\\") + export_file_name + ".txt"), 'w')
                # creat_file.write('artist,song')
                creat_file.close()

        response = {
            'message': export_file_name
        }

    elif export_file_name == "":
        file_name_list = []
        for x in range(len(ExportFileName.objects.values('name'))):
            if re.match("^default list\s\d+$", ExportFileName.objects.values()[x]['name']) is not None:
                file_name_list.append(ExportFileName.objects.values()[x]['name'])

        default_number = 0
        for file_name in file_name_list:
            if default_number <= int(re.match("^default list\s(\d+)$", file_name)[1]):
                default_number = int(re.match("^default list\s(\d+)$", file_name)[1])
            else:
                continue

        default_export_file_name = "default list " + str(default_number + 1)
        print(default_export_file_name)
        ExportFileName.objects.create(name=default_export_file_name)
        creat_file = open((os.path.abspath(ExportFolderName.objects.values('name')[len(ExportFolderName.objects.values('name')) - 1]['name'] + "\\") + default_export_file_name + ".csv"), 'w')
        # creat_file.write('artist,song')
        creat_file.close()

        response = {
            'message': default_export_file_name
        }

    else:
        response = {
            'message': "This Cover Band name does not exist in the Band list! Please, try again!"
        }

    return JsonResponse(response)
# ______________________________________________________________________________________________________________________


def sort_track_list_change(request):

    """ URL:
        Function:
        File: .html """

    reverse_mode = request.GET['reverse_mode']
    print(reverse_mode)
    context = {
        "value_1" "song",
        "value_2" "song",
    }
    response = {
        'message': request.GET['reverse_mode']
    }
    # print(request.GET['cover_band_1_details'])
    # print(request.GET['cover_band_2_details'])
    render(response)

    return render(request, "main_page.html", context)
# ______________________________________________________________________________________________________________________


# def song_list_page(request):
#
#     """ URL:
#         Function:
#         File: .html """
    # try:
    #     x = request.GET.getlist()
    # except MultiValueDictKeyError:
    #     x = False

    # print(x)
    # response = render(request, "song_list_page.html", {})
    # return response
    # pass


def player(request):

    """ URL:
        Function:
        File: .html """

    response = render(request, "main_page.html", {'song': Song.objects.all()[0]})
    response.set_cookie(key="path_name", value="main_page")
    return response


def history(request):

    """ URL:
        Function:
        File: .html """

    try:
        history_all = request.GET["history"]
    except MultiValueDictKeyError:
        history_all = False

    history_register_time = History(time=datetime.now(), event="test_event", user=request.user).save()

    # history_reg_time.created.strftime('%d.%m.%Y %H:%M')

    response = HttpResponseRedirect(request.COOKIES["path_name"])
    response.set_cookie(key="path_name", value="main_page")
    return response


def new(request):

    """ URL: new
        Function: new
        File: new.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        response = render(request, "new.html", {})
        response.set_cookie(key="path_name", value="new")
        return response


def import_file(request):

    """ URL: new
        Function: new
        File: new.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        import_file_name = r"" + str(request.GET['add_cb_open_folder_form']) + ""
        import_file_name_split = import_file_name.split("\\")
        import_file_name_split_2 = import_file_name_split[-1].split(".csv")
        result = import_file_name_split_2[0]
        # print(result)
        response = {
            "message": result
        }
        return JsonResponse(response)


def import_file_to_database(request):

    """ URL: new
        Function: new
        File: new.html """

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login_page')
    else:
        # import_file_name = r"" + str(request.GET['add_cb_open_folder_form']) + ""
        # import_file_name_split = import_file_name.split("\\")
        # import_file_name_split_2 = import_file_name_split[-1].split(".csv")
        # result = import_file_name_split_2[0]
        # print(result)
        # result = request.GET["result_to_view"]
        result = request.GET["result_to_view"]
        all_bands = Band.objects.all()

        band_name_list = []
        num = 0
        for item in all_bands:
            band_name_list.append(all_bands[num].band_name)
            print(band_name_list)
            num = num + 1

        if len(result) == 0:
            response = {
                'message': "Nothing was ever done_(file_name)!"
            }
        elif result in band_name_list:
            print("Yes")
            response = {
                'message': "This Cover Band is already exist_(file_name)!"
            }
        else:
            current_band = Band(band_name=result)
            current_band.save()
            response = {
                'message': "Was Created!",
                'created_band_name': current_band.band_name,
            }

            ru_alphabet = ['б', 'Б', 'в', 'г', 'Г', 'д', 'Д', 'ё', 'Ё', 'ж', 'Ж', 'з', 'З', 'и', 'И', 'й', 'Й', 'к', 'л', 'Л', 'м', 'н', 'п', 'П', 'т', 'У',
                           'ф', 'Ф', 'ц', 'Ц', 'ч', 'Ч', 'ш', 'Ш', 'щ', 'Щ', 'э', 'Э', 'ю', 'Ю', 'я', 'Я', ];
            en_alphabet = ['b', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'i', 'I', 'k', 'l', 'L', 'm', 'n', 'N', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'u', 'U', 'v',
                           'V', 'w', 'W', 'Y', 'z', 'Z', ]

            current_track = Track.objects.all()
            en_language_alphabet_list = []
            ru_language_alphabet_list = []
            tr_num = 0
            for x in current_track[tr_num].song_name:
                if x in ru_alphabet:
                    ru_language_alphabet_list.append('ru')
                    tr_num = tr_num + 1
                elif x in en_alphabet:
                    en_language_alphabet_list.append('en')
                    tr_num = tr_num + 1
                else:
                    tr_num = tr_num + 1
            if en_language_alphabet_list > ru_language_alphabet_list:
                language_track_par = "en"
            else:
                language_track_par = "ru"

            import_folder_name = ImportFolderName.objects.all()
            current_import_folder_name = import_folder_name[0].name
            current_path = os.getcwd() + "\\" + current_import_folder_name

            import_db = pandas.read_csv(current_path + "\\" + current_band.band_name + ".csv")
            for iter_number in range(import_db.shape[0]):
                current_band.tracks.create(artist_name=import_db.artist[iter_number], song_name=import_db.song[iter_number])

        return JsonResponse(response)

    # os.chdir("C:\\Users\\User\\PycharmProjects\\web\\files")
    # for dir_object in os.listdir():
    #     current_file = dir_object
    # creat_file = open(os.getcwd() + "\\" + current_file, 'w')
    # creat_file.write("band:\n")
    # for w in Band.objects.values_list('band_name', flat=True):
    #     creat_file.write(w + "\n")
    #     print(w)
    # creat_file.close()

