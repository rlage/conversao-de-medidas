import timeConversion
import bytesConversion
import calculate
def decide(measureValue, measureUnit):
  return {
    'ms': calculate.calculateMeasure(timeConversion.objectTime(measureValue)),
    'B': bytesConversion.calculate(measureValue, measureUnit),
    '': 3
  }.get(measureUnit, "measure not found")