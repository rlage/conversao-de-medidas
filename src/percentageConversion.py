def objectPercentage(measureValue):
  if(measureValue > 1):
    return "wrong format"
  measureValueInPercentage = round(measureValue * 100)
  return {
    'percentage': {
      'value': measureValueInPercentage,
      'unit': '%'
    }
  }
