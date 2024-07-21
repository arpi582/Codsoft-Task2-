import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        
        self.tasks = []
        self.load_tasks()
        
        # Title Label
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
        self.title_label.pack(pady=10, fill=tk.X)
        
        # Task Listbox with Scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(self.frame, font=("Helvetica", 12), width=30, height=10, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.add_button.pack(pady=5)
        
        # Update Task Button
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.update_button.pack(pady=5)
        
        # Delete Task Button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.delete_button.pack(pady=5)
        
        # Mark as Completed Button
        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.complete_button.pack(pady=5)
        
        # Save Tasks Button
        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.save_button.pack(pady=5)
        
        # Load Initial Tasks (if any)
        self.update_listbox()

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]["task"]
            new_task = simpledialog.askstring("Update Task", "Update task:", initialvalue=selected_task)
            if new_task:
                self.tasks[selected_task_index[0]]["task"] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")
            
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            
    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = not self.tasks[selected_task_index[0]]["completed"]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
            
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["completed"]:
                task_text += " (Completed)"
            self.task_listbox.insert(tk.END, task_text)
            
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Info", "Tasks saved successfully.")
        
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
