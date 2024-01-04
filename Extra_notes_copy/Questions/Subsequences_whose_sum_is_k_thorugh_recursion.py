class Recursion_test3:
    def recur_q12(self, i, arr, sub_sequence, sumK, required_sum):
        if i==len(arr):
            if sumK==required_sum:
                print(*sub_sequence, end="\n" if sub_sequence else "[]\n")
            return
        
        sub_sequence.append(arr[i])
        sumK+= arr[i]
        self.recur_q12(i+1, arr, sub_sequence, sumK, required_sum)
        
        sumK-= arr[i]
        sub_sequence.pop()
        self.recur_q12(i+1, arr, sub_sequence, sumK, required_sum)
        
if __name__=='__main__':
    ans= Recursion_test3()
    arr= [1, 2, 1]
    sub_sequence= []
    ans.recur_q12(0, arr, sub_sequence, 0, 2)