$(document).ready(function() {
  $("p").click(function() {
    $("<p>This is a click Event</p>").appendTo("body");
  });
  
  $("p").dblclick(function() {
    $("<p>This is a double-click Event</p>").appendTo("body");
  });
});


/*
#!/usr/bin/node

$("p").bind("click", function(){
   $( "This is a click Event").appendTo( "body" );
});

$("p").bind("dblclick", function(){
   $( "This is a double-click Event"  ).appendTo( "body" );
});

*/
