# Step-by-Step Guide to Embed a Spotify Player

1. **Get the Embed Code from Spotify:**

   - Open Spotify and find the track, album, playlist, or podcast you want to embed.
   - Click on the "..." (More) button next to the item.
   - Select "Share" and then "Copy Embed Code."
2. **Create the HTML Structure:**

   - Create a new HTML file or open your existing one.
   - Add a container for the Spotify iframe and a preloader.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spotify Embed</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="preloader" id="preloader"></div>
    <div class="spotify-container">
        <iframe src="YOUR_SPOTIFY_EMBED_URL" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    </div>
    <script src="scripts.js"></script>
</body>
</html>
```

3. **Add CSS for Responsiveness and Preloader:**
   - Create a `styles.css` file and add the following styles:

```css
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
}

.spotify-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
}

iframe {
    width: 100%;
    height: 380px;
    border: none;
}

.preloader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #fff url('preloader.gif') no-repeat center center;
    z-index: 9999;
}

@media (max-width: 600px) {
    iframe {
        height: 300px;
    }
}

@media (max-width: 400px) {
    iframe {
        height: 250px;
    }
}
```

4. **Add JavaScript for Preloader:**
   - Create a `scripts.js` file and add the following script to hide the preloader once the iframe is loaded:

```javascript
document.addEventListener("DOMContentLoaded", function() {
    var iframe = document.querySelector("iframe");
    var preloader = document.getElementById("preloader");

    iframe.onload = function() {
        preloader.style.display = "none";
    };
});
```
