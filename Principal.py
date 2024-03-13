from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import PhotoImage
from tkcalendar import DateEntry

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

tareas = []
def crear_perfil():
    # Información predeterminada del perfil
    nombre_predeterminado = "Patrick J.M"
    id_predeterminado = "157986354"
    grado_predeterminado = "1 Bachillerato"
    promo_predeterminado = "2022-2023"

    # Función para guardar cambios
    def guardar_cambios():
        nonlocal nombre_predeterminado, id_predeterminado, grado_predeterminado, promo_predeterminado

        # Obtener valores actualizados de los campos de entrada
        nombre_actualizado = nombre_entry.get()
        id_actualizado = id_entry.get()
        grado_actualizado = grado_entry.get()
        promo_actualizado = promo_entry.get()

        # Actualizar valores predeterminados con los nuevos
        nombre_predeterminado = nombre_actualizado if nombre_actualizado else nombre_predeterminado
        id_predeterminado = id_actualizado if id_actualizado else id_predeterminado
        grado_predeterminado = grado_actualizado if grado_actualizado else grado_predeterminado
        promo_predeterminado = promo_actualizado if promo_actualizado else promo_predeterminado

        # Actualizar etiqueta de información del perfil
        perfil_info = f"Estudiante: {nombre_predeterminado}\nID: {id_predeterminado}\nGrado: {grado_predeterminado}\nPromo: {promo_predeterminado}"
        perfil_label.config(text=perfil_info)

    profile_window = Toplevel(root)
    profile_window.title("Perfil")
    profile_window.geometry('300x250')

    # Etiquetas y campos de entrada para actualizar la información del perfil
    nombre_label = Label(profile_window, text="Nombre:")
    nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    nombre_entry = Entry(profile_window)
    nombre_entry.grid(row=0, column=1, padx=10, pady=5)
    nombre_entry.insert(0, nombre_predeterminado)

    id_label = Label(profile_window, text="ID:")
    id_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    id_entry = Entry(profile_window)
    id_entry.grid(row=1, column=1, padx=10, pady=5)
    id_entry.insert(0, id_predeterminado)

    grado_label = Label(profile_window, text="Grado:")
    grado_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    grado_entry = Entry(profile_window)
    grado_entry.grid(row=2, column=1, padx=10, pady=5)
    grado_entry.insert(0, grado_predeterminado)

    promo_label = Label(profile_window, text="Promo:")
    promo_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    promo_entry = Entry(profile_window)
    promo_entry.grid(row=3, column=1, padx=10, pady=5)
    promo_entry.insert(0, promo_predeterminado)

    # Botón para guardar cambios
    btn_guardar = Button(profile_window, text="Guardar Cambios", command=guardar_cambios)
    btn_guardar.grid(row=4, columnspan=2, padx=10, pady=10)

    # Mostrar información predeterminada del perfil
    perfil_info = f"Estudiante: {nombre_predeterminado}\nID: {id_predeterminado}\nGrado: {grado_predeterminado}\nPromo: {promo_predeterminado}"
    perfil_label = Label(profile_window, text=perfil_info)
    perfil_label.grid(row=5, columnspan=2, padx=10, pady=10)

    # Botón para cerrar la ventana del perfil
    btn_regresar = Button(profile_window, text="Regresar", command=profile_window.destroy)
    btn_regresar.grid(row=6, columnspan=2, padx=10, pady=10)

def creacion_edicion():
    def guardar_tarea():
        descripcion = entry_descripcion.get()
        fecha_vencimiento = entry_fecha.get_date()
        prioridad = entry_prioridad.get()

        tarea = {
            'descripcion': descripcion,
            'fecha_vencimiento': fecha_vencimiento,
            'prioridad': prioridad
        }

        tareas.append(tarea)

        tarea_info = f"Descripción: {descripcion}\nFecha de vencimiento: {fecha_vencimiento.strftime('%d/%m/%Y')}\nPrioridad: {prioridad}"
        messagebox.showinfo("Tarea Guardada", tarea_info)

    def ver_tareas():
        tareas_info = ""
        for tarea in tareas:
            tarea_info = f"Descripción: {tarea['descripcion']}\nFecha de vencimiento: {tarea['fecha_vencimiento'].strftime('%d/%m/%Y')}\nPrioridad: {tarea['prioridad']}\n\n"
            tareas_info += tarea_info

        tareas_window = Toplevel(root)
        tareas_window.title("Tareas Enlistadas")
        tareas_window.geometry('400x300')

        label_tareas = Label(tareas_window, text=tareas_info)
        label_tareas.pack(pady=10)

    # Crear ventana de creación y edición de tareas
    tarea_window = Toplevel(root)
    tarea_window.title("Creación y Edición de Tareas")
    tarea_window.geometry('400x300')

    label_descripcion = Label(tarea_window, text="Descripción:")
    label_descripcion.pack(pady=10)
    entry_descripcion = Entry(tarea_window)
    entry_descripcion.pack(pady=5)

    label_fecha = Label(tarea_window, text="Fecha de vencimiento (dd/mm/yyyy):")
    label_fecha.pack(pady=10)
    entry_fecha = DateEntry(tarea_window, date_pattern='dd/mm/yyyy')
    entry_fecha.pack(pady=5)

    label_prioridad = Label(tarea_window, text="Prioridad:")
    label_prioridad.pack(pady=10)
    entry_prioridad = Entry(tarea_window)
    entry_prioridad.pack(pady=5)

    # Crear un Frame para contener los botones y centrarlos en la misma línea
    button_frame = Frame(tarea_window)
    button_frame.pack(pady=10)

    btn_guardar = Button(button_frame, text="Guardar Tarea", command=guardar_tarea)
    btn_guardar.pack(side=LEFT, padx=10)  # Alinear el botón a la izquierda

    btn_ver_tareas = Button(button_frame, text="Ver Tareas", command=ver_tareas)
    btn_ver_tareas.pack(side=LEFT, padx=10)  # Alinear el botón a la izquierda
def foro():
    def publicar_mensaje():
        mensaje = entry.get("1.0", "end-1c")
        messagebox.showinfo("Mensaje publicado", f"Mensaje publicado en el foro:\n\n{mensaje}")
        ventana_foro.destroy()

    ventana_foro = Toplevel(root)
    ventana_foro.title("Foro")
    ventana_foro.geometry("400x300")

    etiqueta = Label(ventana_foro, text="Publicar mensaje en el foro:", font=("Arial", 12))
    etiqueta.pack(pady=10)

    entry = Text(ventana_foro, height=10, width=50)
    entry.pack(pady=10)

    boton = Button(ventana_foro, text="Publicar", command=publicar_mensaje)
    boton.pack(pady=10)


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
