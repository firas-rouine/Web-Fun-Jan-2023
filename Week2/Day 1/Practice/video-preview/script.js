console.log("page loaded...");

var video =document.querySelector("video")
function mute(){
    if(video.muted==false){
        video.muted=true;
    }else{
        video.muted=false;
    }   
}
function playVid(){
    video.play();
}
function pauseVid(){
    video.pause();
}

