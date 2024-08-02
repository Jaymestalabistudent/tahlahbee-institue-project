
Orchid Project:
# Known Issues and Workarounds

As with any web development project, there are a few known issues that have been identified. Below is a list of these issues along with suggested workarounds, planned fixes, and additional details.

## 1. General Color Contrast
   - Issue: Certain areas of the website have insufficient color contrast, making it difficult for users with visual impairments to read text or distinguish between different elements.
   - Details: This issue mainly affects users with conditions such as color blindness or low vision. The lack of contrast can make navigation and content consumption challenging.
   - Workaround: Users can temporarily improve contrast using browser extensions like the High Contrast plugin for Chrome or accessibility features in their operating system. In upcoming updates, the color scheme will be revised to ensure better compliance with WCAG (Web Content Accessibility Guidelines) standards, improving overall accessibility.

## 2. Navigation Types Disabled on Smaller Devices
   - Issue: Certain navigation elements, such as dropdown menus or sidebars, may not function properly on smaller screens, like mobile phones or tablets.
   - Details: This issue is due to the responsive design not being fully optimized for all device types, which can lead to navigation options being hidden or unusable.
   - Workaround: Users can access navigation via the main menu or by enabling the desktop view in their mobile browser settings. The development plan includes redesigning the navigation structure to be fully responsive, ensuring that all elements are accessible across all screen sizes.

## 3. High Page Load Times
   - Issue: The website currently experiences high page load times, particularly on slower networks or older devices. This is primarily due to large media files, complex animations, and unoptimized CSS/JavaScript.
   - Details: High load times can lead to a poor user experience, increased bounce rates, and lower search engine rankings.
   - Workaround: Users can temporarily disable images and scripts in their browser settings to reduce load times. Future updates will focus on optimizing images by using modern formats (e.g., WebP), reducing the reliance on heavy animations, and minifying CSS and JavaScript files. Additionally, lazy loading techniques will be implemented to further enhance performance.

## 4. Large CSS Files
   - Issue: The CSS files used in the project are larger than necessary, contributing to slower load times and potential conflicts between styles.
   - Details: The inclusion of extensive CSS rules, many of which are unused, has bloated the files, leading to inefficiencies in both load times and rendering.
   - Workaround: While the immediate impact is on load times, the long-term solution involves a complete audit of the CSS to remove unused styles, modularize the remaining code, and apply minification techniques. CSS files will also be split by page to ensure that only necessary styles are loaded, reducing the overall load on each page.

## 5. Security Concerns (Hosted on GitHub)
   - Issue: The website is currently hosted on GitHub Pages, which lacks certain security features like HTTPS, making it less secure for users.
   - Details: Without HTTPS, data transmitted between the user and the website is not encrypted, leaving it vulnerable to interception or tampering.
   - Workaround: Users are advised not to enter any sensitive information on the website until it is migrated to a more secure hosting platform, such as Render or Vercel, which will include HTTPS support. The migration is a top priority to ensure user data is protected and to comply with modern web security standards.

## 6. Bootstrap and Nicepage CSS/JS Errors and Security Flaws

- Issue: Integration of Bootstrap and Nicepage has resulted in some CSS/JS errors and potential security vulnerabilities.
- Details: These errors may cause certain UI elements to behave unexpectedly or introduce security risks that could be exploited.
   - Workaround: Unfortunately, there is no effective workaround for this issue at the moment other than accepting the errors as they are. The development team is aware of these flaws, and regular monitoring is in place. Updates and patches will be applied as they become available from the respective libraries. In the meantime, users should be aware of potential inconsistencies in the UI and avoid relying on the site for critical operations until these issues are resolved.

## 7. No Website Backup Currently
   - Issue: The project currently lacks an automated backup solution, increasing the risk of data loss in the event of a server failure or security breach.
   - Details: Without backups, recovering the website after an incident could be challenging and time-consuming, potentially leading to extended downtime.
   - Workaround: As an interim measure, manual backups of the website's files and database are being performed regularly. Implementing an automated backup solution is a high priority for future development, ensuring that the website can be quickly restored if needed.

---

### Conclusion

While these issues present challenges, workarounds are available for most, and plans are in place to address them in future updates. For issues without workarounds, users are advised to be cautious and aware of the limitations. The ongoing development efforts will focus on resolving these issues to improve the website's performance, security, and accessibility.