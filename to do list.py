# Import the required libraries
import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create task list box
        self.task_list = tk.Listbox(self.root, width=40, height=10)
        self.task_list.pack(pady=10)

        # Create task entry box
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        # Create buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        # Create add task button
        add_task_button = tk.Button(buttons_frame, text="Add Task", command=self.add_task)
        add_task_button.pack(side=tk.LEFT, padx=10)

        # Create delete task button
        delete_task_button = tk.Button(buttons_frame, text="Delete Task", command=self.delete_task)
        delete_task_button.pack(side=tk.LEFT, padx=10)

        # Create save tasks button
        save_tasks_button = tk.Button(buttons_frame, text="Save Tasks", command=self.save_tasks)
        save_tasks_button.pack(side=tk.LEFT, padx=10)

        # Create load tasks button
        load_tasks_button = tk.Button(buttons_frame, text="Load Tasks", command=self.load_tasks)
        load_tasks_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved successfully")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = file.readlines()
                self.tasks = [task.strip() for task in self.tasks]
                self.task_list.delete(0, tk.END)
                for task in self.tasks:
                    self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved tasks found")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()
