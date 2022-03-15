def getFivePercentage(a, b):
  return sum((a, b)) * 0.05


def withMultiArgs(*args):
  # args type is tuple
  return sum(args) * 0.05
