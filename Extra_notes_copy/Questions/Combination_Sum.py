class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find_combinations(index, target, candidates, ans, ds):
            if index==len(candidates):
                if target==0:
                    ans.append(ds.copy())
                return
            
            #pick
            if candidates[index]<=target:
                ds.append(candidates[index])
                find_combinations(index, target-candidates[index], candidates, ans, ds)
                ds.pop()

            #not pick
            find_combinations(index+1, target, candidates, ans, ds)
        
        ans= []
        ds= []
        find_combinations(0, target, candidates, ans, ds)
        return ans