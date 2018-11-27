var ixusername = localStorage.getItem('ixusername');
/* alert('home js '+ixusername); */
var welcomemsg = $("#welcomemsg");
if (ixusername){
  welcomemsg.text('Welcome to SolutionsLoad! '+ixusername);
}else {
  welcomemsg.text('Welcome to SolutionsLoad!');
}
