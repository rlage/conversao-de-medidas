def calculate(measureValue, measureUnit):
  measureValueInKiloBytes = measureValue / 1000
  measureValueInMegaBytes = measureValueInKiloBytes / 1000

  if (measureValueInKiloBytes >= 1):
    measureUnit = "Kb"
    measureValue = measureValueInKiloBytes

  if (measureValueInMegaBytes >= 1):
    measureUnit = "Mb"
    measureValue = measureValueInMegaBytes

  return (measureValue, measureUnit)