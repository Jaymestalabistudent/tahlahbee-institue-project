document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.getElementById('overlay').style.display = 'none';
        document.getElementById('main-content').classList.add('show');
    }, 6000); // 6000 milliseconds = 6 seconds
});
