/* alert('here in index.js'); */
function validation(){
  var ixpassword = document.querySelector("#password").value;
  var ixusername = document.querySelector("#username").value;
  alert('index js '+ixusername);
  localStorage.setItem('ixusername',ixusername);
  if (ixpassword === "test"){
    return window.location.replace("home.html");
  }else {
    alert("password is incorrect, try again");
    return false;
  }
}
