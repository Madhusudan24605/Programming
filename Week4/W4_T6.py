print("Program starting.")
feed = int(input("Insert a positive integer: "))
sequences = feed
step = 0

while feed != 1:
    if feed % 2 == 0:
        feed = feed // 2
    else:
        feed = (feed * 3) + 1
    sequences = sequences, feed
    step += 1
print(' -> '.join(str(feed) for feed in sequences))
print(f"Sequence had {step} steps.")
print("\n\nProgram ending.")
