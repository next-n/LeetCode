# https://leetcode.com/problems/two-sum/
def twoSum(nums, target):
	dictmap = {}
	for i in range(len(nums)):
		if nums[i] in dictmap:
			return [dictmap[nums[i]], i]
		else:
			dictmap[target - nums[i]] = i


nums1 = [2, 7, 11, 15]
target1 = 9

print(twoSum(nums1, target1))

