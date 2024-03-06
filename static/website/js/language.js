$(".language-list").on("click", ".init", function() {
    $(this).closest(".language-list").children('li:not(.init)').toggle();
});

var allOptions = $(".language-list").children('li:not(.init)');
$(".language-list").on("click", "li:not(.init)", function() {
    allOptions.removeClass('selected');
    $(this).addClass('selected');
    $(".language-list").children('.init').html($(this).html());
    allOptions.toggle();
});