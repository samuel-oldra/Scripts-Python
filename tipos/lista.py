nums = [1, 2, 3]

print(type(nums))

nums.append(3)
nums.append(4)
nums.append(500)

print(len(nums))

nums[3] = 100
nums.insert(0, -200)

print(nums[6])
print(nums[-1])
print(nums[-2])
print(nums)