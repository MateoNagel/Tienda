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
        if num[i] >= "a" and num[i] <= "z":
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
        print("La opción no existe, por favor ingresa una opción válida")
        print()
        os.system("pause")
        Menu_Productos()

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
        print("El código debe ser de tipo [AAAA0000]")
        cod = input("Ingrese el código del producto: ").lower()
        print()
        Tamaño(cod) #Se encarga de comprobar que la variable "cod" posea 8 dígitos
        while VerificarCodigo(cod): #Verifica que los primeros 4 dígitos sean letras y los 4 dígitos restantes sean números
            print("El código ingresado no cumple con los requerimientos solicitados, por favor intenteló nuevamente")
            print()
            os.system("pause")
            cod = input("Ingrese el código del producto: ").lower()
            Tamaño(cod) #Se encarga de comprobar si la variable "cod" posee 8 dígitos
        if Busqueda(cod) != -1: #Comprueba que no exista un producto con el mismo código registrado en el sistema
            print("El codigo ya se encuentra registrado en el sistema")
            os.system("pause")
            Carga()
        else:
            rProd = Producto()
            alProductos.seek(0, 2)
            rProd.codigo = cod.upper()
            rProd.nombre = input("Ingrese el nombre del producto: ").upper()
            print()
                
    else:
        print("La opción ingresada no existe, por favor ingresela nuevamente")
        print()
        os.system("pause")
        Carga()
    os.system("pause")
    Carga()    

def Busqueda(num):
    global alProductos, afProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0, 0)
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

Menu_Principal()        