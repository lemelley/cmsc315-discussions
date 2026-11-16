# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

* Implement linear search
* Implement binary search
* Compare performance
* Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.



## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Implementation Documentation

# Linear Search

I implemented linear\_search() with a for loop that went through the range of a list from the first position to the last. At each index, it compared the item to the target and returned the index if it found a match. If the loop completed without a match, it returned -1 indicating a failure to find the number. This is O(n) because in the worst case, when the target was last in a list or missing entirely, it checked every item, so the work that needed to be performed grew in steps depending on the size of the list.

# Binary Search

I implemented binary\_search() with low and high variables that marked the part of the list that was searched. Each go around of the while loop calculated the middle position and compared that item to the target. If it matched, the index was returned. If it didn't and the middle item was smaller than the target, the low was set to mid + 1, and if the middle was larger than the target, high was set to mid - 1. In both instances, the number of items that needed to get searched was halved. The middle item was skipped (+/-1) because middle had already been compared. The function returned -1 once low was greater than the high.

# Small Dataset

I tested both search methods on the sorted list \[4, 9, 17, 24, 41, 59, 73]. Both found 24 at index 3 and returned -1 for 60. Given that it was a small list of seven items, there was no significant time difference between the two searches.

# Large Dataset

I created a sorted list of two million numbers and searched for the last item which was the worst case scenario for linear search. Both searches returned the same index, but the real difference was noted based off the number of checks/steps needed. Linear search needed up to 2,000,000 checks, but the binary search only needed to halve the list 20 times. Doubling the list doubles the checks needed for a linear search, but adds only one more step for binary search.

# Edge Cases

I tested an empty list, a single-item list with the target present and missing, and a target at the first and the last positions of a given list. For the empty list, both searches returned -1. The linear search didn't have to execute its loop because there were no items in the list. In the binary search, the high started at -1, so the while loop didn't run. For the single-item list, they both returned index 0 when the item existed and -1 when it was missing. For the first and last positions, both searches found the correct index. Linear search found the first item immediately, but had to go through the entire list for the last item. Binary search reached both ends of the list in a couple of steps.

# Real-World Scenario: Calibration Records

I modeled calibration records with serial numbers as I do in my daily job. The full database here was sorted by serial number, so a binary search found the serial number that existed and returned its index. For the serial number that didn't exist, it returned -1. A short list of serial numbers planned for one day's workload was put into a list in no given order, so linear search was the better choice because sorting a couple of items would take more time than just searching them in the given order. A binary search could not be used when the data was not sorted because it needed to be able to halve the items in a sorted list to determine which half needed to get discarded. I also ran a binary search on an unsorted workload list for \[127561] that returned -1 even though the number was in the list whereas the linear search for the same item returned the actual index. 
    
# How to Run

python unit5\_discussion.py

# Discussion Board Reflection

In this assignment, I learned how linear and binary searches apply to different lists and how their performance compares as the list grows. I wrote both searches and tested them on a small list, a list of two million numbers, and a couple edge cases. I was mostly impressed by the fact that with a 2,000,000 item list, a binary search only needed 20 halves and doubling that list only adds one more. 

The main challenge I faced was how to write/compare the middle value with the +/-1 since the middle value was already compared. Actually writing the code out made it easier to grasp the halving concept.

Linear search is the better choice when the list is not sorted, small, or if only one search is needed to run because sorting it then searching would take more time. A binary search is better for large, sorted data that needs to get searched frequently, such as with a calibration database.

