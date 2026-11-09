# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

# Reflection
In this assignment, I learned how a binary search tree is built and used. I wrote recursive methods to insert values, search for them, and traverse the tree in order. I also went with a more complicated real-world example to learn about more complex cases. Although getting into it was pretty straightforward, I planned on linking numbers to the names but then saw that I could just insert the values in pairs (hours, name) and the tree would sort them by hours. 

A BST keeps smaller values in the left subtree and larger ones in the right subtree. Because of this sorting order, each comparison during a search lets the program skip one side of the tree. In a balanced tree, that takes less steps when compared to a linear search going through a list which may need to check every value. An in order traversal also comes out sorted so inserting a value doesn't require shifting every element in the same way that a sorted list requires. Although this does have its advantages, a tree that is built from values that were pre-sorted creates a lopsided tree resulting in the search function being as slow as a list.

# Implementation Documentation

## Tree Structure
I built a binary search tree with a Node class and a BST class, each Node stored a value and references to a left and a right child, both were initialized as None. The BST stored a root, which was also initialized as None.

## Insertion
insert() started at the root and called _insert_recursive(). At each node, the method compared the new values to the current node's value. Smaller values went into the left subtree and larger values went to the right. When the method reached an empty spot, it created a new node. Duplicate values were ignored. I inserted [40, 30, 90, 50, 20, 70, 10], which put values into both subtrees.

## Search
search() uses _search_recursive() to follow the same go-left or go-right rule from insertion returning True when the value is found and False when the end of the branch is reached. Each comparison skipped one side of the tree which made the search faster than checking every value in a balanced tree. A lopsided tree would lose that speed advantage.

## In Order Traversal
inorder() used _inorder_recursive() to visit the left subtree, the current node, then the right subtree. With the left side holding smaller values and the right holding the larger values, the output comes out sorted even when the values were inserted out of order.

## Search Tests
I searched two values that did exist (20 & 70) which both returned True, and two that did not (100 and 45), which both returned False.

## Edge Cases
I tested three edge cases: 
- An empty tree that returned an empty list for traversal and False for a search.
- Inserting a duplicate (50) didn't affect the tree
- A tree with a single node that just returned that value
Although it makes sense, printing an empty tree just prints out empty brackets ([]) instead of a simple blank. This is intuitive for the user to see an empty tree.

## Real-World Scenario
I used a leaderboard for calibration hours. Each entry was a pair of hours and a name so the tree ordered the people by the hours first. The reversal of the order resulted in the leaderboard being sorted by hours highest to lowest. Using the search function required the whole pair because the tree was sorted by hours.

## How to Run
```
python unit4_discussion.py
```