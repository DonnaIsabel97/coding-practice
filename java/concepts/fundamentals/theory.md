# Java Fundamentals

## 1. Variables

### What is a variable?

> A variable is a named location used to store data that can be accessd and, depending on how it is declared, changed throughout a program.

### Declaration vs. Initialization

**Declaration:**

> In declaration, I define the variable's name and data type, such as `String`, `int`, or an array.

**Initialization:**

> In initialization, I assign the variable its initial value. For example, I can initialize an empty array or initialize an integer with the value of `2`. 

Example:

```java
 // Declaration

 String a;

 //Initialization

 a = "Hello";

 // We can declare and initialize simultaneosly

 String a = "Hello";
 int b = 2;

```

### Variable Types / Scope

Explain each:

* **Local variable:** Declared inside a method, constructor or block. Accessible only within that block.
* **Instance variable:** Declare inside a class but outside any method. Each object of the class has its own copy.
* **Static/Class variable:** Declared with the static keyword inside a class. Shared by all objects of the class.

### `final`

**What does `final` mean when applied to a variable?**

> When you apply the keyword final to a variable, the value cannot be changed once assigned.

**When would I use it?**

> Whe you need an inmutable variable

Example:

```java
public class VariablesDemo{
    // Instance variable
    int instaceVar = 10;

    // Static variable
    static String staticVar = "I am static";

    final int finalVar = 120;

    public void showVariables(){
        int localVar = 5;

        System.out.print("Local variable: " + localVar);
        System.out.print("Static variable: " + staticVar);
        System.out.print("Instance Variable: " + instanceVar);
        System.out.print("Final Variable: " + finalVar);
    }

    public static void main(Strings[] args){
        // Creating an object
        VariablesDemo obj1 = new VariablesDemo();
        obj1.showVariables();

        //Accesing static variable directly using class name
        System.out.print("Accessing static variable via Class: " + VariablesDemo.staticVar );
    }
}
```

---

# 2. Primitive Data Types

## What is a primitive type?

> Primitive data types are predefined, built-in types in Java that represent simple values. Java has eight primitive types. Unlike reference types, primitive variables hold their values directly and cannot be null. Primitives are not objects, so they do not have methods.

## The 8 Primitive Types

| Type      | What does it store?                                        | Example                        |
| --------- | ---------------------------------------------------------- | ------------------------------ |
| `byte`    | Whole numbers from -128 to 127 in 1 byte of memory         | byte age = 25                  |
| `short`   | Whole numbers from -32768 to 32767 in 2 bytes of memory    | short year = 2050              |
| `int`     | Whole numerbes from -2B to 2B in 4 bytes of memory         | int salary = 55000             |
| `long`    | Massive numbers up to 9 quintillion in 8 bytes of memory   | long population = 80000000000L |
| `float`   | Fractional decimal numbers with 6/7 digit of precision     | float pi = 3.14f               |
| `double`  | Fractional decimal numbers with 15 digit of precision      | double price= 19.99            |
| `char`    | Single letter, number or symbol enclosed in single quotes  | char grade = 'A'(single quotes)|
| `boolean` | Only 2 possible states                                     | boolean isJavaFun = true       |

## Things to Remember

**Which type would I normally use for whole numbers?**

> I would normally use `int`.

**Which type would I normally use for decimal numbers?**

> I would normally use `double`.

**What is the difference between `float` and `double`?**

> The main difference between `float` and `double` is their precision. A `double` can store more decimal digits and provides greater precision than a `float`.

**What does `char` represent?**

> It represent a single character, such as a letter, numbe or symbol

---

# 3. Primitive vs. Reference Types

## Primitive Types

> Predefined data types that store raw data values directly in Stack memory and cannot by null.

Example:

```java
```

## Reference Types

> Non-primitive types that store memory addresses (references) pointing to dynamically allocated objects on the Heap.

Examples of reference types:

* Strings
* Arrays
* Classes

## Key Differences

| Primitive            | Reference               |
| -------------------- | ----------------------- |
| Stores actual values | Stores memory addresses |
| Cannot be null       | Can be null             |
| Cannot call methods  | Can call methods        |

### Interview Question

**What is the difference between a primitive type and a reference type in Java?**

My answer:

> Primitive variables hold their values directly, while reference variables hold references to objects or arrays. Java has eight primitive types, and unlike reference types, primitives cannot be null.

---

# 4. Type Casting

## What is type casting?

> Type casting is the process of converting a values from one data type to another.

## Widening Casting

**What is it?**

> Widening castin is converting smaller data type to a larger data type size.

**Is it automatic or manual?**

> It's automatic.

Example:

```java

int myInt = 9;

double myDouble = myInt; // Automatically casting: int to double
```

## Narrowing Casting

**What is it?**

> Narrowing casting is converting a larger data type to a smaller data type size.

**Is it automatic or manual?**

> It's manual.

Example:

```java
double myDouble = 9.78d;

int myInt = (int) myDouble; // Manual cating: double to int
```

### Interview Question

**Why can narrowing conversion cause data loss?**

> Narrowing conversion can cause data loss because we are converting a value from a type with a larger range or greater precision to a type with a smaller range or lower precision. The destination type may not be able to represent the original value completely.

## Reference Type Casting

**What is it?**

> Reference types can also be converted between compatible types, particularly when inheritance or interfaces are involved.

### Upcasting

**What is it?**

> Converting a subclass reference to a superclass reference.

Example:

```java
Dog dog = new Dog();
Animal animal = dog;
```
### Downcasting

> Converting a superclass reference back to a more specific subclass reference. Requires explicit casting, and an important risk is that can cause a `ClassCastException` at runtime.
> More in OOP section

Example:

```java
Animal animal - new Cat();
Dog dog = (Dog) animal; //ClassCastException
```

---

# 5. Operators

## Arithmetic Operators

Examples:

```text
+
-
*
/
%
```

What does `%` do?

> It would answer with the module 

## Comparison Operators

```text
==
!=
>
<
>=
<=
```

## Logical Operators

```text
&&
||
!
```

Explain:

* `&&` → Reference to the `and` logical operator, i.e. a condition only would be true if both statements are true.
* `||` → Reference to the `or` logical operator, i.e. a condition would be true if either of the statements are true.
* `!` → Referent to the `not` operation, i.e a condition would be true if the statement/statements are different to the target.

## Increment / Decrement

Explain the difference between:

```java
++x
x++
```

> 

---

# 6. Conditional Statements

## `if / else`

**When would I use it?**

>

Example:

```java
```

## `else if`

Example:

```java
```

## `switch`

**When might `switch` be preferable to multiple `if/else` statements?**

>

Example:

```java
```

---

# 7. Loops

## `for`

**When would I normally use a `for` loop?**

>

Example:

```java
```

## `while`

**When would I normally use a `while` loop?**

>

Example:

```java
```

## `do-while`

**What makes `do-while` different from `while`?**

>

Example:

```java
```

## `break` and `continue`

**`break`:**

>

**`continue`:**

>

### Interview Question

**When would I choose `for` vs. `while` vs. `do-while`?**

>

---

# 8. Methods

## What is a method?

>

## Basic Structure

```java
returnType methodName(parameters) {
    
}
```

Explain:

* **Return type:**
* **Method name:**
* **Parameters:**
* **Method body:**
* **Return statement:**

## Parameters vs. Arguments

**Parameter:**

>

**Argument:**

>

Example:

```java
```

## `void`

What does `void` mean?

>

## Return Values

Example:

```java
```

---

# 9. Method Overloading

## What is method overloading?

>

Example:

```java
```

## How can methods be overloaded?

*
*
*

## What cannot be used by itself to overload a method?

>

### Interview Question

**What is the difference between method overloading and method overriding?**

>

> Note: Revisit this question after studying OOP and inheritance.

---

# 10. Arrays — Basic Introduction

## What is an array?

>

## Declaration

```java
```

## Initialization

```java
```

## Accessing Elements

```java
```

## Iterating Through an Array

### Traditional `for`

```java
```

### Enhanced `for`

```java
```

## Important Characteristics

* Are arrays fixed or dynamic in size?
* What index does an array start at?
* How do I get the length of an array?
* What happens if I access an invalid index?

---

# 🧠 Interview Quick Review

After completing this file, I should be able to answer these **without looking at my notes**:

1. What are Java's eight primitive types?
2. What is the difference between primitive and reference types?
3. What does `final` mean?
4. What is widening vs. narrowing casting?
5. What is the difference between `==` and `=`?
6. What is the difference between `&&` and `||`?
7. When would I use `for`, `while`, or `do-while`?
8. What is the difference between a parameter and an argument?
9. What does `void` mean?
10. What is method overloading?
11. What is the difference between `break` and `continue`?
12. How do Java arrays work?

---

# 📝 My Weak Areas

Concepts I need to review again:

*
*
*

# 💡 Key Takeaways

The 3–5 most important things I learned:

1.
2.
3.
4.
5.
