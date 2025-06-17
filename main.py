from vehiculo import Vehiculo
from basedatos import BaseDatos

def mostrar_menu():
    print("\n--- Menu de gestion de vehiculos ---")
    print("1. Registrar Vehiculo")
    print("2. Listar Vehiculo")
    print("3. Buscar Vehiculo")
    print("4. Eliminar Vehiculo")
    print("5. Actualizar Vehiculo")
    print("6. Exportar a CSV Fabio")
    print("7. Exportar a CSV Kevin")
    print("8. Exportar a CSV Daniel")
    print("9. Exportar a CSV Yerco")
    print("0. Salir")

def main():
    bd = BaseDatos()

    bd.conectar()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion:")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = input("Año: ")
            vehiculo = Vehiculo(marca,modelo,anio)
            bd.insertar_vehiculo(vehiculo)
            print("Vehiculo Registrado.")

        elif opcion == "2":
            vehiculos = bd.listar_vehiculos()
            for v in vehiculos:
                print(f"ID: {v[0]}, Marca: {v[1]}, Modelo: {v[2]}, Año: {v[3]}")
      
        elif opcion == "3":
            id_v = int(input("ID Vehiculo: "))
            v = bd.buscar_vehiculo(id_v)
            if v:
                print(f"ID: {v[0]}, Marca: {v[1]}, Modelo: {v[2]}, Año: {v[3]}")
            else:
                print("Vehiculo no encontrado. ")

        elif opcion == "4":
            id_v = int(input("ID del Vehiculo a Eliminar: "))
            bd.eliminar_vehiculo(id_v)
            print("Vehiculo Eliminado.")
        
        elif opcion == "5":
            try:
                vehiculo_id = int(input("ingrese el id del vehiculo a actualizar:"))
                nueva_marca = input("ingrese marca nueva: ")
                nuevo_modelo = input("ingrese nuevo modelo: ")
                nuevo_anio = input("ingrese nuevo año: ")
                bd.actualizar_vehiculo(vehiculo_id, nueva_marca, nuevo_modelo, nuevo_anio) 
            except ValueError:
                print("datos invalidos, ingrese el id correcto")
        



        elif opcion == "0":
            print("saliendo del programa.")
            bd.cerrar()
            break

        else:
            print("opcion invalida")

if __name__ == "__main__":
    main()

