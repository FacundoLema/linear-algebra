import vectors

options = ["Vector addition", "Vector subtraction", "Vector Scaling", "Vector Multiplication", "Vector Magnitude", "Dot Product", "Dot Product (Self)", "Cross Product", "Angle"]
functions = ["vectors.add_vectors()", "vectors.subtract_vectors()", "vectors.scale_vector()", " " , "vectors.modulus()", "vectors.dot_product()", "vectors.dot_product_self()", " ", "vectors.angle()"]

def masterprogram():
    print("Choose an option:")
    for option in range(len(options)): print(str(option + 1) + '. ' + options[option])
    option = int(input("Option: ")) - 1
    print(eval(functions[option]), 2)
    return

if __name__ == "__main__":
    while True:
        masterprogram()
        ext = input("Do you want to continue? [Y/n]: ").lower()
        if ext == 'n': exit(0)