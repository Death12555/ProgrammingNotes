
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