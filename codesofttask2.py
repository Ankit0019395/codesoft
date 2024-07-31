import tkinter as tk
from tkinter import messagebox


def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operation = operation_var.get()
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text="Result: " + str(result))
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Simple Calculator")


label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()


label_operation = tk.Label(root, text="Select operation:")
label_operation.pack()

operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")  

operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()


label_result = tk.Label(root, text="")
label_result.pack()


root.mainloop()

