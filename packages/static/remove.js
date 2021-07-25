
function main(){
$('.remove').click(function () {
    const remove = $(this)
    $.ajax({
        type: 'POST',
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
}

$(main);
