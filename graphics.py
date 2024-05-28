import tkinter as tk

def create_app():
    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("My Python App")

    # Create a label widget
    label = tk.Label(window, text="Hello, welcome to my Python app!")
    label.pack()

    # Create an entry widget for user input
    entry = tk.Entry(window)
    entry.pack()

    # Create a label widget for output
    output_label = tk.Label(window, text="")
    output_label.pack()

    # Create a button widget
    button = tk.Button(window, text="Submit", command=lambda: output_label.config(text="You entered: " + entry.get()))
    button.pack()

    # Run the event loop
    window.mainloop()

if __name__ == "__main__":
    create_app()
