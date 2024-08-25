import time
currenttime= time.strftime ('%H:%M:%S')
print(currenttime)
if (currenttime>='05' and currenttime<'12'):
  print("Good Morning,SIR")
elif (currenttime>='12' and currenttime<='17'):
  print("Good Afternoon,SIR")
else:
  print("Good Evening,SIR")
