tuple=[   'Apple',
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
for alphabets in tuple:
    alphabet=input("Enter the alphabet from (a-z)or (A-Z)")
    alpha=alphabet.lower()
    str=alphabets[0]
    str1=str.lower()
    print(str1)
    if(str1==alpha):
        print(f"{alphabets}")
    else:
        print("Enter the correct alpabet")
        break