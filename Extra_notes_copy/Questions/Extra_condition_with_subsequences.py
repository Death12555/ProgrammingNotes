class Recursion_test3:
    def recur_q12_only_one_sum(self, i, arr, sumK, required_sum):
        if sumK>required_sum: return 0          #etra condition, condition not satisfied, only possible if all elements are positive
        if i==len(arr):
            #condition satisfied
            if sumK==required_sum:
                return 1
            
            #condition not statisfied
            else: return 0
        
        sumK+= arr[i]
        l= self.recur_q12_only_one_sum(i+1, arr, sumK, required_sum)
        
        sumK-= arr[i]
        r= self.recur_q12_only_one_sum(i+1, arr, sumK, required_sum)

        return l+r

if __name__=='__main__':
    ans= Recursion_test3()
    arr= [1, 2, 1]
    print(ans.recur_q12_only_one_sum(0, arr, 0, 2))