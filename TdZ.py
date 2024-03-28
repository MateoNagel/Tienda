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
    if res == "n":
        print("Regresando al menú anterior...")
        os.system("pause")
        Menu_Productos()
    elif res == "s":
        cod = str(input("Ingrese el código del producto con el siguiente formato [ABCD - 123] o 0 para salir: ").upper())
        while cod != "0":
            os.system("cls")
            pos = Busqueda(cod)
            if pos != -1:
                print("El código ingresado se encuentra registrado en el sistema, por favor ingrese otro")
                print()
                os.system("pause")
            else:
                rProd = Producto()
                alProductos.seek(0, 2)
                rProd.codigo = cod
                rProd.nombre = str(input("Ingrese el nombre del producto: ").upper())
                print()
                rProd.marca = str(input("Ingrese la marca del producto: ").upper())
                print()
                rProd.talle = int(input("Ingrese el talle del producto [25 - 45]: "))
                print()
                while ValidarEntero(rProd.talle, 25, 45):
                    print()
                    print("El talle ingresado no está en el rango de los permitidos. [25 - 45]")
                    os.system("pause")
                    os.system("cls")
                    rProd.talle = int(input("Ingrese el talle del producto [25 - 45]: "))
                    print()
                rProd.precio = float(input("Ingrese el precio del producto: "))
                while ValidarReal(rProd.precio, 80000, 250000):
                    print()
                    print("El precio ingresado no respeta el rango asignado. [80000 - 250000]")
                    os.system("pause")
                    os.system("cls")
                    rProd.precio = float(input("Ingrese el precio del producto [80000 - 250000]: "))
                rProd.stock = int(input("Ingrese la cantidad de productos que ingresaron: "))
                while ValidarEntero(rProd.stock, 0, 999999):
                    print()
                    print("No es posible cargar la cantidad ingresada, por favor ingresa nuevamente")
                    os.system("pause")
                    os.system("cls")
                    rProd.stock = int(input("Ingrese la cantidad de productos que ingresaron: "))    
                os.system("cls")
                print("Código: ",rProd.codigo)
                print("Nombre:",rProd.nombre)
                print("Marca: ",rProd.marca)
                print("Talle: ",rProd.talle)
                print("Precio: ",rProd.precio)
                print("Stock: ",rProd.stock)
                print()
                res2 = str(input("¿Confirmar carga del producto? [S - N]: ").lower())
                if res2 == "s":
                    pickle.dump(rProd, alProductos)
                    alProductos.flush()
                    print("Carga registrada")
                    print()
                    os.system("pause")
            os.system("cls")
            cod = str(input("Ingrese el código del producto o 0 para salir: ").upper())
    else:
        print("Lo ingresado no corresponde con las opciones dadas, por favor vuelva a intetarlo")
        print()
        os.system("pause")
        Carga()
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