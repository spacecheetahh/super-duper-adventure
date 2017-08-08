def is_prime(x):
  if x > 0 and x <= 2 and x != 1:
    return True
  elif x > 0 and x > 2:
    for n in range(2, x-1):
      print n
      if x % n == 0:
        return False
    return True
  else:
    return False
