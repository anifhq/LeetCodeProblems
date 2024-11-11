class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            hash_map[target - num] = index
        for index, num in enumerate(nums):
            if num in hash_map and hash_map[num] != index:
                return [hash_map[num], index] if hash_map[num] < index else [index, hash_map[num]]
        return []
