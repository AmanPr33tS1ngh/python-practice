# Problem 8 — Custom Prefix-Sum Exercise

# Given:

nums = [3, 1, 4, 2, 5]
      # 3, 4, 8, 10,15

# Answer multiple queries:

# sum(0, 2)
# sum(1, 3)
# sum(2, 4)

# Expected:

# 8
# 7
# 11
def prefix_sum(nums):
  result = [0]
  prev_sum = 0
  
  for i in nums:
    prev_sum += i
    result.append(prev_sum)

  return result
  
prefix = prefix_sum(nums)
print(prefix)
def prefix_query(left, right):
  return prefix[right + 1] - prefix[left]

print(prefix_query(2, 3))
  