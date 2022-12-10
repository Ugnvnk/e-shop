$(function ($) {

    $('#login_form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            //headers: {'X-CSRFToken': getCookie('csrftoken')},
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.status === 201) {
                    window.location.reload()
                } else if (response.status === 400) {
                    $('.alert-danger').text(response.error).removeClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
            }
        })
    })
})

$(function ($) {

    $('#register_form').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            //headers: {'X-CSRFToken': getCookie('csrftoken')},
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response)
                if (response.status === 201) {
                    window.location.reload()
                } else if (response.status === 400) {
                    $('.alert-danger').text(response.error).removeClass('d-none')
                }
            },
            error: function (response) {
                console.log('err - ', response)
            }
        })
    })
})
