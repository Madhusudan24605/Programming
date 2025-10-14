print("Program starting.\n")
print("Check multiplicative persistence.")
number = input("Insert an integer: ")

step = 0

while len(number) > 1:
    digits = [int(d) for d in number]
    product = 1
    for d in digits:
        product *= d
    print(f"{' * '.join(str(d) for d in digits)} = {product}")
    number = str(product)
    step += 1
print("No more steps.\n")
print(f"This program took {step} step(s)\n")
print("Program ending.")
