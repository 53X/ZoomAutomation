from helium import *
import time
from ZoomAutomation import ZoomAutomation
zoom = ZoomAutomation()
driver = zoom.login()
End_Time = time.time() + 50 * 60
while time.time() < End_Time:
    try:
        zoom.main(driver)
    except Exception as e:
        print(e)
        pass
kill_browser()