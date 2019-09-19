import time

# this is the Program to illustrate the measuring the time that elapses between the start and end clicks
def start():

    return int(time.time())

st = start()

time.sleep(10)

print("The start time is :",st, end="\n ")


def stop():
    return int(time.time())

sp = stop()

print(" the Stop Time is :",sp, end="\n " )

tstamp = st-sp
print("The Time stamp between the start and stop is :", tstamp, end=" ")
