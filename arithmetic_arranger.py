def arithmetic_arranger(ari_problems, answer=False):
    #Spliting each expression into a list
    big_list = list()
    list_for_join = list()
    list_j = list()
    for index, element in enumerate(ari_problems):
        n1 = ari_problems[index].split(' ')
        big_list.append(n1)
    #ERROS spotting
    if len(ari_problems) > 5:
        return 'Error: Too many problems.'
    for v in range(len(big_list)):
        if big_list[v][0].isnumeric() is False or big_list[v][2].isnumeric() is False:
            return 'Error: Numbers must only contain digits.'
        if big_list[v][1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        if len(big_list[v][0]) > 4 or len(big_list[v][2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'


    #Print the TOP line of Operands
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        list_j.append(f'{big_list[v][0]:>{size+2}}    ')
    list_for_join.append(''.join(list_j[:]))
    list_j.clear()

    # Print the Operators and BOTTOM line of Operands
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        list_j.append(f'{big_list[v][1]:<} {big_list[v][2]:>{size}}    ')
    list_for_join.append(''.join(list_j[:]))
    list_j.clear()

    # Print the Dashes
    for v in range(len(big_list)):
        if len(big_list[v][0]) > len(big_list[v][2]):
            size = len(big_list[v][0])
        else:
            size = len(big_list[v][2])
        list_j.append(f'{"-"*(size+2)}    ')
    list_for_join.append(''.join(list_j[:]))
    list_j.clear()

    # Print Results
    if answer is True:
        for v in range(len(big_list)):
            if len(big_list[v][0]) > len(big_list[v][2]):
                size = len(big_list[v][0])
            else:
                size = len(big_list[v][2])
            if big_list[v][1] == '+':
                sum = int(big_list[v][0]) + int(big_list[v][2])
                list_j.append(f'{sum:>{size+2}}    ')
            elif big_list[v][1] == '-':
                minus = int(big_list[v][0]) - int(big_list[v][2])
                list_j.append(f'{minus:>{size+2}}    ')
        list_for_join.append(''.join(list_j[:]))
        list_j.clear()

    stripped = list(map(str.rstrip, list_for_join))

    ans_str = '\n'.join(stripped)
    return ans_str





print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print()
print(arithmetic_arranger(['32 - 698', '1 + 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print()
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))