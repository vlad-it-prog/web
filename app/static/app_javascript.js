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


    $('#id100').click(function (f) {
        $.post(
            "ajax_clock",
            {
                'a': ''
            },
            function (response) {
                $('#100_1').attr({"placeholder": response.message})
            }
        );
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


    $('#id_time').mouseenter(function (f) {
        $.post(
            "ajax_clock",
            {
                'k': ''
            },
            function (response) {
                alert(response.message)
            }
        );

    })
//______________________________________________________________________________________________________________________


    $("#delete_cb_yes").click(function () {
        $.get(
            "delete_cover_band",
            {
                'select_to_delete_cover_band': $("#delete_cb_select").val()
            }),
        window.location.pathname = '/main_page'
        alert(('Cover Band "') + $("#delete_cb_select").val() + ('" was deleted successfully!'))
    })
//______________________________________________________________________________________________________________________


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

});
