import call, gui
import time

while True:
    if(gui.is_on):
        call.read
        call.write
        time.sleep(5)
        print("currently running")
    