
function genQuote() {
  var randNum = Math.floor(Math.random() * 8) + 1;
  document.getElementById('quote').innerHTML = quotes[randNum];
}

//quote array
var quotes = ["Blank", "\"Dude, suckin' at something is the first step at being sorta good at something.\"<br>-  Jake <small><em>(Adventure Time)</em></small>", "\"Either I will find a way, or I will make one.\"<br> - Philip Sidney", "\"Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.\"<br>- Thomas A. Edison", "\"You are never too old to set another goal or to dream a new dream.\"<br>- C.S Lewis", "\"If you can dream it, you can do it.\"<br>- Walt Disney", "\"Fun is never just that, some time you will pay for ever.\"<br>- Tahlahbee", "\"I know where I'm going and I know the truth, and I don't have to be what you want me to be. I'm free to be what I want.\"<br>- Muhammad Ali", "\"Embrace today as a fresh start, for every sunrise brings new opportunities.\"<br>- Tahlahbee",];
