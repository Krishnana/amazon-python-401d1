1. Reverse an Array(#reverse)
   1.1	Challenge (#reverseChallenge)
   1.2  Approach & Efficiency (#reverseApproach)
   1.3  Solution (#solution)
2. Shift Array (#shift)
   2.1	Challenge (#shiftChallenge)
   2.2  Approach & Efficiency (#shiftApproach)
   2.3  Solution (#shiftSolution)

<a name="reverse"></a>
# Reverse an Array
Get list of numbers from user and reverse the list. Also, get the number of elements in list.

<a name="reverseChallenge"></a>
## Challenge
Input list from user should contain only integers. Otherwise, process should error out. 

<a name="reverseApproach"></a>
## Approach & Efficiency
Swap 1st and last element. Continue to swap until middle element. This reduces the iterations by half. 

<a name="solution"></a>
## Solution
![White Board](assets/array-reverse.jpg)

<a name="shift"></a>
# Shift Array
Insert an element to mid index of an array

<a name="shiftChallenge"></a>
## Challenge
Insert an element to mid indes of an array. You cannot use any existing python functions for inserting

<a name="shiftApproach"></a>
## Approach & Efficiency
Create an empty array with 1 element more than input array. Assign all indices except the mid index

<a name="shiftSolution"></a>
## Solution
![White Board](assets/array-shift.jpg)
