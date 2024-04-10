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
        self.activo = True

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
                return True  
        except:
            return True 
    else:
        print("No se ha ingresado un número, por favor intenteló de nuevo.")
        print()
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
        Salir()
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


### Verifica que la variable "respuesta" sea igual a las propuestas en la función ###
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


### Realiza una búsqueda para comprobar si la variable "num" es igual a un código ya cargado en el archivo productos.dat ###
def BuscarCodigo(num):
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


### En esta función se podrán cargar productos ### 
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
        print("El código debe ser de tipo [AAAA0000].")
        cod = input("Ingrese el código del producto: ").upper()
        print()
        while VerificarCodigo(cod): #Verifica que los primeros 4 dígitos sean letras y los 4 dígitos restantes sean números
            cod = input("Ingrese el código del producto: ").upper()
            print()
        pos = BuscarCodigo(cod)
        if pos == -1: #Comprueba que no exista un producto con el mismo código registrado en el sistema
            rProd = Producto()
            rProd.codigo = cod.upper()
            rProd.nombre = input("Ingrese el nombre del producto: ").upper()
            print()
            while ValidarTexto(rProd.nombre):
                rProd.nombre = input("Ingrese el nombre: ").upper()
                print()
            rProd.marca = input("Ingrese la marca del producto: ").upper()
            print()
            while ValidarTexto(rProd.marca):
                rProd.marca = input("Ingrese la marca del producto: ").upper()
                print()
            print("Los talles permitidos van de 25 a 45.")
            rProd.talle = input("Ingrese el talle del producto: ")
            print()
            while ValidarEntero(rProd.talle, 25, 45):
                os.system("pause")
                os.system("cls")
                print("Los talles permitidos van de 25 a 45.")
                rProd.talle = input("Ingrese el talle del producto: ")
                print()
            print("Los precios van de 75000 a 750000.")
            rProd.precio = input("Ingresa el precio del producto: ")
            print()
            while ValidarReal(rProd.precio, 75000, 750000):
                os.system("pause")
                os.system("cls")
                print("Los precios van de 75000 a 750000.")
                rProd.precio = input("Ingresa el precio del producto: ")
                print()
            rProd.stock = input("Ingrese la cantidad de stock que posee del producto: ")
            while ValidarEntero(rProd.stock, 1, 999999):
                os.system("pause")
                os.system("cls")
                rProd.stock = input("Ingrese la cantidad de stock que posee del producto: ")
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


### En esta función se muestran los productos cargados ###
def MostrarProductos():
    global alProductos, afProductos
    os.system("cls")
    t = os.path.getsize(afProductos)
    alProductos.seek(0)
    rProd = Producto()
    while alProductos.tell() < t:
        rProd = pickle.load(alProductos)
        if rProd.activo == True:    
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
            print("Activo: Sí")
            print("------------------------------")
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
            os.system("cls")
            MostrarProductos()
            print("El código debe ser de tipo [AAAA0000].")
            cod = input("Ingrese el codigo del producto que desea eliminar: ").upper()
            print()
            while VerificarCodigo(cod): #Verifica que los primeros 4 dígitos sean letras y los 4 dígitos restantes sean números
                MostrarProductos()
                print("El código debe ser de tipo [AAAA0000].")
                cod = input("Ingrese el código del producto que desea eliminar: ").upper()
                print()
            pos = BuscarCodigo(cod)
            if pos == -1:
                print("El código ingresado no se encuentra cargado en el sistema.")
                print()
                os.system("pause")
                Eliminar()
            else:
                alProductos.seek(pos, 0)
                rProd = pickle.load(alProductos)
                if rProd.activo == False:
                    print("El producto ya se encuentra dado de baja.")
                    print()
                    os.system("pause")
                    Eliminar()
                else:
                    rProd.activo = False
                    alProductos.seek(pos)
                    pickle.dump(rProd, alProductos)
                    alProductos.flush()
                    print("El producto fue dado debaja exitosamente")
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
    print("Activo: Sí")
    print("------------------------------")
    print()

### En esta función se podrán modificar los productos ###
def Modificar():
    global afProductos, alProductos
    os.system("cls")
    t = os.path.getsize(afProductos)
    if t == 0:
        print("No se han encontrado productos en el sistema")
        print()
        os.system("pause")
        Menu_Productos()
    else:
        res = input("¿Desea modificar algún producto? [S - N]: ").lower()
        print()
        if res == "n":
            print("Regresando al menú anterior...")
            os.system("pause")
            Menu_Productos()
        elif res == "s":
            os.system("cls")
            MostrarProductos()
            print("El código debe ser de tipo [AAAA0000].")
            cod = input("Ingrese el codigo del producto que desea modificar: ").upper()
            print()
            while VerificarCodigo(cod): #Verifica que los primeros 4 dígitos sean letras y los 4 dígitos restantes sean números
                MostrarProductos()
                print("El código debe ser de tipo [AAAA0000].")
                cod = input("Ingrese el código del producto que desea modificar: ").upper()
                print()
            pos = BuscarCodigo(cod)
            if pos == -1:
                print("El código no se encuentra cargado en el sistema.")
                print()
                os.system("pause")
                Modificar()
            else:
                alProductos.seek(pos, 0)
                rProd = pickle.load(alProductos)
                if rProd.activo == False:
                    print("El producto se encuentra dado de baja. Si quiere modificarlo deberá de darlo de alta en el menú correspondiente.")
                    print()
                    os.system("pause")
                    Modificar()
                else:    
                    while True:
                        os.system("cls")
                        print("Las opciones a modificar son: ")
                        print()
                        print("R - Recargar")
                        print("C - Código")
                        print("N - Nombre")
                        print("M - Marca")
                        print("T - Talle")
                        print("P - Precio")
                        print("S - Stock")
                        print()
                        op = input("Ingrese la opción que desea modificar: ")
                        if op == "r":
                            while True:
                                os.system("cls")
                                Mostrar(pos)
                                print("El código debe ser de tipo [AAAA0000].")
                                cod = input("Ingrese el nuevo código que tendrá el producto: ").upper()
                                print()
                                if VerificarCodigo(cod) == False and BuscarCodigo(cod) == -1:
                                    break
                                elif VerificarCodigo(cod) == False and BuscarCodigo(cod) != -1:
                                    print("El código ingresado ya se encuentra registrado en un producto.")
                                    print("")
                                    os.system("pause")        
                            rProd.codigo = cod.upper()
                            rProd.nombre = input("Ingrese el nombre del producto: ").upper()
                            print()
                            while ValidarTexto(rProd.nombre):
                                rProd.nombre = input("Ingrese el nombre: ").upper()
                                print()
                            rProd.marca = input("Ingrese la marca del producto: ").upper()
                            print()
                            while ValidarTexto(rProd.marca):
                                rProd.marca = input("Ingrese la marca del producto: ").upper()
                                print()
                            print("Los talles permitidos van de 25 a 45.")
                            rProd.talle = input("Ingrese el talle del producto: ")
                            print()
                            while ValidarEntero(rProd.talle, 25, 45):
                                os.system("pause")
                                os.system("cls")
                                print("Los talles permitidos van de 25 a 45.")
                                rProd.talle = input("Ingrese el talle del producto: ")
                                print()
                            print("Los precios van de 75000 a 750000.")
                            rProd.precio = input("Ingresa el precio del producto: ")
                            print()
                            while ValidarReal(rProd.precio, 75000, 750000):
                                os.system("pause")
                                os.system("cls")
                                print("Los precios van de 75000 a 750000.")
                                rProd.precio = input("Ingresa el precio del producto: ")
                                print()
                            rProd.stock = input("Ingrese la cantidad de stock que posee del producto: ")
                            while ValidarEntero(rProd.stock, 1, 999999):
                                os.system("pause")
                                os.system("cls")
                                rProd.stock = input("Ingrese la cantidad de stock que posee del producto: ")
                                print()   
                            os.system("cls")
                            print("Código:",rProd.codigo[0:4],"-",rProd.codigo[4:8])
                            print("Nombre:",rProd.nombre)
                            print("Marca:",rProd.marca)
                            print("Talle:",rProd.talle)
                            print("Precio:",rProd.precio)
                            print("Stock:",rProd.stock)
                            print()
                            res = str(input("¿Desea modificar el producto? [S - N] :").lower())
                            print()
                            Confirmar(res)
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El producto se registró con éxito.")
                            print()
                            os.system("pause")
                            Menu_Productos()
                        elif op == "c":
                            while True:
                                os.system("cls")
                                Mostra(pos)
                                print("El código debe ser de tipo [AAAA0000].")
                                cod = input("Ingrese el nuevo código para el producto: ").upper()
                                print()
                                if VerificarCodigo(cod) == False and BuscarCodigo(cod) == -1:
                                    break
                                elif VerificarCodigo(cod) == False and BuscarCodigo(cod) != -1:
                                    print("El código ingresado ya se encuentra registrado en un producto.")
                                    print("")
                                    os.system("pause")
                            rProd.codigo = cod.upper()
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El código fue actualizado correctamente.")
                            print()
                            os.system("pause")
                            Modificar()
                        elif op == "n":
                            while True:
                                os.system("pause")
                                Mostrar(pos)
                                nombre = input("Ingrese el nuevo nombre del producto: ").upper()
                                print()
                                if ValidarTexto(nombre) == False and rProd.nombre != nombre:
                                    break
                                elif ValidarTexto(nombre) == False and rProd.nombre == nombre:
                                    print("El producto ya posee ese nombre.")
                                    print()
                                    os.system("pause")
                            rProd.nombre = nombre.upper()
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El nombre fue actualizado correctamente.")
                            print()
                            os.system("pause")
                            Modificar()
                        elif op == "m":
                            while True:
                                os.system("cls")
                                Mostrar(pos)
                                marca = input("Ingrese la nueva marca del producto: ").upper()
                                print()
                                if ValidarTexto(marca) == False and rProd.marca != marca:
                                    break
                                elif ValidarTexto(marca) == False and rProd.marca == marca:
                                    print("El producto ya posee esa marca.")
                                    print()
                                    os.system("pause")
                            rProd.marca = marca.upper()
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("La marca fue actualizada correctamente.")
                            print()
                            os.system("pause")
                            Modificar()
                        elif op == "t":
                            while True:
                                os.system("cls")
                                Mostrar(pos)
                                talle = input("Ingrese el nuevo talle del producto: ")
                                if ValidarEntero(talle, 25, 45) == False and rProd.talle != talle:
                                    break
                                elif ValidarEntero(talle, 25, 45) == False and rProd.talle == talle:
                                    print("El producto ya posee este talle.")
                                    print()
                                    os.system("pause")
                            rProd.marca = talle
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El talle fue actualizada correctamente.")
                            print()
                            os.system("pause")
                            Modificar()
                        elif op == "p":
                            while True:
                                os.system("cls")
                                Mostrar(pos)
                                precio = input("Ingresa el nuevo precio del producto: ")
                                if ValidarReal(precio, 75000, 750000) == False and rProd.precio != precio:
                                    break
                                elif ValidarReal(precio, 75000, 750000) == False and rProd.precio == precio:
                                    print("El producto ya posee este precio.")
                                    print()
                                    os.system("pause")
                            rProd.precio = precio
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El precio fue actualizado correctamente.")
                            print()
                            os.system("pause")
                            Modificar()
                        elif op == "s":
                            while True:
                                os.system("cls")
                                Mostrar(pos)
                                stock = input("Ingresa el nuevo stock del producto: ")
                                if ValidarEntero(stock, 1, 999999) == False and rProd.stock != stock:
                                    break
                                elif ValidarEntero(stock, 1, 999999) == False and rProd.stock == stock:
                                    print("El producto ya posee este stock.")
                                    print()
                                    os.system("pause")
                            rProd.stock == stock
                            alProductos.seek(pos)
                            pickle.dump(rProd, alProductos)
                            alProductos.flush()
                            print("El stock fue actualizado correctamente.")
                            print()
                            os.system("pause")
                            Modificar()                                          
        else:
            print("La opción ingresada no existe, por favor ingresela nuevamente.")
            print()
            os.system("pause")
            Modificar()            


Menu_Principal()        