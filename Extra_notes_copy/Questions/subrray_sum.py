class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count= {0:1}
        current_sum= 0
        count= 0

        for i in nums:
            current_sum+= i
            count+= sum_count.get(current_sum-k, 0)
            sum_count[current_sum]= sum_count.get(current_sum, 0)+1
        
        return count