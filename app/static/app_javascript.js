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
    })
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

    // delete_cover_band End______________________________________________________________________________________________________________________

    // $("#add_cb_open_folder").click(function f() {
    //     if ($("#add_cb_select").val() > "") {
    //         $("#add_cb_open_folder").val().attr({"disabled": true})
    //     } else {
    //         $("#add_cb_open_folder").val().attr({"disabled": false})
    //     }
    // })
    $("#add_cb_open_folder").click(function f() {
        $("#add_cb_select").val(onreset)
        $("#add_cb_select").hide()
    });
    $("#add_cb_select").click(function f() {
        $("#add_cb_open_folder").val(onreset)
        $("#add_cb_open_folder").hide()
    });
    $("#import_file_name_reset").click(function f() {
        $("#add_cb_open_folder").val(onreset)
        $("#add_cb_open_folder").attr({"disabled": false})
        $("#add_cb_open_folder").show()
        $("#add_cb_select").val(onreset)
        $("#add_cb_select").attr({"disabled": false})
        $("#add_cb_select").show()
    });

    // (function (){
    //     if ($("#add_cb_select").val() == "") {
    //         $("#add_cb_open_folder").attr({"disabled": false})
    //     } else if ($("#add_cb_open_folder").val() == "") {
    //         $("#add_cb_select").attr({"disabled": false})
    //     };
    // })
    // $("#add_cb_open_folder").click(function f() {
    //     $("#add_cb_open_folder").attr({"disabled": false})
    //     $("#add_cb_select").val(onreset)
    //     $("#add_cb_select").attr({"disabled": true})
    // })
    // $("#add_cb_select").click(function f() {
    //     $("#add_cb_select").attr({"disabled": false})
    //     $("#add_cb_open_folder").val(onreset)
    //     $("#add_cb_open_folder").attr({"disabled": true})
    // })

    $("#add_cb_open_folder").change(function () {
        $.get(
            "import_file",
            {
                // 'new_export_file_name': $(document).forms["export_form"].export_file_name.value
                'add_cb_open_folder_form': $("#add_cb_open_folder").val()
                // 'add_cb_open_folder_form': $("#add_cb_open_folder").attr("value")
            },
            // $("#add_cb_select").val( ""),
            (function (response) {
                // document.getElementById("add_cb_select").val = response["message"],
                // document.getElementById("add_cb_select").attr({"placeholder": response["message"]}),
                // $("#add_cb_select").placeholder = response["message"],
                // $("#add_cb_select").val(onreset)

                // if ($("#add_cb_open_folder").val() > "") {
                //     $("#add_cb_select").attr({"value": response["message"]})
                //     $("#add_cb_select").attr({"disabled": true})
                // } else {
                //     $("#add_cb_select").attr({"disabled": false})
                //     $("#add_cb_select").attr({"value": ""})
                //     // $("#add_cb_select").show()
                // };
                alert(response['message'])
                $.get(
                "import_file_to_database",
                {
                    'result_to_view': response['message']
                },
                    (function (response) {
                        if ($("#add_cb_open_folder").show()){
                        if (response["message"] == "Nothing was ever done_(file_name)!") {
                            alert("You have not enter the Cover Band name! Please, try again.")
                        } else if (response["message"] == "This Cover Band is already exist_(file_name)!") {
                            alert("This Cover Band is already exist! Please, try again.")
                        } else if (response["message"] == "Was Created!") {
                            alert('Cover Band "' + response["created_band_name"] + '" was added successfully!')
                        } else {
                            alert("Что-то пошло не так")
                        };
                        // window.location.pathname = '/main_page'
                            }

                    }),
                )
            })
        )
    });

    $("#add_cb_yes").click(function () {
         $.get(
            "add_cover_band",
            {
                'select_to_add_cover_band': $("#add_cb_select").val()
            },
            (function (response) {
                if ($("#add_cb_select").show()) {
                if (response.message == "Nothing was ever done!") {
                    alert("You have not enter the Cover Band name! Please, try again.")
                    // $("#main_menu_add_cover_band").selected()
                } else if (response.message == "This Cover Band is already exist!") {
                    alert(("This Cover Band is already exist! Please, try again."))
                } else {
                    alert(('Cover Band "') + $("#add_cb_select").val() + ('" was added successfully!'))
                }
                }
            })
        );
        window.location.pathname = '/main_page'
    })

     //     function (response) {
     //        alert(response.message)
     //        document.getElementById("#add_cb_file_name").attr({"placeholder": response.message})
     //     });

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
                    document.getElementById("language").click()
                } else {
                    alert(('Export Folder was renamed "') + $("#new_export_folder_name_input").val() + ('" successfully!'))
                    document.getElementById("language").click()
                }
            })
        );
        $.get(
            "rename_import_folder",
            {
                'new_import_folder_name': $("#new_import_folder_name_input").val()
            },
            (function (response) {
                if (response.message == "don't alert") {
                } else {
                    alert(('Import Folder was renamed "') + $("#new_import_folder_name_input").val() + ('" successfully!'))
                }
            })
        )
    })

    // rename_export_folder End_________________________________________________________________________________________
    // rename_import_folder End_________________________________________________________________________________________


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

    
    $('#do_logout_button').click(function () {
        $.post(
            "do_logout",
            {
                'k': ''
            },
            // function (response) {
            //     alert(response.message)
            // }
        );
    });

//______________________________________________________________________________________________________________________

    //     """ URL:
    //         Function:
    //         File:
    //         Element path (web/html):
    //         JS path: """

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
        if (document.getElementById('time')) {
            document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
        }
        t = setTimeout(function() {
            startTime()
        }, 500);
    }
    startTime();
//______________________________________________________________________________________________________________________

//______________________________________________________________________________________________________________________

    //    """ URL: rename_export_folder
    //         Function: rename_export_folder
    //         File: main_page.html
    //         Element path (web/html): "MAIN MENU" button --> "Settings" button --> "Settings Modal Window" --> "Export Files Folder
    //         Name:..." input + "Save Changes" button
    //         JS path: """

    $("#add_cb_open_folder_button").click(function () {
        document.getElementById("open_folder_hidden").click()
    })
//______________________________________________________________________________________________________________________

    //     $("#add_cb_yes").click(function () {
    //     $.get(
    //         "name_import_file",
    //         {
    //             // 'new_export_file_name': $(document).forms["export_form"].export_file_name.value
    //             'new_import_file_name': $("#add_cb_select").val()
    //         },
    //         (function (response) {
    //             if ($("#add_cb_select").val() == "") {
    //                 alert('File "' + response.message + '.csv" was successfully created on path !')
    //                 window.location.pathname = '/main_page'
    //             } else if (response.message == "This Cover Band name does not exist in the Band list! Please, try again!") {
    //                 alert(response.message)
    //                 window.location.pathname = '/main_page'
    //                 // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
    //             } else {
    //                 alert('File "' + response.message + '.csv" was successfully created on path !')
    //                 window.location.pathname = '/main_page'
    //                 // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
    //             }
    //         })
    //     )
    // });
 //______________________________________________________________________________________________________________________

    // // $("#add_cb_open_folder").blur(function () {
            // (function (response) {
            //     if ($("#export_cb_name_select").val() == "") {
            //         alert('File "' + response.message + '.csv" was successfully created on path !')
            //         window.location.pathname = '/main_page'
            //     } else if (response.message == "This Cover Band name does not exist in the Band list! Please, try again!") {
            //         alert(response.message)
            //         window.location.pathname = '/main_page'
            //         // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
            //     } else {
            //         alert('File "' + response.message + '.csv" was successfully created on path !')
            //         window.location.pathname = '/main_page'
            //         // $('#new_export_folder_name_input').attr({"placeholder": $("#new_export_folder_name_input").val()})
            //     }
            // })
    //     )
    // });

     $("#track_list_menu_1").mouseenter(function () {
         alert("Привет, ты выбрал Full Track List")
     });
     $("#track_list_menu_2").mouseup(function () {
         alert("Привет, ты выбрал Foreign Track List")
     });
     $("#track_list_menu_3").mouseup(function () {
         alert("Привет, ты выбрал Domestic Track List")
     });

});
