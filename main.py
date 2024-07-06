import os
import json
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Préstamo de libros.")
ventana.geometry("800x600")

nombreApp = tk.Label(ventana, text="Bienvenido al sistema para préstamos de libros")
nombreApp.pack(pady=10)

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

    boton_ingresar = tk.Button(ventana_login, text="Ingresar")
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
                    usuarios = []

                usuarios.append(datos)

                with open('informacion.json', 'w') as archivo_json:
                    json.dump(usuarios, archivo_json, indent=4)

        comprobarDatos()        

    btnRegistrar = ttk.Button(ventana_registro, text="Registrar", command=obtenerDatos)
    btnRegistrar.pack(padx=20, pady=20)

    estado = tk.Label(ventana_registro)
    estado.pack()

def registrarCliente():
    ventana_registro_cliente = tk.Toplevel(ventana)
    ventana_registro_cliente.title("Registro de cliente")
    ventana_registro_cliente.geometry("400x600")

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
    rol = ttk.Combobox(ventana_registro_cliente, values= roles)
    rol.pack(padx=10, pady=10)
    btn_registrar_cliente = ttk.Button(ventana_registro_cliente, text="Registrar")
    btn_registrar_cliente.pack(padx=20, pady=20)
    

btn_registrar_usuario = ttk.Button(ventana, text="Registrar Usuario", command=registrarUsuario)
btn_registrar_usuario.pack(pady=10)    

menu = tk.LabelFrame(ventana, text="Menú", borderwidth=2, relief="ridge")
menu.pack(pady=20)

btn_comprobar_usuarios = ttk.Button(menu, text="Comprobar usuarios")
btn_comprobar_usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

btn_config_costos = ttk.Button(menu, text="Configurar costos")
btn_config_costos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

btn_revisar_deudas = ttk.Button(menu, text="Revisar deudas")
btn_revisar_deudas.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

btn_registrar_cliente = ttk.Button(menu, text="Registrar cliente", command=registrarCliente)
btn_registrar_cliente.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

btn_registrar_prestamo = ttk.Button(menu, text="Registrar préstamo")
btn_registrar_prestamo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

btn_eliminar_prestamo = ttk.Button(menu, text="Eliminar préstamo")
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