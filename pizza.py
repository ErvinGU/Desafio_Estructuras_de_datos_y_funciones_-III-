# Opciones
MASAS = ["Tradicional", "Delgada", "Bordes de Queso"]
SALSA = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
INGREDIENTES_BASE = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

# Personalizar Pizza
pizza = {
    "masa": "Tradicional",
    "salsa": "Tomate",
    "ingredientes": INGREDIENTES_BASE.copy()
}

def seleccionar_masa():
    print("Seleccione el tipo de masa:")
    for i, masa in enumerate(MASAS, 1):
        print(f"{i}. {masa}")
    opcion = int(input("Ingrese opción: ")) - 1
    pizza["masa"] = MASAS[opcion]

def seleccionar_salsa():
    print("Seleccione el tipo de salsa:")
    for i, salsa in enumerate(SALSA, 1):
        print(f"{i}. {salsa}")
    opcion = int(input("Ingrese opción: ")) - 1
    pizza["salsa"] = SALSA[opcion]

def modificar_ingredientes():
    while True:
        print("\nIngredientes actuales:", pizza["ingredientes"])
        print("1. Agregar ingrediente\n2. Eliminar ingrediente\n3. Salir")
        opcion = input("Seleccione opción: ")
        
        if opcion == "1":
            nuevo = input("Ingrese nuevo ingrediente: ").capitalize()
            if nuevo not in pizza["ingredientes"]:
                pizza["ingredientes"].append(nuevo)
        elif opcion == "2":
            eliminar = input("Ingrese ingrediente a eliminar: ").capitalize()
            if eliminar in pizza["ingredientes"]:
                pizza["ingredientes"].remove(eliminar)
        elif opcion == "3":
            break

def calcular_tiempo_preparacion():
    tiempo = 20 + (len(pizza["ingredientes"]) * 2)
    return tiempo

def mostrar_pizza():
    print("\nTu pizza personalizada 🍕:")
    print(f"- Masa: {pizza['masa']}")
    print(f"- Salsa: {pizza['salsa']}")
    print(f"- Ingredientes: {', '.join(pizza['ingredientes'])}")

def confirmar_pedido():
    mostrar_pizza()
    tiempo_estimado = calcular_tiempo_preparacion()
    print(f"Tiempo estimado de preparación: {tiempo_estimado} minutos.")
    confirmar = input("¿Desea confirmar el pedido? (S/N): ").strip().lower()
    if confirmar == "s":
        print("¡Pedido confirmado! 🍕 Tu pizza estará lista pronto.")

def menu_principal():
    while True:
        print("\n--- Bienvenido a Pizza JAT ---")
        print("1. Seleccionar Masa")
        print("2. Seleccionar Salsa")
        print("3. Modificar Ingredientes")
        print("4. Mostrar Pizza")
        print("5. Confirmar Pedido")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            seleccionar_masa()
        elif opcion == "2":
            seleccionar_salsa()
        elif opcion == "3":
            modificar_ingredientes()
        elif opcion == "4":
            mostrar_pizza()
        elif opcion == "5":
            confirmar_pedido()
        elif opcion == "6":
            print("¡Gracias por visitar la Pizzería! 👋")
            break

# Ejecutar el menú
menu_principal()
