import tkinter as tk

def create_app():
    # Create a new tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("My Python App")

    # Create a label widget
    label = tk.Label(window, text="Hello, welcome to my Python app!")
    label.pack()

    # Create a button widget
    button = tk.Button(window, text="Click me!", command=lambda: label.config(text="Button clicked!"))
    button.pack()

    # Run the event loop
    window.mainloop()

if __name__ == "__main__":
    create_app()
