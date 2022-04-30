import datetime
import time
import json

with open("config.json") as config_file:
 data = json.load(config_file)

hours = 0
minutes = 0
format = data["Format"]
print(format)

def decideFormat(hours, format):
 intHours = int(hours)

 if format == "12h":
  if intHours > 12:
   intHours = intHours - 12
   return intHours
  else:
   return intHours
 else:
  return intHours

def updateHours(hours):
 hours = datetime.datetime.now().strftime("%H")
 return hours

def updateMinutes(minutes):
 minutes = datetime.datetime.now().strftime("%M")
 return minutes

def isLeadingZero(input):
 intInput = int(input)

 if intInput < 10:
  strInput = str(intInput)
  strInput = "0" + strInput
  return strInput
 else:
  strInput = str(input)
  return strInput

hours = updateHours(hours)
minutes = updateMinutes(minutes)
hours = decideFormat(hours, format)
strHours = isLeadingZero(hours)
strMinutes = isLeadingZero(minutes)
print(strHours + ":" + strMinutes)
