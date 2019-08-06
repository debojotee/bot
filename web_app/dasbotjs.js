

function send_msg(){
  var msg=document.getElementById("data").value
  eel.input(msg)(show_msg)
  var ul = document.getElementById("texts");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(msg));
  li.setAttribute("class", "text_wrapper_right");
  ul.appendChild(li);
}


function show_msg(str){
  var ul = document.getElementById("texts");
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(str));
  li.setAttribute("class", "text_wrapper_left"); // added line
  ul.appendChild(li);
}