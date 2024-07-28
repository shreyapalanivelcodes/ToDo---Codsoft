import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x400")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.master, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        # For simplicity, we won't implement task loading from a file
        # In a real application, you might load tasks from a database or file
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
