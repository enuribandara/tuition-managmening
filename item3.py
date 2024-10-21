from tkinter import Tk, Label

# Create the main window
window = Tk()

# Set the window size
window.geometry("600x300")

# Add a label
label = Label(window, text="Welcome to the Tuition Management System!")
label.pack(pady=20)

# Run the application
window.mainloop()
