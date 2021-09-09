function navFunction() {
    var x = document.getElementById("myNav");
    if (x.className === "navmenu") {
        x.className += " responsive";
    } else {
        x.className = "navmenu";
    }
}