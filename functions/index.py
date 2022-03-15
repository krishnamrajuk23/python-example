from argsParamFun import getFivePercentage, withMultiArgs


def execute():
  percentage = getFivePercentage(10, 20)
  print("percentage of two numbers", percentage)

  percentage = withMultiArgs(10, 20, 100, 200)
  print("percentage of multi values using *args", percentage)
