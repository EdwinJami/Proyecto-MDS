from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import PhotoImage
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
from tkcalendar import Calendar

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Encabezado
header = Label(root, text='Gestión de eventos escolares de la Unidad Educativa "Lev Vygotsky"', bg='#fff', fg='#333', font=('Arial', 20, 'bold'))
header.pack(pady=20, padx=20)

# Resto del código sin cambios
img = PhotoImage(file='login.png')
label_img = Label(root, image=img, bg='white')
label_img.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def signin():
    username=user.get()
    password=code.get()

    if username == 'Anahy' and password == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        cal = Calendar(screen, selectmode='day', year=2024, month=3, day=13)
        cal.pack(pady=20)

        screen.mainloop()

    elif username != 'admin' and password != '1234':
        messagebox.showerror("Inválido", "nombre de usuario y contraseña inválidos")

    elif password != "1234":
        messagebox.showerror("Inválido", "contraseña inválida")

    elif username != 'Anahy':
        messagebox.showerror("Inválido", "usuario inválida")

img = PhotoImage(file='login.png')
label_img = Label(root, image=img, bg='white')
label_img.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
###############################################################
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Nombre de usuario')

user = Entry(frame, width=25, fg='black', bd=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Nombre de usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
################################################################

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Contraseña')

code = Entry(frame, width=25, fg='black', bd=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

################################################################
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

print("Hola")

root.mainloop()
