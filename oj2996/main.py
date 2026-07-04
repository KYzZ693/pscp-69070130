'''main'''
def main():
    '''main'''
    text = input().lower()
    revers = ""
    for t in range(4,-1,-1):
        revers+=text[t]
    print(revers)
main()
