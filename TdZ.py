import os
import pickle
import os.path

class Producto:
    def __init__(self):
        self.codigo = ""
        self.nombre = ""
        self.marca = ""
        self.talle = 0
        self.precio = 0.0
        self.stock = 0

class Cliente:
    def __init__(self):
        self.nombre = ""
        self.direccion = ""
        self.telefono = ""
        self.historial = "" 

def ValidarReal(nro, desde, hasta):
    try:
        float(nro)
        if float(nro) >= desde and float(nro) <= hasta:
            return False
        else:
            return True
    except:
        return True    

def ValidarEntero(nro, desde, hasta):
    try:              
        int(nro)      
        if int(nro) >= desde and int(nro) <= hasta:
            return False
        else:
            return True  
    except:
        return True
    
def VerificarCodigo(num):
    i = 0
    while i != 4:
        if num[i].lower() >= "a" and num[i].lower() <= "z":
            next
        else:
            return True
        i = i+1
    while i != 8:
        if num[i] >= "0" and num[i] <= "9":
            next
        else:
            return True
        i = i+1

def VerificarTexto(name, cant):
    i = 0
    while i != cant:
        if name[i].lower() >= "a" and name[i].lower() <= "z":
            next
        elif name[i].lower() >= 0 and str(name[i]).lower() <= 9:
            return True
        i = i+1

def TamañoTexto(name):    
    while str(name) == "":
        print("No se ha ingresado ningún nombre, por favor ingreselo nuevamente.")
        print()
        os.system("pause")
        name = str(input("Ingrese el nombre del producto: ").upper())                       

def Tamaño(num):
    while len(num) < 0 or len(num) > 8:
        print("El código debe contener 8 dígitos")
        print()
        os.system("pause")
        num = input("Ingrese el código del producto: ").lower()                        


### Programa Principal###
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

#MENU PRINCIPAL#
def Menu_Principal():
    os.system("cls")
    print("MENU PRINCIPAL")
    print()
    print("1 - PRODUCTOS")
    print("2 - CLIENTES")
    print("3 - VENTAS")
    print("4 - REPORTES")
    print("5 - SALIR")
    print()
    Op = str(input("Ingrese la opción: "))
    print()
    if Op == "1":
        Menu_Productos()
    elif Op == "2":
        Menu_Clientes()    
    elif Op == "3":
        Menu_Ventas()
    elif Op == "4":
        Menu_Reportes()
    elif Op == "5":
        Salir()
    else:
        print("La opción no existe, por favor ingresa una opción válida")
        print()
        os.system("pause")
        Menu_Principal()   

def Menu_Productos():
    os.system("cls")
    print()
    print("MENU DE PRODUCTOS")
    print()
    print("1 - CARGAR PRODUCTO")
    print("2 - ELIMINAR PRODUCTO")
    print("3 - MODIFICAR PRODUCTO")
    print("4 - LISTA DE PRODUCTOS")
    print("5 - VOLVER")
    print()
    Op = str(input("Ingrese la opción: "))
    print()
    if Op == "1":
        Carga()
    elif Op == "2":
        Eliminar()
    elif Op == "3":
        Modificar()
    elif Op == "4":
        Lista()
    elif Op == "5":
        Menu_Principal()     
    else:
        print("La opción no existe, por favor ingresa una opción válida.")
        print()
        os.system("pause")
        Menu_Productos()

def Confirmar(respuesta):
    if respuesta == "n":
        print("Registro cancelado")
        print()
        os.system("pause")
        Carga()
    elif respuesta == "s":
        return True
    else:
        print("La opción ingresada no existe, por favor intenteló de nuevo.")
        print()
        os.system("pause")
    res = str(input("¿Desea registrar el producto? [S - N] :").lower())
    Confirmar(res)    

def Busqueda(num):
    global alProductos, afProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0)
    rProd = Producto()
    encontrado = False
    while alProductos.tell() < t and not encontrado:
        pos = alProductos.tell()
        rProd = pickle.load(alProductos)
        if rProd.codigo == num:
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1        

def Carga():
    global alProductos, afProductos                
    os.system("cls")
    res = str(input("¿Desea ingresar un nuevo producto? [S - N]: ").lower())
    print()
    if res == "n":
        print("Regresando al menú anterior...")
        os.system("pause")
        Menu_Productos()
    elif res == "s":
        rProd = Producto()
        print("El código debe ser de tipo [AAAA0000].")
        cod = input("Ingrese el código del producto: ").upper()
        print()
        Tamaño(cod) #Se encarga de comprobar que la variable "cod" posea 8 dígitos
        while VerificarCodigo(cod): #Verifica que los primeros 4 dígitos sean letras y los 4 dígitos restantes sean números
            print("El código ingresado no cumple con los requerimientos solicitados, por favor intenteló nuevamente.")
            print()
            os.system("pause")
            cod = input("Ingrese el código del producto: ").upper()
            print()
            Tamaño(cod) #Se encarga de comprobar si la variable "cod" posee 8 dígitos
        pos = Busqueda(cod)
        if pos == -1: #Comprueba que no exista un producto con el mismo código registrado en el sistema
            rProd = Producto()
            rProd.codigo = cod.upper()
            rProd.nombre = input("Ingrese el nombre del producto: ").upper()
            print()
            TamañoTexto(rProd.nombre)
            while VerificarTexto(rProd.nombre, len(rProd.nombre)):
                print("El nombre posee números o caracteres especiales, por favor ingrese nuevamente.")
                print()
                os.system("pause")
                rProd.nombre = str(input("Ingrese el nombre del producto: ").upper())
                print()
                TamañoTexto(rProd.nombre)
            rProd.marca = str(input("Ingrese la marca del producto: ").upper())
            print()
            print("Los talles permitidos van de 25 a 45.")
            rProd.talle = int(input("Ingrese el talle del producto: "))
            print()
            while ValidarEntero(rProd.talle, 25, 45):
                print("El talle ingresado no está dentro del rango permitido.")
                print()
                os.system("pause")
                print("Los talles permitidos van de 25 a 45.")
                rProd.talle = int(input("Ingrese el talle del producto: "))
                print()
            print("Los precios van de 75000 a 750000.")
            rProd.precio = float(input("Ingresa el precio del producto: "))
            print()
            while ValidarReal(rProd.precio, 75000, 750000):
                print("El precio ingresado es menor o supera al mencionado anteriormente, por favor ingresa un nuevo precio.")
                print()
                os.system("pause")
                print("Los precios van de 75000 a 750000.")
                rProd.precio = float(input("Ingresa el precio del producto: "))
                print()
            rProd.stock = int(input("Ingrese la cantidad de stock que posee del producto: "))
            while ValidarEntero(rProd.stock, 1, 999999):
                print("El stock ingresado es menor a 1, por favor ingresa un stock válido.")
                print()
                os.system("pause")
                rProd.stock = int(input("Ingrese la cantidad de stock que posee del producto: "))
                print()
            os.system("cls")
            print("Código:",rProd.codigo[0:4],"-",rProd.codigo[4:8])
            print("Nombre:",rProd.nombre)
            print("Marca:",rProd.marca)
            print("Talle:",rProd.talle)
            print("Precio:",rProd.precio)
            print("Stock:",rProd.stock)
            print()
            res = str(input("¿Desea registrar el producto? [S - N] :").lower())
            print()
            Confirmar(res)
            pickle.dump(rProd, alProductos)
            alProductos.flush()
            print("El producto se registró con éxito.")
            print()
        else:
            print("El codigo ya se encuentra registrado en el sistema.")
            os.system("pause")
            Carga()  
    else:
        print("La opción ingresada no existe, por favor ingresela nuevamente.")
        print()
        os.system("pause")
        Carga()
    os.system("pause")
    Carga()            

Menu_Principal()        