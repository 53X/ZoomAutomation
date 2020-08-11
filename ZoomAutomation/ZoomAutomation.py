from helium import *
import time
import pickle
from selenium.webdriver import ChromeOptions
import random


class ZoomAutomation:
    def __init__(self, MeetingID, password, cookies, name, proxy_id=None, proxy_port=None):
        self.id = MeetingID
        self.password = password
        self.cookies = cookies
        self.name = name
        self.proxy_id = proxy_id
        self.proxy_port = proxy_port
        self.bahna = ['Sorry i have no camera for video play',
                      'apna km kr',
                      'hatttt',
                      'oh yeahhhh ']  # list of bahna

    def login(self):
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--proxy-server=' + str(self.proxy_id) + ':' + str(self.proxy_port))
        if self.proxy_id is not None:  # if user use proxy
            driver = start_chrome('https://zoom.us', options=options)
        else:  # if user don't use proxy
            driver = start_chrome('https://zoom.us')  # opening the Chrome window
        cookies = pickle.load(open(self.cookies, 'rb'))  # loading cookies so that we can bypass authentication
        try:
            print('loading cookies')
            for cookie in cookies:
                print(cookie)
                driver.add_cookie(cookie)  # Adding cookies in our Chrome driver
        finally:
            print('Cookies loaded Sucessfully')
            go_to('https://zoom.us/wc/join/' + str(self.id))  # joining the meeting
        wait_until(lambda: Text('Your Name').exists())  # Waiting until 'Your Name' get appear
        time.sleep(0.5)
        name = driver.find_element_by_id('inputname')  # selecting input field
        if name.get_attribute('value') == 0:  # checking if our input field is not empty
            click(name)
            write(self.name)  # if empty writing name
            joinbtn = driver.find_element_by_id('joinBtn')  # selecting join button
            click(joinbtn)  # clicking in join button
        else:
            joinbtn = driver.find_element_by_id('joinBtn')
            click(joinbtn)
        wait_until(lambda: Text('Meeting Passcode').exists(), 160)  # now again waiting for password field to appear
        time.sleep(0.5)
        passcode = driver.find_element_by_id('inputpasscode')  # selecting passcode field
        click(passcode)  # clicking on passcode field
        write(self.password)  # writing our passcode
        if TextField('Meeting Passcode').value == self.password:  # checking if our passcode is filled
            joinbtn = driver.find_element_by_id('joinBtn')  # selecting join button
            click(joinbtn)  # clicking on join button
        updatecookies = driver.get_cookies()  # updating cookies so that is not get expire soon
        pickle.dump(updatecookies, open('cookies.pkl', 'wb'))
        return driver

    def Start_My_Video(self, driver):
        if Text('Later').exists(): #waitng for Start my video to appear
            click('Later') # if appear click on later
            print('Later is clicked ')
            self.chat(driver) #calling chat function to drop the message
        elif Text('Stay muted').exists():#waitng for unmute  to appear
            click('Stay muted') # if appear click on later
            print('Muted is clicked')#calling chat function to drop the message
            self.chat(driver)
        else:
            print('we got nothing')
            pass

    def chat(self, driver):
        if driver.get_window_size()['width'] < 778:
            self.SChat(driver)
        else:
            self.LCHat(driver)

    def LCHat(self, driver):
        if not Text('open the chat pane').exists():
            footer = driver.find_element_by_class_name('footer__btns-container')
            hover(footer)
        if not Text('Zoom Group Chat').exists():
            click('open the chat pane')
        textARE = driver.find_element_by_class_name('chat-box__chat-textarea')
        click(textARE)
        text = random.choice(self.bahna)
        write(text)
        press(ENTER)

        try:
            section_menu = driver.find_element_by_id('chatSectionMenu')
            click(section_menu)
            section_menu_list = driver.find_elements_by_class_name('chat-header__menu')[0]
            Close = section_menu_list.find_element_by_tag_name('a')
            click(Close)
        except:
            time.sleep(0.5)
            cross = driver.find_element_by_xpath(
                '//*[(@id = "chat-window")]//*[contains(concat( " ", @class, " " ), concat( " ", "ax-outline-blue", " " ))]')
            click(cross)

    def SChat(self, driver):
        print('small screen working')
        More = driver.find_element_by_id('moreButton')
        click(More)
        click('Chat')
        textARE = driver.find_element_by_class_name('chat-box__chat-textarea')
        click(textARE)
        text = random.choice(self.bahna)
        write(text)
        press(ENTER)
        cross = driver.find_element_by_xpath(
            '//*[(@id = "chat-window")]//*[contains(concat( " ", @class, " " ), concat( " ", "ax-outline-blue", " " ))]')
        click(cross)


if __name__ == '__main__':
    zoom = ZoomAutomation('Meeting id', 'passcode', 'cookies.pkl','Your Name')
    driver = zoom.login()
    End_Time = time.time() + 50 * 60
    while time.time() < End_Time:
        try:
            zoom.Start_My_Video(driver)
        except Exception as e:
            print(e)
            pass
    kill_browser()
