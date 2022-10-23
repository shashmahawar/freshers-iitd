function navHandle() {
    var nav = document.getElementById('nav-links');
    if (nav.style.height != '200px') {
        nav.style.height = '200px';
    } else {
        nav.style.height = 0;
    }
}

window.onload = function() {
    if (!localStorage.getItem("unofficial")) {
        alert("This is an unofficial website for incoming Freshers at IIT Delhi created by Students of IIT Delhi. This website is not affiliated with IIT Delhi in any way.");
        localStorage.setItem("unofficial", "true");
    }
}