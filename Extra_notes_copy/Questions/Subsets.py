class Solution:
    def subsets(self, nums):
        def sub_set(index, arr, current_set, sub_set_arr):
            if index==len(arr):
                sub_set_arr.append(current_set.copy())
                return

            current_set.append(arr[index])
            sub_set(index+1, arr, current_set, sub_set_arr)
            current_set.pop()

            sub_set(index+1, arr, current_set, sub_set_arr)

        current_set= []
        sub_set_of_inputs= []
        sub_set(0, nums, current_set, sub_set_of_inputs)

        return sub_set_of_inputs

if __name__=='__main__':
    ans= Solution()
    arr= [0, 98, 87, 100]
    ans_= ans.subsets(arr)
    print(*ans_)