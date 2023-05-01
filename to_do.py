# Import tkinter library for creating the graphical user interface (GUI)
import tkinter as tk

# Import tkinter.simpledialog for user input dialogs
import tkinter.simpledialog

# Import Calendar widget from tkcalendar library for date selection
from tkcalendar import Calendar

# Define a class for the to-do list application
class TodoList:
    def __init__(self):
        # Initialize the tkinter window
        self.window = tk.Tk()
        self.window.title("To-Do List")
        self.window.geometry("600x600")

        # an empty list to hold the to-do items
        self.todo_list = []

        # label for the to-do list
        self.label = tk.Label(self.window, text="To-Do List", font=("Arial", 16))
        self.label.pack(pady=10)

        # listbox to display the to-do items
        self.listbox = tk.Listbox(self.window, height=20, width=70)
        self.listbox.pack(pady=10)

        # buttons for adding, deleting, and updating to-do items
        self.add_button = tk.Button(self.window, text="Add", command=self.add_todo)
        self.add_button.pack()

        self.delete_button = tk.Button(self.window, text="Delete", command=self.delete_todo)
        self.delete_button.pack()

        self.update_button = tk.Button(self.window, text="Update", command=self.update_todo)
        self.update_button.pack()

        # button for selecting a due date for a to-do item
        self.calendar_button = tk.Button(self.window, text="Select Date", command=self.select_date)
        self.calendar_button.pack()

        # Initialize a variable to hold the selected due date
        self.selected_date = None

        # dictionary to map levels of importance to background colors
        self.color_map = {
            "low": "green",
            "medium": "yellow",
            "high": "red"
        }

        # label to display the importance key
        self.color_key = tk.Label(self.window, text="Importance Key:", font=("Arial", 12))
        self.color_key.pack(pady=10)

        # frame to hold the color key labels and boxes
        color_key_frame = tk.Frame(self.window)
        color_key_frame.pack()

        # labels and boxes for each level of importance
        self.low_key = tk.Label(color_key_frame, text="Low: ", font=("Arial", 9))
        self.low_key.pack(side="left", padx=10)
        self.low_box = tk.Canvas(color_key_frame, width=15, height=15, bg=self.color_map["low"])
        self.low_box.pack(side="left", padx=5)

        self.medium_key = tk.Label(color_key_frame, text="Medium: ", font=("Arial", 9))
        self.medium_key.pack(side="left", padx=10)
        self.medium_box = tk.Canvas(color_key_frame, width=15, height=15, bg=self.color_map["medium"])
        self.medium_box.pack(side="left", padx=5)

        self.high_key = tk.Label(color_key_frame, text="High: ", font=("Arial", 9))
        self.high_key.pack(side="left", padx=10)
        self.high_box = tk.Canvas(color_key_frame, width=15, height=15, bg=self.color_map["high"])
        self.high_box.pack(side="left", padx=5)

        # Start the tkinter event loop
        self.window.mainloop()

    # Define a method for adding a new to-do item to the list
    def add_todo(self):
        # Ask the user to enter a new to-do item
        todo = tk.simpledialog.askstring("New To-Do", "Enter a new to-do:")
        if todo:
            importance = tk.simpledialog.askstring("Importance", "Enter a level of importance (low, medium, high):")
            self.todo_list.append((todo, self.selected_date, importance))
            self.update_listbox()

    def delete_todo(self):
        # Get the selected item from the listbox
        selection = self.listbox.curselection()
        # Check if a selection was made
        if selection:
            # Get the index of the selected item
            index = selection[0]
            # Remove the item from the todo_list
            self.todo_list.pop(index)
            # Update the listbox to reflect the changes
            self.update_listbox()

    def update_todo(self):
        # Get the selected item from the listbox
        selection = self.listbox.curselection()
        # Check if a selection was made
        if selection:
            # Get the index of the selected item
            index = selection[0]
            # Get the current todo, date, and importance values from the todo_list
            todo, date, importance = self.todo_list[index]
            # Ask the user for a new todo value
            new_todo = tk.simpledialog.askstring("Update To-Do", "Enter a new value for the selected to-do:", initialvalue=todo)
            # Check if the user entered a value
            if new_todo:
                # Update the todo_list with the new todo value
                self.todo_list[index] = (new_todo, date, importance)
                # Update the listbox to reflect the changes
                self.update_listbox()

    def select_date(self):
        # Create a new window
        top = tk.Toplevel(self.window)
        # calendar widget in the new window
        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US', date_pattern='mm-dd-yyyy')
        cal.pack(fill="both", expand=True)
        # make a "OK" button to close the window and set the selected date
        ok_button = tk.Button(top, text="OK", command=lambda: self.set_date(cal.selection_get()))
        ok_button.pack()

    def set_date(self, date):
        # Set the selected_date attribute to the selected date
        self.selected_date = date

    def update_listbox(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)
        # Loop through the todo_list and add each item to the listbox
        for todo, date, importance in self.todo_list:
            if date is not None:
                # Add the todo and date to the listbox if a date exists
                self.listbox.insert(tk.END, "{} ({})".format(todo, date))
            else:
                # Add only the todo to the listbox if no date exists
                self.listbox.insert(tk.END, todo)
            # Get the background color for the item based on its importance level
            bg_color = self.color_map.get(importance, "white")
            # Set the background color of the item in the listbox
            self.listbox.itemconfigure(tk.END, bg=bg_color)

# Create a TodoList object if this file is run as the main program
if __name__ == "__main__":
    TodoList()