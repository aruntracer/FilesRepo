var ixusername = localStorage.getItem('ixusername');
if (ixusername == null){
  localStorage.setItem('ixredirect','ixredirect');
  window.location.replace("index.html");
};

$("#hi-msg").text('Hi '+ixusername+',');

$('#logout-bt').on("click",function() {
  localStorage.removeItem('ixusername');
  localStorage.removeItem('ixpassword');
});

$('#preserve-bt').on("click",function() {
  window.location.replace("preseveidea.html");
});

$('#view-bt').on("click",function() {
  window.location.replace("viewidea.html");
});
