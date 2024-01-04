class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def find_combinations(index, target, candidates, ans, ds):
            if target==0:
                ans.append(ds.copy())
                return
            
            if index>=len(candidates):
                return            

            #recurrence relation(look at target to understand)
            if target>=candidates[index]:
                ds.append(candidates[index])

                find_combinations(index + 1, target-candidates[index], candidates, ans, ds) #pick

                ds.pop()
            
            i= index+1
            while i<len(candidates) and candidates[i]==candidates[i-1]:
                i+= 1
            find_combinations(i, target, candidates, ans, ds) #not pick

        candidates.sort()
        ans= []
        ds= []
        find_combinations(0, target, candidates, ans, ds)
        return ans