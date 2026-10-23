"""
Python Calculator (Tkinter)

A simple graphical calculator with a display and buttons.
It supports the four basic operations (+, -, *, /), the "="
button to show the result, and the "c" button to clear the display.
Invalid expressions and division by zero show "Error".
"""

import tkinter as tk


def press(symbol):
    """Add the pressed number or operator to the display."""
    entry.insert(tk.END, symbol)


def clear():
    """Clear the display."""
    entry.delete(0, tk.END)


def calculate():
    """Evaluate the expression in the display and show the result."""
    expression = entry.get()
    try:
        result = eval(expression)
        if result == int(result):
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except (ZeroDivisionError, SyntaxError, NameError):
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Python Calculator")

entry = tk.Entry(window, width=25, borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout: each row is a list of button labels
layout = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["c", "0", "=", "/"],
]

for row_index, row in enumerate(layout, start=1):
    for col_index, symbol in enumerate(row):
        if symbol == "c":
            command = clear
        elif symbol == "=":
            command = calculate
        else:
            command = lambda s=symbol: press(s)

        tk.Button(
            window,
            text=symbol,
            width=10,
            command=command,
        ).grid(row=row_index, column=col_index)

window.mainloop()
