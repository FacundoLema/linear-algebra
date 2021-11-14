from math import sqrt, degrees
from numpy import add, subtract, multiply, arccos

def add_vectors():
    vectors = int(input("How many vectors do you want to add together? "))
    if vectors < 2: exit("At least two vectors are needed to perform additon")
    print("Write each vector coordinate separated by a comma")
    print("All vectors should have the same dimension and they should be, at least, bi-dimensional")
    vector = []; vecsum = ()
    for i in range(vectors): vector.append(tuple(int(x) for x in (str(input("Vector %i: " %(i+1))).split(","))))
    for i in range(len(vector[0])): vecsum = vecsum + (0,)
    for i in range(vectors): vecsum = tuple(add(vector[i], vecsum))
    return vecsum

def subtract_vectors():
    print("Write each vector coordinate separated by a comma")
    print("All vectors should have the same dimension and they should be, at least, bi-dimensional")
    vector = []
    for i in range(2): vector.append(tuple(int(x) for x in (str(input("Vector %i: " %(i+1))).split(","))))
    vecsub = tuple(subtract(vector[0], vector[1]))
    return vecsub

def scale_vector():
    print("Write each vector coordinate separated by a comma")
    print("All vectors should have the same dimension and they should be, at least, bi-dimensional")
    vector = tuple(int(x) for x in (str(input("Vector: ")).split(","))); scalar = int(input("Scalar: "))
    scaled = tuple(multiply(vector, scalar))
    return scaled

def dot_product():
    print("Write each vector coordinate separated by a comma")
    print("All vectors should have the same dimension and they should be, at least, bi-dimensional")
    vector = []; product = 0
    for i in range(2): vector.append(tuple(int(x) for x in (str(input("Vector %i: " %(i+1))).split(","))))
    for i in range(len(vector[0])): product += (vector[0][i] * vector[1][i])
    return product

def dot_product_self():
    print("Write each vector coordinate separated by a comma")
    vector = tuple(int(x) for x in (str(input("Vector: ")).split(","))); product = 0
    for elem in vector: product += (elem * elem)
    return product

def modulus():
    print("Write each vector coordinate separated by a comma")
    vector = tuple(int(x) for x in (str(input("Vector: ")).split(","))); modulus = 0
    for elem in vector: modulus += (elem * elem)
    return sqrt(modulus)

def angle():
    product = dot_product()
    modulus1 = modulus()
    modulus2 = modulus()
    angle = arccos(product / (modulus1 * modulus2))
    return degrees(angle)