print("Program starting.")
feed = int(input("Insert a positive integer: "))
sequences = [feed]  # Use a list to store the sequence
step = 0

while feed != 1:
    if feed % 2 == 0:
        feed = feed // 2
    else:
        feed = (feed * 3) + 1
    sequences.append(feed)
    step += 1

print(' -> '.join(str(num) for num in sequences))
print(f"Sequence had {step} total steps.\n")
print("Program ending.")
print("Program ending.")
