import os
os.system("cls")
import json

# registrador de pedidos nombre , apellido , comuna y detalles pedido
#VALIDAR NOMBRE :
def registrar_pedidos ():#pq es vacio pq no sirve ningun parametro onda es cambiante entonces vacio no es fijo

    #validar datos
    nombre = "" 
    apellido = ""
    direccion = ""
    while True:
        try:
            nombre=input("ingrese nombre:")
        except: 
            nombre = "" #distinto a vacio
          
        if nombre != "":
            print("valido")
            break
        else:
            print("porfa ingrese algo ")
    while True:
        try:
            apellido=input("ingrese apellido:")
        except: 
            apellido= ""
           
        if apellido != "":
            print("valido")
            break
        else:
            print("porfa ingrese algo ")
    while True:
        try:
            direccion=input("ingrese direccion:")
        except: 
            direccion= ""
          
        if direccion!= "":
            print("valido")
            break
        else:
            print("porfa ingrese algo ")
    while True:
        sectores_ad={
            "sector1":["independecia","ñuñoa","santiago"],
            "sector2":["lo prado"," cerro navia","pudahuel "],
            "sector3":["pac","cerrillos","maipu"],
        }
        print("1-sector (1)independencia,ñuñoa,santiago")
        print("2-sector (2)lo padro ,cerro navia,pudahuel")
        print("3-sector (3)pac,cerrilllos,maipu")

        try:
            sector=int(input("ingrese sector:"))
        except: 
            sector= 0
            print("invalido")
        if sector == 1 :
            print("sector 1",sectores_ad["sector1"])
            break
        elif sector == 2:
            print("sector 2",sectores_ad["sector2"])
            break
        elif sector == 3:
            print("sector 3",sectores_ad["sector3"])
            break
        else:
            print("opcion invalida ")
            
    cant_cilindro45=0
    cant_cilindro5=0
    cant_cilindro15=0   
    while True:
        print("cilindros que tenemos")
        print("1-cilindro 5 kg")
        print("2-cilindro 15 kg")
        print("3.cilindro 45 kg")
        print("4.salir apreta(4)")
        
        try:
            
            opcion_cilindroskg = int(input("ingrese el opcion que desea : "))
        except:
            opcion_cilindroskg = 0
            print("opcion invalida, ingrese kg correcto")

        if opcion_cilindroskg == 1:
            print("elegiste 5kg")
            while True:
                try:
                    cant_cilindro5 = int(input("ingrese cantidad de cilindros min (1) :"))
                except:
                    cant_cilindro5 = 0
                    print("opcion invalida")
                if cant_cilindro5 > 0 :#mayor a 0 
                    print("es valido ")
                    break
        elif opcion_cilindroskg == 2:
            print("elegiste 15kg")
            while True:
                try:
                    cant_cilindro15 = int(input("ingrese cantidad de cilindros min(1) : "))
                except:
                    cant_cilindro15 = 0
                    print("opcion invalida")
                if cant_cilindro15 > 0 :#mayor a 0 
                    print("es valido ")
                    break# mientras sea valido se sale
        elif opcion_cilindroskg == 3:
            print("elegiste 45kg")
            while True:
                try:
                    cant_cilindro45 = int(input("ingrese cantidad de cilindros min (1) :"))
                except:
                    cant_cilindro45 = 0
                    print("opcion invalida")
                if cant_cilindro45 > 0 :#mayor a 0 
                    print("es valido ")
                    break
        
        elif opcion_cilindroskg == 4:
            print("saliste")
            break
        else:
            print("invalida")

    #diciconario dentro de def
    diccionario_pedidos = {
        "nombre":nombre,
        "apellido":apellido,
        "direccion":direccion,
        "cilindro_5kg": cant_cilindro5,
        "cilindro_15kg":cant_cilindro15,
        "cilindro_45kg":cant_cilindro45,
        "Sector_ingresado":sector,
        }
    return diccionario_pedidos

#lista solicitada parte dos
#imprimir hoja de pedidos
def mostrar_pedidos(pedidos):
   for pedido in pedidos:
       #imprimir pedido
        print(pedido)
#menu repartidor ,  es para q cuando me marquen  1 me vean todos los pedidos de la zona 1 y asi etc
def imprimir_hoja (pedidos):
    
    while True:
    
        print("1-sector (1)")
        print("2-sector (2)")
        print("3-sector (3)")
        try:
            sector = int(input("ingrese sector:"))
            
        except:
            sector = -1
            print("invalido")
        if sector in range (0,4):
            break
    # otra validacion para mostrar el sector filtrado segun el pedido repartidor
    #filtrar los pedidos pq? pq solo deben ser los de una zona , pq no me importa q pidio paula
    pedidos_filtrados = []
    for pedido in pedidos :
        if pedido["Sector_ingresado"] == sector:
            pedidos_filtrados.append(pedido)
    
# por cada objeto en objetos 
#se buca cumplir la condicion en if con objeto en lista del sector que pusimos al comienzo en este caso
#objeto que buscamos validar y eso seria == sector q ingreso el usuario
#se añade a la variable vacia q creamos con el appen y el objeto .

    with open ("gasarchivo.txt","w")as archivo:

        for pedido in pedidos_filtrados:
            archivo.write(f'\n{pedido["nombre"]},{pedido["apellido"]},{pedido["direccion"]},{pedido["Sector_ingresado"]},{pedido["cilindro_5kg"]},{pedido["cilindro_15kg"]},{pedido["cilindro_45kg"]},')
    with open("gasarchivo.json","w")as archivo:
        json.dump(pedidos_filtrados,archivo,indent=2)
        
        


    




lista_pedidos=[]
while True:
 

    print("1.registro")
    print("2.lista")
    print("3.imprimir hoja ruta")
    print("4.salir")
    try:
        opcion = int(input("ingrese opcion :"))
        
    except:
        opcion = 0
        print("opcion no valida")
    if opcion == 1:
        nuevo_pedido =registrar_pedidos()
        lista_pedidos.append(nuevo_pedido)

        
        

    
    elif opcion == 2:
        mostrar_pedidos(lista_pedidos)
# importar archivos 
    elif opcion == 3:
        imprimir_hoja(lista_pedidos)
    elif opcion == 4:
        print("saliste")
        break
    else:
        print("opcion invalida uwu")

        
        
        
    

       
       


        


        
