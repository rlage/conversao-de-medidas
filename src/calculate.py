def calculateMeasure(obj):
  values = obj
  for key in values.keys():
    print(values[key])
    if (values[key]['value'] >= 1):
      return (values[key]['value'], values[key]['unit'])
  return (values[0]['value'], values[0]['unit'])