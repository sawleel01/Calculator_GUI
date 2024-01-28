import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_display()

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        update_display()
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = calculation[:-1]  # Remove the last character
    update_display()

def clear_all():
    global calculation
    calculation = ""
    update_display()

def update_display():
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

root = tk.Tk()
root.geometry("300x375")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda b=button: add_to_calculation(b) if b != '=' else evaluate_calculation()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", width=5, height=2, command=clear_field).grid(row=row_val, column=col_val)

# Backspace button
tk.Button(root, text="<-", width=5, height=2, command=clear_field).grid(row=row_val, column=col_val + 1)

# Clear All button
tk.Button(root, text="AC", width=5, height=2, command=clear_all).grid(row=row_val, column=col_val + 2)

root.mainloop()
