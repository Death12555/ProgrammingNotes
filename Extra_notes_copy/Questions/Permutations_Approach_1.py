class Solution:
    def permute(self, nums):
        
        def approach_1(nums, ds, ans, map_for_permutation):
            if len(ds)==len(nums):
                ans.append(ds.copy())
                return
            
            for i in range(len(nums)):
                if not map_for_permutation[i]:
                    map_for_permutation[i]= True
                    ds.append(nums[i])
                    approach_1(nums, ds, ans, map_for_permutation)
                    ds.pop()
                    map_for_permutation[i]= False
        
        ans= []
        ds= []
        map_for_permutation= [False for i in range(len(nums))]
        approach_1(nums, ds, ans, map_for_permutation)
        
        return ans

if __name__=='__main__':
    ans= Solution()
    arr= [0, 98, 87, 100]
    ans_= ans.permute(arr)
    print(*ans_)