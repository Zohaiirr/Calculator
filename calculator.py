import tkinter as tk

# Colors
BG_COLOR = "#0f0f0f"
BTN_COLOR = "#00ffff"
TEXT_COLOR = "#ffffff"
BTN_HOVER = "#00ff9f"
ENTRY_COLOR = "#1a1a1a"

# Main window
root = tk.Tk()
root.title("Cyberpunk Calculator")
root.configure(bg=BG_COLOR)
root.geometry("340x500")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Consolas", 24), bg=ENTRY_COLOR, fg=TEXT_COLOR, bd=0,
                 justify="right", insertbackground=TEXT_COLOR)
entry.pack(pady=20, padx=10, fill='x')

# Button click logic
def on_click(symbol):
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, symbol)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
    ['C', '=', '', '']
]

# Frame for buttons (to use grid inside it)
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

# Create buttons inside the frame (not root)
def create_button(text, row, col):
    if text == "":
        return
    btn = tk.Button(frame, text=text, font=("Consolas", 18), fg=BTN_COLOR, bg=BG_COLOR,
                    activebackground=BTN_HOVER, activeforeground=TEXT_COLOR,
                    bd=0, width=5, height=2, command=lambda: on_click(text))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Render all buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        create_button(char, r, c)

root.mainloop()
