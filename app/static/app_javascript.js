$(document).ready(function() {
    $('#tr2').hide()
    $('#id20').show()
    $('#id21').hide()

    $('#id45').click(function (e) {
        alert($('#input21').val())
    })
    $('#id100').mouseenter(function (f) {
        $.post(
            "path_3",
            {
                'a': ''
            },
            function (response) {
                alert(response.message)
            }
        );

    })

    $('#id101').keydown(function (f) {
        $.post(
            "path_3",
            {
                'a': ''
            },
            function (response) {
                alert(response.message)
            }
        );
    });



    $("#login").click(function () {
        $.post(
            "path_4",
            {
                'a': $("#login").val()
            },
            function (response) {
                if (response.user_exist) {
                    alert('Такого пользователя уже существует')
                }
            })
    });

    $('#id105').click(function (p) {
        $('#tr1').hide()
        $('#tr2').show()


    })
    $('#id106').click(function (p) {
        $('#tr1').show()
        $('#tr2').hide()

    })

    $('#id_form').click(function (o) {
        $('#id_form_link').onclick()

    })



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


    $("#id105").click(function () {
        $.post(
            "page_1",
            {
                'b': 'artist'
            })

    }),


    $("#id106").click(function () {
        $.post(
            "page_1",
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
});