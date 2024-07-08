import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector
from datetime import datetime

fechaHoy = datetime.now()

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Biblioteca Inacap"
)

cursor = conexion.cursor()

ventana = tk.Tk()
ventana.title("Préstamo de libros.")
ventana.geometry("800x600")

nombreApp = tk.Label(ventana, text="Bienvenido al sistema para préstamos de libros")
nombreApp.pack(pady=10)

dueño = "INACAP"
claveDueño = "123456"
usuarioActivo = ""
varControl = 0
    
def iniciarSesion():
    ventana_login = tk.Toplevel(ventana)
    ventana_login.title("Iniciar sesión")

    nomUsuario = tk.Label(ventana_login, text="Usuario:")
    nomUsuario.pack()
    entryUsuario = tk.Entry(ventana_login)
    entryUsuario.pack(padx=20, pady=20)
    contraUsuario = tk.Label(ventana_login, text="Contraseña:")
    contraUsuario.pack()
    entryContraseña = tk.Entry(ventana_login, show="*")
    entryContraseña.pack(padx=20, pady=20)
    labelEstado = tk.Label(ventana_login, text="")
    labelEstado.pack(padx=20, pady=10)

    def validarInicio():
        user = entryUsuario.get()
        password = entryContraseña.get()

        if user == dueño and password == claveDueño:
            messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido!")
            ventana_login.destroy()

            btn_registrar_usuario.config(state="normal")
            btn_config_costos.config(state="normal")
            btn_registrar_cliente.config(state="normal")
            btn_registrar_prestamo.config(state="normal")
            btn_eliminar_prestamo.config(state="normal")

        else:
            labelEstado.configure(text="Credenciales erroneas")    

    boton_ingresar = tk.Button(ventana_login, text="Ingresar", command=validarInicio)
    boton_ingresar.pack(pady=20)

    estado = tk.Label(ventana_login)
    estado.pack(pady=10)

btn_inicio_sesion = ttk.Button(ventana, text="Iniciar sesión", command=iniciarSesion)
btn_inicio_sesion.pack(pady=10)

def registrarUsuario():
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registrar usuario")
    ventana_registro.geometry("400x600")

    rutUsuarioRegistro = ttk.Label(ventana_registro, text="RUT:")
    rutUsuarioRegistro.pack()
    entryRutRegistro = ttk.Entry(ventana_registro, width=200)
    entryRutRegistro.pack(padx=20, pady=20)
    nomUsuarioRegistro = ttk.Label(ventana_registro, text="Nombre:")
    nomUsuarioRegistro.pack()
    entryNomRegistro = ttk.Entry(ventana_registro, width=200)
    entryNomRegistro.pack(padx=20, pady=20)
    apeUsuarioRegistro = ttk.Label(ventana_registro, text="Apellido:")
    apeUsuarioRegistro.pack()
    entryApeRegistro = ttk.Entry(ventana_registro, width=200)
    entryApeRegistro.pack(padx=20, pady=20)
    numUsuarioRegistro = ttk.Label(ventana_registro, text="Número telefonico:")
    numUsuarioRegistro.pack()
    entryNumRegistro = ttk.Entry(ventana_registro, width=200)
    entryNumRegistro.pack(padx=20, pady=20)
    emailUsuarioRegistro = ttk.Label(ventana_registro, text="Correo electronico:")
    emailUsuarioRegistro.pack()
    entryEmailRegistro = ttk.Entry(ventana_registro, width=200)
    entryEmailRegistro.pack(padx=20, pady=20)
    claveUsuarioRegistro = ttk.Label(ventana_registro, text="Contraseña:")
    claveUsuarioRegistro.pack()
    entryClaveRegistro = ttk.Entry(ventana_registro, width=200)
    entryClaveRegistro.pack(padx=20, pady=20)

    def obtenerDatos():
        rut = entryRutRegistro.get()
        nombre = entryNomRegistro.get()
        apellido = entryApeRegistro.get()
        numero = entryNumRegistro.get()
        email = entryEmailRegistro.get()
        clave = entryClaveRegistro.get()

        def comprobarDatos():
            if rut == "" or nombre == "" or apellido == ""  or numero == "" or email == "" or clave == "":
                estado.configure(text="Favor de verificar informacion.")
            else:   
                insertar_usuario = "INSERT INTO usuarios (rut, nombre, apellido, telefono, correo, clave)VALUES (%s, %s, %s, %s, %s, %s)"
                valores_usuario = (rut, nombre, apellido, numero, email, clave)

                try:
                    cursor.execute(insertar_usuario, valores_usuario)
                    estado.configure(text="Usuario registrado con éxito!.")
                    conexion.commit()

                except mysql.connector.IntegrityError as e:
                    if e.errno == 1062:
                        estado.configure(text=f"Error: El RUT: {rut} ya está registrado en la base de datos.")
                    else:
                        estado.configure(text=f"Error: {e}")

        comprobarDatos()        

    btnRegistrar = ttk.Button(ventana_registro, text="Registrar", command=obtenerDatos)
    btnRegistrar.pack(padx=20, pady=20)

    estado = tk.Label(ventana_registro)
    estado.pack()

btn_registrar_usuario = ttk.Button(ventana, text="Registrar Usuario", command=registrarUsuario, state="disabled")
btn_registrar_usuario.pack(pady=10)    

menu = tk.LabelFrame(ventana, text="Menú", borderwidth=2, relief="ridge")
menu.pack(pady=20)

def comprobarUsuarios():
    ventana_usuarios = tk.Toplevel(ventana)
    ventana_usuarios.title("Usuarios registrados")
    ventana_usuarios.geometry("400x200")

    labelUsuarios = tk.Label(ventana_usuarios, text="Usuarios registrados:")
    labelUsuarios.pack(padx=20, pady=10)

    cursor.execute("SELECT nombre, rut FROM usuarios")
    usuarios = cursor.fetchall()

    opciones = [f"{nombre} / Rut: {rut}" for nombre, rut in usuarios]

    selUsuariosRegistrado = ttk.Combobox(ventana_usuarios, values=opciones, state="readonly", width=200)
    selUsuariosRegistrado.pack(padx=20, pady=10)

    def eliminarUsuario():
        usuario = selUsuariosRegistrado.get()
        if usuario:
            rut = usuario.split(" / Rut: ")[1]
            cursor.execute("DELETE FROM usuarios WHERE rut = %s", (rut,))
            conexion.commit()
            estado.configure(text="Usuario eliminado con éxito.")
        
    btn_eliminar = ttk.Button(ventana_usuarios, text="Eliminar usuario", command=eliminarUsuario)
    btn_eliminar.pack(padx=20, pady=10)

    estado = tk.Label(ventana_usuarios, text="")
    estado.pack(padx=20, pady=10)

btn_comprobar_usuarios = ttk.Button(menu, text="Comprobar usuarios", command=comprobarUsuarios)
btn_comprobar_usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

def configurarCostos():
    ventana_costos = tk.Toplevel(ventana)
    ventana_costos.title("Configurar costos roles")
    ventana_costos.geometry("400x300")

    cursor.execute("INSERT IGNORE INTO costos (id, estudiante, docente) values (1, 0, 0)")

    consulta = "SELECT estudiante, docente FROM costos"
    cursor.execute(consulta)
    costo = cursor.fetchone()

    costo_estudiante, costo_docente = costo

    labelCostos = tk.Label(ventana_costos, text="Costos asociados a dia de atraso para los roles del solicitante")
    labelCostos.pack(padx=20, pady=10)
    labelEstudiante = tk.Label(ventana_costos, text="Estudiante: ")
    labelEstudiante.pack(padx=20, pady=10)
    entryCostoEstudiante = ttk.Entry(ventana_costos)
    entryCostoEstudiante.insert(0, costo_estudiante)
    entryCostoEstudiante.pack(padx=20, pady=10)
    labelDocente = tk.Label(ventana_costos, text="Docente: ")
    labelDocente.pack(padx=20, pady=10)
    entryCostoDocente = ttk.Entry(ventana_costos)
    entryCostoDocente.insert(0, costo_docente)
    entryCostoDocente.pack(padx=20, pady=10)

    def fijarCostos():
        costoEstudiante = entryCostoEstudiante.get()
        costoDocente = entryCostoDocente.get()

        cursor.execute(f"UPDATE costos SET estudiante = {costoEstudiante}, docente = {costoDocente} WHERE id = 1")

        estado.configure(text="Valores fijados con éxito.")

    btn_fijar_costos = ttk.Button(ventana_costos, text="Registrar valores", command=fijarCostos)
    btn_fijar_costos.pack(padx=20, pady=10)

    estado = tk.Label(ventana_costos, text="")
    estado.pack(padx=20, pady=10)

btn_config_costos = ttk.Button(menu, text="Configurar costos", command=configurarCostos, state="disabled")
btn_config_costos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

def revisarDeudas():
    ventana_deudas = tk.Toplevel(ventana)
    ventana_deudas.title("Deudas clientes")
    ventana_deudas.geometry("200x400")
    
    labelCliente = tk.Label(ventana_deudas, text="Seleccione al cliente:")
    labelCliente.pack(padx=20, pady=10)

    cursor.execute("SELECT nombre FROM clientes")
    nombres = [nombre[0] for nombre in cursor.fetchall()]

    selCliente = ttk.Combobox(ventana_deudas, values=nombres, state="readonly")
    selCliente.pack(padx=20, pady=10)

    def obtenerFechasDevolucion():
        cliente = selCliente.get()

        if varControl == 1:
            btn_pagar.config(state="normal")
        
        consulta = "SELECT devolucion FROM deudores WHERE nombreCliente = %s"
        cursor.execute(consulta, (cliente,))
        fechas_devolucion = cursor.fetchall()
        
        if fechas_devolucion:
            fechas = [datetime.strptime(str(fecha[0]), '%Y-%m-%d') for fecha in fechas_devolucion]
            fechas_str = "\n".join([fecha.strftime('%Y-%m-%d') for fecha in fechas])
            segundoLabelDeuda.config(text=fechas_str)
            
        else:
            segundoLabelDeuda.config(text="No hay deudas registradas")

        for fecha in fechas:
            if fecha < fechaHoy:
                diferencia_dias = (fecha - fechaHoy).days
                
        consultaDos = "SELECT rol FROM clientes WHERE nombre = %s"
        cursor.execute(consultaDos, (cliente,))
        rol = cursor.fetchone()
        rol = rol[0]
        
        if rol == "Estudiante":
            cursor.execute("SELECT estudiante FROM costos")
            costo = cursor.fetchone()
            costo = costo[0]
            costo = int(costo)
            costoFinal = costo * diferencia_dias

            cuartoLabelDeuda.configure(text=f"$ {costoFinal}")

    btn_ver= ttk.Button(ventana_deudas, text="Revisar", command=obtenerFechasDevolucion)    
    btn_ver.pack(padx=20, pady=10)

    labelDeuda = tk.Label(ventana_deudas, text="Fecha de devolucion:")
    labelDeuda.pack(padx=20, pady=10)
    segundoLabelDeuda = tk.Label(ventana_deudas, text="")
    segundoLabelDeuda.pack(padx=20, pady=10)
    tercerLabelDeuda = tk.Label(ventana_deudas, text="Monto a pagar:")
    tercerLabelDeuda.pack(padx=20, pady=10)
    cuartoLabelDeuda = tk.Label(ventana_deudas, text="0")
    cuartoLabelDeuda.pack(padx=20, pady=10)

    btn_pagar = ttk.Button(ventana_deudas, text="Pagar")
    btn_pagar.pack(padx=20, pady=10)

btn_revisar_deudas = ttk.Button(menu, text="Revisar deudas", command=revisarDeudas)
btn_revisar_deudas.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

def registrarCliente():
    ventana_registro_cliente = tk.Toplevel(ventana)
    ventana_registro_cliente.title("Registro de cliente")
    ventana_registro_cliente.geometry("400x460")

    rutCliente = tk.Label(ventana_registro_cliente, text="RUT")
    rutCliente.pack(padx=10, pady=10)
    entryRutCliente = ttk.Entry(ventana_registro_cliente)
    entryRutCliente.pack(padx=10, pady=10)
    nomCliente = tk.Label(ventana_registro_cliente, text="Nombre")
    nomCliente.pack(padx=10, pady=10)
    entryNomCliente = ttk.Entry(ventana_registro_cliente)
    entryNomCliente.pack(padx=10, pady=10)
    apeCliente = tk.Label(ventana_registro_cliente, text="Apellido")
    apeCliente.pack(padx=10, pady=10)
    entryApeCliente = ttk.Entry(ventana_registro_cliente)
    entryApeCliente.pack(padx=10, pady=10)
    roles = ["Estudiante", "Docente"]
    rolLabel = tk.Label(ventana_registro_cliente, text="Seleccione el rol")
    rolLabel.pack(padx=10, pady=10)
    rol = ttk.Combobox(ventana_registro_cliente, values=roles, state="readonly")
    rol.pack(padx=10, pady=10)

    def obtenerDatos():
        rut = entryRutCliente.get()
        nombre = entryNomCliente.get()
        apellido = entryApeCliente.get()
        rolC = rol.get()

        def comprobarDatos():
            if rut == "" or nombre == "" or apellido == ""  or rolC == "":
                estado.configure(text="Favor de verificar informacion.")
            else:   
                insertar_cliente = "INSERT INTO clientes (rutCliente, nombre, apellido, rol) VALUES (%s, %s, %s, %s)"
                valores_cliente = (rut, nombre, apellido, rolC)

                try:
                    cursor.execute(insertar_cliente, valores_cliente)
                    conexion.commit()
                    estado.configure(text="Cliente registrado con éxito!.")

                except mysql.connector.IntegrityError as e:
                    if e.errno == 1062:
                        estado.configure(text=f"Error: El RUT: {rut} ya está registrado en la base de datos.")
                    else:
                        estado.configure(text=f"Error: {e}")

        comprobarDatos()        

    btn_registrar_cliente = ttk.Button(ventana_registro_cliente, text="Registrar", command=obtenerDatos)
    btn_registrar_cliente.pack(padx=20, pady=20)

    estado = tk.Label(ventana_registro_cliente, text="")
    estado.pack(padx=20, pady=10)

btn_registrar_cliente = ttk.Button(menu, text="Registrar cliente", command=registrarCliente, state="disabled")
btn_registrar_cliente.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

def registrarPrestamo():
    ventana_registrar_prestamo = tk.Toplevel(ventana)
    ventana_registrar_prestamo.title("Registrar préstamo")
    ventana_registrar_prestamo.geometry("400x520")    

    cursor.execute("SELECT nombre FROM clientes")
    nombres_clientes = [nombre[0] for nombre in cursor.fetchall()]

    cursor.execute("SELECT nombreLibro FROM libros")
    nombres_libros = [nombre[0] for nombre in cursor.fetchall()]

    labelCliente = ttk.Label(ventana_registrar_prestamo, text="Seleccione al cliente")
    labelCliente.pack(padx=20, pady=10)
    listaClientes = ttk.Combobox(ventana_registrar_prestamo, values=nombres_clientes, state="readonly")
    listaClientes.pack(padx=10, pady=10)
    labelLibros = ttk.Label(ventana_registrar_prestamo, text="Seleccione el libro")
    labelLibros.pack(padx=20, pady=10)
    listaLibros = ttk.Combobox(ventana_registrar_prestamo, values=nombres_libros, state="readonly")
    listaLibros.pack(padx=20, pady=10)
    labelPrestamo = ttk.Label(ventana_registrar_prestamo, text="Fecha de solicitud")
    labelPrestamo.pack(padx=20, pady=10)
    fechaPrestamo = DateEntry(ventana_registrar_prestamo, width=12, background="darkblue", foreground="white", borderwidth=2, state="readonly")
    fechaPrestamo.pack(padx=20, pady=10)
    labelDevolucion = ttk.Label(ventana_registrar_prestamo, text="Fecha de devolucion")
    labelDevolucion.pack(padx=20, pady=10)
    fechaDevolucion = DateEntry(ventana_registrar_prestamo, width=12, background="darkblue", foreground="white", borderwidth=2, state="readonly")
    fechaDevolucion.pack(padx=20, pady=10)

    def registrarPrestamoLibro():
        cliente = listaClientes.get()
        libro = listaLibros.get()
        fecha_solicitud = fechaPrestamo.get_date()
        fecha_devolucion = fechaDevolucion.get_date()

        if cliente == "" or libro == "":
            estado.configure(text="Verifique la informacion entregada.")

        else:
            consulta = "INSERT INTO prestamos (cliente, libro, fecha_solicitud, fecha_devolucion) values (%s, %s, %s, %s)"
            datos = (cliente, libro, fecha_solicitud, fecha_devolucion)

            cursor.execute(consulta, datos)

            consultaDos = "UPDATE libros SET stock = stock - %s WHERE nombreLibro = %s"
            datosDos = (1, libro)

            cursor.execute(consultaDos, datosDos)

            consultaTres = "INSERT INTO deudores (nombreCliente, solicitud, devolucion, libro) values (%s, %s, %s, %s)"
            datosTres = (cliente, fecha_solicitud, fecha_devolucion, libro)

            cursor.execute(consultaTres, datosTres)

            conexion.commit()

            estado.configure(text="Préstamo registrado.")

    btn_registrar = ttk.Button(ventana_registrar_prestamo, text="Registrar préstamo", command=registrarPrestamoLibro)
    btn_registrar.pack(padx=20, pady=10)

    estado = tk.Label(ventana_registrar_prestamo, text="")
    estado.pack(padx=20, pady=10)

btn_registrar_prestamo = ttk.Button(menu, text="Registrar préstamo", command=registrarPrestamo, state="disabled")
btn_registrar_prestamo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

def eliminarPrestamo():
    ventana_eliminar_prestamo = tk.Toplevel(ventana)
    ventana_eliminar_prestamo.title("Devolver préstamo")
    ventana_eliminar_prestamo.geometry("400x400")

    def obtenerClientes():
        cursor.execute("SELECT DISTINCT cliente FROM prestamos")
        return cursor.fetchall()

    def obtenerLibrosPorCliente(cliente):
        cursor.execute("SELECT libro FROM prestamos WHERE cliente = %s", (cliente,))
        return cursor.fetchall()

    def cargarLibros(event):
        cliente_seleccionado = selClientes.get()
        if cliente_seleccionado:
            libros = obtenerLibrosPorCliente(cliente_seleccionado)
            listbox_libros.delete(0, tk.END)
            for libro in libros:
                listbox_libros.insert(tk.END, libro[0]) 
        else:
            listbox_libros.delete(0, tk.END)

    labelClientes = tk.Label(ventana_eliminar_prestamo, text="Seleccionar cliente:")
    labelClientes.pack(padx=20, pady=10)

    clientes = obtenerClientes()
    opciones_clientes = [cliente[0] for cliente in clientes]

    selClientes = ttk.Combobox(ventana_eliminar_prestamo, values=opciones_clientes, state="readonly")
    selClientes.pack(padx=20, pady=10)
    selClientes.bind("<<ComboboxSelected>>", cargarLibros)

    labelLibros = tk.Label(ventana_eliminar_prestamo, text="Libros en posesión:")
    labelLibros.pack(padx=20, pady=10)

    listbox_libros = tk.Listbox(ventana_eliminar_prestamo, width=80, height=8)
    listbox_libros.pack(padx=20, pady=10)        

    def borrarPrestamo():
        cliente_seleccionado = selClientes.get()
        seleccion = listbox_libros.curselection()
        libro_seleccionado = listbox_libros.get(seleccion[0]) 

        consulta = "DELETE FROM prestamos WHERE cliente = %s AND libro = %s"  
        datos = (cliente_seleccionado, libro_seleccionado) 

        cursor.execute(consulta, datos)

        consultaDos = "UPDATE libros SET stock = stock + %s WHERE nombreLibro = %s"
        datosDos = (1, libro_seleccionado)

        cursor.execute(consultaDos, datosDos)

        consultaTres = "DELETE FROM deudores WHERE nombreCliente = %s and libro = %s"
        datosTres = (cliente_seleccionado, libro_seleccionado)

        cursor.execute(consultaTres, datosTres)

        conexion.commit()

        estado.configure(text="Préstamo eliminado con éxito.")

    btn_eliminar = ttk.Button(ventana_eliminar_prestamo, text="Eliminar préstamo", command=borrarPrestamo)
    btn_eliminar.pack(padx=20, pady=10)

    estado = tk.Label(ventana_eliminar_prestamo, text="")
    estado.pack(padx=20, pady=10)
    
btn_eliminar_prestamo = ttk.Button(menu, text="Devolver préstamo", command=eliminarPrestamo, state="disabled")
btn_eliminar_prestamo.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

def ingresarLibro():
    ventana_libros = tk.Toplevel(ventana)
    ventana_libros.title("Ingresar ejemplar")
    ventana_libros.geometry("400x360")

    labelNombre = tk.Label(ventana_libros, text="Ingrese el titulo del libro")
    labelNombre.pack(padx=20, pady=10)
    entryNombreLibro = ttk.Entry(ventana_libros)
    entryNombreLibro.pack(padx=20, pady=10)
    labelAutor = tk.Label(ventana_libros, text="Ingrese el autor del libro")
    labelAutor.pack(padx=20, pady=10)
    entryAutor = ttk.Entry(ventana_libros)
    entryAutor.pack(padx=20, pady=10)
    labelStock = tk.Label(ventana_libros, text="Digite el stock disponible")
    labelStock.pack(padx=20, pady=10)
    entryStock = ttk.Entry(ventana_libros)
    entryStock.pack(padx=20, pady=10)

    def registrarLibro():
        nombre = entryNombreLibro.get()
        autor = entryAutor.get()
        stock = entryStock.get()

        if nombre == "" or autor == "" or stock == "":
            estado.configure(text="Revise la informacion registrada.")

        else:
            consulta = "INSERT INTO libros (nombreLibro, autor, stock) VALUES (%s, %s, %s)"
            datos = (nombre, autor, stock)

            cursor.execute(consulta, datos)

            conexion.commit()

            estado.configure(text="Libro registrado con éxito.")

    btn_registrar_libro = ttk.Button(ventana_libros, text="Registrar libro", command=registrarLibro)
    btn_registrar_libro.pack(padx=20, pady=10)

    estado = tk.Label(ventana_libros, text="")
    estado.pack(padx=20, pady=10)

btn_ingresar_libro = ttk.Button(menu, text="Ingresar libro", command=ingresarLibro)
btn_ingresar_libro.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

def revisarLibros():
    ventana_revisar_libros = tk.Toplevel(ventana)
    ventana_revisar_libros.title("Ejemplares disponibles")

    cursor.execute("SELECT nombreLibro, autor, stock FROM libros")

    datos = cursor.fetchall()

    tabla = ttk.Treeview(ventana_revisar_libros, columns=("Nombre", "Autor", "Stock"), show="headings")
    tabla.pack(padx=20, pady=10)    

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Autor", text="Autor")
    tabla.heading("Stock", text="Stock")

    for dato in datos:
        tabla.insert("", "end", values=dato)

btn_revisar_libros = ttk.Button(menu, text="Revisar libros", command=revisarLibros)
btn_revisar_libros.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

infoLegal = tk.Frame(ventana, borderwidth=2, relief="ridge")
infoLegal.pack(pady=20)

terminosYcondiciones = tk.Label(infoLegal, text="Terminos y condiciones")
terminosYcondiciones.pack()
contenidoTerminos = tk.Label(infoLegal, text="""Al hacer uso de esta aplicacion da el consentimiento a Inacap para hacer uso de los datos
personales que usted ingrese, asi mismo, acepta estar de acuerdo con la entrega de dicha informacion a las autoridades pertinentes en caso 
de caer en el uso indebido de la informacion que este software contiene.""")
contenidoTerminos.pack()
aceptarTerminos = tk.Label(infoLegal, text="Haga click en la casilla para comprobar que está de acuerdo con los terminos y condiciones.")
aceptarTerminos.pack()
checkTerminos = tk.Checkbutton(infoLegal, text="Tomo conocimiento de los terminos y condiciones del Software.")
checkTerminos.pack()

btnDescargarTerminos = ttk.Button(ventana, text="Descargar Terminos y Condiciones")
btnDescargarTerminos.pack(pady=40)

ventana.mainloop()