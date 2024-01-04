class Recursion_test3:
    def recur_q12_only_one_sum(self, i, arr, sub_sequence, sumK, required_sum):
        if i==len(arr):
            #condition satisfied
            if sumK==required_sum:
                print(*sub_sequence, end="\n" if sub_sequence else "[]\n")
                return True
            
            #condition not statisfied
            return False
        
        sub_sequence.append(arr[i])
        sumK+= arr[i]
        if self.recur_q12_only_one_sum(i+1, arr, sub_sequence, sumK, required_sum): return True
        
        sumK-= arr[i]
        sub_sequence.pop()
        if self.recur_q12_only_one_sum(i+1, arr, sub_sequence, sumK, required_sum): return True
        
        return False

if __name__=='__main__':
    ans= Recursion_test3()
    arr= [1, 2, 1]
    sub_sequence= []
    ans.recur_q12_only_one_sum(0, arr, sub_sequence, 0, 2)