import os
import pickle
import os.path

class Producto:
    def __init__(self):
        self.codigo = ""
        self.nombre = ""
        self.marca = ""
        self.talle = ""
        self.precio = 0.0
        self.stock = 0

class Cliente:
    def __init__(self):
        self.nombre = ""
        self.direccion = ""
        self.telefono = ""
        self.historial = "" 

### Programa Principal###
afProductos = "C:\\Users\\matth\\Desktop\\Tienda de Zapatillas\\productos.dat"
if not os.path.exists(afProductos):
    alProductos = open(afProductos, "w+b")
else:
    alProductos = open(afProductos, "r+b")

afClientes = "C:\\Users\\matth\\Desktop\\Tienda de Zapatillas\\clientes.dat"
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
    os.system("cls")
    Res = str(input("¿Desea ingresar un nuevo producto? [S - N]: ").lower())
    if Res == "n":
        print("Regresando al menú anterior...")
        os.system("pause")
        Menu_Productos()
    elif Res == "s":
        rProd = Producto()
        Cod = str(input("Ingrese el código del producto: "))
        while Cod != "0":
            pos = Busqueda(Cod)
            if pos == -1:
                print("El código de este producto ya se encuentra cargado en el sistema")
                print()
                os.system("pause")
            else:
                alProductos.seek(0, 2)



    
    else:
        print("No se ha podido registrar la respuesta, por favor ingrese una respuesta correcta")
        os.system("pause")
        Carga()