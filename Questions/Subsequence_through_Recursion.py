class Recursion_Test2:
    def recursion_q11_pick(self, i, sub_sequence, arr):
        if i>=len(arr):
            for item in sub_sequence:
                print(item, end=" ")

            if len(sub_sequence)==0:
                print("[]")
            print()
            return

        # Pick the element at index i and recurse
        sub_sequence.append(arr[i])
        self.recursion_q11_pick(i+1, sub_sequence, arr)
        sub_sequence.pop()

        # Do not pick the element at index i and recurse
        self.recursion_q11_pick(i+1, sub_sequence, arr)

    def recursion_q11_not_pick(self, i, sub_sequence, arr):
        if i >= len(arr):
            print(*sub_sequence, end= "\n" if sub_sequence else "[]\n")
            return
        
        # Do not pick the element at index i and recurse
        self.recursion_q11_not_pick(i+1, sub_sequence, arr)

        # Pick the element at index i and recurse
        sub_sequence.append(arr[i])
        self.recursion_q11_not_pick(i+1, sub_sequence, arr)
        sub_sequence.pop()

if __name__ == '__main__':
    ans = Recursion_Test2()
    arr = [3, 1, 2]
    sub_sequence_not_pick = []
    sub_sequence_pick= []

    ans.recursion_q11_pick(0, sub_sequence_pick, arr)
    ans.recursion_q11_not_pick(0, sub_sequence_not_pick, arr)