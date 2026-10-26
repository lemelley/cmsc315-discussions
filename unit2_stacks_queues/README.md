# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

# Implementation Documentation

## Stack
I implemented the Stack class with a Python list called items. push() added a value to the end of the list,
and pop() removed and returned the last value, so the item that was most recently added always came out 
first (LIFO). peek() returned the last item without removing it, and is_empty() returned True when the list 
had no items. pop() and peek() both checked is_empty() first and raised an IndexError("The Stack is empty")
instead of the program ending abruptly with a Python error.

## Queue
I implemented the Queue class with enqueue() which added a value to the back and dequeue() which used popleft()
to remove the oldest value from the front so that items are left in the same order in which they were added (FIFO).
front() returned the oldest item in the list without removing it. Similar to the stack, dequeue() and front() 
both raised an IndexError when the queue was empty

## Demonstrations
The stack demonstration pushed A, B, C, and D, then popped them in LIFO order: D, C, B, A. The queue demonstration
enqueued four print jobs (Job 4011 through Job 4014), and removed them in the FIFO order or order in which they
were submitted in this case: Job 4011 through Job 4014.

## Edge Cases
I tested three edge cases for each structure:
- Popping or dequeuing from an empty stack or queue
- Peeking at or checking the front of an empty stack or queue
- A stack or queue with one item, which was subsequently removed and checked with is_empty() which then returned True

Each empty-structure error was raised by my own methods and was caught in main() with try/except blocks so the program
prints the error message and keeps running.

I chose to raise an error instead of simply returning a message because it makes it so that the error is unmistakable.
If the data entered into the stack or queue is the same as what the message would say, it could be mistaken as an error
when in reality it's simply the data that was entered in. With this, an error is raised and displayed to the user.

## Real-World Scenario
The queue demonstration modeled a shared office printer, which was based on a printer queue I recently saw in my office
space. Jobs were printed in the order they were submitted. A stack would have been the wrong choice to use because then 
the newest job would take precedence over the older jobs.

An undo history paired with the use of ctrl+z would be a perfect example of where a stack is the better choice. With
a stack, the LIFO structure is used so the last item that was entered is the first one removed. 

## How to Run
```
python unit2_discussion.py
```

## Discussion Board Reflection

While I already knew what LIFO and FIFO both were in theory, putting it into use was very interesting. I had previously
used pop and append, but hadn't used deque or popleft previously. This exercise helped me understand how pop and append
connect to LIFO and deque and popleft connect to FIFO. When putting the program together, I kept running into problems 
with syntax mistakes (missing colons, incorrect variable names) and selecting where to place my try blocks. The syntax
errors were pretty straightforward because IntelliJ kept pointing them out. The try blocks were more of a trial/error 
as well as doing some research into where these blocks should be placed. In a stack, the last item that is entered is 
the more important item because it follows the LIFO structure which removes the last item that was added. This can be 
easily visualized by an undo button (and its corresponding history tracking method). History is tracked and when called, 
the last item that was added is the item that is removed. A queue differs from this in that the first item that is added
to a queue is the first item that gets removed when called. Thinking about it visually, a printer operates by receiving
jobs and printing them in the order they are received, not by being prioritized by which item was last added.
