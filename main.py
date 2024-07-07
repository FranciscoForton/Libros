import os
import json
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Préstamo de libros.")
ventana.geometry("800x600")

nombreApp = tk.Label(ventana, text="Bienvenido al sistema para préstamos de libros")
nombreApp.pack(pady=10)

dueño = "INACAP"
claveDueño = "123456"
clientes = []
usuarios = []
libros = []
usuarioActivo = ""

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

    nomUsuarioRegistro = ttk.Label(ventana_registro, text="Nombres:")
    nomUsuarioRegistro.pack()
    entryNomRegistro = ttk.Entry(ventana_registro, width=200)
    entryNomRegistro.pack(padx=20, pady=20)
    apeUsuarioRegistro = ttk.Label(ventana_registro, text="Apellidos:")
    apeUsuarioRegistro.pack()
    entryApeRegistro = ttk.Entry(ventana_registro, width=200)
    entryApeRegistro.pack(padx=20, pady=20)
    rutUsuarioRegistro = ttk.Label(ventana_registro, text="RUT:")
    rutUsuarioRegistro.pack()
    entryRutRegistro = ttk.Entry(ventana_registro, width=200)
    entryRutRegistro.pack(padx=20, pady=20)
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
        nombres = entryNomRegistro.get()
        apellidos = entryApeRegistro.get()
        rut = entryRutRegistro.get()
        numero = entryNumRegistro.get()
        email = entryEmailRegistro.get()
        clave = entryClaveRegistro.get()

        def comprobarDatos():
            if nombres == "" or apellidos == "" or rut == "" or numero == "" or email == "" or clave == "":
                estado.configure(text="Favor de verificar informacion.")
            else:
                estado.configure(text="Usuario registrado.")    

                datos = {
                "nombres" : nombres,
                "apellidos" : apellidos,
                "rut" : rut,
                "numero" : numero,
                "email" : email,
                "clave" : clave
                }

                if os.path.exists('informacion.json'):
                    with open('informacion.json', 'r') as archivo_json:
                        usuarios = json.load(archivo_json)
                else:
                    usuarios.append(datos)
                with open('informacion.json', 'w') as archivo_json:
                    json.dump(usuarios, archivo_json, indent=4)

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

    selUsuariosRegistrado = ttk.Combobox(ventana_usuarios, values=usuarios)
    selUsuariosRegistrado.pack(padx=20, pady=10)

    btn_eliminar = ttk.Button(ventana_usuarios, text="Eliminar usuario")
    btn_eliminar.pack(padx=20, pady=10)

btn_comprobar_usuarios = ttk.Button(menu, text="Comprobar usuarios", command=comprobarUsuarios)
btn_comprobar_usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

def configurarCostos():
    ventana_costos = tk.Toplevel(ventana)
    ventana_costos.title("Configurar costos roles")
    ventana_costos.geometry("400x300")

    labelCostos = tk.Label(ventana_costos, text="Costos asociados a dia de atraso para los roles del solicitante")
    labelCostos.pack(padx=20, pady=10)
    labelEstudiante = tk.Label(ventana_costos, text="Estudiante: ")
    labelEstudiante.pack(padx=20, pady=10)
    entryCostoEstudiante = ttk.Entry(ventana_costos)
    entryCostoEstudiante.pack(padx=20, pady=10)
    labelDocente = tk.Label(ventana_costos, text="Docente: ")
    labelDocente.pack(padx=20, pady=10)
    entryCostoDocente = ttk.Entry(ventana_costos)
    entryCostoDocente.pack(padx=20, pady=10)

    btn_fijar_costos = ttk.Button(ventana_costos, text="Registrar valores")
    btn_fijar_costos.pack(padx=20, pady=10)

btn_config_costos = ttk.Button(menu, text="Configurar costos", command=configurarCostos, state="disabled")
btn_config_costos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

def revisarDeudas():
    ventana_deudas = tk.Toplevel(ventana)
    ventana_deudas.title("Deudas clientes")
    ventana_deudas.geometry("200x300")
    
    labelCliente = tk.Label(ventana_deudas, text="Seleccione al cliente:")
    labelCliente.pack(padx=20, pady=10)
    selCliente = ttk.Combobox(ventana_deudas, values="")
    selCliente.pack(padx=20, pady=10)
    labelDeuda = tk.Label(ventana_deudas, text="Deuda registrada:")
    labelDeuda.pack(padx=20, pady=10)
    segundoLabelDeuda = tk.Label(ventana_deudas, text="0")
    segundoLabelDeuda.pack(padx=20, pady=10)
    labelEstado = tk.Label(ventana_deudas, text="Estado de la deuda:")
    labelEstado.pack(padx=20, pady=10)
    segundoLabelEstado = tk.Label(ventana_deudas, text="0")
    segundoLabelEstado.pack(padx=20, pady=10)

btn_revisar_deudas = ttk.Button(menu, text="Revisar deudas", command=revisarDeudas)
btn_revisar_deudas.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

def registrarCliente():
    ventana_registro_cliente = tk.Toplevel(ventana)
    ventana_registro_cliente.title("Registro de cliente")
    ventana_registro_cliente.geometry("400x460")

    nomCliente = tk.Label(ventana_registro_cliente, text="Nombre")
    nomCliente.pack(padx=10, pady=10)
    entryNomCliente = ttk.Entry(ventana_registro_cliente)
    entryNomCliente.pack(padx=10, pady=10)
    apeCliente = tk.Label(ventana_registro_cliente, text="Apellido")
    apeCliente.pack(padx=10, pady=10)
    entryApeCliente = ttk.Entry(ventana_registro_cliente)
    entryApeCliente.pack(padx=10, pady=10)
    rutCliente = tk.Label(ventana_registro_cliente, text="RUT")
    rutCliente.pack(padx=10, pady=10)
    entryRutCliente = ttk.Entry(ventana_registro_cliente)
    entryRutCliente.pack(padx=10, pady=10)
    roles = ["Estudiante", "Docente"]
    rolLabel = tk.Label(ventana_registro_cliente, text="Seleccione el rol")
    rolLabel.pack(padx=10, pady=10)
    rol = ttk.Combobox(ventana_registro_cliente, values=roles)
    rol.pack(padx=10, pady=10)
    btn_registrar_cliente = ttk.Button(ventana_registro_cliente, text="Registrar")
    btn_registrar_cliente.pack(padx=20, pady=20)

btn_registrar_cliente = ttk.Button(menu, text="Registrar cliente", command=registrarCliente, state="disabled")
btn_registrar_cliente.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

def registrarPrestamo():
    ventana_registrar_prestamo = tk.Toplevel(ventana)
    ventana_registrar_prestamo.title("Registrar préstamo")
    ventana_registrar_prestamo.geometry("400x500")    

    labelCliente = ttk.Label(ventana_registrar_prestamo, text="Seleccione al cliente")
    labelCliente.pack(padx=20, pady=10)
    listaClientes = ttk.Combobox(ventana_registrar_prestamo, values=clientes)
    listaClientes.pack(padx=10, pady=10)
    labelLibros = ttk.Label(ventana_registrar_prestamo, text="Seleccione el libro")
    labelLibros.pack(padx=20, pady=10)
    listaLibros = ttk.Combobox(ventana_registrar_prestamo, values=libros)
    listaLibros.pack(padx=20, pady=10)
    labelPrestamo = ttk.Label(ventana_registrar_prestamo, text="Fecha de solicitud")
    labelPrestamo.pack(padx=20, pady=10)
    fechaPrestamo = DateEntry(ventana_registrar_prestamo, width=12, background="darkblue", foreground="white", borderwidth=2)
    fechaPrestamo.pack(padx=20, pady=10)
    labelDevolucion = ttk.Label(ventana_registrar_prestamo, text="Fecha de devolucion")
    labelDevolucion.pack(padx=20, pady=10)
    fechaDevolucion = DateEntry(ventana_registrar_prestamo, width=12, background="darkblue", foreground="white", borderwidth=2)
    fechaDevolucion.pack(padx=20, pady=10)
    labelTarifa = tk.Label(ventana_registrar_prestamo, text="Monto a cancelar por dia de atraso:")
    labelTarifa.pack(padx=20, pady=10)
    labelMonto = tk.Label(ventana_registrar_prestamo, text="0")
    labelMonto.pack(padx=20, pady=10)

    btn_registrar = ttk.Button(ventana_registrar_prestamo, text="Registrar préstamo")
    btn_registrar.pack(padx=20, pady=10)

btn_registrar_prestamo = ttk.Button(menu, text="Registrar préstamo", command=registrarPrestamo, state="disabled")
btn_registrar_prestamo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

def eliminarPrestamo():
    ventana_eliminar_prestamo = tk.Toplevel(ventana)
    ventana_eliminar_prestamo.title("Devolver préstamo")
    ventana_eliminar_prestamo.geometry("400x460")

    labelCliente = tk.Label(ventana_eliminar_prestamo, text="Seleccione al cliente")
    labelCliente.pack(padx=20, pady=10)
    selCliente = ttk.Combobox(ventana_eliminar_prestamo, values=clientes)
    selCliente.pack(padx=20, pady=10)
    labelLibro = tk.Label(ventana_eliminar_prestamo, text="Seleccion libro a devolver")
    labelLibro.pack(padx=20, pady=10)
    selLibro = ttk.Combobox(ventana_eliminar_prestamo, values="")
    selLibro.pack(padx=20, pady=10)
    labelFechaDevolucion = tk.Label(ventana_eliminar_prestamo, text="Fecha registrada para devolucion")
    labelFechaDevolucion.pack(padx=20, pady=10)
    fechaDevolucion = tk.Label(ventana_eliminar_prestamo, text="0")
    fechaDevolucion.pack(padx=20, pady=10)
    labelDeuda = tk.Label(ventana_eliminar_prestamo, text="Monto a cancelar")
    labelDeuda.pack(padx=20, pady=10)
    montoDeuda = tk.Label(ventana_eliminar_prestamo, text="0")
    montoDeuda.pack(padx=20, pady=10)

    btn_eliminar = ttk.Button(ventana_eliminar_prestamo, text="Eliminar préstamo")
    btn_eliminar.pack(padx=20, pady=10)
    
btn_eliminar_prestamo = ttk.Button(menu, text="Devolver préstamo", command=eliminarPrestamo, state="disabled")
btn_eliminar_prestamo.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

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