import time

def interruptible_sleep(seconds, stop_event):
    end_time = time.time() + seconds
    while time.time() < end_time:
        if stop_event.is_set():
            break
        time.sleep(0.1)