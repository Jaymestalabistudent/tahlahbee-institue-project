# Lottie Files

### Contributors

1. **Soumyajeet Das**
2. **Abdul Latif**
3. **Manny Hernandez**
4. **Kishwar Jabeen**

### Introduction to Lottie

Lottie is an open-source animation file format that is lightweight, scalable, and versatile, making it an ideal choice for adding animations to web pages. Created by Airbnb, Lottie allows designers to export animations created in Adobe After Effects as JSON files. These files can then be rendered natively on web and mobile platforms, providing high-quality, smooth animations that enhance the user experience without a significant impact on performance.

### Why Use Lottie for Web Animations?

1. **Lightweight and Efficient**: Lottie animations are compact JSON files that are much smaller in size compared to GIFs or video files, ensuring faster loading times.
2. **Scalability**: Being vector-based, Lottie animations can be scaled up or down without losing quality, making them perfect for responsive designs.
3. **Cross-Platform Compatibility**: Lottie works seamlessly across multiple platforms, including iOS, Android, and web, ensuring a consistent user experience.
4. **Interactivity**: Lottie animations can be controlled via JavaScript, allowing for dynamic and interactive web experiences.
5. **Easy to Use**: With a plethora of libraries and tools available, integrating Lottie animations into your project is straightforward and developer-friendly.

### How to Add Lottie Animations to a Web Page

1. **Include Lottie Web Library**:
   To get started, include the Lottie Web library in your HTML file. You can do this by adding the following script tag to your HTML head section:

   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.6/lottie.min.js"></script>
   ```
2. **Add an HTML Element for the Animation**:
   Create a container element in your HTML where the animation will be rendered. For example:

   ```html
   <div id="lottie-animation" style="width: 300px; height: 300px;"></div>
   ```
3. **Load and Render the Animation**:
   Use JavaScript to load and render the Lottie animation. Here is a basic example of how to do this:

   ```html
   <script>
       var animation = lottie.loadAnimation({
           container: document.getElementById('lottie-animation'), // the DOM element that will contain the animation
           renderer: 'svg', // the rendering mode (svg/canvas/html)
           loop: true, // whether the animation should loop
           autoplay: true, // whether the animation should start playing automatically
           path: 'path/to/animation.json' // the path to the animation JSON file
       });
   </script>
   ```

   Replace `'path/to/animation.json'` with the actual path to your Lottie animation file.

### Useful Links for Lottie

- [LottieFiles](https://lottiefiles.com/): A community and marketplace for Lottie animations, providing a wide range of animations ready to use.
- [Lottie Web GitHub Repository](https://github.com/airbnb/lottie-web): The official GitHub repository for Lottie Web, where you can find documentation and source code.
- [LottieFiles Editor](https://lottiefiles.com/editor): An online tool to edit and preview Lottie animations directly in the browser.

### Conclusion

Lottie animations offer a powerful way to enhance web applications with high-quality, interactive animations. By leveraging the Lottie Web library, developers can easily integrate these animations into their projects, improving user engagement and creating visually appealing web experiences.
