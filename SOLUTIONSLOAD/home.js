var ixusername = localStorage.getItem('ixusername');
if (ixusername == null){
  localStorage.setItem('ixredirect','ixredirect');
  window.location.replace("index.html");
};

var logoutbt = $('.logout-bt');
var welcomemsg = $("#welcomemsg");
if (ixusername){
  welcomemsg.text('Welcome to SolutionsLoad! '+ixusername);
}else {
  welcomemsg.text('Welcome to SolutionsLoad!');
};
logoutbt.on("click",function() {
  localStorage.removeItem('ixusername');
  localStorage.removeItem('ixpassword');
});
