import timeConversion
import bytesConversion
def decide(measureValue, measureUnit):
  return {
    'ms': timeConversion.calculate(measureValue, measureUnit),
    'B': bytesConversion.calculate(measureValue, measureUnit),
    '': 3
  }.get(measureUnit, "measure not found")