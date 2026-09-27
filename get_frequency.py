# Problem 2 — Easy

# Given an array, return the frequency of every element.

# Input:
arr = [1, 2, 2, 3, 1, 1]

# Output:
# {
#     1: 3,
#     2: 2,
#     3: 1
# }

freq = {}
def get_freq(arr):
  for i in arr:
    freq[i] = freq.get(i, 0) + 1
  return freq

result = get_freq(arr)
print(result)