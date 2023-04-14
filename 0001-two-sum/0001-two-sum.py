class Solution:
    def twoSum(self, nums: List[int], target: int):
        # O(N*2)
        #
        hash_map = dict()

        for i, v in enumerate(nums):
            hash_map[v] = i

        for i, v in enumerate(nums):
            diff = target - v

            if diff in hash_map and hash_map[diff] != i:
                return [i, hash_map[diff]]

            