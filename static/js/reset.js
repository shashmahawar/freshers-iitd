function passwordCheck() {
    var password = document.getElementById("password").value;
    var password2 = document.getElementById("password2").value;
    var error = document.getElementById("reset-error");
    var btn = document.getElementById("reset-button");
    if (password.length < 8) {
        error.style.display = "block";
        error.innerText = "Password must be at least 8 characters long.";
        btn.disabled = true;
    } else if (password != password2) {
        error.style.display = "block";
        error.innerText = "Passwords do not match.";
        btn.disabled = true;
    } else {
        error.style.display = "none";
        btn.disabled = false;
    }
}