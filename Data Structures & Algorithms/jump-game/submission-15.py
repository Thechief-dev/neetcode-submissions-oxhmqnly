# mokoko mokoko mokokokokokokokokoko

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums) - 1 # certain destination

        for i in range(destination - 1, -1, -1):
            if nums[i] + i >= destination: # value always need to greater than mokoko
                destination = i # if yes get that mokoko index for new dest
            # not no need to worry will be decrease all the time. ;)
        # result never change it babe
        if destination == 0:
            return True
        else:
            return False