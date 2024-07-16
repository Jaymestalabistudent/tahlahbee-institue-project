document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.getElementById('overlay').style.display = 'none';
        document.getElementById('main-content').style.display = 'block';
    }, 6000); // 6000 milliseconds = 6 seconds
});
