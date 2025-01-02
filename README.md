# Piscine_Python

This README is designed to explain the Python concepts encountered in each exercise. It clarifies common challenges for developers transitioning from C or other languages to Python.

---

## Exercice 00: Lists, Tuples, Sets, and Dictionaries

### Understanding Python Data Types

1. **List (`ft_list`)**

   - **Definition:** An **ordered, mutable** collection of items.
   - **Syntax:** `ft_list = ["Hello", "World!"]`
   - **Key Properties:**
     - Supports duplicate elements.
     - Elements can be added, removed, or modified.
   - **Accessing Items:** Index-based. Example: `ft_list[0]` returns `"Hello"`.
   - **Common Use Case:** Storing a collection of related items in order.

2. **Tuple (`ft_tuple`)**

   - **Definition:** An **ordered, immutable** collection of items.
   - **Syntax:** `ft_tuple = ("Hello", "France!")`
   - **Key Properties:**
     - Cannot be changed after creation.
     - Supports indexing like lists.
   - **Accessing Items:** Example: `ft_tuple[1]` returns `"France!"`.
   - **Common Use Case:** Fixed sets of related data that shouldn't change (e.g., coordinates).

3. **Set (`ft_set`)**

   - **Definition:** An **unordered collection of unique items**.
   - **Syntax:** `ft_set = {"Hello", "Paris!"}`
   - **Key Properties:**
     - Automatically removes duplicates.
     - Does not support indexing (items have no specific order).
   - **Common Use Case:** Removing duplicates or performing set operations like union or intersection.

4. **Dictionary (`ft_dict`)**

   - **Definition:** A **collection of key-value pairs**.
   - **Syntax:** `ft_dict = {"Hello": "42Paris!"}`
   - **Key Properties:**
     - Keys must be unique.
     - Values can be any type.
   - **Accessing Items:** Example: `ft_dict["Hello"]` returns `"42Paris!"`.
   - **Common Use Case:** Storing relationships or mappings between keys and values.

---

## Exercice 01: f-strings and Date Formatting

1. **What is an f-string?**

   - Syntax: `f"Your text {expression}"`
   - Allows embedding expressions inside strings, evaluated at runtime.
   - Example:
     ```python
     timestamp = 1666355857.3622
     print(f"Seconds since January 1, 1970: {timestamp:.4f}")
     ```
     - `{timestamp:.4f}` formats the value to 4 decimal places.
     - `{timestamp:.2e}` formats the value in scientific notation.

2. **What does `%b` mean?**

   - Used with the `strftime()` method for formatting dates.
   - `%b`: Abbreviated month name (e.g., "Oct" for October).
   - Example:
     ```python
     from datetime import datetime
     print(datetime.now().strftime("%b %d %Y"))  # Outputs: Oct 21 2022
     ```
   - Other format codes:
     - `%d`: Day of the month.
     - `%Y`: Full year.

---

## Exercice 02: Object Types and `__name__`

1. **Understanding `type()`**

   - The `type()` function returns the type of an object.
   - Example:
     ```python
     obj = [1, 2, 3]
     print(type(obj))  # Outputs: <class 'list'>
     ```

2. **What does `.__name__` do?**

   - `type(obj).__name__` extracts the **name of the type** as a string (e.g., "list", "str").
   - Example:
     ```python
     obj = [1, 2, 3]
     print(type(obj).__name__)  # Outputs: list
     ```

3. **What is `__name__`?**

   - `__name__` is a special variable in Python that indicates whether a script is being run directly or imported as a module.
   - Syntax:
     ```python
     if __name__ == "__main__":
         print("This script is being run directly!")
     ```
   - **Meaning:**
     - When the script is run directly, `__name__` is set to `"__main__"`.
     - When the script is imported as a module, `__name__` is set to the module's name.

   **Why use it?**
   - To define behavior that only executes when the script is run directly, not when imported.

---

## Exercice 03: Handling Exceptions

1. **What is `try` and `except`?**

   - A way to handle errors gracefully in Python without crashing the program.
   - Syntax:
     ```python
     try:
         # Code that might raise an exception
     except ExceptionType:
         # Handle the exception
     ```

2. **Why use `try-except` in Ex03?**

   - The function checks if the type of an object can be determined.
   - If an error occurs (e.g., invalid input), it prevents the program from crashing by catching the exception.
   - Example:
     ```python
     try:
         print(f"{obj}: {type(obj)}")
         return 0
     except Exception:
         print("Type not Found")
         return 1
     ```

3. **Why don't we use `.__name__` here?**

   - In Ex03, the goal is to print both the object and its type for debugging purposes.
   - Using `type(obj)` provides more detailed information (e.g., `<class 'list'>`), which can be helpful for identifying issues.
   - If simplicity is preferred, you could still use `type(obj).__name__` for a cleaner output.

---

## Exercice 04: Using `raise`

1. **What is `raise`?**

   - `raise` is used to explicitly raise an exception in Python.
   - Example:
     ```python
     if len(sys.argv) != 2:
         raise AssertionError("More than one argument is provided")
     ```

2. **Why use `raise`?**

   - To signal that an error has occurred and stop execution immediately.
   - **Key Differences:**
     - `raise` is for explicitly triggering exceptions.
     - `try-except` is for catching and handling exceptions.

3. **Common Use Cases:**

   - Validating inputs:

     ```python
     if not isinstance(arg, int):
         raise ValueError("Expected an integer")
     ```

   - Stopping execution when a critical error occurs:

     ```python
     raise RuntimeError("Critical error occurred!")
     ```

---

docstring and flake8

generator and iterator (yield)

ex05 how __main__ works
ex06 what filter does. what is a generator and list comprehension et lambda
ex07 join et rstrip
ex08 '\r' and sys.stdout.write doesnt have '\n' compare to print, iterateur et yield

