
## Recursion:
When a function calls itself until a specified condition is fulfilled/met.
If there is no specified condition the function will call itself infinite times.
In that case the program will run unlimited times until it runs out of memory.
This is what is known as stack overflow.

![[Screenshot 2023-12-07 at 5.13.28 PM (2).png]]

![[Screenshot 2023-12-07 at 5.14.56 PM (2).png]]

In the memory stack new function calls will be waiting at line no. 2, and these calls will be waiting in memory because they are yet not completed.

## When do we call a function to be completed?
When the last line has been successfully completed.
But in the above example the the function has not been completed because the last line is calling the function again and again hence the last line hasn't been executed.

So this 'wait' in the memory stack is what is known as stack overflow.
Segmentation fault(calling a function over and over indefinitely) is what is commonly known as stack overflow. When there are numerous function calls waiting due to recursion. This is why infinite recursions are not written because it will cause stack overflow.

![[Screenshot 2023-12-07 at 5.22.21 PM (2).png]]

So to avoid this condition there needs to be a base condition that needs to be written.
The condition that is used to stop calling functions/recursion is known as base condition.

![[Screenshot 2023-12-07 at 5.50.26 PM (2).png]]

There can be more than 1 base condition.

## Recursion Test:

![[Screenshot 2023-12-07 at 5.53.02 PM (2).png]]

Stack overflow/ Stack space is the space where the remaining non executed functions are kept.

For time complexity in recursion, it is dependant on the number of calls.
The space complexity is dependant on the stack space taken.

![[Screenshot 2023-12-07 at 6.17.12 PM (2).png]]

In the above Q. about printing a statement till i>n, the time complexity is O(N) and Space complexity is O(N). where N is the number of calls.

Reversing an array using recursion:

![[Screenshot 2023-12-07 at 7.49.23 PM (2).png]]

Multiple Recursions:

![[Screenshot 2023-12-07 at 8.48.21 PM (2).png]]

For multiple recursion calls they happen sequentially.

![[Screenshot 2023-12-07 at 8.49.55 PM (2).png]]

![[Screenshot 2023-12-07 at 8.58.16 PM (2).png]]

For this question the time complexity will be O(2^n), where n is exponential in nature, i.e.: the value of the exponent is near n not exactly because here, not every recursive function has 2 calls.

![[Screenshot 2023-12-07 at 9.01.08 PM (2).png]]

Subsequence:
	A contiguous/non-contiguous sequence, which follows the order.

	![[Screenshot 2023-12-08 at 3.30.02 PM.png]]

	![[Screenshot 2023-12-08 at 3.38.38 PM.png]]
	
	![[Screenshot 2023-12-08 at 3.55.44 PM.png]]

Printing a subsequence whose sum=k:
	 ![[Screenshot 2023-12-08 at 5.56.12 PM.png]]

	![[Screenshot 2023-12-08 at 5.58.24 PM.png]]

Modifying the code to print only one instance of sum being equal to k instead of all:
	![[Screenshot 2023-12-08 at 6.18.22 PM.png]]
	
	![[Screenshot 2023-12-08 at 6.19.51 PM.png]]

	![[Screenshot 2023-12-08 at 6.35.54 PM.png]]

	![[Screenshot 2023-12-08 at 6.37.45 PM.png]]
	
	![[Screenshot 2023-12-08 at 6.38.25 PM.png]]

	![[Screenshot 2023-12-08 at 6.39.21 PM.png]]

	![[Screenshot 2023-12-08 at 6.39.42 PM.png]]

	![[Screenshot 2023-12-08 at 6.40.02 PM.png]]

Finding the number of subsequences whose sum is k:
	![[Screenshot 2023-12-08 at 6.41.27 PM.png]]

	![[Screenshot 2023-12-08 at 6.42.26 PM.png]]

	![[Screenshot 2023-12-08 at 6.56.39 PM.png]]

Merge Sort:
	![[Screenshot 2023-12-08 at 7.04.48 PM.png]]

	![[Screenshot 2023-12-08 at 7.11.18 PM.png]]

	![[Screenshot 2023-12-08 at 7.11.52 PM.png]]

	![[Screenshot 2023-12-08 at 7.18.08 PM.png]]

	![[Screenshot 2023-12-08 at 7.18.21 PM.png]]

	![[Screenshot 2023-12-08 at 7.24.05 PM.png]]
	
	![[Screenshot 2023-12-08 at 7.24.52 PM.png]]

	![[Screenshot 2023-12-08 at 7.25.33 PM.png]]
	Time complexity: O(NlogN(base 2))
	![[Screenshot 2023-12-08 at 8.47.03 PM.png]]![[Screenshot 2023-12-08 at 8.48.09 PM.png]]
	Space Complexity: O(N)
	
	![[Screenshot 2023-12-08 at 8.50.06 PM.png]]

Quick Sort:
	![[Screenshot 2023-12-08 at 8.57.03 PM.png]]
	
	![[Screenshot 2023-12-08 at 9.01.26 PM.png]]
	
	![[Screenshot 2023-12-08 at 9.04.57 PM.png]]
	
	![[Screenshot 2023-12-08 at 9.06.04 PM.png]]
	
	![[Screenshot 2023-12-08 at 9.07.40 PM.png]]
	Since i and j might go out range make the loops i<=high-1 and j>=low+1 in the while loops

Combination Sum:
	![[Screenshot 2023-12-11 at 8.37.52 PM.png]]
	

Combination Sum II:
	![[Screenshot 2023-12-11 at 9.17.24 PM.png]]

Subset Sum:
	![[Screenshot 2023-12-14 at 3.53.03 PM.png]]
	
	![[Screenshot 2023-12-14 at 3.55.41 PM.png]]
	
	![[Screenshot 2023-12-14 at 3.57.55 PM.png]]
	
	![[Screenshot 2023-12-14 at 4.40.09 PM.png]]
	
Subset Sum II:
	![[Screenshot 2023-12-14 at 5.44.51 PM.png]]
	
	![[Screenshot 2023-12-14 at 6.34.29 PM.png]]
	O(n) is the auxiliary space complexity here.
	![[Screenshot 2023-12-14 at 6.38.33 PM.png]]
	

Permutations:
	![[Screenshot 2023-12-14 at 11.41.42 PM.png]]
	
	![[Screenshot 2023-12-14 at 11.45.06 PM.png]]
	So ultimately there are 6 permutations(2+2+2) in this example.
	
	![[Screenshot 2023-12-14 at 11.48.54 PM.png]]
	O(n) is auxiliary space complexity.

Approach 2:
	![[Screenshot 2023-12-15 at 12.34.23 AM.png]]
	
	![[Screenshot 2023-12-15 at 12.37.30 AM.png]]
	O(n) is also the auxiliary space.
	O(n) for the recursion space and a O(n!) for returning the answer.
	