class Sub_set:
    def sub_set(self, index, sum_of_elements, arr, sub_set_sums):
        if index==len(arr):
            sub_set_sums.append(sum_of_elements)
            return
        
        self.sub_set(index+1, sum_of_elements+arr[index], arr, sub_set_sums)
        
        self.sub_set(index+1, sum_of_elements, arr, sub_set_sums)
        
    def sum_sub_sets(self, arr, N):
        sub_set_sums= []
        self.sub_set(0, 0, arr, sub_set_sums)
        sub_set_sums.sort()
        return sub_set_sums

if __name__=='__main__':
    ans= Sub_set()
    arr= [0, 98, 87, 100]
    ans_= ans.sum_sub_sets(arr, len(arr))
    print(*ans_)