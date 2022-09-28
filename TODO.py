#Python to-do list is a SW that holds information about upcoming tasks or events.
#Features to be add in the application: Listbox, Scrollbars, Frame, Buttons, Entry box, Messagebox.
#import modules tkinter - step 1
from tkinter import *
from tkinter import messagebox

# Define a new task function
def newTask():
    task = my_entry.get()
    if task !="":
        lb.insert(END, task)
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# Define a delete task function
def deleteTask():
    lb.delete(ANCHOR)

# Create and configure window - step 2
# These instructions will specify the screen for the application.  
wd = Tk()
wd.geometry('500x500+500+300')
wd.title('Lista de afazeres')
wd.config(bg='#223441')
wd.resizable(width=False, height=False)

# Create a frame widget to hold other widgets, (UX)/(UI) clean and organized
# Place a listbox, scrollbars & buttons inside the frame.
frame = Frame(wd)
frame.pack(pady=10)

# Create a variable to store the listbox, give its specs
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
)
lb.pack(side=LEFT, fill=BOTH)

#Add data into the application
task_list = [
    'Ler por 45mins',
    'Fazer almoco',
    'Academia',
    'Escrever Software',
    'Soneca',
    ]

for item in task_list:
    lb.insert(END, item)

# Adding scrolls bars
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Adding entry box
my_entry = Entry(
    wd,
    font=('times', 24)
)
my_entry.pack(pady=20)

# Adding another frame for buttons
button_frame = Frame(wd)
button_frame.pack(pady=20)

# Adding buttons
add_task_button = Button(
    button_frame,
    text="Adicione tarefa",
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask,
)
add_task_button.pack(fill=BOTH, expand=True, side=LEFT)

del_task_button = Button(
    button_frame,
    text='Deletar tarefa',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask,
)
del_task_button.pack(fill=BOTH, expand=True, side=LEFT)

# App's main loop
wd.mainloop()
