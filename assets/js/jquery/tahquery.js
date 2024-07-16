// Code to get the IP address of the user
   $.get('http://jsonip.com', function(data) {
       console.log(data.ip);
   });