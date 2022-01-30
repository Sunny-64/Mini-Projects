import time
from plyer import notification

if __name__ == "__main__": 
   while True: 
      notification.notify(
       title = "Drink Water fool You fool",
       message = "Drinking water = glowing skin and a lot more",
       app_name = 'For Sunny',
       app_icon = 'F:\Mini Projects\Drink_Water_Notification\icon.ico',
       timeout = 10,
       toast = False
       )
      time.sleep(60*60)
