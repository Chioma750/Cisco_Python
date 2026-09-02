x = float(input("Enter value for x: "))

layer_1 = 1 / x
layer_2 = 1 / (x + layer_1)
layer_3 = 1 / (x + layer_2)
y = 1 / (x + layer_3)

print("y =", y)

# Test Data

# Sample input: 1
# Expected output: y = 0.6000000000000001

# Sample input: 10
# Expected output: y = 0.09901951266867294

# Sample input: 100
# Expected output: y = 0.009999000199950014

# Sample input: -5
# Expected output: y = -0.19258202567760344
