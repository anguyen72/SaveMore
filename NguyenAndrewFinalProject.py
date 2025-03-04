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
        self.root.title("SaveMore - Financial Planner")
        self.root.geometry("600x450")

        """Loaded Images"""
        self.income_icon = PhotoImage(file="money.png")
        self.expense_icon = PhotoImage(file="receipt.png")

        """Image sizes"""
        self.income_icon = self.income_icon.subsample(2, 2)
        self.expense_icon = self.expense_icon.subsample(2, 2)

        """Home window creation"""
        self.create_home_window()

    def create_home_window(self):
        """Home Page - Main navigation hub of the application."""
        self.clear_window()

        tk.Label(self.root, text="SaveMore", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text="Your personal finance tracker", font=("Arial", 12)).pack(pady=5)

        # Display income icon
        tk.Label(self.root, image=self.income_icon, compound="top").pack()
        tk.Button(self.root, text="Income", command=self.open_income_window).pack(pady=5)

        # Display expense icon
        tk.Label(self.root, image=self.expense_icon, compound="top").pack()
        tk.Button(self.root, text="Expenses", command=self.open_expenses_window).pack(pady=5)

        tk.Button(self.root, text="Budgeting", command=self.open_budgeting_window).pack(pady=5)
        tk.Button(self.root, text="Settings", command=self.open_settings_window).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_application).pack(pady=20)

    def open_income_window(self):
        """Income Page - Users can input their income."""
        self.clear_window()
        tk.Label(self.root, text="Income Page", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Enter Your Income:").pack()
        self.income_entry = tk.Entry(self.root)
        self.income_entry.pack()

        tk.Button(self.root, text="Submit", command=self.validate_income).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def validate_income(self):
        """User input for income."""
        income_text = self.income_entry.get().strip()
        if not income_text:
            messagebox.showerror("Error", "Income field cannot be empty!")
            return

        try:
            income = float(income_text)
            if income < 0:
                raise ValueError("Income cannot be negative.")
            messagebox.showinfo("Success", f"Income Recorded Successfully: ${income:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid numeric amount.")

    def open_expenses_window(self):
        """Expenses Page - Displays an expense chart."""
        self.clear_window()
        tk.Label(self.root, text="Expenses Page", font=("Arial", 14, "bold")).pack(pady=10)

        fig, ax = plt.subplots(figsize=(4, 3))
        labels = ["Rent", "Food", "Transport", "Others"]
        sizes = [500, 200, 100, 150]
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def open_budgeting_window(self):
        """Budgeting Page - Users can plan their budget."""
        self.clear_window()
        tk.Label(self.root, text="Budgeting Page", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Coming Soon: A budget planner tool!").pack()
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def open_settings_window(self):
        """Settings Page - Modify personal and app settings."""
        self.clear_window()
        tk.Label(self.root, text="Settings Page", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Coming Soon: Settings and customization!").pack()
        tk.Button(self.root, text="Back", command=self.create_home_window).pack(pady=20)

    def exit_application(self):
        """Exit the application with confirmation."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    def clear_window(self):
        """Helper to clear the window before switching pages."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyPlannerApp(root)
    root.mainloop()


