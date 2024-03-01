# Loop Control Statements = Change a loops execution from its normal sequence

# Break = Used to terminate the loop entirely
# Continue = Skips to the next iteration of the loop.
# pass = does nothing, acts as a placeholder

while True:
    name= input('Enter you name')
    if name != "":
        break
phone_number = '0332-197-1624'
for i in phone_number:
    if i =='-':
        continue
    print(i,end='')
for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)

