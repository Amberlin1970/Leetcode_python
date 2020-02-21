1342. Number of Steps to Reduce a Number to Zero

Level:Easy

Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Examples:
1) Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

2)Input: num = 10
Output: 5
Explanation: 
Step 1) 10 is even; divide by 2 and obtain 5. 
Step 2) 5 is odd; subtract 1 and obtain 4. 
Step 3) 4 is even; divide by 2 and obtain 2. 
Step 4) 2 is even; divide by 2 and obtain 1. 
Step 5) 1 is odd; subtract 1 and obtain 0.

Constraints:
0 <= num <= 10^6
