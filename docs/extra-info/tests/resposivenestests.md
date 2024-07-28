# Debug on Responsiveness:

During the development of the Spotify embed page, ensuring responsiveness across various devices and screen sizes was a primary focus. Initially, the iframe was not properly centered and did not scale well on smaller screens.

 To address this, I utilized CSS Flexbox to center the iframe both horizontally and vertically within its container. The .spotify-container class was set to use Flexbox with justify-content: center and align-items: center to achieve this centering.

Additionally, media queries were implemented to adjust the height of the iframe based on the viewport size.



This ensures that the iframe maintains an appropriate aspect ratio and remains fully visible without causing overflow issues on smaller screens. 

The max-width property was also applied to the iframe to prevent it from exceeding a certain width, ensuring it remains visually appealing and functional on larger screens.Despite these adjustments, there were challenges with maintaining consistent padding and margins across different devices. By setting margin: 0 auto; on the iframe, I ensured equal spacing on both sides, which helped in maintaining a balanced layout.

 Testing across various devices and screen sizes was crucial to identify and resolve these issues, ultimately leading to a responsive and user-friendly design.
