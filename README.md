Format: ![Alt Text](https://img.shields.io/github/license/deepusingla0448/ZoomAutomation)
# ZoomAutomation
 This Script will automate our zoom meetings 
 
	Before running the script make sure to install
	all the require packages
	[*] pip install helium
	[*] pip install selenium

##Then we will get cookies to bypass the authentication of zoom app
execute the following commands to get cookies

##Make sure to run it on console one by one not directly

```from helium import *
import pickle```

*Open the zoom app*
```driver = start_chrome('https://zoom.us')```

*first login into your zoom account*

*now after login*
*use this command to get cookies*
```cookies = driver.get_cookies()```

*load cookies in pickle file to use it*
```pickle.dump(cookies,open('cookies.pkl','wb'))```

*after completing kill the browser by this command or simply by close*
```kill_browser()```

