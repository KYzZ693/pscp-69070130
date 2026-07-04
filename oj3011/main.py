'''main'''
def main():
    '''main'''
    color1 = input()
    color2 = input()
    green = ["Yellow", "Blue"]
    orange = ["Red", "Yellow"]
    violet = ["Red", "Blue"]
    if color1 == color2 and color1 in ('Red', 'Blue', 'Yellow'):
        print(color1)
    elif color1 == color2 and color1 not in ('Red', 'Blue', 'Yellow'):
        print("Error")
    elif color1 in green and color2 in green:
        print("Green")
    elif color1 in orange and color2 in orange:
        print("Orange")
    elif color1 in violet and color2 in violet:
        print("Violet")
    else:
        print("Error")
main()
