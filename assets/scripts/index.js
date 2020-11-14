window.onload = function() {
    document.addEventListener("scroll", function() {
        var elem  = document.getElementById("navbar");
        if(window.scrollY != 0) {
            elem.classList.add("shadow");
        } else {
            elem.classList.remove("shadow");
        }
    });
    
    var angle = 0; //Initial angle 
    document.getElementById("custom-toggler").addEventListener("click", function() {
        var elem = document.getElementById("custom-toggler");
        elem.style.transitionDuration = "0.5s";
        if(angle == 0) {
            elem.style.transform = "rotate(90deg)"; 
        } else {
            elem.style.transform = "rotate(0)";
        }
        setTimeout(function() {
            var st = window.getComputedStyle(elem, null);
            var tr = st.getPropertyValue("-webkit-transform") ||
                st.getPropertyValue("-moz-transform") ||
                st.getPropertyValue("-ms-transform") ||
                st.getPropertyValue("-o-transform") ||
                st.getPropertyValue("transform");
            var values = tr.split('(')[1],
            values = values.split(')')[0],
            values = values.split(',');

            var a = values[0]; 
            var b = values[1]; 
            var c = values[2]; 
            var d = values[3];
            angle = Math.round(Math.asin(b) * (180/Math.PI));
            console.log(angle);
        },500);
        
    });
}