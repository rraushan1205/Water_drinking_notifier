
import time
from plyer import notification
from time import strftime
 
if __name__=="__main__":
    while True:
        string = strftime('%H:%M:%S %a')
        min_time = int(strftime('%M'))
        string1 = strftime('\n%b, %d, %Y ')
        if min_time == 00:
            notification.notify(
                title = string + string1,
                message=" Drink a glass full of water to stay hydrated" ,
                app_icon="E:\projects rough\Deks_notifier\water.ico",
                # displaying time
                timeout=2, toast=False)
            # waiting time
            time.sleep(30)