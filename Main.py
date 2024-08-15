import json
import os
import datetime
Bol=True
while Bol==True:
    with open("Ventas.json", encoding="utf-8") as ventas:
        jventas=json.load(ventas)
    with open("Compra.json", encoding="utf-8") as compras:
        jcompras=json.load(compras)
    with open("Medicamentos.json", encoding="utf-8") as file: 
        jmedicamentos=json.load(file)
    with open("Empleados.json", encoding="utf-8") as empleados: 
        jempleados=json.load(empleados)
    with open("Pacientes.json", encoding="utf-8") as pacientes: 
        jpacientes=json.load(pacientes)        
    with open("Proveedores.json", encoding="utf-8") as proveedores: 
        jproveedores=json.load(proveedores)   
    os.system("clear")
    print("---------------\n1).Compra\n2).Vender\n3).Generar Informes\n0).Salir\n---------------")
    Opcion1=input(str("Ingrese un número para ir a la opcion deseada"))

    if Opcion1=="1":#___________________Compras_____________________
        contador=0
        for i in jmedicamentos:
            contador+=1
            print(contador,".", i["nombre"])
        comp=str(input("ingresa el nombre del producto a comprar:"))
        for a in jmedicamentos:
            if comp == a ["nombre"]:
                print("Tu producto elegido es: ",a)
                Cant=int(input("Cuantas unidades deseas comprar?"))
                NomProveedor=str(input("Ingresa el nombre del proveedor"))
                ContProveedor=str(input("Ingresa el contacto del proveedor"))
                PreTotal=Cant*a["precio"]
                Fecha=str(datetime.datetime.now())

                jcompras.append(
                    {
                        "fechaCompra": Fecha,
                        "proveedor": {
                             "nombre": NomProveedor,
                            "contacto": ContProveedor
                        },
                        "medicamentosComprados": [
                            {
                                "nombreMedicamento": a,
                                "cantidadComprada": Cant,
                                "precioCompra":PreTotal
                            }
                        ]
                    }
                )

                with open("Compra.json", "w") as CopCompra:
                    json.dump(compras,CopCompra)

        input("Precione enter")

    elif Opcion1=="2":#________________Vender_________________
        NomEmpleado=str(input("ingrese el nombre del empleado"))
        compEmple=0
        for b in jempleados:
            compEmple=+1
            if compEmple == b["nombre"]:
                contador=0
                for c in jmedicamentos:
                    contador+=1
                    print(contador,".", c["nombre"])
                comp=str(input("Ingresa el nombre del producto que se vendera"))
                for d in jmedicamentos:
                    if comp == d["nombre"]:
                        print("el producto que se vendera sera:")
                        Cant=int(input("Ingrresa la cantidad que se vendera"))
                        NomPaciente=str(input("Ingresa el nombre del paciente"))
                        DirecPaciente=str(input("Ingresa la direccion del paciente"))
                        PreTotal=Cant*d["precio"] 
                        Fecha=str(datetime.datetime.now())

                        jventas.append(
                            {
                                "fechaVenta": "2023-01-10T00:00:00Z",
                                "paciente": 
                                {
                                    "nombre": "Juan",
                                    "direccion": "Calle 123"
                                },
                                "empleado": 
                                {
                                    "nombre": "Pedro",
                                    "cargo": "Vendedor"
                                },
                                "medicamentosVendidos": 
                                [
                                    {
                                        "nombreMedicamento": "Paracetamol",
                                        "cantidadVendida": 2,
                                        "precio": 20
                                    }
                                ]
                            }
                        )
                        with open("Ventas.json", "w") as CopVentas:
                            json.dump(ventas,CopVentas)
    elif Opcion1 == "3":
        boleano=True
        os.system("cls")
        while boleano == True:
            print("________________\n1).Informes de compras. \n2).Informes de ventas. \n3).Salir \n______________________")
            Opcion2=str(input("Ingrese un número para ir a la opcion deseada"))
            
            if Opcion2 == "1":
                for e in jcompras:
                    print("Fecha: ",e["fechaCompra"], "Proveedor: ",e["proveedor"]["nombre"],e["medicamentosComprados"][0]["nombreMedicamento"])

            elif Opcion2 == "2":
                for e in jventas:
                    print("Fecha: ",e["fechaVenta"],"Nombre del Paciente: ",e["paciente"]["nombre"],"Venta: ",e["medicamentosVendidos"][0]["nombreMedicamento"])
                    
                input("Precione enter")
            elif Opcion2 == 3:
                boleano=False
    
    elif Opcion1 == "4":
        print("Preciona enter para terminar de salir")
        input("")
        Bol=False                
#Desarrollador por Valentina Isabel Molina Lopera 