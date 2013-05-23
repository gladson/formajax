jQuery(function ($) {
    var body_find_form = $('body').find('form');
    var count, add_count_forms = $('form');
    for (count = 1; count <= body_find_form.length; count++){
        add_count_forms.eq(count).addClass('form' + count);
        var forms_in_body = $('.form' + count);
    }

    //var contato_form = $('.form-signin');
    forms_in_body.ajaxForm({
        url: this.action,
        dataType: 'json',
        success: function (json) {

            if ((json.errors).length !== 0) {
                process_form_errors(json, forms_in_body);

                $('.form-signin').each(function () {
                    $(this).find('div.control-group').each(function () {
                        if ($(this).find('.errorlist').length <= 0) {
                            $(this).removeClass('error').addClass('control-group required').fadeIn(4500);
                        } else if ($(this).find('.errorlist').length >= 0) {
                            $(this).removeClass('required').addClass('control-group error').fadeIn(4500);
                        } else {
                            hide_form_errors();
                            $(this).removeClass('error').addClass('control-group required').fadeIn(4500);
                        }
                    });
                });
            }

        },
        error: function (json) {
            $('.form-signin').find("input[type=text], input[type=password], input[type=email], input[type=checkbox], input[type=radio], textarea").val("");
            hide_form_errors();

            $('<div class="alert alert-success save">Salvo com sucesso!</div>').fadeIn(2500).insertAfter('.form-signin-heading').fadeOut(3000, function () {
                $('.save').remove();
            });
            $('.control-group').addClass('control-group success').fadeIn(4500).delay(4000).fadeOut(1, function () {
                $('.control-group').removeClass('error success').addClass('required').css({
                    display: 'block'
                });
            });
        }
    });
});

function hide_form_errors() {
    $('.errorlist').remove();
}

function process_form_errors(json, form) {
    hide_form_errors();
    errors = json.errors;

    if (errors.__all__ !== undefined) form.append(errors.__all__);

    prefix = form.find(":hidden[name='prefix']").val();

    prefix == undefined ? prefix = '' : prefix = prefix + '-';
    for (field in errors)
    $('#id_' + prefix + field).after(errors[field]);

}