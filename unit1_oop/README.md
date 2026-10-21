# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

---

# Implementation Documentation

## Design Approach

I built a small smart home model. `SmartDevice` was the parent class. It had a class variable (`hub_name`), instance variables (`name`, `room`, `_powered_on`), 
and the methods `power_on()`, `power_off()`, and `describe()`. `SmartLock` was the child class. 
It inherited from `SmartDevice`, called `super().__init__()` to reuse the parent's setup, and added a class variable (`max_attempts`), 
instance variables (`_pin`, `locked`, `failed_attempts`, `access_log`), and a new method (`unlock()`). It also overrode `describe()` so the output showed whether the lock was locked.

## Namespaces

`demonstrate_namespaces()` created two locks, a front door and a back door. 
I read `max_attempts` through the class and through an object, and both returned 3. 
I added `battery_low` to the back door only. 
Printing `__dict__` for each object showed that attribute in the back door's namespace. 
I also printed `SmartLock.__dict__` to show the class namespace, which held the class variable and the methods.

## Shallow vs. Deep Copy

`demonstrate_copying()` copied a lock that held a list (`access_log`). 
After I unlocked the original, its log and the shallow copy's log both showed the new entry, because they shared one list. 
The deep copy's log stayed empty because it had its own list. The `is` comparisons showed this (`True` for the shallow copy, `False` for the deep copy).

## Edge Case

I tested a lock with three wrong PINs and then showed the entering of the correct one. 
The first three attempts returned `Wrong PIN (1/3)`, `(2/3)`, and `(3/3)`. 
The correct PIN then resulted in the lockout message, and the lock stayed `LOCKED`. 
This happened because `unlock()` checked the failed attempt count before it checked the PIN. 
The access log held three `Failed attempt` entries resulting in the full Lockout.

Something that I was surprised with in the output is the length of the namespace output. Although it makes sense, after I completed the program, I found a way to print it better, but kept it for the sake of finishing the assignment.

## Real-World Use

I have smart devices in my home already and one that I keep having problems with is a smart bulb that disconnects itself from the network about every 3 months. I don't know what the correct solution would be to fix it, but it's evident that it was disconnected from the network because when I try to turn on the light, it continues to flash until a new connection is made. Relating to this class, the bulb is a device with a specific type of failure and its program handles the disconnection in a way that it can't recover on its own whereas in this program, the lockout is final. 

## How to Run

## Discussion Board Reflection

In the assignment, I learned how a child class reuses a parent through super(), how namespaces work, and the differences between a shallow copy and a deep copy. In my program, I built a smart home with a SmartDevice parent and a SmartLock child that locks out after three wrong PINs. The parent holds the shared attributes; the child inherits them and adds its own unlock().

My main challenge was small mistakes, partly because I'm transitioning from Java, and I feel like I just learned to use super in Java, so I was surprised to see it in Python. I kept running into problems where I had typos and missing commas, but after the constant errors, I managed  to get it right

Compared to procedural programming, where I'd send data to different functions, OOP keeps data and the code that uses that data in a single object. For example, the lock checks its own PIN and attempt counts, so I didn't have to repeat that logic whenever I needed to recall it.

This helps maintainability and reusability because I can change describe() in one place. Setting up classes can be tedious at first (overhead), but it pays off down the road with future projects where objects share the same traits. 


```
python unit1_discussion.py
```

