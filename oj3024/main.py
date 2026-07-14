'''main'''
def main():
    '''main'''
    total = float(input())
    highest = float(input())
    lowest = 0
    total -= highest
    for i in range(101):
        for j in range(101):
            if i/10.0 + j/10.0 == total:
                #print(f"{i/10.0} + {j/10.0} = {total}")
                if i/10.0 > j/10.0 and total - j/10.0 <= highest:
                    lowest = j/10.0
                    #print(lowest)
                elif j/10.0 > i/10.0 and total - i/10.0 <= highest:
                    lowest = i/10.0
                    #print(lowest)
                else:
                    lowest = total - highest
                    #print(lowest)
    #print(f"highest: {highest}, lowest: {lowest}")
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
