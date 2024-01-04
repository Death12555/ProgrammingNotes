class Solution:
    def permute(self, nums):
        
        def approach_2(index, nums, ans):
            if index==len(nums):
                ds= []

                for i in range(len(nums)):
                    ds.append(nums[i])
                
                ans.append(ds)
                return
            
            for i in range(index, len(nums)):
                nums[index], nums[i]= nums[i], nums[index]
                approach_2(index+1, nums, ans)
                nums[index], nums[i]= nums[i], nums[index]
        
        ans= []
        approach_2(0, nums, ans)
        
        return ans

if __name__=='__main__':
    ans= Solution()
    arr= [0, 98, 87, 100]
    ans_= ans.permute(arr)
    print(*ans_)