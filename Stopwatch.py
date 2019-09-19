import time
while True:
    try:
        print(" Press Enter to Start the Timer and CTRL-C to end the timer")
        start_time = time.time()
        print(" The timer is started")
        while True:
            print("time elapsed = ", round(time.time() - start_time, 0), 'secs', end='\n')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Time is Stopped")
        end_time = time.time()
        print(" Elapsed time is", round(start_time - end_time, 2), 'secs')
        break

