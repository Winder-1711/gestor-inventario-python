#Entrada de datos
catalogo = []

while True:
    print("1. Ver catálogo de productos")
    print("2. Registrar nuevo producto")
    print("3. Buscar producto por nombre")
    print("4. Salir")
    print("\n==========================")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n=== CATÁLOGO DE PRODUCTOS ===")
        if len(catalogo) == 0:
            print("⚠️ El catálogo está vacío actualmente.")
        else:
            for producto in catalogo:
                print(f"- {producto['nombre']}: ${producto['precio']:.2f} (Stock: {producto['stock']})")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("❌ El nombre del producto no puede estar vacío. Intenta de nuevo.")
            nombre = input("Ingrese el nombre del producto: ").strip()
        while True:
            try:
                precio = float(input(f"Ingrese el precio de '{nombre}': $ "))
                if precio < 0:
                    print("❌ El precio no puede ser negativo. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada inválida. Por favor, ingrese un número válido para el precio.")
        while True:
            try:
                stock = int(input(f"Ingrese la cantidad en stock de '{nombre}': "))
                if stock < 0:
                    print("❌ La cantidad en stock no puede ser negativa. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada inválida. Por favor, ingrese un número entero para el stock.")
        producto = {"nombre": nombre, "precio": precio, "stock": stock}
        catalogo.append(producto)
        print(f"'{nombre}' ✅ Producto agregado con éxito.")
    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in catalogo:
            if producto['nombre'].lower() == nombre_buscar.lower():
                print(f"Producto encontrado: {producto['nombre']}: ${producto['precio']:.2f} (Stock: {producto['stock']})")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("❌ Opción no reconocida. Intenta de nuevo.")