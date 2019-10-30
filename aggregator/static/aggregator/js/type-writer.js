$(document).ready(function() {
    var f = document.getElementById('terminal-logo');
    var text = 'Terminal'
    var i = 0
    
    function TypeWriter(){
        if(f.innerHTML == 'Terminal' && i == 0){
            f.innerHTML=''
        }
        if(i < text.length){
            f.innerHTML = f.innerHTML.slice(0,-1)
            f.innerHTML += text.charAt(i)+'|'
            i++
            setTimeout(TypeWriter,70);
        } else {
            f.innerHTML = f.innerHTML.slice(0,-1)
            i = 0
        }
    }
    setInterval(TypeWriter,10000)
});