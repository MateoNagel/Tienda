import os
import pickle
import os.path

### Creación de registros ###
class Producto:
    def __init__(self):
        self.codigo = ""
        self.nombre = ""
        self.marca = ""
        self.talle = 0
        self.precio = 0.0
        self.stock = 0
        self.activo = "A" #"A" = Activo - "B" = "Baja"

class Cliente:
    def __init__(self):
        self.usuario = ""
        self.direccion = [" "," "," "," "]
        self.telefono = ""
        self.mail = ""
        self.activo = "A" #"A" = Activo - "B" = "Baja"
        self.deudas = "N" #"N" = No - "S" = Sí

### Valida que el "nro" ingresado este dentro del rango asignado en las variables "desde" y "hasta" ###
def ValidarReal(nro, desde, hasta):
    if nro >= "1" and nro <= "9":
        try:
            float(nro)
            if float(nro) >= desde and float(nro) <= hasta:
                return False
            else:
                print("El precio ingresado es menor o supera al mencionado anteriormente, por favor ingresa un nuevo precio.")
                print()
                return True
        except:
            return True
    else:
        print("No se ha ingresado un número, por favor intenteló de nuevo.")
        print()
        return True        


### Valida que el "nro" ingresado este dentro del rango asignado en las variables "desde" y "hasta" ###
def ValidarEntero(nro, desde, hasta):
    if nro >= "1" and nro <= "9":   
        try:                    
            int(nro)
            if int(nro) >= desde and int(nro) <= hasta:
                return False
            else:
                print("El talle ingresado no está dentro del rango permitido.")
                print()
                os.system("pause")
                return True  
        except:
            return True 
    else:
        print("No se ha ingresado un número, por favor intenteló de nuevo.")
        print()
        os.system("pause")
        return True
    
### Verifica que los primeros 4 dígitos sean letras y los otros 4 dígitos sean números ###    
def VerificarCodigo(num):
    i = 0
    if len(num) == 8:
        while i != 4:
            if num[i].lower() >= "a" and num[i].lower() <= "z":
                next
            else:
                print("El código ingresado no cumple con los requerimientos solicitados, por favor intenteló nuevamente.")
                print()
                os.system("pause")
                os.system("cls")
                return True
            i = i+1
        while i != 8:
            if num[i] >= "0" and num[i] <= "9":
                next
            else:
                print("El código ingresado no cumple con los requerimientos solicitados, por favor intenteló nuevamente.")
                print()
                os.system("pause")
                os.system("cls")
                return True
            i = i+1
    else:
        print("El código debe contener 8 dígitos.")
        print()
        os.system("pause")
        os.system("cls")    
        return True
    return False    


### Valida que el nombre y marca ingresado no esté vacío y que tampoco tenga números o caracteres especiales ###
def ValidarTexto(name):
    i = 0
    if name != "":
        while i != len(name):
            if name[i].lower() >= "a" and name[i].lower() <= "z" or name[i] == " ":
                next               
            else:
                print("El nombre no puede contener números o caracteres especiales.")
                print()
                os.system("pause")
                os.system("cls")
                return True
            i = i+1
    else:
        print("El producto debe de contener un nombre, por favor ingreseló.")
        print()                    
        os.system("pause")
        os.system("cls")
        return True                      
    return False


### Valida que la opción ingresada es igual a las propuestas ###
def ValidarOpcion(opcion):
    if opcion == "r" or opcion == "c" or opcion == "n" or opcion == "m" or opcion == "t" or opcion == "p" or opcion == "s":
        return False
    else:
        print("La opción ingresada no existe, por favor intente de nuevo.")
        print()
        os.system("pause")
        return True


### Creación de Archivos ###
afProductos = "C:\\Users\\matth\\Desktop\\TdZ\\productos.dat"
if not os.path.exists(afProductos):
    alProductos = open(afProductos, "w+b")
else:
    alProductos = open(afProductos, "r+b")

afClientes = "C:\\Users\\matth\\Desktop\\TdZ\\clientes.dat"
if not os.path.exists(afClientes):
    alClientes = open(afClientes, "w+b")
else:
    alClientes = open(afClientes, "r+b")

### MENÚ PRINCIPAL ###
def Menu_Principal():
    os.system("cls")
    while True:
        os.system("cls")
        print("MENU PRINCIPAL")
        print()
        print("1 - PRODUCTOS")
        print("2 - CLIENTES")
        print("3 - VENTAS")
        print("4 - REPORTES")
        print("5 - SALIR")
        print()
        Op = input("Ingrese la opción: ")
        print()
        if Op == "1":
            Menu_Productos()
            pass
        elif Op == "2":
            Menu_Clientes()
            pass    
        elif Op == "3":
            Menu_Ventas()
            pass
        elif Op == "4":
            Menu_Reportes()
            pass
        elif Op == "5":
            alProductos.close()
            alClientes.close()
            exit()          
        else:
            print("La opción no existe, por favor ingresa una opción válida")
            print()
            os.system("pause")  


### MENÚ PRODUCTOS ###
def Menu_Productos():
    os.system("cls")
    while True:
        os.system("cls")    
        print("MENU DE PRODUCTOS")
        print()
        print("1 - CARGAR PRODUCTO")
        print("2 - ELIMINAR PRODUCTO")
        print("3 - MODIFICAR PRODUCTO")
        print("4 - LISTA DE PRODUCTOS")
        print("5 - REGRESAR")
        print()
        Op = input("Ingrese la opción: ")
        print()
        if Op == "1":
            CargaProducto()
            pass
        elif Op == "2":
            EliminarProducto()
            pass
        elif Op == "3":
            ModificarProducto()
            pass
        elif Op == "4":
            ListaProducto()
            pass
        elif Op == "5":
            Menu_Principal()
            pass
        else:
            print("La opción no existe, por favor ingresa una opción válida.")
            print()
            os.system("pause")


### MENU CLIENTES ###
def Menu_Clientes():
    os.system("cls")
    while True:
        os.system("cls")
        print("MENU DE CLIENTES")
        print()
        print("1 - REGISTRAR CLIENTE")
        print("2 - ELIMINAR CLIENTE")
        print("3 - MODIFICAR CLIENTE")
        print("4 - LISTA DE CLIENTES")
        print("5 - REGRESAR")
        print()
        Op = input("Ingrese la opción: ")
        if Op.lower() == "1":
            RegistrarCliente()
            pass
        elif Op.lower() == "2":
            #EliminarCLiente()
            pass
        elif Op.lower() == "3":
            #ModificarCliente
            pass
        elif Op.lower() == "4":
            #ListaCliente()
            pass
        elif Op.lower() == "5":
            Menu_Principal()
            pass
        else:
            print("La opción no existe, por favor ingresa una opción válida.")
            print()
            os.system("pause")

### Comprueba la existencia de un cliente en el archivo clientes.dat ###
def BuscarCliente(dato):
    alClientes, afClientes  
    t = os.path.getsize(afClientes)
    alClientes.seek(0)
    encontrado = False
    while alClientes.tell() < t and not encontrado:
        pos = alClientes.tell()
        rClie = pickle.load(alClientes)
        if rClie.usuario.lower() == dato.lower():
            encontrado = True
    if encontrado:
        return True
    else:
        return -1        

###  ###
def RegistrarCliente():
    global alClientes, afClientes
    rClie = Cliente()
    os.system("cls")
    while True:
        os.system("cls")
        res = input("¿Desea registrar un cliente? [S - N]: ")
        print()
        if res.lower() == "n":
            os.system("cls")
            print("Regresando al menú anterior...")
            print()
            os.system("pause")
            Menu_Clientes()
        elif res.lower() == "s":
            os.system("cls")
            while True:
                os.system("cls")
                nombre = input("Ingrese el nombre del cliente: ")
                print()
                pos = BuscarCliente(nombre)
                if pos != -1:
                    os.system("cls")
                    alClientes.seek(pos)
                    rClie = pickle.load(alClientes)
                    if rClie.activo == "B":
                        while True:
                            os.system("cls")
                            print("El cliente está dado de baja.")
                            print()
                            res = input("¿Quiere darlo de alta nuevamente? [S - N]: ")
                            print()
                            if res.lower() == "n":
                                print("El cliente seguirá de baja.")
                                print()
                                os.system("pause")
                            elif res.lower() == "s":
                                rClie.activo = "A"
                                alClientes.seek(pos)
                                pickle.dump(rClie, alClientes)
                                alClientes.flush()
                                print("El cliente fue dado de alta nuevamente.")
                                print()
                                os.system("pause")
                                RegistrarCliente()
                            else:
                                print("La opción ingresada no existe, por favor ingresela nuevamente.")
                                print()
                                os.system("pause")
                    else:
                        print("El usuario ya está registrado en el sistema.")
                        print()
                        os.system("pause")
                elif nombre == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    RegistrarCliente()    
                elif pos == -1 and ValidarTexto(nombre) == False:
                    break
            os.system("cls")
            while True:
                os.system("cls")
                print("Ingrese la dirección de su vivienda o departamento.")
                print()
                direccion = input("Ingrese el nombre de la calle: ")
                if ValidarTexto(direccion) == False:
                    break
            while True:
                os.system("cls")
                print("Ingrese la dirección de su vivienda o departamento.")
                print()
                num = input("Ingrese el número: ")
                flag = False
                for i in range(len(num)):
                    if num[i] >= "1" and num[i] <= "9":
                        flag = True
                    else:
                        print("Debe ingresar un número para continuar.")
                        print()
                        os.system("pause")
                if flag:
                    break
            os.system("cls")       
            while True:
                os.system("cls")
                print("Ingrese la dirección de su vivienda o departamento.")
                print()
                print("Opcional - Si no tiene departamento solo presione [ENTER]")
                numdpto = input("Ingrese el número del departamento: ")
                print()
                if numdpto == "":
                    break
                elif numdpto >= "1" and numdpto <= "9":
                    while True:
                        os.system("cls")
                        print("Ingrese la dirección de su vivienda o departamento.")
                        print()
                        dpto = input("Ingrese el departamento: ")
                        print()
                        if len(dpto) == 1:
                            if ValidarTexto(dpto) == False:
                                break
                            else:
                                os.system("cls")
                                print("Solo debe ingresar el caracter que corresponda a su departamento.")
                                print()
                                os.system("pause")
                        else:
                            os.system("cls")
                            print("El departamento solo debe poseer un caracter")
                            print()
                            os.system("pause")
                    break
                else:
                    os.system("cls")
                    print("Debe ingresar el número de departamento.")
                    print()
                    os.system("pause")    
            os.system("cls")
            while True:
                os.system("cls")
                print("Solo ingrese la caracterísitca y su número sin espacios entre medio.")
                tel = input("Ingrese su teléfono: ")
                print()
                if len(tel) > 8 and len(tel) < 12:
                    if tel >= "0" and tel <= "9":
                        break
                    else:
                        os.system("cls")
                        print("El teléfono no debe poseer letras y/o caracteres especiales.")
                        print("")
                        os.system("pause")
                else:
                    os.system("cls")
                    print("Ingrese un número de teléfono válido.")
                    print("")     
                    os.system("pause")   
            os.system("cls")
            while True:
                os.system("cls")
                correo = input("Ingrese su correo electrónico: ")
                print()
                if correo == " ":
                    break
                else:
                    flag = False
                    for i in range(len(correo)):
                        if correo[i] == "@":
                            flag = True
                    if flag:
                        break
                    else:
                        os.system("cls")
                        print("El correo ingresado no es válido, un ejemplo de correo puede ser: alvaro29@gmail.com")
                        print()
                        os.system("pause")
            os.system("cls")
            while True:
                os.system("cls")
                res = input("¿Confirmar registro de cliente? [S - N]: ")
                if res.lower() == "n":
                    os.system("cls")
                    print("Registro cancelado.")
                    print()
                    os.system("pause")
                elif res.lower() == "s":
                    rClie.usuario = nombre.upper()
                    rClie.direccion[0] = direccion.upper()
                    rClie.direccion[1] = num
                    rClie.direccion[2] = numdpto
                    rClie.direccion[3] = dpto.upper()
                    rClie.telefono = tel
                    rClie.mail = correo
                    pickle.dump(rClie, alClientes)
                    alClientes.flush()
                    print("El cliente se registró con éxito.")
                    print()
                    os.system("pause")
                    RegistrarCliente()        
                else:
                    print("La opción ingresada no existe, por favor ingresela nuevamente.")
                    print()
                    os.system("pause")
        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")                    





### Ordena el archivo productos.dat del menor talle al mayor ###
def Ordenamiento():
    global alProductos
    alProductos.seek(0)
    productos = []
    while True:
        try:
            productos.append(pickle.load(alProductos))
        except EOFError:
            break
    productos.sort(key=lambda x: x.talle)
    alProductos.seek(0)
    alProductos.truncate()  # Limpiar el archivo
    for prod in productos:
        pickle.dump(prod, alProductos)
    alProductos.flush()


### Comprueba la existencia de un producto en el archivo productos.dat ###
def Buscar(dato):
    global alProductos, afProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0)
    rProd = Producto()
    encontrado = False
    while alProductos.tell() < t and not encontrado:
        pos = alProductos.tell()
        rProd = pickle.load(alProductos)
        if rProd.codigo.lower() == dato.lower() or rProd.nombre.lower() == dato.lower() or rProd.marca.lower() == dato.lower():
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1        


def PrintsProductos():
    print()
    print("Código", end="         ")
    print("Nombre", end="                   ")
    print("Marca", end="          ")
    print("Talle", end="          ")
    print("Precio", end="         ")
    print("Stock", end="          ")
    print("Actividad")
    print()


### En esta función se podrán cargar productos ### 
def CargaProducto():
    global alProductos, afProductos
    rProd = Producto()                
    os.system("cls")
    while True:
        os.system("cls")
        res = input("¿Desea ingresar un nuevo producto? [S - N]: ")
        print()
        if res.lower() == "n":
            os.system("cls")
            print("Regresando al menú anterior...")
            print()
            os.system("pause")
            Menu_Productos()
        elif res.lower() == "s":
            os.system("cls")
            while True:
                os.system("cls")
                print("El código debe ser de tipo [AAAA0000].")
                cod = input("Ingrese el código del producto: ")
                pos = Buscar(cod)
                print()
                if pos != -1:
                    alProductos.seek(pos)
                    rProd = pickle.load(alProductos)
                    if rProd.activo == "B":
                        while True:
                            os.system("cls")
                            print("El producto está dado de baja.")
                            print()
                            res = input("¿Quiere darlo de alta nuevamente? [S - N]: ")
                            print()
                            if res.lower() == "n":
                                print("El producto seguirá de baja.")
                                print()
                                os.system("pause")
                            elif res.lower() == "s":
                                rProd.activo = "A"
                                alProductos.seek(pos)
                                pickle.dump(rProd, alProductos)
                                alProductos.flush()
                                print("El producto fue dado de alta nuevamente.")
                                print()
                                os.system("pause")
                                CargaProducto()
                            else:
                                print("La opción ingresada no existe, por favor ingresela nuevamente.")
                                print()
                                os.system("pause")
                    else:
                        print("El código ya le pertenece a otro producto.")
                        print()
                        os.system("pause")
                elif cod == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                elif pos == -1 and VerificarCodigo(cod) == False:
                    break
            while True:        
                os.system("cls")
                nombre = input("Ingrese el nombre del producto: ")
                if nombre == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                elif ValidarTexto(nombre) == False:
                    break
            while True:
                os.system("cls")
                marca = input("Ingrese la marca del producto: ")
                if marca == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                elif ValidarTexto(marca) == False:
                    break
            while True:
                os.system("cls")
                print("Los talles con los que trabajamos van de 35 a 45.")
                talle = input("Ingrese el talle del producto: ")
                if talle == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                elif ValidarEntero(talle, 25, 45) == False:
                    break
            while True:
                os.system("cls")
                print("Los precios actuales van desde 50.000 a 800.000")
                precio = input("Ingrese el precio del producto: ")
                if precio == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                elif ValidarReal(precio, 50000, 800000) == False:
                    break
            while True:
                os.system("cls")
                stock = input("Ingrese la cantidad de stock que posee: ")
                if stock == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    CargaProducto()
                if ValidarEntero(stock, 1, 999999) == False:
                    break
            while True:
                os.system("cls")
                res = input("¿Desea registrar el producto? [S - N]: ")
                print()
                if res.lower() == "n":
                    os.system("cls")
                    print("El registro del producto fue cancelado.")
                    print()
                    os.system("pause")
                elif res.lower() == "s":
                    rProd = Producto()
                    rProd.codigo = cod.upper()
                    rProd.nombre = nombre.upper()
                    rProd.marca = marca.upper()
                    rProd.talle = talle
                    rProd.precio = precio
                    rProd.stock = stock
                    rProd.activo = "A"
                    pickle.dump(rProd, alProductos)
                    alProductos.flush()
                    print("El producto se registró con éxito.")
                    print()
                    os.system("pause")
                    CargaProducto()
                else:
                    print("La opción ingresada no existe, por favor ingresela nuevamente.")
                    print()
                    os.system("pause")    
        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")


### Se realiza la baja lógica del producto colocandolé una "B" en el campo de .activo ###
def EliminarProducto():
    global alProductos, afProductos
    os.system("cls")
    t = os.path.getsize(afProductos)
    if t == 0:
        print("No se han encontrado productos en el sistema")
        print()
        os.system("pause")
        Menu_Productos()
    else:    
        res = input("¿Desea eliminar un producto? [S - N]: ").lower()
        print()
        if res == "n":
            print("Regresando al menú anterior...")
            os.system("pause")
            Menu_Productos()
        elif res == "s":
            while True:
                os.system("cls")
                print("Lista de Productos Activos")
                PrintsProductos()
                print("---------------------------------------------------------------------------------------------------------------")
                alProductos.seek(0)
                while alProductos.tell() < t:
                    rProd = pickle.load(alProductos)
                    if rProd.activo == "A":
                        mostrarProducto(rProd)
                print("---------------------------------------------------------------------------------------------------------------")
                print()
                print("El código debe ser de tipo [AAAA0000].")
                cod = input("Ingrese el codigo del producto que desea eliminar: ").upper()
                print()
                pos = Buscar(cod)
                if cod == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    EliminarProducto()
                elif pos == -1:
                    print("El código ingresado no se encuentra cargado en el sistema.")
                    print()
                    os.system("pause")
                elif VerificarCodigo(cod) == False and pos != -1:
                    break
            alProductos.seek(pos)
            rProd = pickle.load(alProductos)
            if rProd.activo == "B":
                os.system("cls")
                print("El producto actualmente se encuentra dado de baja.")
                print()
                os.system("pause")
                EliminarProducto()
            else:
                while True:
                    os.system("cls")
                    res = input("¿Está seguro que quiere dar de baja el producto? [S - N]: ")
                    print()
                    if res.lower() == "n":
                        print("Baja cancelada.")
                        print()
                        os.system("pause")
                        EliminarProducto()
                    elif res.lower() == "s":
                        rProd.activo = "B"
                        alProductos.seek(pos)
                        pickle.dump(rProd, alProductos)
                        alProductos.flush()
                        print("La baja fue dada con éxito.")
                        print()
                        os.system("pause")
                        EliminarProducto()
                    else:
                        print("La opción ingresada no existe, por favor ingresela nuevamente.")
                        print()
                        os.system("pause")
                        EliminarProducto()
        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")
            EliminarProducto()
        os.system("pause")
        EliminarProducto()


def Mostrar(posicion):
    alProductos.seek(posicion)
    rProd = pickle.load(alProductos)
    print("PRODUCTO A MODIFICAR")
    print()
    print("------------------------------")
    print("Código:",rProd.codigo[0:4],"-",rProd.codigo[4:8])
    print("Nombre:",rProd.nombre, end=' ')
    print("|", end=' ')
    print("Marca:",rProd.marca)
    print("Talle:",rProd.talle, end=' ')
    print("|", end=' ')
    print("Precio:",rProd.precio)
    print("Stock:",rProd.stock, end=' ')
    print("|", end=' ')
    print("Actividad:",rProd.activo)
    print("------------------------------")
    print()    

def mostrarProducto(vrProd):
    salida = ""
    salida = salida + '{:<15}'.format(vrProd.codigo.strip())
    salida = salida + '{:<25}'.format(vrProd.nombre.strip())
    salida = salida + '{:<15}'.format(vrProd.marca.strip())
    salida = salida + '{:<15}'.format(vrProd.talle.strip())
    salida = salida + '{:<15}'.format(vrProd.precio.strip())
    salida = salida + '{:<15}'.format(vrProd.stock.strip())
    salida = salida + '{:<15}'.format(vrProd.activo.strip())
    print(salida)


### Se modifican los campos del registro Producto() a elección del usuario ###
def ModificarProducto():
    global afProductos, alProductos
    os.system("cls")
    t = os.path.getsize(afProductos)
    if t == 0:
        print("No se han encontrado productos en el sistema")
        print()
        os.system("pause")
        Menu_Productos()
    else:
        while True:
            res = input("¿Desea modificar un producto? [S - N]: ")
            print()
            if res.lower() == "n":
                print("Regresando al menú anterior.")
                print()
                os.system("pause")
                pass
                Menu_Productos()
            elif res.lower() == "s":
                os.system("cls")
                print("Lista de Productos")
                PrintsProductos()
                print("---------------------------------------------------------------------------------------------------------------")
                alProductos.seek(0)
                while alProductos.tell() < t:
                    prod = pickle.load(alProductos)
                    mostrarProducto(prod)
                print("---------------------------------------------------------------------------------------------------------------")    
                print()
                print("El código debe ser de tipo [AAAA0000].")
                cod = input("Ingrese el código del producto que desea modificar: ").upper()
                print()
                while VerificarCodigo(cod):
                    os.system("cls")
                    print("El código debe ser de tipo [AAAA0000].")
                    cod = input("Ingrese el código del producto que desea modificar: ").upper()
                pos = Buscar(cod)
                if pos == -1:
                    print("El código ingresado no se encuentra registrado en un producto.")
                    print()
                    os.system("pause")
                    ModificarProducto()
                else:
                    alProductos.seek(pos)
                    rProd = pickle.load(alProductos)
                    while True:
                        os.system("cls")
                        Mostrar(pos)
                        print("¿Qué desea modificar del producto?")
                        print()
                        print("1 - Código")
                        print("2 - Nombre")
                        print("3 - Marca")
                        print("4 - Talle")
                        print("5 - Precio")
                        print("6 - Stock")
                        print("7 - Finalizar")
                        print()
                        Op = input("Ingrese la opción: ")    
                        if Op == "1":    
                            while True:
                                os.system("cls")
                                cod = input("Ingrese el nuevo código para el producto: ").upper()
                                if cod == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                    ModificarProducto()
                                elif rProd.codigo == cod:
                                    print("El código ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif Buscar(cod) != -1:
                                    print("El código ingresado se encuentra registrado en otro producto.")
                                    os.system("pause")
                                elif VerificarCodigo(cod) == False and rProd.codigo != cod:
                                    break
                            rProd.codigo = cod.upper()    
                        elif Op == "2":        
                            while True:
                                os.system("cls")
                                nombre = input("Ingrese el nuevo nombre para el producto: ").upper()
                                if nombre == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                elif rProd.nombre == nombre:
                                    print("El nombre ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif Buscar(nombre) != -1:
                                    print("El nombre ingresado se encuentra registrado en otro producto.")
                                    print()
                                    os.system("pause")    
                                elif ValidarTexto(nombre) == False and rProd.nombre != nombre:
                                    break
                            rProd.nombre = nombre.upper()    
                        elif Op == "3":    
                            while True:
                                os.system("cls")
                                marca = input("Ingrese la nueva marca del producto: ").upper()
                                if marca == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                elif rProd.marca == marca:
                                    print("La marca ingresada es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarTexto(marca) == False:
                                    break
                            rProd.marca = marca.upper()        
                        elif Op == "4":    
                            while True:
                                os.system("cls")
                                print("Los talles con los que trabajamos van de 35 a 45.")
                                talle = input("Ingrese el nuevo talle para el producto: ")
                                if talle == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                elif rProd.talle == talle:
                                    print("El talle ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarEntero(talle, 35, 45) == True:
                                    print("El rango del talle va de 25 a 45. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarEntero(talle, 35, 45) == False and rProd.talle != talle:
                                    break
                            rProd.talle = talle    
                        elif Op == "5":    
                            while True:
                                os.system("cls")
                                print("Los precios actuales van desde 50.000 a 800.000")
                                precio = input("Ingrese el nuevo precio para el producto: ")
                                if precio == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                elif rProd.precio == precio:
                                    print("El precio ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarReal(precio, 50000, 800000) == False and rProd.precio != precio:
                                    break
                            rProd.precio = precio    
                        elif Op == "6":    
                            while True:
                                os.system("cls")
                                stock = input("Ingrese el nuevo stock para el producto: ")
                                if stock == "0":
                                    print("Reiniciando menú...")
                                    print()
                                    os.system("pause")
                                elif rProd.stock == stock:
                                    print("El stock ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")                         
                                elif ValidarEntero(stock, 1, 999999) == False and rProd.stock != stock:
                                    break
                                rProd.stock = stock
                            os.system("cls")
                        elif Op == "7":    
                            while True:
                                res = input("¿Quiere confirmar la modificación del producto? [S - N]: ")
                                print()
                                if res.lower() == "s":
                                    os.system("cls")
                                    alProductos.seek(pos)
                                    pickle.dump(rProd, alProductos)
                                    alProductos.flush()
                                    print("El producto se modificó con éxito.")
                                    print()
                                    os.system("pause")
                                    ModificarProducto()
                                elif res.lower() == "n":
                                    print("Modificación cancelada.")
                                    print()
                                    os.system("pause")
                                    ModificarProducto()
                                else:
                                    print("La respuesta ingresada no es válida. Por favor, intenteló de nuevo.")
                                    print()
                                    os.system("pause")
            else:
                print("La opción ingresada no es válida. Intenteló de nuevo.")
                print()
                os.system("pause")

def ListaProducto():
    global alProductos, afProductos
    os.system("cls")
    t = os.path.getsize(afProductos)
    if t == 0:
        print("No hay productos cargados")
        print()
        os.system("pause")
        Menu_Productos()
    else:
        Ordenamiento()
        alProductos.seek(0)
        while True:
            os.system("cls")
            print("Ingrese la opción por la que desea buscar.")
            print()
            print("1 - Mostrar Todo")
            print("2 - Buscar Por Marca")
            print("3 - Salir")
            print()
            res = input("Ingrese la opción: ")
            if res == "1":
                os.system("cls")
                print("Listado Completo de Productos")
                PrintsProductos()
                print("---------------------------------------------------------------------------------------------------------------")
                while True:
                    try:
                        rProd = pickle.load(alProductos)
                        mostrarProducto(rProd)
                    except EOFError:
                        break
                print("---------------------------------------------------------------------------------------------------------------")    
                os.system("pause")    
                ListaProducto()                    
            elif res == "2":
                os.system("cls")
                while True:
                    os.system("cls")
                    marca = input("Ingrese la marca que desea buscar: ")
                    print()
                    if Buscar(marca) == -1:    
                        print("La marca ingresada no se encuentra registrada en el sistema.")
                        print()
                        os.system("pause")
                    elif ValidarTexto(marca) == False and Buscar(marca) != -1:
                        break
                print("Listado de",marca.upper())
                PrintsProductos()
                print("---------------------------------------------------------------------------------------------------------------")
                alProductos.seek(0)
                while alProductos.tell() < t:
                    prod = pickle.load(alProductos)
                    if prod.marca.lower() == marca.lower():
                        mostrarProducto(prod)
                print("---------------------------------------------------------------------------------------------------------------")                        
                print()
                os.system("pause")                                                   
                ListaProducto()
            elif res == "3":
                print("Regresando al menú anterior...")
                print()
                os.system("pause")
                Menu_Productos()
            else:
                print("La opción ingresada no es válida. Intenteló de nuevo.")
                print()
                os.system("pause")   


Menu_Principal()        