# Nested loops= The "inner loop" will finish all of it's iterations before finishing one
# iterations of the "outer loop"
row = int(input('How many rows do you want'))
column = int(input('How many columns do you want'))
symbol = input('Enter a symbol you want to use')
for i in range(row):
    for j in range(column):
        print(symbol, end='')
    print()