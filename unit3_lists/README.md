# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

In this assignment, I got to practice using insert, delete, and search in a Python list. Inserting or deleting shifts every element after the position so doing it at the beginning costs the most (time and resources) and doing it at the end costs the least. I also learned why delete_at() checks the index first. Without the check, pop() raises an IndexError on an invalid index or an empty list. 

Although not necessarily a challenge with the program itself, I had some trouble setting the configuration in IntelliJ on my computer. It worked great for Week 2, but the configuration reset completely so I had to go and find where Python was installed.

List operations affect performance in real-world applications because the impact felt by needing to shift every element (due to insertion/deletion from the beginning) only gets worse by increased sizes of lists. A playlist or to-do list with common changes to the front or middle of the lists would reflect this whereas adding to the end of these would have less of an impact. I think using a different structure such as a linked list would make a significant difference in performance. 

---

# Implementation Documentation

## Functions

I implemented three functions on a Python list. `insert_at()` used `list.insert()`, which placed the value at the given index and shifted every element after it one spot to the right. `delete_at()` checked that the index was valid and then used `list.pop(index)`, which returned the removed value and shifted the later elements left. An invalid index returned `None` instead of crashing. `search_value()` used a loop that checked each element in order and returned the index of the first match, or `-1` when the value was not found.

## Insertion and Deletion Tests

I started with the list `[10, 20, 30, 40, 50]` and inserted at the beginning, the middle, and the end, printing the list after each step. I then deleted from the beginning, the middle, and the end, printing both the removed value and the updated list. Operations at the end of the list moved nothing, while operations at the beginning moved every other element, so they did the most work.

## Search Tests

I searched for a value that existed (40, found at index 3) and a value that did not (99, which returned -1). The search was linear because the list was not sorted, so the only way to find a value was to check each element from the front.

## Edge Cases

I tested three edge cases. Deleting with an invalid index (50) returned `None`. Deleting from an empty list also returned `None`. Inserting into an empty list worked and produced `[7]`. The index check in `delete_at()` kept these cases from raising an `IndexError`.

Last week, we went over pop(). Calling pop() instead of deleting would've raised an IndexError, but in my program, both situations returned None because the index check failed and pop() was never called.

## Real-World Scenario

The program used a music playlist: a song was added as the second track, the first track was removed, and a search found the position of a song. A playlist changes often in the middle, which is where list inserts and deletes cost the most.

## How to Run

```
python unit3_discussion.py
```
