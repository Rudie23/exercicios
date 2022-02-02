number_1 = 100
number_2 = 20035
number_3 = 150

if number_1 > number_2 and number_3:
    print(f'{number_1} é o maior número')
elif number_2 > number_1 and number_3:
    print(f'{number_2} é o maior número')
elif number_3 > number_1 and number_2:
    print(f'{number_3} é o maior número')

if number_1 < number_2 and number_3:
    print(f'{number_1} é o menor número')
elif number_2 < number_1 and number_3:
    print(f'{number_2} é o menor número')
elif number_3 < number_1 and number_2:
    print(f'{number_3} é o menor número')