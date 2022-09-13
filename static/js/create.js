function aboutCharCount(element) {
    var text = element.value;
    var textLength = text.length;
    if (textLength > 800) {
        element.value = text.substring(0, 800);
        textLength = 800;
    }
    var charCount = document.getElementById('about-char-count');
    charCount.innerText = `${textLength}/800`;
}

function checkImageSize(element) {
    if (element.files[0].size > 1048576) {
        element.value = '';
        alert('Image must be less than 1MB');
    }
}