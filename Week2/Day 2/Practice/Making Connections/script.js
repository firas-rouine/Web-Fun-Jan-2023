console.log("page loaded...");
var x = document.querySelector("#card-list-item1")
var y = document.querySelector("#card-list-item2")
function Remove1(){
    x.remove()
}
function Remove2(){
    y.remove()
}


var Name =document.querySelector(".name")
function Change(){
    Name.innerHTML="Rouine Firas"
}


var elm =document.querySelector(".badge")
var Elm =document.querySelector(".badge").innerHTML
function decrease(){
    console.log(elm)
    Elm--
    elm.innerHTML=Elm
}


var elm1 =document.querySelector("#badge")
var Elm1 =document.querySelector("#badge").innerHTML
function increase(){
    console.log(elm1)
    Elm1++
    elm1.innerHTML=Elm1
}