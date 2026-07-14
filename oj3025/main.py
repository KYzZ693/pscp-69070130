'''main'''
def main():
    '''main'''
    winter = [1,2,3]
    spring = [4,5,6]
    summer = [7,8,9]
    fall = [10,11,12]
    month = int(input())
    day = int(input())
    if month in winter:
        if day >= 21 and not month % 3:
            print("spring")
        else:
            print("winter")
    elif month in spring:
        if day >= 21 and not month % 3:
            print("summer")
        else:
            print("spring")
    elif month in summer:
        if day >= 21 and not month % 3:
            print("fall")
        else:
            print("summer")
    elif month in fall:
        if day >= 21 and not month % 3:
            print("winter")
        else:
            print("fall")
main()
