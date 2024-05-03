def large_num(nums):
    if not nums:  
        return "0"

    class Container:
        def __init__(self, number):
            self.number = str(number)

        def __lt__(self, other):
            combined1 = self.number + other.number
            combined2 = other.number + self.number
            return combined2 < combined1  


    containers = [Container(num) for num in nums]

    containers.sort()


    if containers[0].number == "0":
        return "0"

    
    large_num = "".join(container.number for container in containers)

    return large_num

nums = list(map(int, input("Enter the non-negative integers separated by spaces: ").split()))

large_str = large_num(nums)

print(large_str)
----------------------------------------------------------------------------------------------------------------------------------------------------
def long_inc_subseq(nums):
  n = len(nums)
  if n == 0:
    return 0

  curr_len = 1
  max_len = 1

  for i in range(1, n):

    if nums[i] > nums[i - 1]:
      curr_len += 1
    else:
    
      curr_len = 1
    max_len = max(max_len, curr_len)

  return max_len


nums = list(map(int, input("Enter the integers separated by spaces: ").split()))

length = long_inc_subseq(nums)


print(length)
