#python code to demostrate the sleep/time module.
import time
 
for i in range(5):
   current_time = time.localtime()
   timestamp = time.strftime("%I:%m:%S", current_time)
   time.sleep(2)
   print(timestamp)



from time import sleep
 
story_intro = ["It", "was", "a", "dark", "and", "stormy", "night", "..."]
for x in story_intro:
   print(x)
   sleep(1)   