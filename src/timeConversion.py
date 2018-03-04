def calculate(measureValue, measureUnit):
  measureValueInSeconds = measureValue / 1000
  measureValueInMinutes = measureValueInSeconds / 60
  measureValueInHours = measureValueInMinutes / 60

  if (measureValueInSeconds >= 1):
    measureUnit = "s"
    measureValue = measureValueInSeconds

  if (measureValueInMinutes >= 1):
    measureUnit = "m"
    measureValue = measureValueInMinutes


  if (measureValueInHours >= 1):
    measureUnit = "h"
    measureValue = measureValueInHours
  return (measureValue, measureUnit)