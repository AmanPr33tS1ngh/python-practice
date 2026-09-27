# Problem 1 — Easy

# Given:

arr = [3, 1, 4, 1, 5, 9]

# return whether the array contains duplicates.

def contains_duplicate(arr):
  seen = set()
  for i in arr:
    if i in seen:
      return True
    seen.add(i)
  return False

def return_duplicate(arr):
  seen = set()
  for i in arr:
    if i in seen:
      return i
    seen.add(i)
  return -1

dup = contains_duplicate(arr)
print(dup)

dup_element = return_duplicate(arr)
print(dup_element)
