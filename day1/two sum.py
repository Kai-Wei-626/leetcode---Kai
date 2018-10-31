## 2 sum

nums = [2, 7, 11, 15]
target = 9
def twosum(nums, target):
    dic = {}
    for index, num in enumerate(nums):
        if num in dic:
            return [dic[num],index]
        dic[target - num] = index
 
# other than this, we can use brute force
