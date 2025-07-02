import tkinter as tk

# Function to update the expression in the text entry box
def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to evaluate the final expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Main GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.resizable(0, 0)

expression = ""
input_text = tk.StringVar()

# Entry field for expressions
input_frame = tk.Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Buttons
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# First row
tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click("/")).grid(row=0, column=3, padx=1, pady=1)

# Second row
tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(7)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(8)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(9)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third row
tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(4)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(5)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(6)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth row
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=evaluate).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()