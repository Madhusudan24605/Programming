print("Program starting.\n")

pointstart = int(input("Insert starting point: "))
pointstop = int(input("Insert stopping point: "))
pointinspect = int(input("Insert inspection point: "))

run = True

if pointstart >= pointstop:
    print("starting point value must be less than stopping point value.")

    run = False

if ((pointstart > pointinspect) or (pointinspect > pointstop)):
    print("inspection point value must be within the range of start and stop.)")
    run = False
    
if run:
    print("\nFirst loop - inspection with break:")
    for i in range(pointstart, pointstop):
        if i == pointinspect:
            break
        else:
            print(i, end=' ')
        
    print("\nSecond loop - inspection with continue:")
    for i in range(pointstart, pointstop):
        if i == pointinspect:
            continue
        else:
            print(i, end=' ')
            
print("\n\nProgram ending.")