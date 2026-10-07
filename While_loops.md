# Python Lesson: `while` Loops

## What is a `while` loop?

A `while` loop repeats a block of code **as long as a condition is true**. It's useful when you don't know in advance exactly how many times you need to repeat something — you just know the *condition* under which you should keep going (or stop).

```python
while condition:
    # do something
```

Python checks the condition before every pass through the loop. As soon as it's `False`, the loop stops and the program moves on.

---

## Example 1: Counting down with `while True` and `break`

```python
x = 500
y = 0

while True:
    if x > 0:
        x = x - 100
        print(x)
    else:
        break
```

### How it works

- `while True:` creates a loop that would normally run **forever**, since `True` is always true.
- Inside the loop, we check `if x > 0:`. If it is, we subtract 100 from `x` and print it.
- If `x` is *not* greater than 0 (i.e., it's reached 0 or below), we hit `break`, which immediately exits the loop.

### Tracing through it

| Pass | `x` before | Is `x > 0`? | Action | `x` after | Printed |
|------|-----------|-------------|--------|-----------|---------|
| 1 | 500 | Yes | subtract 100 | 400 | `400` |
| 2 | 400 | Yes | subtract 100 | 300 | `300` |
| 3 | 300 | Yes | subtract 100 | 200 | `200` |
| 4 | 200 | Yes | subtract 100 | 100 | `100` |
| 5 | 100 | Yes | subtract 100 | 0 | `0` |
| 6 | 0 | No | `break` | — | (loop ends) |

**Output:**
```
400
300
200
100
0
```

### Key idea: the "infinite loop + break" pattern

Notice this loop uses `while True`, which never becomes false on its own. Instead, we control when it stops using `break` inside an `if` statement. This is a very common pattern in Python — it gives you full control over *exactly* when and why the loop exits, rather than relying on the `while` condition itself.

> **Note:** The variable `y = 0` is created at the top but never used in the loop. It doesn't affect the program — but it's a good reminder that unused variables can be a sign of leftover or incomplete code!

### Equivalent version without `while True`

You could also write this same logic using the condition directly:

```python
x = 500

while x > 0:
    x = x - 100
    print(x)
```

Both versions produce the same output. The `while True` + `break` version is useful when the stopping logic is more complex than a simple condition (see Example 2).

---

## Example 2: Getting input from the user until they type "exit"

```python
while True:
    z = input("multiply?")
    if z == "exit":
        break
```

### How it works

- Again, `while True:` starts a loop with no built-in stopping point.
- `z = input("multiply?")` pauses the program, shows the prompt `multiply?`, and waits for the user to type something.
- If what the user typed is exactly `"exit"`, the loop `break`s and ends.
- Otherwise, the loop repeats and asks again.

### Why use `while True` here?

This is a great example of when `while True` is genuinely necessary: we don't know **how many times** the user will need to respond before they type "exit". It could be once, or it could be a hundred times. Using `while True` with a `break` lets the loop keep running *indefinitely* until the user gives us a specific signal to stop.

### Try it yourself

This loop currently reads input but doesn't do anything with it besides checking for `"exit"`. As an exercise, try modifying it to actually multiply numbers:

```python
while True:
    z = input("Enter a number to multiply by 2 (or 'exit' to quit): ")
    if z == "exit":
        break
    number = float(z)
    print(number * 2)
```

---