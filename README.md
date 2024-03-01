No external libraries were used for either part A or B. Only the built-in socket module: from socket import *
For Part A: 
Port: 8000

Note:
-Webserver, if the image does not render, please refresh and it works successfully !

How to run:
1) Run the webserver.py code file.
2) To test if it works, open a new browser and enter http://localhost:8000/hello.html
3) It should work and show Hello World if you have a hello.html in your directory.
4) If you want to test if images render, add your own image to the directory and include <img> in the html file
5) To test if it fails, open a new browser and enter http://localhost:8000/bye.html
6) It should show Error 404 page not found because you don't have bye.html in your directory.

For Part B:
proxyPort = 8888
serverPort = 80  

Notes:
-If you store a webpage in the cache, and then try to search the website again, mhen you refresh, it renders the underlying sense HTML on the website. But it still successfully stores the cache and the TA Tyler Osborne said this HTML display was fine.

-Might have to restart the server if you wanna try several websites in succession like google and then amazon. 

-Sometimes, if you search for a webpage for the first time, it will redirect you to the actual website and won't cache it properly. Just try to refresh and try again.

-After leaving the server on idle for a while, it'll say something like traceback most recent call last: IndexError: list index out of range and then the server will close. Please just restart and it'll be working fine again.

-It might take a little while to load a website, perhaps 10-20 seconds for some of them. 

How to Run:
1) Run the proxyserver.py code file.
2) To test if it works, open a browser and type in localhost:8888/http://captive.apple.com or just localhost:8888/{your_website_link}
3) To test if it caches, just reload the page or search for the same web page again, but it might render the underlying HTML.

HTTP ONLY WEBSITES THAT WORKED FOR ME:

http://captive.apple.com

http://example.com 

http://info.cern.ch

http://www.testingmcafeesites.com

http://gaia.cs.umass.edu

http://http.badssl.com

http://neverssl.com

http://http-textarea.badssl.com

Websites that failed for me:
