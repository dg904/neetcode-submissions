class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzero_total = 1 
        zero_count = 0 #counting number of zeroes in the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nonzero_total *= nums[i]
            else:
                zero_count += 1
        output = [0]*len(nums)
        for i in range(len(nums)):
            if zero_count > 0:
                if zero_count > 1:
                    # More than one zero total list is [0,0,...,0]
                    return output
                else:
                    if nums[i] == 0:
                        output[i] = nonzero_total
            else:
                output[i]= int(nonzero_total/nums[i])
                    
        return output