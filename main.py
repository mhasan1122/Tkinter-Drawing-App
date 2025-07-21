import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="white")

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Task list
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
task_listbox.pack(pady=10)

# Delete and Clear buttons
delete_button = tk.Button(root, text="Delete Selected", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
clear_button.pack(pady=5)

# Start GUI
root.mainloop()
