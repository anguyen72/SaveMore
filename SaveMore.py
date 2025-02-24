"""
Andrew Nguyen
2/19/2025
Project - Save More
I want to make an application to help people save and manage their money.
"""


import tkinter as tk
from tkinter import messagebox, PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MoneyPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SaveMore")
        self.root.geometry("600x400")

        # Load images (ensure the images exist in the project directory)
        self.income_icon = PhotoImage(file="money.png")  # Example image
        self.expense_icon = PhotoImage(file="receipt.png")  # Example image

        self.create_home_window()

    def create_home_window(self):
        """Home Page"""
        self.clear_window()

        tk.Label(self.root, text="SaveMore", font=("Arial", 16)).pack(pady=10)

        # Display images
        tk.Label(self.root, image=self.income_icon).pack()
        tk.Label(self.root, text="Income Tracking").pack()

        tk.Button(self.root, text="Income", command=self.open_income_window).pack(pady=5)
        tk.Button(self.root, text="Expenses", command=self.open_expenses_window).pack(pady=5)
        tk.Button(self.root, text="Budgeting", command=self.open_budgeting_window).pack(pady=5)
        tk.Button(self.root, text="Settings", command=self.open_settings_window).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def open_income_window(self):
        """Income Page"""
        self.clear_window()
        tk.Label(self.root, text="Income Page", font=("Arial", 14)).pack(pady=10)

        # Entry Field with Validation
        tk.Label(self.root, text="Enter Your Income:").pack()
        self.income_entry = tk.Entry(self.root)
        self.income_entry.pack()
        tk.Button(self.root, text="Submit", command=self.validate_income).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def validate_income(self):
        """Validate Income Entry"""
        try:
            income = float(self.income_entry.get())
            messagebox.showinfo("Success", f"Income Recorded: ${income}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def open_expenses_window(self):
        """Expenses Page"""
        self.clear_window()
        tk.Label(self.root, text="Expenses Page", font=("Arial", 14)).pack(pady=10)

        # Pie Chart Example (Simulating Expense Categories)
        fig, ax = plt.subplots(figsize=(4, 3))
        labels = ["Rent", "Food", "Transport", "Others"]
        sizes = [500, 200, 100, 150]
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def open_budgeting_window(self):
        """Budgeting Page"""
        self.clear_window()
        tk.Label(self.root, text="Budgeting Page", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def open_settings_window(self):
        """Settings Page"""
        self.clear_window()
        tk.Label(self.root, text="Settings Page", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def clear_window(self):
        """Helper function to clear the window before switching pages"""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyPlannerApp(root)
    root.mainloop()
