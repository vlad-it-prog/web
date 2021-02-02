from django.urls import path
from app.views import \
    main_page, test, login_user, do_logout, \
    login_page, register, registration, ajax_path, ajax_valid, \
    ajax_cb, band_list, \
    page_3, main_test_cash, test_html, help_page, \
    add_new_cover_band_to_band_list, delete_cover_band, add_cover_band, cover_bands_details, \
    rename_export_folder, name_export_file, sort_track_list_change, player, start_page, language, \
    history, new, rename_import_folder, import_file_to_database, import_file

urlpatterns = [

    path('', start_page),
    path('login_page', login_page),
    path('registration', registration),  # Путь к странице с формой регистрации      (registration.html)

    path('main_page', main_page),  # Путь к главной странице                   ('main_page.html')
    path('help_page', help_page),  # Путь к странице помощи                    ('help_page.html')

    path('add_new_cover_band_to_band_list', add_new_cover_band_to_band_list),

    # Путь к странице с формой Login

    path('login_user', login_user),  #
    path('test', test),  # Путь к тестовой страние                   (test.html)
    path('do_logout', do_logout),  #
    path('register', register),  #
    path('path_4', ajax_valid),  #
    path('path_5', ajax_cb),  #
    # path('path_7', button_ok),                      #
    path('path_8', band_list),  #
    # path('path_9', exchange_rates),
    # path('path_10', experiment),
    path('page_3', page_3),  # Путь к тестовой странице                  ('page_3.html')
    path('path_11', main_test_cash),  # Путь к тестовой функции кеширования
    # данных на странице page_3.html            ('page_3.html')

    path('error', test_html),
    path('ajax_path', ajax_path),
    path('delete_cover_band', delete_cover_band),
    path('add_cover_band', add_cover_band),
    path('cover_bands_details', cover_bands_details),
    path('rename_export_folder', rename_export_folder),
    path('name_export_file', name_export_file),
    path('sort_track_list_change', sort_track_list_change),
    # path('song_list_page', song_list_page),
    path('player', player),
    path('language', language),
    path('history', history),
    path('new', new),
    path('rename_import_folder', rename_import_folder),
    path('import_file_to_database', import_file_to_database),
    path('import_file', import_file),

]
