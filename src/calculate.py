def calculateMeasure(obj):
  values = obj
  if type(values) is dict:
    for key in values.keys():
      if (values[key]['value'] >= 1):
        return str(values[key]['value']) + " " + values[key]['unit']
    return str(values[0]['value']) + " " + values[0]['unit']
  else:
    return obj
