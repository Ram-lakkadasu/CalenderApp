import calendar
import tkinter as tk
from tkinter import ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.year = tk.IntVar()
        self.month = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        # Year input
        self.year_label = ttk.Label(self.root, text="Year:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)
        self.year_entry = ttk.Entry(self.root, textvariable=self.year)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)

        # Month input
        self.month_label = ttk.Label(self.root, text="Month:")
        self.month_label.grid(row=1, column=0, padx=5, pady=5)
        self.month_entry = ttk.Entry(self.root, textvariable=self.month)
        self.month_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to display calendar
        self.show_button = ttk.Button(self.root, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Calendar display area
        self.calendar_text = tk.Text(self.root, height=10, width=25)
        self.calendar_text.grid(row=3, columnspan=2, padx=5, pady=5)

    def show_calendar(self):
        try:
            year = self.year.get()
            month = self.month.get()
            cal = calendar.month(year, month)
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, cal)
        except ValueError:
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, "Please enter valid year and month.")

def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
