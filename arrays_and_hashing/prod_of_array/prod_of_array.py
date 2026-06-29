class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # modified_int_list = [1] * (len(nums))
        # prefix_num = 1
        # for i in range(len(nums)):
        #     modified_int_list[i] = prefix_num
        #     prefix_num *= nums[i]
        # post_fix_num = 1
        # for j in range(len(nums) - 1, -1, -1):
        #     modified_int_list[j] *= post_fix_num
        #     post_fix_num *= nums[j]
        # return modified_int_list
        modified_int_list = []
        for i in range(len(nums)):
            product_num = 1
            for k in range(len(nums)):
                if k != i:
                    product_num *= nums[k]
            modified_int_list.append(product_num)
        return modified_int_list