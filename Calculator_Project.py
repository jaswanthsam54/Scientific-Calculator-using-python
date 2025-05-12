import math

def display_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Log (base 10)")
    print("11. Natural Log (ln)")
    print("12. Factorial")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a + b)

            elif choice == '2':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a - b)

            elif choice == '3':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a * b)

            elif choice == '4':
                a = float(input("Enter numerator: "))
                b = float(input("Enter denominator: "))
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Error: Division by zero!")

            elif choice == '5':
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print("Result:", math.pow(base, exponent))

            elif choice == '6':
                num = float(input("Enter number: "))
                if num >= 0:
                    print("Result:", math.sqrt(num))
                else:
                    print("Error: Negative number!")

            elif choice == '7':
                angle = math.radians(float(input("Enter angle in degrees: ")))
                print("Result:", math.sin(angle))

            elif choice == '8':
                angle = math.radians(float(input("Enter angle in degrees: ")))
                print("Result:", math.cos(angle))

            elif choice == '9':
                angle = math.radians(float(input("Enter angle in degrees: ")))
                print("Result:", math.tan(angle))

            elif choice == '10':
                num = float(input("Enter number: "))
                if num > 0:
                    print("Result:", math.log10(num))
                else:
                    print("Error: Log of non-positive number!")

            elif choice == '11':
                num = float(input("Enter number: "))
                if num > 0:
                    print("Result:", math.log(num))
                else:
                    print("Error: Log of non-positive number!")

            elif choice == '12':
                num = int(input("Enter integer: "))
                if num >= 0:
                    print("Result:", math.factorial(num))
                else:
                    print("Error: Factorial of negative number!")

            elif choice == '0':
                print("Exiting Scientific Calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()

