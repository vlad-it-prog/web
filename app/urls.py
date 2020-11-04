from django.urls import path
from app.views import index, main_page, main, test, login_user, do_logout, logout_page, \
main_page_2, register, registration_form, ajax_path, ajax_valid, ajax_cb, button_ok, band_list, experiment, exchange_rates, page_3



urlpatterns = [
    path('main_page', index),
    path('page_1', main_page),
    path('page_3', main_page_2),
    path('main', main),
    path('main_error', login_user),
    path('test', test),
    path('logout_page', logout_page),
    path('logout', do_logout),
    path('register_1', registration_form),
    path('register_2', register),
    path('path_3', ajax_path),
    path('path_4', ajax_valid),
    path('path_5', ajax_cb),
    path('path_7', button_ok),
    path('path_8', band_list),
    path('path_9', exchange_rates),
    path('path_10', experiment),
    path('new_page_3', page_3)

]

