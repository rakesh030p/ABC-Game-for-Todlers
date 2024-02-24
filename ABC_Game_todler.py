
dicta={
    'a':'Apple',
    'b':'Ball',
    'c':'Cat',
    'd':'Dog',
    'e':'Elephant',
    'f':'Fox',
    'g':'Giraff',
    'h':'House',
    'i':'Ink',
    'j':'jungle',
    'k':'kite',
    'l':'Lemon',
    'm':'Monkey',
    'n':'Nose',
    'o':'Orange',
    'p':'Pilot',
    'q':'Queen',
    'r':'Rakesh',
    's':'Snake',
    't':'Tomato',
    'u':'Umbrella',
    'v':'Vampire',
    'w':'Water',
    'x':'Xerox',
    'y':'Youtube',
    'z':'Zebra',
}
''' Takes the input fomr the user and play this game and learn the basic english alphabet!!!'''
print("Welcome to ABC Game \n"
         "or quit the game ")

alphabet=""
while(alphabet!='quit'):
    alphabet=input("Enther the character from (a-z)or(AtoZ):")
    alphabet=alphabet.lower()
    if(len(alphabet)==1):
        if(alphabet>='a' and alphabet<='z'):
            print(f"{alphabet.upper()} for {dicta[alphabet]}")
        else:
            print("Enter the alphabet either (a-z)or(A-Z)")
    else:
        print("enter the only characters")
        