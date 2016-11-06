var number = 0;

function create_dynamic_suggestion_buttons_from_string_Input(unique_segments){
    //var splitter = string_in.split(":");
    var splitter = unique_segments;
    var $input = $('<br/><div id="dyn_butt"></div>');
    $input.appendTo($("#container"));
    for (i=1;i<splitter.length-1 ;i++){
        var $input = $('<button class="dynamic_buttons_for_suggestion" id="'+number+'" onclick="dynamic_suggestion_button_event_function('+number+',\''+splitter[i]+'\')">'+splitter[i]+'</button>');
        $input.appendTo($("#dyn_butt"));
        number++;
    }
}

function dynamic_suggestion_button_event_function(num,str){
    put_suggestion_directly(str)
}
