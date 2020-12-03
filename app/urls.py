from django.urls import path
from app.views import \
    main_page, main, test, login_user, do_logout, logout_page, \
    login_page, register, registration_form, ajax_clock, ajax_valid, \
    ajax_cb, band_list, \
    page_3, main_test_cash, login, test_html, help_page, add_new_cover_band_to_band_list, ajax_clock


urlpatterns = [

    path('login_page', login_page),
    path('registeration', registration_form),  # Путь к странице с формой регистрации      (registration.html)


    path('main_page', main_page),                      # Путь к главной странице                   ('main_page.html')
    path('help_page', help_page),                      # Путь к странице помощи                    ('help_page.html')

    path('add_new_cover_band_to_band_list', add_new_cover_band_to_band_list),
    path('ajax_clock_path', ajax_clock),


    # Путь к странице с формой Login
    # path('main_page', index),
                        #
    path('main', main),                             #
    path('main_error', login_user),                 #
    path('test', test),                             # Путь к тестовой страние                   (test.html)
    path('logout_page', logout_page),               #
    path('logout', do_logout),                      #

    path('register_2', register),                   #
               #
    path('path_4', ajax_valid),                     #
    path('path_5', ajax_cb),                        #
    # path('path_7', button_ok),                      #
    path('path_8', band_list),                      #
    # path('path_9', exchange_rates),
    # path('path_10', experiment),
    path('new_page_3', page_3),                     # Путь к тестовой странице                  ('page_3.html')
    path('path_11', main_test_cash),                # Путь к тестовой функции кеширования
                                                    # данных на странице page_3.html            ('page_3.html')

    path('error', test_html),


]

