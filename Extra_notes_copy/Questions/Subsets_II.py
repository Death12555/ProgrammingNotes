class Solution:
    def subsetsWithDup(self, nums):
        def find_sub_sets(index, nums, ds, ans_list):
            ans_list.append(ds.copy())

            for i in range(index, len(nums)-1):
                if index and nums[i]==nums[i-1]: continue
                ds.append(nums[i])
                find_sub_sets(i+1, nums, ds, ans_list)
                ds.pop()
        
        nums.sort()
        ds= []
        ans_list= []
        find_sub_sets(0, nums, ds, ans_list)
        
        return ans_list

if __name__=='__main__':
    ans= Solution()
    arr= [0, 98, 98, 87, 87, 100, 100, 100]
    ans_= ans.subsetsWithDup(arr)
    print(*ans_)