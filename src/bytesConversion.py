def objectBytes(measureValue):
  measureValueInKiloBytes = measureValue / 1000
  measureValueInMegaBytes = measureValueInKiloBytes / 1000
  return {
    'megabytes': {
      'value': measureValueInMegaBytes,
      'unit': 'Mb'
    },
    'kilobytes': {
      'value': measureValueInKiloBytes,
      'unit': 'kB'
    },
    'bytes': {
      'value': measureValue,
      'unit': 'B'
    }
  }
