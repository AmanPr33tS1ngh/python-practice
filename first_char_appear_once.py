# Problem 4 — Medium

# Given a string, return the first character that appears only once.

# Input:
s = "leetcode"

# Output:
# "l"

def return_first(s):
  freq = dict()
  for i in s:
    freq[i] = freq.get(i, 0) + 1

  for i, k in freq.items():
    if k == 1:
      return i
  return "Not Found"

result = return_first(s)
print(result)