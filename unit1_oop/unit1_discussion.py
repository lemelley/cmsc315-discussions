"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SmartDevice:
    hub_name = "HomeHub"

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self._powered_on = False

    def power_on(self):
        self._powered_on = True

    def power_off(self):
        self._powered_on = False

    def describe(self):
        state = "ON" if self._powered_on else "OFF"
        return f"{self.name} in {self.room}: {state}"

    def __str__(self):
        return self.describe()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SmartLock(SmartDevice):
    max_attempts = 3

    def __init__(self, name, room, pin):
        super().__init__(name, room)
        self._pin = pin
        self.locked = True
        self.failed_attempts = 0
        self.access_log = []

    def unlock(self, pin):
        if self.failed_attempts >= self.max_attempts:
            return "Locked out, too many failed attempts"
        if pin == self._pin:
            self.locked = False
            self.failed_attempts = 0
            self.access_log.append("Unlocked")
            return "Unlocked"
        self.failed_attempts += 1
        self.access_log.append("Failed attempt")
        return f"Wrong PIN ({self.failed_attempts}/{self.max_attempts})"

    def describe(self):
        state = "LOCKED" if self.locked else "UNLOCKED"
        return super().describe() + ", " + state


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    d1 = SmartLock("Front Door", "Entryway", "1234")
    d2 = SmartLock("Back Door", "Kitchen", "2345")

    # Class variable accessed through the class itself and an object
    print("From the class:", SmartLock.max_attempts)
    print("From the object:", d1.max_attempts)

    # Add a new attribute to only one object after it is created
    d2.battery_low = True

    # Display object's namespace using __dict__
    print("\nd1.__dict__:", d1.__dict__)
    print("d2.__dict__:", d2.__dict__)

    # Display information about the class namespace

    print("\nSmartLock class namespace:", SmartLock.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    front_door = SmartLock("Front Door", "Entryway", "1234")

    # Shallow copy: new object but the access log is shared with the original
    shallow = copy(front_door)

    # Deep copy: new copy but copies the access log as well, creating an independent object
    deep = deepcopy(front_door)

    # Modify the original object's data
    front_door.unlock("1234")

    print("Original Access Log:", front_door.access_log)
    print("Shallow  Access Log:", shallow.access_log)
    print("Deep     Access Log:", deep.access_log)
    print("Same list object? shallow:", shallow.access_log is front_door.access_log,
          "\ndeep: ", deep.access_log is front_door.access_log)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n-- Parent Object --")
    lamp = SmartDevice("Bedroom lamp", "Main Bedroom")
    print(lamp)
    lamp.power_on()
    print(lamp)

    print("\n-- Child Object --")
    garage_door = SmartLock("Garage Door", "Garage", "1234")
    garage_door.power_on()
    print(garage_door)
    print("Unlock attempt:", garage_door.unlock("1234"))
    print(garage_door)

    print("\nEdge case: full Lockout after too many wrong attempts ")
    back_door = SmartLock("Back Door", "Kitchen", "5678")
    print("Trying wrong PIN 0000 = ", back_door.unlock("0000"))
    print("Trying wrong PIN 1111 = ", back_door.unlock("1111"))
    print("Trying wrong PIN 2222 = ", back_door.unlock("2222"))
    print("Trying correct PIN 5678 = ", back_door.unlock("5678"))
    print(back_door)
    print("Access log:", back_door.access_log)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
