
from time import time
from datetime import datetime, date, timedelta
import math
import notification

now = datetime.today()
notification.cancel_all()
# Must be multiples of 15min
start_of_day = datetime(now.year, now.month, now.day, 10, 30)
end_of_day = datetime(now.year,now.month,now.day + 1,2)
def schedule_15min_notifications(start_of_day, end_of_day):
    duration_start_to_end = end_of_day - start_of_day
    num_15min_Ste = int(duration_start_to_end.total_seconds() / 60 / 15)
    hour_floor_durSte = int(math.floor(duration_start_to_end.total_seconds() / 60 / 60))
    minute_floor_durSte = int(math.floor((duration_start_to_end.total_seconds() - hour_floor_durSte * 60 * 60) / 60))
    # Calcuating first 15minute notification from now
    now_after_colon_in_seconds = now.microsecond * 1e-6 + now.second + now.minute * 60
    now_after_colon_in_minutes = now_after_colon_in_seconds / 60
    now_minute_to_15_ceil = int(15 * (math.floor(now_after_colon_in_minutes / 15) + math.ceil((now_after_colon_in_minutes % 15) / 15)))
    dur_minutes_from_now_to_15ceil = now_minute_to_15_ceil - now.minute 
    first_notification = now + timedelta(minutes=dur_minutes_from_now_to_15ceil) - timedelta(seconds=now.second, microseconds=now.microsecond)

    # Duration first_notification to end of day
    dur_first_notif_to_end = end_of_day - first_notification
    num_15min_notifications = int(1 + dur_first_notif_to_end.total_seconds() / 60 / 15)

    for i in range(num_15min_notifications):

        #calculate notification delay_seconds
        i_notification = first_notification + timedelta(minutes=(15 * i))
        delay_timedelta = i_notification - now 
        delay_seconds = int(delay_timedelta.total_seconds())

        # Calculate notifcation message
        duration_iNotif_to_end = end_of_day - i_notification
        hour_floor_durInte = int(math.floor(duration_iNotif_to_end.total_seconds() / 60 / 60))
        minute_floor_durInte = int(math.floor((duration_iNotif_to_end.total_seconds() - hour_floor_durInte * 60 * 60) / 60))
        percentage_used = 100 * round((duration_iNotif_to_end.total_seconds() / duration_start_to_end.total_seconds()), 3)
        num_15min_notifications_left = int(duration_iNotif_to_end.total_seconds() / 60 / 15)
        
        message = "{:.2f}".format(percentage_used) + "per. " + str(num_15min_notifications_left) + "/" + str(num_15min_Ste) + " " + str(hour_floor_durInte) + "h" + "{:01d}".format(minute_floor_durInte) + "m" + "/" + str(hour_floor_durSte) + "h" + "{:01d}".format(minute_floor_durSte) + "m " + str(i_notification.hour) + ":" + "{:02d}".format(i_notification.minute) + " " + str(start_of_day.hour) + ":" + "{:02d}".format(start_of_day.minute) + " - " + str(end_of_day.hour) + ":" + "{:02d}".format(end_of_day.minute)

        print(delay_seconds)
        print(message)
        
        notification.schedule(message, delay_seconds, "Input")
schedule_15min_notifications(start_of_day,end_of_day)
