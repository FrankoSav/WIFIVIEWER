import os

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print("       ==============================================================================================================================")
    print("                                                    Menu")
    print("       ==============================================================================================================================")
    print("\n")
    print("                1. Presiona ENTER para ver todas las redes y escribe el nombre de la red para saber su clave.")
    print("\n")
    print("       ==============================================================================================================================")
    print("\n\n")

def show_networks():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print("Redes disponibles:")
    os.system("netsh wlan show profile")
    network_name = input("Escribe el nombre de la red y presiona Enter para ver información y clave: ")
    if network_name == "":
        print("No se ha ingresado un nombre de red.")
    else:
        os.system(f"netsh wlan show profile name=\"{network_name}\" key=clear")
    input("\nPulsa Enter para continuar...")
    show_menu()

def main():
    show_menu()
    option = input("Ingresa una opción: ")
    if option == "1":
        show_networks()
    else:
        print("Opción inválida. Inténtalo de nuevo.")
        input("Pulsa Enter para continuar...")
        main()

if __name__ == "__main__":
    main()
