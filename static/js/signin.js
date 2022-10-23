function checkKerberosLength(element) {
    document.getElementById("initial-error").style.display = "none";
    if (element.value.length == 9) {
        document.getElementById("initial-continue").style.display = "flex";
    } else {
        document.getElementById("initial-continue").style.display = "none";
    }
}

function checkPasswordLength(element) {
    if (element.value.length < 8) {
        document.getElementById("signin-error").style.display = "block";
        document.getElementById("signin-error").innerText = "Password must be at least 8 characters long";
        document.getElementById("signin-submit").style.display = "none";
    } else {
        document.getElementById("signin-error").style.display = "none";
        document.getElementById("signin-submit").style.display = "block";
    }
}

function checkKerberos() {
    var btn = document.getElementById("initial-continue");
    btn.disabled = true;
    btn.innerText = "Please Wait..."
    var kerberos = document.getElementById("initial-kerberos").value;
    data = {'kerberos': kerberos};
    body = JSON.stringify(data);
    options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: body
    };
    fetch('/api/checkKerberos/', options).then(response => {
        if (response.status == 200) {
            document.getElementById("initial-continue").style.display = "none";
            document.getElementById("initial-error").style.display = "none";
            document.getElementById("initial-kerberos").disabled = true;
            document.getElementById("signin").style.display = "block";
            document.getElementById("forgot-password").style.display = "block";
        } else if (response.status == 404 || response.status == 400) {
            var error = document.getElementById("initial-error");
            error.style.display = "block";
            response.json().then(data => error.innerText = data.message);
            btn.innerText = "Continue";
            btn.disabled = false;
        } else if (response.status == 201) {
            document.getElementById("initial").style.display = "none";
            document.getElementById("initial-error").style.display = "none";
            document.getElementById("initial-continue").style.display = "none";
            document.getElementById("register").style.display = "block";
        }
    })
}

function login() {
    var btn = document.getElementById("signin-submit");
    btn.disabled = true;
    btn.innerText = "Please Wait..."
    var kerberos = document.getElementById("initial-kerberos").value;
    var password = document.getElementById("signin-password").value;
    data = {'kerberos': kerberos, 'password': password};
    body = JSON.stringify(data);
    options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: body
    };
    fetch('/api/login/', options).then(response => {
        if (response.status == 200) {
            window.location.href = "/intro/";
        } else {
            var error = document.getElementById("signin-error");
            error.style.display = "block";
            response.json().then(data => error.innerText = data.message);
            btn.innerText = "Sign In";
            btn.disabled = false;
        }
    });
}

function forgot() {
    var btn = document.getElementById("signin-submit");
    btn.style.display = "block";
    btn.disabled = true;
    btn.innerText = "Please Wait..."
    document.getElementById("forgot-password").style.display = "none";
    var kerberos = document.getElementById("initial-kerberos").value;
    data = {'kerberos': kerberos};
    body = JSON.stringify(data);
    options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: body
    };
    fetch('/api/forgot/', options).then(response => {
        if (response.status == 201) {
            document.getElementById("initial").style.display = "none";
            document.getElementById("signin").style.display = "none";
            document.getElementById("signin-error").style.display = "none";
            document.getElementById("signin-error").style.display = "none";
            document.getElementById("signin-submit").style.display = "none";
            document.getElementById("forgot").style.display = "block";
        }
    });
}