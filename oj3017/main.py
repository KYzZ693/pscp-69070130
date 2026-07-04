'''main'''
def main():
    '''main'''
    price = int(input())
    total = price
    if price*0.1 <= 50 :
        total += 50
    elif price*0.1 >= 1000:
        total += 1000
    else:
        total += price*0.1
    print(f"{total + (total*0.07):.2f}")
main()
