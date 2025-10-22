def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectArea(PWidth, PHeight) -> float:
    Area = PWidth * PHeight
    return float(Area)


def main() -> None:
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectArea(Width, Height)
    print("")
    print(f"Area is {Area}²")
    print("program ending.")
    return None

main()