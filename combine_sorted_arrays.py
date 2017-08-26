a = [1, 7, 9, 11, 13, 20, 22, 25, 30]
b = [2, 4, 6, 8, 14, 15, 17, 21]


def arr_sort(arr_1, arr_2):
  res = []
  i = 0
  j = 0
  while i < len(arr_1) and j < len(arr_2):
    if arr_1[i] < arr_2[j]:
      res.append(arr_1[i])
      i += 1
    else:
      res.append(arr_2[j])
      j += 1
  for k in range(i, len(arr_1)):
    res.append(arr_1[k])
  for k in range(j, len(arr_2)):
    res.append(arr_2[k])
  return res


result = arr_sort(a, b)
print result
