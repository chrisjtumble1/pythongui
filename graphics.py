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

    # Create a dropdown menu
    options = ["Option 1", "Option 2", "Option 3"]
    selected_option = tk.StringVar(window)
    selected_option.set(options[0])  # set the default option
    dropdown = tk.OptionMenu(window, selected_option, *options)
    dropdown.pack()

    # Create a button widget
    button = tk.Button(window, text="Submit", command=lambda: output_label.config(text="You entered: " + entry.get() + ", You selected: " + selected_option.get()))
    button.pack()

    # Run the event loop
    window.mainloop()

if __name__ == "__main__":
    create_app()
