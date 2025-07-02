import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.configure(bg="white")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=('Segoe UI', 26),
                 bg="white", fg="black", bd=0, justify='right')
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=(10, 0))


def press(btn):
    global expression
    try:
        if btn == '=':
            expression = str(eval(expression))
        elif btn == 'C':
            expression = ''
        elif btn == '⌫':
            expression = expression[:-1]
        elif btn == '1/x':
            expression = str(1 / float(expression))
        elif btn == 'x²':
            expression = str(float(expression) ** 2)
        elif btn == '√':
            expression = str(math.sqrt(float(expression)))
        elif btn == '%':
            expression = str(float(expression) / 100)
        else:
            expression += str(btn)
    except:
        expression = "Error"
    input_text.set(expression)

def create_btn(frame, text, color="#f0f0f0", fg="black", w=5, h=2):
    return tk.Button(frame, text=text, font=('Segoe UI', 14), width=w, height=h,
                     bg=color, fg=fg, bd=0, relief=tk.FLAT, command=lambda: press(text))


memory_frame = tk.Frame(root, bg="white")
memory_frame.pack(pady=5)
for m in ['MC', 'MR', 'M+', 'M-', 'MS', 'Mv']:
    create_btn(memory_frame, m, color="#f9f9f9", fg="gray", w=6).pack(side='left', padx=2)

buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['+/-', '0', '.', '=']
]

btns_frame = tk.Frame(root, bg="white")
btns_frame.pack(pady=5)

for row in buttons:
    row_frame = tk.Frame(btns_frame, bg="white")
    row_frame.pack(expand=True, fill='both')
    for btn in row:
        if btn == '=':
            create_btn(row_frame, btn, color="#4ccfff", fg="white", w=6).pack(side='left', expand=True, fill='both', padx=2, pady=2)
        else:
            create_btn(row_frame, btn, w=6).pack(side='left', expand=True, fill='both', padx=2, pady=2)


def key(event):
    if event.char in '0123456789+-*/().':
        press(event.char)
    elif event.keysym == 'Return':
        press('=')
    elif event.keysym == 'BackSpace':
        press('⌫')


root.bind("<Key>", key)

root.mainloop()
