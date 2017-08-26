fac_cache_r = {}
fac_cache_i = {}


def fac_r(n):  # recursive factorial
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return n * fac_r(n - 1)


def fac_i(n):  # iterative factorial
  length = len(fac_cache_i)
  fac_cache_i[0] = 1
  if n == 0:
    return 1
  elif length - 1 >= n:
    return fac_cache_i[n]
  elif length - 1 < n:
    f = fac_cache_i[length - 1]
    for it in range(length, n + 1):
      f *= it
      fac_cache_i[it] = f
    return f


# for i in range(10):
#   print fac_r(i)

for i in range(7):
  print fac_i(i)

for i in range(4, 11):
  print fac_i(i)
