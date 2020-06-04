$(document).foundation();

$(document).ready(
    $('#flash-messages')
    .slideDown(500, 'swing')
    .fadeIn(1000, 'swing')
    .delay(1000)
    .fadeOut(2000, 'swing')
    .slideUp(2000, 'swing', function () {
        $(this).remove()
    })
)
