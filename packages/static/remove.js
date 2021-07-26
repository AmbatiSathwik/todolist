
$(document).ready(function(){

$('.remove').click(function () {
    const remove = $(this)
    $.ajax({
        type: 'POST',
        async: true,
        url: '/delete/' + remove.data('source'),
        success: function (res) {
            console.log(res.response)
            location.reload();
        },
        error: function () {
            console.log('Error');
        }
    });
});

$('.today').click(function () {
    let url = window.location.href;
    if (url.slice(-6) != '/today'){
        url = url + '/today'
        window.location.replace(url);
    }
    else{
        location.reload();
    }
});

});


