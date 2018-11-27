var stusername = localStorage.getItem('ixusername');
var stpassword = localStorage.getItem('ixpassword');
var stredirect = localStorage.getItem('ixredirect');

if (stusername == null && stredirect != null){
  localStorage.removeItem('ixredirect');
  window.alert('You are not logged in, Please login!');
};

if (stusername != null && stpassword != null){
  validation();
};

function validation(){
  var ixpassword = document.querySelector("#password").value;
  var ixusername = document.querySelector("#username").value;
  localStorage.setItem('ixusername',ixusername);
  localStorage.setItem('ixpassword',ixpassword);
  if (ixusername != "arun" && ixpassword != "test" ){
    return window.location.replace("home.html");
  }else {
    alert("password is incorrect, try again");
    return false;
  }
}
