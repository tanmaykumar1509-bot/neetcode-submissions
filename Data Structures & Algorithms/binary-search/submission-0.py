class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        if target not in nums:
            return -1
        else:
            while left <= right:
                mid = left + (right - left)//2

                if target == nums[mid]:
                    return mid
                    break
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1