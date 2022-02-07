def arithmetic_arranger(ari_problems, answer=False):
    #Spliting each expression into a list
    big_list = []
    for index, element in enumerate(ari_problems):
        n1 = ari_problems[index].split(' ')
        big_list.append(n1)
    #ERROS spotting
    if len(ari_problems) > 5:
        print('Error: Too many problems.')
        quit()
    for v in range(len(big_list)):
        if big_list[v][0].isnumeric() is False or big_list[v][2].isnumeric() is False:
            print('Error: Numbers must only contain digits')
            quit()
        if big_list[v][1] in '/*':
            print('Error: Operator must be "+" or "-"')
            quit()
        if len(big_list[v][0]) > 4 or len(big_list[v][2]) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
    #Print the TOP line of Operands
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        print(f'{big_list[v][0]:>{size+2}}', end=' '*4)
    print()
    # Print the Operators and BOTTOM line of Operands
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        print(f'{big_list[v][1]:<} {big_list[v][2]:>{size}}', end=' '*4)
    print()
    # Print the Dashes
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        print("-"*(size+2), end=' '*4)
    print()
    # Print Results
    if answer is True:
        for v in range(len(big_list)):
            if len(big_list[v][0]) > len(big_list[v][2]):
                size = len(big_list[v][0])
            else:
                size = len(big_list[v][2])
            if big_list[v][1] == '+':
                sum = int(big_list[v][0]) + int(big_list[v][2])
                print(f'{sum:>{size+2}}', end=' '*4)
            elif big_list[v][1] == '-':
                minus = int(big_list[v][0]) - int(big_list[v][2])
                print(f'{minus:>{size+2}}', end=' '*4)




arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
print()
print()

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

print()
print()
arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True)
