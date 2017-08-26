fib_r_cache_i = {}
fib_r_cache_r = {}


def fib_r(n):  # recursive fibonacci
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fib_r(n - 1) + fib_r(n - 2)


def fib_i(n):  # iterative fibonacci
  lenght = len(fib_r_cache_i)
  fib_r_cache_i[0] = 0
  fib_r_cache_i[1] = 1
  if n == 1:
    return 0
  elif n == 2:
    return 1
  elif lenght >= n:
    return fib_r_cache_i[n - 1]
  else:
    a = fib_r_cache_i[lenght - 2]
    b = fib_r_cache_i[lenght - 1]
    for it in range(lenght, n):
      tmp = b
      b = a + b
      a = tmp
      fib_r_cache_i[it] = b
    return b


# for i in range(1, 10):
#   print fib_r(i)

for i in range(1, 10):
  print fib_i(i)

print fib_r_cache_i

for i in range(4, 12):
  print fib_i(i)
