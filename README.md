<a href="https://github.com/deepusingla0448/ZoomAutomation/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/deepusingla0448/ZoomAutomation"></a>
<a href="https://github.com/deepusingla0448/ZoomAutomation/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/deepusingla0448/ZoomAutomation"></a>
<a href="https://www.instagram.com/_.abhi_singla_/"><img alt="Instagram" src="https://img.shields.io/badge/join-instragram-ff69b4"></a>

# ZoomAutomation
 This Script will automate our zoom meetings 
 
	Before running the script make sure to install
	all the require packages
	[*] pip install helium
	[*] pip install selenium

##Then we will get cookies to bypass the authentication of zoom app
execute the following commands to get cookies

##Make sure to run it on console one by one not directly
``` python
from helium import *
import pickle

# Open the zoom app
driver = start_chrome('https://zoom.us

# first login into your zoom account*

# now after login
# use this command to get cookies
cookies = driver.get_cookies()

# load cookies in pickle file to use it
pickle.dump(cookies,open('cookies.pkl','wb'))

# after completing kill the browser by this command or simply by close
kill_browser()
```