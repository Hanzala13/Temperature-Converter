def main():
    while True:
        print("\nTemperature Converter")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Quit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius * 9 / 5 + 32
            print(f"{celsius} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()