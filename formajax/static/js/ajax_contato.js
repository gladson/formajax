function validateInput(input) { 
	$.post('/contato/ajax_contato/validando/?field=' + input.attr('id').replace('id_', ''), 
		$('form').formToArray(), function(data) {
			var json = '(' + data + ')';
			showErrors(input, json.errors);
		} 
	); 
}

$(function() { 
	$(':input').blur(function() { 
		validateInput($(this)); 
	}); 
});

function relatedErrorList(input, input_name){
	var prevUL = $(input).parent().prev();
	if (prevUL && prevUL.attr('class') == 'errorlist') {
		return prevUL;
	}
	var errorlist = $('<ul class="errorlist"></ul>');
	input.parent().before(errorlist);
	return errorlist;
}

function showErrors(input, errors) {
	var errorlist = relatedErrorList(input);
	errorlist.empty();
	//$.each(errors, function(index, error) {
	if(errors != undefined && errors != undefined){
		errorlist.append('<li>' + error + '</li>');
	//});
	}
}