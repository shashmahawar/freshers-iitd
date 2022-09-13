function navHandle() {
    var nav = document.getElementById('nav-links');
    if (nav.style.height != '200px') {
        nav.style.height = '200px';
    } else {
        nav.style.height = 0;
    }
}