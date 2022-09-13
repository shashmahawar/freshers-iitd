var images = [...document.getElementsByClassName("intro-images")];
var i = 0;
var j = 0;
images.forEach(element => {
    if (element.classList.contains("active-image")) {
        i = j;
    }
    j++;
})

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

var csrftoken = readCookie('csrftoken');

function moveLeft() {
    images[i].classList.remove("active-image");
    i--;
    if (i < 0) {
        i = images.length - 1;
    }
    images[i].classList.add("active-image");
}

function moveRight () {
    images[i].classList.remove("active-image");
    i++;
    if (i >= images.length) {
        i = 0;
    }
    images[i].classList.add("active-image");
}

function changeLike(element) {
    var kerberos = new URL(window.location.href).pathname.split('/')[2];
    var data = {'kerberos': kerberos};
    var body = JSON.stringify(data);
    var options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: body
    };
    fetch('/api/manageLike/', options).then(response => {
        if (response.status == 200) {
            var count = document.getElementById("like-count");
            count.innerText = parseInt(count.innerText) - 1;
        } else if (response.status == 201) {
            var count = document.getElementById("like-count");
            count.innerText = parseInt(count.innerText) + 1;
        }
    })
    if (element.classList.contains("fa-regular")) {
        element.classList.remove("fa-regular");
        element.classList.add("fill-red");
        element.classList.add("fa-solid");
    } else {
        element.classList.remove("fa-solid");
        element.classList.remove("fill-red");
        element.classList.add("fa-regular");
    }
}