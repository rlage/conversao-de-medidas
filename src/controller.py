import timeConversion
import bytesConversion
import percentageConversion
import calculate

def decide(measureValue, measureUnit):
  if(measureUnit == 'ms'):
    return calculate.calculateMeasure(timeConversion.objectTime(measureValue))
  if(measureUnit == 'B'):
    return calculate.calculateMeasure(bytesConversion.objectBytes(measureValue))
  if(measureUnit == ''):
    return calculate.calculateMeasure(percentageConversion.objectPercentage(measureValue))
  return "measure not found"
