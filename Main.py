import json
import os
import datetimeE
Bol=True
while Bol==True:
    with open("Ventas.json", encoding="utf-8") as ventas:# VENTAS
        ventas=json.load(ventas)
    with open("Compra.json", encoding="utf-8") as compras:
        compras=json.load(compras)
    with open("Medicamentos.json", encoding="utf-8") as file: 
        medicamentos=json.load(file)
    with open("Empleados.json", encoding="utf-8") as empleados: 
        empleados=json.load(empleados)
    with open("Pacientes.json", encoding="utf-8") as pacientes: 
        pacientes=json.load(pacientes)        
    with open("Proveedores.json", encoding="utf-8") as proveedores: 
        proveedores=json.load(proveedores)   
    os.system("clear")
    print("---------------\n1).Compra\n2).Vender\n3).Generar Informes\n0).Salir\n---------------")
    Opcion1=input(str("Ingrese un número para ir a la opcion deseada"))
    if Opcion1=="1":
        NomProovedor=str(input("Ingrese el nombre del proveedor"))
        bol1=True
        while bol1==True:
            os.system("clear")
            print("---------------\n1).Panaderia\n2).Pasteleria\n3).Bebidas\n4).Promociones\n0).Salir\n---------------")
            Opcion2=input(str("Ingrese un número para ir a la opcion deseada"))
            if Opcion2=="1":
                os.system("clear")
                print("---------------Panaderia---------------")
                for i in PrePan["Panaderia"]:
                    print(i, "Precio:",PrePan["Panaderia"][i])
                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in medicamentos["Panaderia"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cant=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cant*PrePan["Panaderia"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NomEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cant,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)   
                        input("Producto añadido al carrito, presione Enter para continuar")  
                    elif Contador < 11:
                        os.system("clear")
                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            elif Opcion2=="2":
                os.system("clear")
                print("---------------Pasteleria---------------")
                for i in PrePan["Pasteleria"]:
                    print(i, "Precio:",PrePan["Pasteleria"][i])
                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrePan["Pasteleria"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cant=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cant*PrePan["Pasteleria"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NomEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cant,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)    
                        input("Producto añadido al carrito, presione Enter para continuar")
                    elif Contador < 11:
                        os.system("clear")
                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            elif Opcion2=="3":
                os.system("clear")
                print("---------------Bebidas---------------")
                for i in PrePan["Bebidas"]:
                    print(i, "Precio:",PrePan["Bebidas"][i])
                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrePan["Bebidas"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cant=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cant*PrePan["Bebidas"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())  
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NomEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cant,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        
                        input("Producto añadido al carrito, presione Enter para continuar")
                    elif Contador < 10:
                        os.system("clear")
                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            elif Opcion2=="0":
                os.system("clear")
                print("---------------Apartado de promociones---------------")
                for i in PrePan["Apartado de promociones"]:
                    print(i, "Precio:",PrePan["Apartado de promociones"][i])
                Comparador=input(str("Ingrese el nombre del pan a comprar: "))
                Contador=0
                for y in PrePan["Apartado de promociones"]:
                    Contador=Contador+1
                    if Comparador == y:
                        Cant=int(input("¿Que cantidad deseas comprar? "))
                        PPan=Cant*PrePan["Apartado de promociones"][y]
                        Nombre=str(input("Nombre del comprador: "))
                        Direccion=str(input("Direccion del comprador: "))
                        Fecha=str(datetime.datetime.now())
                        Ventas[0]["Personas"].append({
                            "Fecha":Fecha,
                            "Nombre":Nombre,
                            "Direccion":Direccion,
                            "Empleado":NomEmpleado,
                            "Producto":[
                                {
                                    "NombreP":y,
                                    "Cantidad":Cant,
                                    "PrecioP":PPan
                                }
                            ]
                        })
                        with open("DatosVentas.json", "w") as file:
                            json.dump(Ventas,file)
                        input("Producto añadido al carrito, presione Enter para continuar")
                    elif Contador < 10:
                        os.system("clear")
                    else:
                        print("Producto no existente, procura escribir el nombre del producto correctamente")
                        input("Presiona Enter para continuar")
            elif Opcion2=="0":
                os.system("clear")
                print("======Saliendo======")
                input("Presione Enter para continuar")
                bol1=False
    elif Opcion1=="2":
        bol1=True
        while bol1==True:
            os.system("clear")
            print("---------------\n1).Comprar\n2).Salir\n---------------")
            Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
            if Opcion2=="1":
                NombreProovedor=str(input("Nombre del proovedor al que se le comprara: "))
                NumeroProovedor=int(input("Numero del proovedor al que desea comprar: "))
                NombreProducto=str(input("Que producto desea comprar: "))
                CantProducto=int(input("Cantidad del producto que desea comprar: "))
                PrecioProducto=int(input("Precio del producto que desea comprar: "))
                PrecioTotal=PrecioProducto*CantProducto
                Fecha=str(datetime.datetime.now())
                Compras[0]["Personas"].append(
                    {
                        "Fecha": Fecha,
                        "Nombre":NombreProovedor,
                        "Numero":NumeroProovedor,
                        "Producto":NombreProducto,
                        "Cantidad":CantProducto,
                        "Precio Unitario":PrecioProducto,
                        "Precio Total":PrecioTotal
                    }
                )
                with open("DatosCompra.json", "w") as files:
                    json.dump(Compras,files)
            elif Opcion2=="2":
                os.system("clear")
                print("---------------Saliendo---------------")
                input("Presione Enter para continuar")
                bol1=False
    elif Opcion1=="3":
        bol2=True
        while bol2==True:
            os.system("clear")
            print("---------------\n1).Registros ventas\n2).Registros Compras\n3).Salir\n---------------")         
            Opcion2=input(str("Ingrese un numero para ir a la opcion deseada: "))
            if Opcion2=="1":
                os.system("clear")
                for i in Ventas[0]["Personas"]:
                    print("---------------Ventas---------------")
                    print("Fecha de compra: ",i["Fecha"],"\nDireccion: ",i["Nombre"],"\nEmpleado: ",i["Empleado"],"\nProducto: ",i["Producto"][0]["NombreP"],"\nCantidad: ",i["Producto"][0]["Cantidad"],"\nPrecio Venta : ",i["Producto"][0]["PrecioP"])
                    print("-------------------------------------------------")
                input("Presione Enter para continuar")    
            elif Opcion2=="2":
                os.system("clear")
                for i in Compras[0]["Personas"]:
                    print("---------------Compras---------------")
                    print("Fecha de compra: ",i["Fecha"],"\nNombre del proovedor: ",i["Nombre"],"\nProducto: ",i["Producto"],"\nCantidad: ",i["Cantidad"],"\nPrecio Total: ",i["Precio Total"])
                    print("-------------------------------------------------")
                input("Presione Enter para continuar")
            elif Opcion2=="3":
                os.system("clear")
                print("---------------Saliendo--------------")
                input("Presione Enter para continuar")
                bol2=False
    elif Opcion1=="0":
        Bol=False