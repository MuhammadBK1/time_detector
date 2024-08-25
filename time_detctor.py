name = input("Enter your name:")
print("\t\t\tWelcome",name.upper())
import time
currenttime= time.strftime ('%H:%M:%S')
print(currenttime)
if (currenttime>='04' and currenttime<'10'):
  print("Good Morning,SIR")
elif (currenttime>='10' and currenttime<='13'):
  print("Good Noon,SIR")
elif(currenttime>='13' and currenttime<='17:30'):
  print("Good Afternoon,SIR")
elif (currenttime>='17:30' and currenttime<='19'):
  print("Good Evening,SIR")
else:
  print("Good Night,SIR")
