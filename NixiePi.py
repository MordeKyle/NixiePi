import datetime
import time
import json
import RPi.GPIO as GPIO
import sys

with open("config.json") as config_file:
 data = json.load(config_file)

hours = 0
minutes = 0
format = data["Format"]
numbers = [data["Zero"], data["One"], data["Two"], data["Three"], data["Four"], data["Five"], data["Six"], data["Seven"], data["Eight"], data["Nine"]]
#print(numbers[9])

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
