$(function () {

    $(function() {
                $( "#dialog" ).dialog();
              });

    $('[data-update-from]').each(function() {
        var url = $(this).data('update-from');
        $('#comments').load(url);
    });

    $('[data-like]').each(function() {
        var url = $(this).data('like');
        $('#likes').load(url);
    });

    $(function() {
        $('#to_like').click (function() {
        var url = $(this).data('like').valueOf();
            alert(url);
            $('#likes').load(url);
        })
    });


    $('.chosen-select').chosen({no_results_text: "Запрашиваемые топики не найдены"});

    $(function() {
        $('#open').click (function() {
            $('#ok-dialog').dialog ({
                modal: true,
                title: 'О нас',
                show: 'blind',
                hide: 'blind',
                buttons: {
                    "Ясно, понятно": function() {
                        $(this).dialog("close");
                    },
                    "Давай ещё раз, я не понял": function() {
                        $(this).dialog("close")
                    },
                }


            });

            setTimeout (function() {
                $('#ok-dialog').dialog ('close');
            }, 3000);
        });
    });
});



