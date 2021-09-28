from time import strftime, sleep
while True:
    print (strftime("%m/%d/%Y %A %H:%M:%S"), end="", flush=True)
    print("\r", end="", flush=True)
    sleep(1)
