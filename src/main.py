from controller import decide

a = input()
a = a.split()
if(len(a) > 1):
  measureValue = float(a[0])
  measureUnit = a[1]
else:
  measureValue = float(a[0])
  measureUnit = ""

result = decide(measureValue, measureUnit)
print(result)