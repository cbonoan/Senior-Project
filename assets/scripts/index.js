document.addEventListener("scroll", function() {
    var elem  = document.getElementById("navbar");
    if(window.scrollY != 0) {
        elem.classList.add("shadow");
    } else {
        elem.classList.remove("shadow");
    }
});