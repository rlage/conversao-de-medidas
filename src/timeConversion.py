def objectTime(measureValue):
  measureValueInSeconds = measureValue / 1000
  measureValueInMinutes = measureValueInSeconds / 60
  measureValueInHours = measureValueInMinutes / 60
  return {
    'hours': {
      'value': measureValueInHours,
      'unit': 'h'
    },
    'minutes': {
      'value': measureValueInMinutes,
      'unit': 'm'
    },
    'seconds': {
      'value': measureValueInSeconds,
      'unit': 's'
    },
    'miliseconds': {
      'value': measureValue,
      'unit': 'ms'
    }
  }