# Python OOP Practice

**Author:** Hamza Abbas  
**Course:** CodeWithHarry Python  
**Course Chapter:** Chapter 10 — Object-Oriented Programming  
**Repository Folder:** `CHAPTER_09`

> Folder numbering in this repository starts from `CHAPTER_00`, so `CHAPTER_09` contains my practice for course Chapter 10.

## Overview

This folder contains my solutions to six beginner-level Object-Oriented Programming exercises.

The exercises cover creating classes and objects, storing information in attributes, writing methods, and updating an object's state.

## Topics Practised

- Classes and objects
- Instances and instance attributes
- Class attributes
- Initializing objects with `__init__`
- Using `self`
- Instance methods and return values
- Static methods with `@staticmethod`
- Attribute lookup and instance overrides
- Conditional logic inside methods

## Practice Exercises

| Exercise | Implementation | Main Concept |
| --- | --- | --- |
| 1. Programmer | Store programmer names and languages with a shared company name | Class and instance attributes |
| 2. Calculator | Calculate square, cube, and square root | Instance methods and `return` |
| 3. Attribute Comparison | Assign a value to one object's attribute and compare it with the class attribute | Instance attributes do not overwrite the class attribute |
| 4. Greeting | Add a static greeting method to the calculator | `@staticmethod` |
| 5. Train Booking | Display available seats and fare, book tickets, and reject bookings when seats run out | Updating object state |
| 6. Parameter Naming | Use another name in place of `self` | `self` is a naming convention |

## Example: Calculator

For the number `9`, the calculator produces:

```text
Square: 81
Cube: 729
Square root: 3.0
```

Each calculation is handled by a separate method.

## Example: Train Booking

The train example uses sample data:

- Train name: Mansehra Express
- Available seats: 3
- Fare per seat: 500

The program displays the initial status and fare, then attempts four bookings.

Expected behaviour:

```text
Available seats: 3
Fare: 500
Seat reserved!
Seat reserved!
Seat reserved!
NO seats Available
Available seats: 0
```

The first three bookings reduce the available seats. The fourth booking is rejected, and the seat count remains zero.

This is a learning exercise, not a real railway booking system.

## Key Lessons

1. A class defines a structure; an object is an instance of that class.
2. `__init__` initializes an object's information.
3. Instance attributes store information belonging to individual objects.
4. Class attributes can be accessed by instances that do not have their own attribute with the same name.
5. Assigning `object.a = 0` creates or updates that object's attribute without changing `Class.a`.
6. A method can update an object's stored values, such as reducing available seats.
7. A static method does not receive an automatic `self` argument.
8. The name `self` is a convention, not a reserved keyword. I will use `self` in regular Python code for clarity.

## How to Run

### Requirements

- Python 3
- A terminal or a Python editor such as VS Code

No third-party packages are required.

### Steps

1. Download or clone the repository.
2. Open this chapter folder.
3. Select an exercise file.
4. Run it using Python.

From a terminal opened in this folder:

```bash
python your_file.py
```

Replace `your_file.py` with the actual exercise filename.

On Windows, you can also use:

```bash
py your_file.py
```

## Current Scope

These are beginner practice solutions using sample values.

The calculator examples use positive numbers. The train example keeps its data in memory, so its seat count resets when the program starts again. Input validation and persistent storage are possible future improvements.

## Progress

- [x] Complete the six OOP practice exercises
- [x] Practise class and instance attributes
- [x] Practise instance and static methods
- [x] Build a basic seat-booking example

## Next Learning Goals

- Learn basic exception handling with `try` and `except`
- Handle invalid input and missing files
- Build a small project combining functions, File I/O, and appropriate OOP concepts