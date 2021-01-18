$(document).ready(function() {

    $('#tr2').hide()
    $('#id20').show()
    $('#id21').hide()
//______________________________________________________________________________________________________________________


    $('#all_bands-add_cover_band_button').click(function (p) {
        // $('#add_cover_band_cancel_button').hide() ?????????????????????????????????????????????????????????????

    })
//______________________________________________________________________________________________________________________


    $('#id45').click(function (e) {
        alert($('#input21').val())
    })
//______________________________________________________________________________________________________________________


    // $('#id101').keydown(function (f) {
    //     $.post(
    //         "path_3",
    //         {
    //             'a': ''
    //         },
    //         function (response) {
    //             alert(response.message)
    //         }
    //     );
    // });
//______________________________________________________________________________________________________________________


    // $("#login").click(function () {
    //     $.post(
    //         "path_4",
    //         {
    //             'a': $("#login").val()
    //         },
    //         function (response) {
    //             if (response.user_exist) {
    //                 alert('Такого пользователя уже существует')
    //             }
    //         })
    // });
//______________________________________________________________________________________________________________________


    $("#Cover-Band-1-selection").click(function (e) {
        alert('Такого пользователя уже существует')
    });
//______________________________________________________________________________________________________________________


    $('#id105').click(function (p) {
        $('#tr1').hide()
        $('#tr2').show()


    })
//______________________________________________________________________________________________________________________


    $('#id106').click(function (p) {
        $('#tr1').show()
        $('#tr2').hide()

    })
//______________________________________________________________________________________________________________________


    $('#id_form').click(function (o) {
        $('#id_form_link').onclick()

    })
//______________________________________________________________________________________________________________________


    $(".class-band-menu").keydown(function () {
        $.post(
            "path_5",
            {
                'a': $(".class-band-menu").val()
            },
            function (response) {
                alert(response.message)
            })
    });
//______________________________________________________________________________________________________________________


    $("#id120").click(function () {
        $.post(
            "path_5",
            {
                'a': ''
            }),
        window.location.pathname = '/path_7'
        alert('Файл был удачно создан')
    })

    $("#id121").click(function () {
        window.location.pathname = '/path_8'
    })
//______________________________________________________________________________________________________________________


    $("#id105").click(function () {
        $.post(
            "main_page",
            {
                'b': 'artist'
            })

    }),
//______________________________________________________________________________________________________________________


    $("#id106").click(function () {
        $.post(
            "main_page",
            {
                'b': 'song'
            })

    })
        $("#id122").click(function () {
        window.location.pathname = '/path_8'
    })
    $("#id123").click(function () {
        window.location.pathname = '/path_9'
    })
//______________________________________________________________________________________________________________________

        // """ URL: delete_cover_band
        // Function: delete_cover_band
        // File: main_page.html
        // Element path (web/html): "MAIN MENU" button --> "Delete Cover Band" button --> "Delete Cover Band Modal Window"
        // --> "Export Files Folder
        // Name:..." input + "Delete" button
        // JS path: """

    $("#delete_cb_yes").click(function () {
        $.get(
            "delete_cover_band",
            {
                'select_to_delete_cover_band': $("#delete_cb_select").val()
            },
            (function (response) {
                if (response.message == "Nothing was ever done!") {
                    // window.location.pathname = '/main_page'
                    alert(("You have not enter the Cover Band name! Please, try again."))
                    // $("#main_menu_add_cover_band").selected()
                    window.location.pathname = '/main_page'
                } else if (response.message == "This Cover Band does not exist in the band list!") {
                    // window.location.pathname = '/main_page'
                    alert(("This Cover Band does not exist in the band list! Please, try again."))
                    window.location.pathname = '/main_page'
                } else {
                    alert(('Cover Band "') + $("#delete_cb_select").val() + ('" was deleted successfully!'))
                    window.location.pathname = '/main_page'
                }
            })
        )
    })
            // ),
    //     window.location.pathname = '/main_page'
    //     alert(('Cover Band "') + $("#delete_cb_select").val() + ('" was deleted successfully!'))
    // })
    // delete_cover_band End______________________________________________________________________________________________________________________


    $("#add_cb_yes").click(function () {
        $.get(
            "add_cover_band",
            {
                'select_to_add_cover_band': $("#add_cb_select").val()
            },
            (function (response) {
                if (response.message == "Nothing was ever done!") {
                    // window.location.pathname = '/main_page'
                    alert(("You have not enter the Cover Band name! Please, try again."))
                    // $("#main_menu_add_cover_band").selected()
                    window.location.pathname = '/main_page'
                } else if (response.message == "This Cover Band is already exist!") {
                    // window.location.pathname = '/main_page'
                    alert(("This Cover Band is already exist! Please, try again."))
                    window.location.pathname = '/main_page'
                } else {
                    window.location.pathname = '/main_page'
                    alert(('Cover Band "') + $("#add_cb_select").val() + ('" was added successfully!'))
                }
            })
        )
    })
    //         ),
    //     window.location.pathname = '/main_page'
    //     alert(('Cover Band "') + $("#add_cb_select").val() + ('" was added successfully!'))
    // })
//______________________________________________________________________________________________________________________


    $("#cover_bands_details_start").click(function () {
        $.get(
            "cover_bands_details",
            {
                'cover_band_1_details': $("#cover_band_1_details").val(),
                'cover_band_2_details': $("#cover_band_2_details").val()
             })
        // window.location.pathname = '/main_page'
        // alert(('Cover Band "') + $("#add_cb_select").val() + ('" was added successfully!'))
    })
//______________________________________________________________________________________________________________________


    //    """ URL: rename_export_folder
    //         Function: rename_export_folder
    //         File: main_page.html
    //         Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
    //         Name:..." input + "Save Changes" button
    //         JS path: """

    $("#settings_save_changes_button").click(function () {
        $.get(
            "rename_export_folder",
            {
                'new_export_folder_name': $("#new_export_folder_name_input").val()
            },
            (function (response) {
                if (response.message == "don't alert") {
                    window.location.pathname = '/main_page'
                } else {
                    window.location.pathname = '/main_page'
                    alert(('Fxport Folder was renamed "') + $("#new_export_folder_name_input").val() + ('" successfully!'))
                    // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
                }
            })
        )
    })

    // rename_export_folder End_________________________________________________________________________________________

    //    """ URL: name_export_file
    //         Function: name_export_file
    //         File: main_page.html
    //         Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
    //         Name:..." input + "Save Changes" button
    //         JS path: """

    $("#export_cb_yes").click(function () {
        $.get(
            "name_export_file",
            {
                // 'new_export_file_name': $(document).forms["export_form"].export_file_name.value
                'new_export_file_name': $("#export_cb_name_select").val()
            },
            (function (response) {
                if ($("#export_cb_name_select").val() == "") {
                    alert('File "' + response.message + '.csv" was successfully created on path !')
                    window.location.pathname = '/main_page'
                } else if (response.message == "This Cover Band name does not exist in the Band list! Please, try again!") {
                    alert(response.message)
                    window.location.pathname = '/main_page'
                    // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
                } else {
                    alert('File "' + response.message + '.csv" was successfully created on path !')
                    window.location.pathname = '/main_page'
                    // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
                }
            })
        )
    });

    // rename_export_folder End_________________________________________________________________________________________


        //    """ URL: rename_export_folder
    //         Function: rename_export_folder
    //         File: main_page.html
    //         Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
    //         Name:..." input + "Save Changes" button
    //         JS path: """

    $("#id_reverse").click(function () {
        $.get(
            "sort_track_list_change",
            {
                // 'new_export_file_name': $(document).forms["export_form"].export_file_name.value
                'reverse_mode': "artist"
            },

        )
    });
    // $("#id106").click(function () {
    //     $.get(
    //         "sort_track_list_change",
    //         {
    //             'reverse_mode': "artist"//$("#new_export_folder_name_input").val()
    //         })})
    //         },
    //         (function (response) {
    //             if (response.message == "don't alert") {
    //                 window.location.pathname = '/main_page'
    //             } else {
    //                 window.location.pathname = '/main_page'
    //                 alert(('Fxport Folder was renamed "') + $("#new_export_folder_name_input").val() + ('" successfully!'))
    //                 // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
    //             }
    //         })
    //     )
    // })

    // _________________________________________________________________________________________

    // $(function (f) {
    //     $.post(
    //         "login_user",
    //         {
    //             'a': ''
    //         },
    //         // window.location.pathname = '/login_page',
    //         // alert(response.message)
    //     );
    // })

    $('#do_logout_button').click(function (f) {
        $.post(
            "do_logout",
            {
                'k': ''
            },
            // function (response) {
            //     alert(response.message)
            // }
        );

    })



    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }

    function startTime() {
        var today = new Date();
        var h = today.getHours();
        var m = today.getMinutes();
        var s = today.getSeconds();
        // add a zero in front of numbers<10
        m = checkTime(m);
        s = checkTime(s);
        document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
        t = setTimeout(function() {
            startTime()
        }, 500);
    }
    startTime();
//______________________________________________________________________________________________________________________

    //     """ URL:
    //         Function:
    //         File: main_page.html
    //         Element path (web/html):
    //         Name:..."
    //         JS path: """


    // $("#settings_save_changes_button").click(function () {
    //     $.get(
    //         "language",
    //         {
    //             'language': $("#language").val()
    //          })
    // })
//______________________________________________________________________________________________________________________

});
