def calculateMeasure(obj):
  values = obj
  if type(values) is dict:
    for key in values.keys():
      if (values[key]['value'] >= 1):
        return (values[key]['value'], values[key]['unit'])
    return (values[0]['value'], values[0]['unit'])
  else:
    return values
