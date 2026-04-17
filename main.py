import time 
from plyer import notification
while True:
    print("Please sip some water! ")
    notification.notify(title="please drink some water", message      ="you need to drink some waater",)
    time.sleep(60*60)