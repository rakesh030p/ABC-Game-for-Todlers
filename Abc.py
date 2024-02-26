list=[   'Apple',
      'Ball',
    'Cat',
    'Dog',
    'Elephant',
    'Fox',
    'Giraff',
    'House',
    'Ink',
    'jungle',
    'kite',
    'Lemon',
    'Monkey',
    'Nose',
    'Orange',
    'Pilot',
    'Queen',
    'Rakesh',
    'Snake',
    'Tomato',
    'Umbrella',
    'Vampire',
    'Water',
    'Xerox',
    'Youtube',
    'Zebra']
print(list)
alphabet=input("Enter the alphabet from (a-z)or (A-Z)")
for alphabets in list:
    alpha=alphabet.lower()
    str=alphabets[0]
    str1=str.lower()
    # print(str1)
    if(str1==alpha):
        print(f"{alphabets}")
        
    else:
        # print("Enter the correct alpabet")
        # break
        pass
if(len(alphabet)>1):
    print("Plz write the correct alphabet:")
elif(alphabet>='1' and alphabet<='9'):
    print("plz write alphabet form a-z or A-Z")