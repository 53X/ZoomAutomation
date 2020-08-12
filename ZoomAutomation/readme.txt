Before runing the script make sure to install
all the require packages
[*] pip install helium
[*] pip install selenium

Then we will get cookies to bypass the authentication of zoom app
execute the commands of following commands to get cookies

from helium import *
import pickle

##Open the zoom app
driver = start_chrome('https://zoom.us/signin')

#first login into your zoom account
#because we can't automate recaptcha we have to do manual login to get cookies which we can use again and without login in.
#now after login

#use this command to get cookies
cookies = driver.get_cookies()

#load cookies in pickle file to use it
pickle.dump(cookies,open('cookies.pkl','wb'))

#after completing kill the browser by this command or simply by close
kill_browser()
