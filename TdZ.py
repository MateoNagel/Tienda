import keyboard
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
        self.activo = "A"

class Cliente:
    def __init__(self):
        self.nombre = ""
        self.direccion = ""
        self.telefono = ""
        self.historial = "" 


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
        alProductos.close()
        alClientes.close()
    else:
        print("La opción no existe, por favor ingresa una opción válida")
        print()
        os.system("pause")
        Menu_Principal()   


### MENÚ PRODUCTOS ###
def Menu_Productos():
    os.system("cls")
    print()
    print("MENU DE PRODUCTOS")
    print()
    print("1 - CARGAR PRODUCTO")
    print("2 - ELIMINAR PRODUCTO")
    print("3 - MODIFICAR PRODUCTO")
    print("4 - LISTA DE PRODUCTOS")
    print("5 - REGRESAR")
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


### Realiza una búsqueda para comprobar si la variable "num" es igual a un código ya cargado en el archivo productos.dat ###
def Buscar(dato):
    global alProductos, afProductos
    t = os.path.getsize(afProductos)
    alProductos.seek(0)
    rProd = Producto()
    encontrado = False
    while alProductos.tell() < t and not encontrado:
        pos = alProductos.tell()
        rProd = pickle.load(alProductos)
        if rProd.codigo.lower() == dato.lower() or rProd.nombre.lower() == dato.lower():
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1        


### En esta función se podrán cargar productos ### 
def Carga():
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
                                Carga()
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
                    Carga()
                elif pos == -1 and VerificarCodigo(cod) == False:
                    break
            while True:        
                os.system("cls")
                nombre = input("Ingrese el nombre del producto: ")
                if nombre == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    Carga()
                elif ValidarTexto(nombre) == False:
                    break
            while True:
                os.system("cls")
                marca = input("Ingrese la marca del producto: ")
                if marca == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    Carga()
                elif ValidarTexto(marca) == False:
                    break
            while True:
                os.system("cls")
                print("Los talles con los que trabajamos van de 25 a 45.")
                talle = input("Ingrese el talle del producto: ")
                if talle == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    Carga()
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
                    Carga()
                elif ValidarReal(precio, 50000, 800000) == False:
                    break
            while True:
                os.system("cls")
                stock = input("Ingrese la cantidad de stock que posee: ")
                if stock == "0":
                    print("Reiniciando menú...")
                    print()
                    os.system("pause")
                    Carga()
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
                    Carga()
                else:
                    print("La opción ingresada no existe, por favor ingresela nuevamente.")
                    print()
                    os.system("pause")    



        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")

    
def Prints():
    print()
    print("Código", end="         ")
    print("Nombre", end="                   ")
    print("Marca", end="          ")
    print("Talle", end="          ")
    print("Precio", end="         ")
    print("Stock", end="          ")
    print("Actividad")
    print()


### En esta función se podrán elimiar productos ###
def Eliminar():
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
                Prints()
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
                    Eliminar()
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
                Eliminar()
            else:
                while True:
                    os.system("cls")
                    res = input("¿Está seguro que quiere dar de baja el producto? [S - N]: ")
                    print()
                    if res.lower() == "n":
                        print("Baja cancelada.")
                        print()
                        os.system("pause")
                        Modificar()
                    elif res.lower() == "s":
                        rProd.activo = "B"
                        alProductos.seek(pos)
                        pickle.dump(rProd, alProductos)
                        alProductos.flush()
                        print("La baja fue dada con éxito.")
                        print()
                        os.system("pause")
                        Modificar()
                    else:
                        print("La opción ingresada no existe, por favor ingresela nuevamente.")
                        print()
                        os.system("pause")
                        Eliminar()
        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")
            Eliminar()
        os.system("pause")
        Eliminar()

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

### En esta función se podrán modificar los productos ###
def Modificar():
    global afProductos, alProductos, cod, nombre
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
                print("Lista de Productos")
                Prints()
                alProductos.seek(0)
                while alProductos.tell() < t:
                    prod = pickle.load(alProductos)
                    if prod.activo != "A":    
                        mostrarProducto(prod)
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
                    Modificar()
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
                                if rProd.codigo == cod:
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
                                if rProd.nombre == nombre:
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
                                if rProd.marca == marca:
                                    print("La marca ingresada es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarTexto(marca) == False:
                                    break
                            rProd.marca = marca.upper()        
                        elif Op == "4":    
                            while True:
                                os.system("cls")
                                talle = input("Ingrese el nuevo talle para el producto: ")
                                if rProd.talle == talle:
                                    print("El talle ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarEntero(talle, 25, 45) == True:
                                    print("El rango del talle va de 25 a 45. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarEntero(talle, 25, 45) == False and rProd.talle != talle:
                                    break
                            rProd.talle = talle    
                        elif Op == "5":    
                            while True:
                                os.system("cls")
                                precio = input("Ingrese el nuevo precio para el producto: ")
                                if rProd.precio == precio:
                                    print("El precio ingresado es igual al que posee el producto actualmente. Intenteló de nuevo.")
                                    print()
                                    os.system("pause")
                                elif ValidarReal(precio, 75000, 750000) == False and rProd.precio != precio:
                                    break
                            rProd.precio = precio    
                        elif Op == "6":    
                            while True:
                                os.system("cls")
                                stock = input("Ingrese el nuevo stock para el producto: ")
                                if rProd.stock == stock:
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
                                    Modificar()
                                elif res.lower() == "n":
                                    print("Modificación cancelada.")
                                    print()
                                    os.system("pause")
                                    Modificar()
                                else:
                                    print("La respuesta ingresada no es válida. Por favor, intenteló de nuevo.")
                                    print()
                                    os.system("pause")
            else:
                print("La opción ingresada no es válida. Intenteló de nuevo.")
                print()
                os.system("pause")

def Lista():
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
            print("3 - Buscar Por Talle")
            print("4 - Salir")
            print()
            res = input("Ingrese la opción: ")
            if res == "1":
                os.system("cls")
                print("Listado Completo de Productos")
                Prints()
                while True:
                    try:
                        rProd = pickle.load(alProductos)
                        mostrarProducto(rProd)
                    except EOFError:
                        break
                os.system("pause")    
                Lista()                    
            elif res == "2":
                os.system("cls")
                while True:
                    os.system("cls")
                    marca = input("Ingrese la marca que desea buscar: ")
                    print()
                    if ValidarTexto(marca) == False:
                        break
                print("Listado de",marca.upper())
                Prints()
                while alProductos.tell() < t:
                    prod = pickle.load(alProductos)
                    if prod.marca.lower() == marca.lower():
                        mostrarProducto(prod)
                print()
                os.system("pause")                                                   
                Lista()
            elif res == "3":
                os.system("cls")
                while True:
                    os.system("cls")
                    print("Los talles actuales van de 25 a 45.")
                    talle = input("Ingrese el talle que desea buscar: ")
                    print()
                    if ValidarEntero(talle, 25, 45) != False:
                        os.system("pause")
                    else:
                        break
                print("Listado de Productos Talle Número",talle)
                Prints()
                while alProductos.tell() < t:
                    prod = pickle.load(alProductos)
                    if prod.talle == talle:        
                        mostrarProducto(prod)    
                print()
                os.system("pause")
                Lista()        




Menu_Principal()        