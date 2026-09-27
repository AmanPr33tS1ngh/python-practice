# Problem 3 — Easy/Medium

# Given:

arr = [2, 7, 11, 15]
target = 13

# return the indices of the two numbers whose sum is target.

def two_sum_elements(arr, target):
  seen = set()
  for i in arr:
    seen.add(i)
  
  for i in arr:
    k = target - i
    if k in seen:
      return [i, k]
    
  return [-1, -1]

result = two_sum_elements(arr, target)
print(result)


def two_sum_indices(arr, target):
  seen = dict()
  for i in range(0, len(arr)):
    element = arr[i]
    seen[element] = i
  
  for i in range(0, len(arr)):
    element = arr[i]
    k = target - element
    if k in seen:
      return [i, seen[k]]
    
  return [-1, -1]

result = two_sum_indices(arr, target)
print(result)



def two_sum(arr, target):
  i = 0
  j = len(arr) - 1
  
  while i <= j:
    e1 = arr[i]
    e2 = arr[j]
    el_sum = e1 + e2
    
    if el_sum == target:
      return [i, j]
    elif el_sum < target:
      i += 1
    else:
      j -= 1
      
  return [-1, -1]

result = two_sum(arr, target)
print(result)


