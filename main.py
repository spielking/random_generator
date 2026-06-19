from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
#functions
def Copyright():
    win = Toplevel()
    win.title("Copyright data")
    win.geometry("300x100")
    win.minsize(300, 100)
    win.maxsize(300, 100)
    win.configure(bg="#121212")

    CopyrightLabel = Label(win, text="Copyright ©: \n", bg="#121212", fg="#ffffff", font=("Arial", 12))
    CopyrightLabel.pack(pady=(10, 0))
    CopyrightLabel2 = Label(win, text="spielking", bg="#121212", fg="#ffffff", font=("Arial", 12))
    CopyrightLabel2.pack(pady=(10, 0))

def inputArea(root):
    entry = Entry(root, width=20, bg="#312F2F", fg="#ffffff", font=("Arial", 23), borderwidth=0)
    entry.pack(pady=5)
    return entry

def check(entry_min, entry_max, entry_count, output):
    if not entry_min.get() or not entry_max.get() or not entry_count.get():
        messagebox.showerror("Input Error", "All fields must be filled in")
        return
    
    try:
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        count = int(entry_count.get())
    except ValueError:
        messagebox.showerror("Input Error", "Only numbers allowed!")
        return

    generate(entry_min, entry_max, entry_count, output)
    
def generate(entry_min, entry_max, entry_count, output):
    min_val = int(entry_min.get())
    max_val = int(entry_max.get())
    count = int(entry_count.get())
    if min_val > max_val:
        messagebox.showerror("Error", "Min cannot be greater than Max")
        return
    elif min_val == max_val:
        messagebox.showerror("Error", "Min Value = Max Value.")
        return
    elif min_val < 0 or max_val < 0:
        messagebox.showerror("Error", "Values must be non-negative")
        return
    elif count <= 0:
        messagebox.showerror("Error", "Count must be > 0")
        return
    elif count > 10000:
        messagebox.showerror("Error", "Too many numbers in Count")
        return
    elif max_val - min_val < 3:
        messagebox.showerror("Error", "Range too small")
        return
    
    #strError = str(entry_min.get()), str(entry_max.get()), str(entry_count.get()) 

    output.delete("1.0", END)

    for _ in range(count):
        num = random.randint(min_val, max_val)
        output.insert(END, str(num) + " ")

def clear(entry_min, entry_max, entry_count, output):
    entry_min.delete(0, END)
    entry_max.delete(0, END)
    entry_count.delete(0, END)
    output.delete("1.0", END)

def copyBuffer(root, outputTextArea):
    text = outputTextArea.get("1.0", END)
    if not text.strip():
        messagebox.showwarning("Warning", "Nothing to copy")
        return
    else:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Info", "Copied to clipboard")

def closeDesktopApp(root):
    root.destroy()
#main
def mainWindow():
    root = Tk()
    root.title("Random Generator")
    root.geometry("800x600")
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.configure(bg="#121212")
    #root.withdraw()
    #img = PhotoImage(file="background.png")
    #img_label = Label(root, image=img, bg="#121212")
    #img_label.pack(pady=20)

    #inputAreas
    inputAreaLabel1 = Label(root, text="Max value:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    inputAreaLabel1.pack(pady=(10, 0))
    entry_max = inputArea(root)

    inputAreaLabel2 = Label(root, text="Min value:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    inputAreaLabel2.pack(pady=(10, 0))
    entry_min = inputArea(root)

    inputAreaLabel3 = Label(root, text="Count:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    inputAreaLabel3.pack(pady=(10, 0))
    entry_count = inputArea(root)

    #TextArea
    ResultArea = Label(root, text="Result:", bg="#121212", fg="#ffffff", font=("Arial", 12))
    ResultArea.pack(pady=(10, 0))

    text_frame = Frame(root, bg="#121212")
    text_frame.pack(pady=5)

    scroll_y = Scrollbar(text_frame, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)

    outputTextArea = Text(text_frame, width=80, height=15, bg="#312F2F", fg="#ffffff", font=("Arial", 12), borderwidth=0, yscrollcommand=scroll_y.set, wrap=WORD)
    outputTextArea.pack(side=LEFT)

    scroll_y.config(command=outputTextArea.yview)
    
    #Buttons
    btn_copybuffer = Button(
    root,
    text="Copy",
    command=lambda: copyBuffer(root, outputTextArea),
    width=15,
    bg="#312F2F",
    fg="#ffffff",
    font=("Arial", 12)
)
    btn_copybuffer.pack(pady=(10,0))

    btn_copyright = Button(
    root,
    text="Copyright ©",
    command=Copyright,
    width=15,
    bg="#312F2F",
    fg="#ffffff",
    font=("Arial", 12)
)
    btn_copyright.place(x=625, y=43)

    btn_generate = Button(
    root,
    text="Generate",
    command=lambda: check(entry_min, entry_max, entry_count, outputTextArea),
    width=15,
    bg="#312F2F",
    fg="#ffffff",
    font=("Arial", 12)
)
    btn_generate.place(x=50, y=43)

    btn_clear = Button(
    root,
    text="Clear",
    command=lambda: clear(entry_min, entry_max, entry_count, outputTextArea),
    width=15,
    bg="#312F2F",
    fg="#ffffff",
    font=("Arial", 12)
)
    btn_clear.place(x=50, y=125)

    btn_exit = Button(root,
    text="Exit",
    command=lambda: closeDesktopApp(root),
    width=15,
    bg="#312F2F",
    fg="#ffffff",
    font=("Arial", 12))
    btn_exit.place(x=50, y=205)

    root.mainloop()

mainWindow()