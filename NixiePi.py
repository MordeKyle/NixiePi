import datetime
import time

while True:
	hours = datetime.datetime.now().strftime("%H")
	minutes = datetime.datetime.now().strftime("%M")
	print(hours + ":" + minutes)
	time.sleep(30)
