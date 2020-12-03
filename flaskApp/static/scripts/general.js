/*Add file to every HTML page*/
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
function navLinkHover(x) {
    var elem = x.children[0]; 
    elem.style.borderBottom = "3px solid " + getRandomColor();
}
function navLinkMouseOut(x) {
    var elem = x.children[0]; 
    elem.style.borderBottom = 0;
}
window.onload = function() {
    document.addEventListener("scroll", function() {
        var elem  = document.getElementById("navbar");
        if(window.scrollY != 0) {
            elem.classList.add("shadow");
            if(window.innerWidth > 1000)
                elem.style.padding = "0.75rem";
        } else {
            elem.classList.remove("shadow");
            elem.style.padding = "0rem";
        }
    });
    
    var angle = 0; //Initial angle 
    document.getElementById("custom-toggler").addEventListener("click", function() {
        var topBar = document.getElementById("topBar");
        var midBar = document.getElementById("midBar");
        var bottomBar = document.getElementById("bottomBar");
        var dropDownElem = document.getElementById("navbarContent");
        
        topBar.style.transitionDuration = "0.25s";
        midBar.style.transitionDuration = "0.25s";
        bottomBar.style.transitionDuration = "0.25s";
        bottomBar.style.transformOrigin = "center";
        topBar.style.transformOrigin = "center";
        if(window.getComputedStyle(midBar).getPropertyValue("opacity") != 0) {
            topBar.style.transform = "rotate(45deg)";
            topBar.style.transform += "translate(0px,18px)";
            midBar.style.opacity = 0;
            bottomBar.style.transform = "rotate(-45deg)";
            bottomBar.style.transform += "translate(0px,-18px)";
            dropDownElem.style.backgroundColor = "#fbfbff";
            dropDownElem.style.width - "100%";
        } else if(window.getComputedStyle(midBar).getPropertyValue("opacity") == 0){
            topBar.style.transform = "rotate(0deg)";
            midBar.style.opacity = 1;
            bottomBar.style.transform = "rotate(0deg)";
            dropDownElem.style.backgroundColor = "white";
        }

    });

    
}