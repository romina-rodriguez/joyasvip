function hover(img) {
    img.setAttribute('src', '/static/logo/purple-logo.png');
}

function unhover(img) {
    img.setAttribute('src', '/static/logo/white-logo.png');
}

function change_active(nav,div) {
    var currently_active = document.getElementsByClassName("active");
    currently_active[0].className = currently_active[0].className.replace(" active", "");
    document.getElementById(nav).className += " active";  
    
    var contents = document.getElementsByClassName("content");
    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = "none";
    }
    document.getElementById(div).style.display = "flex"; 
}