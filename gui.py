import tkinter as tk
import tkinter.ttk as ttk
window = tk.Tk()

greeting = tk.Label(
    text = "Hello, Tkinter",
    foreground="white",
    background="#34A2FE"
    )
greeting.pack()

entry = tk.Entry(
    fg="white",
    bg="#34A2FE"
)
entry.pack()

button = tk.Button(
    text="Click me!",
    fg="white",
    bg="#34A2FE"
)
button.pack()

text_box = tk.Text(
    bg = "gray"
)
text_box.pack()


##run the app and listen for events
window.mainloop()