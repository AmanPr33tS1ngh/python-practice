# Problem 5 — Medium

# Given two arrays, determine whether they contain the same elements with the same frequencies.

arr1 = [1, 2, 3, 3]
arr2 = [2, 1, 3, 2]

# → True

# But:

# arr1 = [1, 2, 2, 3]
# arr2 = [1, 2, 3, 3]

# → False

def is_len_same(arr1, arr2): return len(arr1) == len(arr2)
  
def el_with_same_freq_1(arr1, arr2):
  if not is_len_same(arr1, arr2):
    return False

  arr1.sort()
  arr2.sort()

  for i in range(0, len(arr1)):
    if arr1[i] != arr2[i]:
      return False
      
  return True

result = el_with_same_freq_1(arr1, arr2)
print(result)
  
def el_with_same_freq_2(arr1, arr2):
  if not is_len_same(arr1, arr2):
    return False

  freq = dict()

  for i in arr1:
    freq[i] = freq.get(i, 0) + 1
  
  for j in arr2:
    freq[j] = freq.get(i, 0) - 1

  for k in freq.values():
    if k != 0:
      return False
      
  return True

result = el_with_same_freq_2(arr1, arr2)
print(result)
  