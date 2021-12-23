class Calculator:
    x = 0.0
    y = 0.0

    def add(self, x, y):
        self.x = x 
        self.y = y
        return x + y

    def sub(self, x, y):
        self.x = x 
        self.y = y
        return x - y

    def mul(self, x, y):
        self.x = x 
        self.y = y
        return x * y

    def div(self, x, y):
        self.x = x 
        self.y = y
        return x / y

def main():

    running = True

    calc = Calculator()

    while running:

        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Select the operation: ")
        
        if choice in ('1', '2', '3', '4'):
            x = float(input("\nEnter 1st number: "))
            y = float(input("Enter 2nd number: "))

            if choice == '1':
                sum = calc.add(x, y)
                print(f"Sum: {sum}")
                # print('{} - {} = {}'.format(x, y, sum))

            elif choice == '2':
                diff = calc.sub(x, y)
                print(f'Difference: {diff}')

            elif choice == '3':
                prod = calc.mul(x, y)
                print(f'Product: {prod}')

            elif choice == '4':
                quot = calc.div(x, y)
                print(f'Quotient: {quot}')

            proceed = input("\nCalculate again? (y/n): ")

            if proceed == "n":
                running = False

        else:
            print("Sorry, Invalid choice...")
            #raise Exception("Sorry, Invalid choice...")

if __name__ == '__main__':
    main()
