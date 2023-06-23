let navbtn=document.getElementById("menubtn");
let container1=document.getElementById("container1");

navbtn.addEventListener("click",function(){
    container1.classList.toggle("active");
    navbtn.classList.toggle("liactive");
});


const width = window.innerWidth;
if(width <750){
    container1.classList.toggle("active");
    navbtn.classList.toggle("liactive");
}
else{
    navbtn.classList.toggle("liactive");
}
