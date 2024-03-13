from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import PhotoImage

#Esto se debe borrar ya que es la ruta del calendar en propia, o instalar cada direccion
import sys #1
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages') #2
from tkcalendar import Calendar #3

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Encabezado
header = Label(root, text='Gestión de eventos escolares de la Unidad Educativa "Lev Vygotsky"', bg='#fff', fg='#333', font=('Arial', 20, 'bold'))
header.pack(pady=20, padx=20)
def crear_perfil():
    perfil_info = "Estudiante: Patrick J.M\nID: 157986354\nGrado: 1 Bachillerato\nPromo:2022-2023"
    profile_window = Toplevel(root)
    profile_window.title("Perfil")
    profile_window.geometry('300x200')

    perfil_label = Label(profile_window, text=perfil_info)
    perfil_label.pack(pady=10)

    btn_regresar = Button(profile_window, text="Regresar", command=profile_window.destroy)
    btn_regresar.pack(pady=10)

def creacion_edicion():
    messagebox.showinfo("Creación y edición de tareas", "Funcionalidad en desarrollo")

def foro():
    messagebox.showinfo("Foro", "Funcionalidad en desarrollo")

def salir():
    messagebox.showinfo("Salir", "Gracias por usar nuestro programa")

def mostrar_calendario_eventos():
    top = Toplevel(root)
    top.title('Calendario y Eventos Anteriores')
    top.geometry('800x500+400+200')

    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2024, month=3, day=13)
    cal.pack(side="left", fill="both", expand=True)

    eventos_frame = Frame(top, bg='white', padx=10, pady=10)
    eventos_label = Label(eventos_frame, text='Eventos Anteriores', font=('Arial', 16, 'bold'), bg='white')
    eventos_label.pack()
    evento1 = Label(eventos_frame, text='Evento 1 - Navidad', bg='white')
    evento1.pack(anchor='w')
    evento2 = Label(eventos_frame, text='Evento 2 - Año nuevo', bg='white')
    evento2.pack(anchor='w')
    evento1 = Label(eventos_frame, text='Evento 3 - Santos reyes', bg='white')
    evento1.pack(anchor='w')
    evento1 = Label(eventos_frame, text='Evento 4 - Dia del amor y la amistad', bg='white')
    evento1.pack(anchor='w')
    evento1 = Label(eventos_frame, text='Evento 5 - Carnaval', bg='white')
    evento1.pack(anchor='w')
    evento1 = Label(eventos_frame, text='Evento 6 - Miercoles de ceniza', bg='white')
    evento1.pack(anchor='w')
    eventos_frame.pack(side="right", fill="both", expand=True)

    # Botón para regresar al menú principal
    def volver_menu_principal():
        top.destroy()  # Cierra la ventana actual

    btn_volver_menu = Button(top, text="Volver al Menú Principal", command=volver_menu_principal)
    btn_volver_menu.pack(pady=10)

def calendario():
    mostrar_calendario_eventos()

def salir():
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
        messagebox.showinfo("Salir", "Gracias por usar nuestro programa")
        root.destroy()  # Cierra la aplicación
def signin():
    username = user.get()
    password = code.get()

    if username == 'Anahy' and password == '1234':
        root.withdraw()  # Oculta la ventana principal de inicio de sesión

        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        frame = Frame(screen, width=350, height=350, bg="white")
        frame.place(x=50, y=90)

        titulo = Label(frame, text='Gestión de eventos escolares de la Unidad Educativa "Lev Vygotsky"',
                       font=('Arial', 25, 'bold'))
        titulo.pack(pady=30)
        titulo.pack(anchor='n')

        btn_tareas = Button(frame, text="Perfil", command=crear_perfil)
        btn_tareas.pack(pady=10)

        btn_colaboracion = Button(frame, text="Calendario", command=calendario)
        btn_colaboracion.pack(pady=10)

        btn_seguimiento = Button(frame, text="Creación y edición de tareas", command=creacion_edicion)
        btn_seguimiento.pack(pady=10)

        btn_import_export = Button(frame, text="Foro", command=foro)
        btn_import_export.pack(pady=10)

        btn_import_export = Button(frame, text="Salir", command=salir)
        btn_import_export.pack(pady=10)

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

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
