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
      
  return None
      
def return_first_element(s):
  result = return_first(s)
  if result:
    return result
  return "Not Found"

result = return_first(s)
print(result)


def return_first_idx(s):
  result = return_first(s)
  if not result:
    return -1
    
  for i in range(0, len(s)):
    val = s[i]
    if val == result:
      return i
  
result = return_first_idx(s)
print(result)