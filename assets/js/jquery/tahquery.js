// Code to get the IP address of the user
   $.get('http://jsonip.com', function(data) {
       console.log(data.ip);
   });

   // Code to get the operating system of the user

   function getOperatingSystem() {
    let OSName = "Unknown OS";
    const appVersion = navigator.appVersion;
    const userAgent = navigator.userAgent;

    if (appVersion.indexOf("Win") !== -1) OSName = "Windows";
    else if (appVersion.indexOf("Mac") !== -1) OSName = "MacOS";
    else if (appVersion.indexOf("X11") !== -1) OSName = "UNIX";
    else if (appVersion.indexOf("Linux") !== -1) OSName = "Linux";
    else if (userAgent.indexOf("Android") !== -1) OSName = "Android";
    else if (userAgent.indexOf("iPhone") !== -1 || userAgent.indexOf("iPad") !== -1) OSName = "iOS";

    // Log the OS name to the console
    console.log("Operating System: " + OSName);

    return OSName;
}

// Call the function to log the OS name
getOperatingSystem();



// Get the user's time zone using the Internationalization API

function getUserTimeZone() {
    // Get the user's time zone using the Internationalization API
    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    // Log the time zone to the console
    console.log("User's Time Zone: " + timeZone);

    return timeZone;
}

// Call the function to log the user's time zone
getUserTimeZone();

