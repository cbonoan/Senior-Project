/*Add file to every HTML page*/
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#E';
    for (var i = 0; i < 5; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
//Adds random bottom border line to nav links
function navLinkHover(x, color) {
    var elem = x.children[0]; 
    elem.style.transitionDuration = '0.5s';
    elem.style.backgroundColor = color;
}
function navLinkMouseOut(x) {
    var elem = x.children[0]; 
    elem.style.backgroundColor = '';
}

window.onload = function() {
    document.addEventListener("scroll", function() {
        var elem  = document.getElementById("navbar");
        if(window.scrollY != 0) {
            elem.classList.add("shadow");
            if(window.innerWidth > 1000)
                elem.style.padding = "0.35rem";
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
            
        } else if(window.getComputedStyle(midBar).getPropertyValue("opacity") == 0){
            topBar.style.transform = "rotate(0deg)";
            midBar.style.opacity = 1;
            bottomBar.style.transform = "rotate(0deg)";
        }
        const nav = document.querySelector('.navList');
        const navLinks = document.querySelectorAll('.navList li');
        //Toggle nav
        nav.classList.toggle('nav-active');
        //Animating links
        navLinks.forEach((link,index) => {
            if(link.style.animation) {
                link.style.animation = ''; 
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
    });

    
}