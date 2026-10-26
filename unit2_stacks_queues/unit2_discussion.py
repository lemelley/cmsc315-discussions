"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Using the append() function support LIFO because append adds a value to the end of the stack
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Using pop() further supports LIFO because it removes the last value in the stack
        if self.is_empty():
            raise IndexError("The Stack is empty")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek looks at the last item in the list, or rather top of the stack. Unlike Pop, Peek doesn't remove it.
        if self.is_empty():
            raise IndexError("The Stack is empty")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Returns True when the internal list has zero items.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # This adds a value to the back of the line so older items stay in the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # This section removes the oldest items with the use of popleft(). The empty check works to raise an error in case the list is empty
        if self.is_empty():
            raise IndexError("The Queue is empty")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Front returns self.items[0] or rather the oldest or first item that was added to the list without removing it.
        # This works similarly to peek in the stack version
        if self.is_empty():
            raise IndexError("The Queue is empty")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("Stack s is created here, values 'A', 'B', 'C', 'D' are appended to the list at the end")
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")

    print("Peeking into the stack (before removing anything):", s.peek())

    print("Using pop, LIFO is demonstrated below, removing all the values added above:")

    print("Popped:", s.pop())
    print("Popped:", s.pop())
    print("Popped:", s.pop())
    print("Popped:", s.pop())

    print("The stack is now empty. Popping one more time to demonstrate the error:")
    try:
        print("Popped:", s.pop())
    except IndexError as error:
        print("An error was caught:", error)

    print("\n=== EDGE CASES ===")
    print("The following is what happens when peeking at an empty stack:")
    try:
        print("Peeking at the top of the stack:", s.peek())
    except IndexError as error:
        print("An error was caught:", error)

    print("Stack with one item test:")
    one_item = Stack()
    one_item.push("E")
    print("Popped:", one_item.pop())
    print("Verification that the stack is empty:", one_item.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    print("Real-world Scenario: A shared office printer. Jobs print in the order they were submitted.")
    q = Queue()
    q.enqueue("Job 4011")
    print("Submitted: Job 4011")
    q.enqueue("Job 4012")
    print("Submitted: Job 4012")
    q.enqueue("Job 4013")
    print("Submitted: Job 4013")
    q.enqueue("Job 4014")
    print("Submitted: Job 4014")

    print("Next job in the queue to print (front, nothing has been removed):", q.front())

    print("Printing jobs with dequeue. FIFO here means that the first job submitted prints first:")
    print("Printed:", q.dequeue())
    print("Printed:", q.dequeue())
    print("Printed:", q.dequeue())
    print("Printed:", q.dequeue())

    print("The queue is now empty. Dequeuing again to demonstrate error shows:")
    try:
        print("Printed:", q.dequeue())
    except IndexError as error:
        print("An error was caught:", error)

    print("\n=== QUEUE EDGE CASES ===")
    print("The following is what happens when checking the front of an empty queue:")
    try:
        print("Next job:", q.front())
    except IndexError as error:
        print("An error was caught:", error)

    print("Queue with one item test:")
    one_job = Queue()
    one_job.enqueue("Job 5001")
    print("Printed:", one_job.dequeue())
    print("Verification that the queue is empty:", one_job.is_empty())

if __name__ == "__main__":
    main()
