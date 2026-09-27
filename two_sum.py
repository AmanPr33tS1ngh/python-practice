# Problem 3 — Easy/Medium

# Given:

arr = [2, 7, 11, 15]
target = 13

# return the indices of the two numbers whose sum is target.

def two_sum_elements(arr, target):
  seen = {}

  for i, x in enumerate(arr):
      needed = target - x

      if needed in seen:
          return [needed, x]

      seen[x] = i

  return [-1, -1]

result = two_sum_elements(arr, target)
print(result)


def two_sum_indices(arr, target):
  seen = {}

  for i, x in enumerate(arr):
      needed = target - x

      if needed in seen:
          return [seen[needed], i]

      seen[x] = i

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


