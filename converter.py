def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def menu():
    print("🌡️ Temperature Converter")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            c = float(input("Enter Celsius: "))
            print(f"= {celsius_to_fahrenheit(c):.2f} °F\n")

        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            print(f"= {fahrenheit_to_celsius(f):.2f} °C\n")

        elif choice == "3":
            c = float(input("Enter Celsius: "))
            print(f"= {celsius_to_kelvin(c):.2f} K\n")

        elif choice == "4":
            k = float(input("Enter Kelvin: "))
            print(f"= {kelvin_to_celsius(k):.2f} °C\n")

        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again!\n")
