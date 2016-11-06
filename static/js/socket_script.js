var socket = io();

  socket.on('connect', function(){
  	
  });

 /* socket.on('event', function(data){

  });
  socket.on('disconnect', function(){});*/

  socket.on('transliteration_success', function (malayalam) {
    console.log("from: "+malayalam);
    if(malayalam){
      var segments = malayalam.split(":");
      var unique_segments = [];
      $.each(segments, function(i, el){
          if($.inArray(el, unique_segments) === -1) unique_segments.push(el);
      });
      if(unique_segments.length>1){
        put_suggestion_directly(unique_segments[0]);
        create_dynamic_suggestion_buttons_from_string_Input(unique_segments)
      }
    }
});

function get_suggestion_from_server(mangleesh) {
    console.log("to: "+mangleesh);
    $( "#dyn_butt" ).remove();
    number = 0
    if(mangleesh){
      socket.emit('request_transliteration', { client_input: mangleesh });
    }
  }

function train_server_with_new_pair(malayalam_val,mangleesh_val) {
    console.log("to traiin: "+mangleesh_val+" - "+malayalam_val);
      socket.emit('request_learning', { malayalam : malayalam_val,
                                        mangleesh : mangleesh_val });
}
