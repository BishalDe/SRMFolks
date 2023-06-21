let navbtn=document.getElementById("menubtn");
let container1=document.getElementById("container1");

navbtn.addEventListener("click",function(){
    container1.classList.toggle("active");
    navbtn.classList.toggle("liactive");
});