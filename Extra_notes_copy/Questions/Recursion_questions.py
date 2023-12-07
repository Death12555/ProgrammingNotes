class Recur_tests:
    def recur_q1(self, i, n):
        if i>n:
            return
        
        print("test_succesful")
        
        return self.recur_q1(i+1, n)
        
    def recur_q2(self, i, n):
        if i>n:
            return
        
        print(i)
        
        return self.recur_q2(i+1, n)
        
    def recur_q3(self, i, n):
        if i<=n:
            return
        
        print(i)
        
        return self.recur_q3(i-1, n)
        
    def recur_q4(self, i, n):
        if i<n:
            return
        
        self.recur_q4(i-1, n)
        
        print(i)
    
    def recur_q5(self, i, n):
        if i>n:
            return
        
        self.recur_q5(i+1, n)
        
        print(i)
    
    def recur_q6_parameterised(self, i, summation):
        if i<1:
            print(summation)
            return
        
        self.recur_q6_parameterised(i-1, summation+i)
    
    def recur_q6_functional(self, n):
        if n==0:
            return 0
        
        return n+self.recur_q6_functional(n-1)
    
    def recur_q7(self, n):
        if n==0:
            return 1
        
        return n*self.recur_q7(n-1)
    
    def recur_q7_parameterised(self, n, fact):
        if n==0:
            print(fact)
            return 1
        
        self.recur_q7_parameterised(n-1, fact*n)
    
    def recur_q8_two_pointers(self, arr, start, end):
        if start>=end:
            return
        arr[start], arr[end]= arr[end], arr[start]
        
        self.recur_q8_two_pointers(arr, start+1, end-1)
    
    def recur_q8_one_pointer(self, arr, i, n):
        if i>=n/2:
            return
        
        arr[i], arr[n-i-1]= arr[n-i-1], arr[i]
        
        self.recur_q8_one_pointer(arr, i+1, n)
    
    def recur_q9(self, pallindrome, i):
        if i>=len(pallindrome)/2:
            return True
        if pallindrome[i]!=pallindrome[len(pallindrome)-i-1]:
            return False
        
        return self.recur_q9(pallindrome, i+1)
    
    def recur_q10(self, n):
        if n<=1:
            return n
        
        last= self.recur_q10(n-1)
        second_last= self.recur_q10(n-2)
        
        return last+second_last

if __name__=='__main__':
    n= int(input("Enter a number: "))
    reverse_n= int(input("Enter a number"))
    
    ans= Recur_tests()
    ans.recur_q1(1, n)
    print("\n")
    ans.recur_q2(1, n)
    print("\n")
    ans.recur_q3(10, reverse_n)
    print("\n")
    ans.recur_q4(10, reverse_n)
    print("\n")
    ans.recur_q5(1, n)
    print("\n")
    ans.recur_q6_parameterised(5, 0)
    print("\n")
    print(ans.recur_q6_functional(5))
    print("\n")
    print(ans.recur_q7(4))
    print("\n")
    ans.recur_q7_parameterised(4, 1)
    print("\n")
    arr= [1, 2, 3, 4, 5]
    ans.recur_q8_two_pointers(arr, 0, len(arr)-1)
    print(arr, "\n")
    ans.recur_q8_one_pointer(arr, 0, len(arr))
    print(arr, "\n")
    pallindrome= "madam"
    print(ans.recur_q9(pallindrome, 0), "\n")
    print(ans.recur_q10(10), "\n")
    