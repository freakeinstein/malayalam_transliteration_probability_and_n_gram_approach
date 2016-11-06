// author: fennecfox

// function to get current cursor location
function getCaret(el) {
  if (el.selectionStart) {
    return el.selectionStart;
  } else if (document.selection) {
    el.focus();

    var r = document.selection.createRange();
    if (r == null) {
      return 0;
    }

    var re = el.createTextRange(),
        rc = re.duplicate();
    re.moveToBookmark(r.getBookmark());
    rc.setEndPoint('EndToStart', re);

    return rc.text.length;
  }
  return 0;
}
/*
//function to suggest malayalam words
function fillWords(box){
    alert("fillWords");
    var textarea = box;
    textarea.focus();
    var currentPos = getCaret(textarea);
    alert(currentPos);

    var tex="";
    var i=0;
    while(textarea.value.charAt(currentPos-i) != " " && currentPos-i > 0){
	    tex+=textarea.value.charAt(currentPos-i);
	    i++;
    }
    tex = textarea.value.substring(currentPos-i,currentPos);
    var malayalam = get_ml(tex);

    var textsuggest = document.getElementById('suggest-para');
    textsuggest.innerHTML = malayalam;

}*/

//function to insert converted malayalam text
function InsertText(from,to) {
    var currentPos = GPS;

    var tex="";
    var i=0;
    /*while(to.val().charAt(currentPos-i) != " " && currentPos-i > 0){
	    tex+=to.val().charAt(currentPos-i);
	    i++;
    }
    tex = to.val().substring(currentPos-i,currentPos);*/
    var malayalam = from.text();
    tex = to.val();
    //tex = tex.replaceAt(currentPos-i,currentPos," "+malayalam+" ");
    to.val(tex.substring(0, GPS) + malayalam + " " + tex.substring(GPS) );
}

/*
//function to replace old english word with new malayalam word
String.prototype.replaceAt=function(sindex, eindex, replace) {
    return this.substr(0, sindex) + replace + this.substr(eindex+replace.length);
}*/




// author: fennecfox

var GPS=0;
var DICT = {}

$(document).delegate('.ta_in', 'keydown', function(e) { 
  var keyCode = e.keyCode || e.which; 

  if (keyCode == 9) { 
    e.preventDefault(); 
    var start = $(this).get(0).selectionStart;
    var end = $(this).get(0).selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    $(this).val($(this).val().substring(0, start)
                + "\t"
                + $(this).val().substring(end));

    // put caret at right position again
    $(this).get(0).selectionStart = 
    $(this).get(0).selectionEnd = start + 1;
  } 
});


$(document).keyup(function(e) {

  if (e.keyCode == 27) { 
      displaySuggestionBox(false,e.which);
      $(".ta_in").focus();
  }   // esc
});

$(document).ready(function(){
	
	var white_space = false;
    $( "#overlay-layer" ).hide();
	
	$(".ta_in").on('keydown',function(e){
		//if(e.which == 32 || e.which == 13 || e.which == 9){
        if (!(/[a-zA-Z0-9/|]/.test(String.fromCharCode(e.which)))){
			displaySuggestionBox(false,e.which);
		}else{
            GPS = getCaret(this);                           // gtore position of text to be inserted
			displaySuggestionBox(true,e.which);
		}

	});
    
    $("#mangleesh-input").on('keyup',function(e){
		if(e.which == 32 || e.which == 13 || e.which == 9){
			displaySuggestionBox(false,e.which);
            $(".ta_in").focus();                             // PIPE LOCATION FOR WRITE MODULE..
            InsertText($("#malayalam-suggestion"),$(".ta_in"));
		}else{
      suggestWOrds(this,$("#malayalam-suggestion"));//this);
      if(e.which == 220){
        var mangleesh_modified = ($( "#mangleesh-input" ).val()).replace(/\\/g,'');
        console.log("special training "+$("#malayalam-suggestion").text()+" - "+mangleesh_modified)
        train_server_with_new_pair($("#malayalam-suggestion").text(),mangleesh_modified)
      }
		}

	});
});

function displaySuggestionBox(display,ch){
	if(display){
        animateBlurEffect(true);
		$( "#overlay-layer" ).show();
		$( "#mangleesh-input" ).val("").focus();
        $( "#mangleesh-input-reflection" ).text($( "#mangleesh-input" ).val());
	}else{
        animateBlurEffect(false);
	}
}


//function to suggest malayalam words
function suggestWOrds(source,target){
	get_suggestion_from_server(source.value)
    target.text( get_ml(source.value) );
}

function put_suggestion_directly(malayalam){
	$("#malayalam-suggestion").text(malayalam);
  $( "#mangleesh-input" ).focus();
}

function animateBlurEffect(animate){
    if(animate){
        $( "#overlay-layer" ).animate({
            opacity: 0.95
            }, 500, function() {
            // Animation complete.
            });
       /* $('.ta_in')
            .css({
               'filter'         : 'blur(2px)',
               '-webkit-filter' : 'blur(2px)',
               '-moz-filter'    : 'blur(2px)',
               '-o-filter'      : 'blur(2px)',
               '-ms-filter'     : 'blur(2px)'
            }); */
    }else{
        $( "#overlay-layer" ).animate({
            opacity: 0
            }, 500, function() {
            // Animation complete.
		$( "#overlay-layer" ).hide();
            });
    }
}