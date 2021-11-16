import vectors
options = { "Vector addition": "add_vectors()", 
            "Vector subtraction": "subtract_vectors()", 
            "Vector Scaling": "scale_vector()", 
            "Vector Multiplication": "Nothing here", 
            "Vector Magnitude": "modulus()", 
            "Dot Product": "dot_product()", 
            "Dot Product (Self)": "dot_product_self()", 
            "Cross Product": "Nothing here", 
            "Angle": "angle()"}

def masterprogram():
    print("Choose an option:"); i = 1
    for option in options:
        print(str(i) + '. ' + option); i += 1
    option = int(input("Option: ")) - 1
    options_list = list(options)
    print(eval(f"vectors.{options[options_list[option]]}"))
    return

if __name__ == "__main__":
    while True:
        masterprogram()
        ext = input("Do you want to continue? [Y/n]: ").lower()
        if ext == 'n': exit(0)