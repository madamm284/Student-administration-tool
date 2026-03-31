# Student-administration-tool
I have developed a small administrative tool that calculates degree classification 
#  Student Exam Result Checker (Python)

A simple Python console application that allows users to input exam scores, calculate an average, optionally apply a bonus, and receive a provisional classification.

---

##  Features

* Input multiple exam scores (comma-separated)
* Automatically rounds scores
* Calculates total and average score
* Optional bonus system (+5 points)
* Displays provisional classification based on the result
* Checks if a specific score exists in the record
* Demonstrates:

  * Membership operators (`in`)
  * Identity operators (`is`)
  * Bitwise operators (`&`, `|`, `^`)

---

##  Concepts Practiced

* Lists and list comprehension
* User input handling
* Conditional statements (`if / elif / else`)
* Boolean logic
* Operators in Python:

  * Arithmetic
  * Membership
  * Identity
  * Bitwise

---

##  How It Works

1. User enters their name

2. User inputs exam scores separated by commas
   Example:

   ```
   70, 80.5, 65
   ```

3. Scores are:

   * Converted to numbers
   * Rounded
   * Stored in a list

4. Program calculates:

   * Total score
   * Average score

5. User chooses whether a bonus should be applied:

   * If **yes** →  "Enter the amount of bonus" points added

6. The final result is displayed along with the classification

---



##  Additional Features

### Score Lookup

Check if a specific score exists in your records:

```python
if check_score in exam_score:
```

###  Identity Check

Demonstrates reference equality:

```python
backup_scores is exam_score
```

### Bitwise Operations

Applies bitwise operators to the first two scores:

```python
a & b   # AND
a | b   # OR
a ^ b   # XOR
```

---

##  Example Output

```
Processing result for: John Smith
Outcome: 75
Provisional Classification: 2.1 Very Good!

Your score is in the record!
Both are the same data

Bitwise AND of the first two scores: 64
Bitwise OR of first two scores: 86
Bitwise XOR of first two scores: 22
```

---

##  Future Improvements

* Add input validation (handle empty or incorrect input)
* Allow editing/removing scores
* Convert into a simple web app
* Save results to a file (CSV/JSON)

---

##  Author

Built as part of a Python learning journey while transitioning into tech. Inspired by the Excel spreadsheet used at work. 
