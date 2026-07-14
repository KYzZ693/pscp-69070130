'''main'''
def main():
    '''main'''
    temp = float(input())
    type_ = input()
    chance_to = input()
    new_temp = 0
    if type_ == "C":
        if chance_to == "C":
            new_temp = temp
        elif chance_to == "F":
            new_temp = (temp * 9/5) + 32
        elif chance_to == "K":
            new_temp = temp + 273.15
        elif chance_to == "R":
            new_temp = (temp + 273.15) * 9/5
    elif type_ == "F":
        new_temp = farenheit(temp, chance_to)
    elif type_ == "K":
        new_temp = kelvin(temp, chance_to)
    elif type_ == "R":
        new_temp = rankine(temp, chance_to)
    print(f"{new_temp:.2f}")
def farenheit(temp, chance_to,new_temp=0):
    '''farenheit'''
    c = (temp - 32) * 5/9
    if chance_to == "C":
        new_temp = c
    elif chance_to == "F":
        new_temp = temp
    elif chance_to == "K":
        new_temp = c + 273.15
    elif chance_to == "R":
        new_temp = (c + 273.15) * 9/5
    return new_temp
def kelvin(temp, chance_to,new_temp=0):
    '''kelvin'''
    c = temp - 273.15
    if chance_to == "C":
        new_temp = c
    elif chance_to == "F":
        new_temp = (c * 9/5) + 32
    elif chance_to == "K":
        new_temp = temp
    elif chance_to == "R":
        new_temp = (c + 273.15) * 9/5
    return new_temp
def rankine(temp, chance_to,new_temp=0):
    '''rankine'''
    c = (temp - 491.67) * 5/9
    if chance_to == "C":
        new_temp = c
    elif chance_to == "F":
        new_temp = (c * 9/5) + 32
    elif chance_to == "K":
        new_temp = c + 273.15
    elif chance_to == "R":
        new_temp = temp
    return new_temp
main()
