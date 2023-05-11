function Alert(){
    alert("loading weather report...")
}
var btn = document.querySelector(".cookie")
function accept(){
    btn.remove()
}
function CtoF(temp){
   return Math.round(9/5*temp+32) 
}
function FtoC(temp){
    return Math.round(5/9*(temp-32)) 
 }
function convert(elm){
    // console.log(elm.value)
    for (var i=1;i<9;i++){
        var x= document.querySelector(".temp" + i)
        var y= document.querySelector(".temp"+ i).innerHTML
        if(elm.value=="°C"){
            x.innerHTML=(FtoC(y))
        }
        else if(elm.value=="°F"){
            x.innerHTML=(CtoF(y)) 
        } 
    }
}
