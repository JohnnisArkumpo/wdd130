# Database of different code segments to save space
# ordered by: Finished projects, code bits, current projects
# Machine at bottom


# projects
def rpg_code():
    # The Great Adventure
    errr = "\nsince you didn't choose a valid option, you spend the rest of eternity in the same spot. Restart the program and please input one of the valid options"
    name = input("What's your characters name? ")
    print("You groggily wake up to your alarm, and get ready for another day at work.")
    fdecision = input(f"\nAs you head to the door, you see a HANDGUN and your BRIEFCASE, which one do you bring with you? \n")
    sdecision = input(f"\nAs you walk to work with your {fdecision.lower()}, you hear screams in the alleyway to your left. Do you go LEFT or CONTINUE? \n")
    if sdecision.lower() == 'left':
        print(f"\nAs you walk into the alley, tightly clutching your {fdecision.lower()}, you see two masked figures in a knife fight")
        tdecision = input(f"\ndo you try and STOP THEM, or turn and RUN? \n")
        if tdecision.lower() == 'stop them':
            if fdecision.lower() == 'handgun':
                print(f"\nBoth masked figures stop and stare at you holding your pistol, and lower their knives. ")
                print(f"\nThe masked figure on the right says 'Please don't shoot, I'm here for an acting gig and this guy tried to mug me!' ")
                print(f"\nThe masked figure on the left doesn't say anything, as it appears he is struggling to breathe.")
                frdecision = input(f"\nNow do you shoot the man on the RIGHT, the man on the LEFT, or call the POLICE? \n")
                if frdecision.lower() == 'right':
                    print("\nThe man on the right falls dead, and the man on the left runs at you with his knife.")
                    print("\nBefore you can react, you're on the floor in a pool of your blood. The end.")
                elif frdecision.lower() == 'left':
                    print("\nThe man on the left deflates, and the man on the right thanks you, then he lifts up a pen, and you see a bright flash of light.")
                    print("\nYou wake up in your bed, not remembering anything that happened. The end")
                elif frdecision.lower() == 'police':
                    print("\nYou remember there are no police in the area, and after a good laugh, all three of you go to subway. The end")
                else:
                    print(errr)
            elif fdecision.lower() == 'briefcase':
                print(f"\nThe man on the left looks up at you with a wild look in his eyes, and while he's distracted the man on the right stabs him in the chest")
                print(f"\nThe man on the left lets out a scream like the first one you heard, and the other man comes running at you with a knife")
                frdecision = input(f"\ndo you try to BLOCK the knife with your briefcase, or do you RUN? \n")
                if frdecision.lower() == 'block':
                    print("\nThe knife enters through the briefcase, and acid sprays out the hole, causing your attacker to fall over and die. The end")
                elif frdecision.lower() == 'run':
                    print("\nYou slip, fall, and die. The end")
                else:
                    print(errr)
            else:
                print(errr)
        elif tdecision.lower() == 'run':
            print(f"\nAs you turn and run with your {fdecision.lower} in you hand, you hear footsteps pounding behind you.")
            if fdecision.lower() == 'handgun':
                frdecision = input("\nDo you turn around and SHOOT, or do you RUN FASTER? \n")
                if frdecision.lower() == 'shoot':
                    print("\nYou shoot a foam dart out of your nerf gun, which hits the face of a 8 foot purple man. The end")
                elif frdecision.lower() == 'run faster':
                    print("\nYou run fast enough that you end up in south america, where you begin a new life. The end")
                else:
                    print(errr)
            elif fdecision.lower() == 'briefcase':
                print("\nYou get to the end of the alley, but you still hear someone running behind you.")
                frdecision = input("\nDo you DROP you briefcase, or do you THROW it behind you?\n")
                if frdecision.lower() == 'drop':
                    print("\nYou hear a man fall behind you, and you keep on running, not looking back. You get to work considerably rattled, but safe. The end")
                elif frdecision.lower() == 'throw':
                    print("\nThe man catches it and runs away. You are now very confused. The end")
                else:
                    print(errr)
            else:
                print(errr)
        else:
            print(errr)
    elif sdecision.lower() == 'continue':
        print(f"\nAs you know it is a dangerous city, you choose to just continue walking to work")
        print(f"\nYou arrive at work holding your {fdecision.lower()} and mumble a greeting to the man at the front desk")
        if fdecision.lower() == 'handgun':
            print("\nHe looks at you in shock and yells 'We have a shooter! Everyone down!'")
            tdecision = input("\nDo you try to EXPLAIN, do you RUN, or do you SHOOT? \n")
            if tdecision.lower() == 'explain':
                print("\nAs you try to explain why you brought a handgun to work, you realize that you don't even know why you brought it. ")
                print("\nYou drop the gun as security handcuffs you. The end.")
            elif tdecision.lower() == 'run':
                print("\nYou turn and run right into the security guard who hits you on the head with the butt of his pistol")
                print("\nAs you black out, you realize that you probably shouldn't have brought a gun to work. The end")
            elif tdecision.lower() == 'shoot':
                print("\nAfter emptying the clip, the realization of what you just did settles in, and you leave running, to never return. The end")
            else:
                print(errr)
        elif fdecision.lower() == 'briefcase':
            print(f"\nHe says 'Hey {name.title()}, the boss wants to talk to you'")
            tdecision = input(f"\nDo you go to your OFFICE first, or do you head straight up to your BOSS? \n")
            if tdecision.lower() == 'office':
                print("\nOnce you get to your desk, you see a note on it.")
                print("\nOnce you read it, you realize it's a promotion. You happily set your things down and go to see the boss. The end.")
            elif tdecision.lower() == 'boss':
                print("\nOnce you get to the boss's office, you open the door to see the room full of baloons")
                print("\nA coworker motions you over, and tells you today is the boss's birthday, and they were going to surprise him, but they don't have a cake")
                print("\nYou open up your briefcase and take out a cake. The end")
            else:
                print(errr)
        else:
            print(errr)
    else:
        print(errr)
def wordle_code():
    import random
    play = True
    wchoice = True
    guessw = '      '
    words = ['Fights', 'Random', 'Russia', 'Orange', 'Mormon', 'Papers']
    guessc = 0
    while play == True:
        if wchoice:
            wcnum = random.randint(0,5)
            seword = words[wcnum]
            wchoice = False
        print('Welcome to the word guessing game!\n')
        
        while guessw.title() != seword:
            guessc += 1
            
            if len(guessw) != len(seword):
                print('Sorry, the guess must have the same number of letters as the secret word.')
            else:
                print(f'Your hint is ', end='')
                # for (i, lettera), (j, letterb) in zip(enumerate(seword), enumerate(guessw)):
                #     if lettera == letterb and i == j:
                #         print(letterb.upper(), end='')
                #     elif lettera == letterb:
                #         print(letterb.lower(), end='')
                #     else:
                #         print('_ ', end='')
                # # I was making this a lot more complicated than it needed to be...
                for i, lettera in enumerate(seword):
                    if guessw[i].upper() == lettera.upper():
                        print(lettera.upper(), end='')
                    elif guessw[i].upper() in seword.upper():
                        print(guessw[i].lower(), end='')
                    else:
                        print('_', end=' ')
            
            print()
            guessw = input('What is your guess? ')
        
        print(f'Congratulations, you won! it took you {guessc} guesses\n')
        pa = input("Would you like to play again? (Y/N) ")
        if pa.upper() == 'Y':
            play = True
            wchoice = True
            guessw = ''
            guessc = 0
        else:
            play = False
            print('\nThank you for playing!\n')
def madlib_code():
    def madlib():
        print(f'The other day, I was really in trouble. '
        f'It all started when I saw a very {adjone.lower()} {animone.lower()} {verone.lower()} down the hallway of the {place.lower()}. '
        f'"{exclone.title()}!" I yelled, causing my {person.lower()} to {vertwo.lower()}. '
        f'Everyone looked at me in disbelief as I {verthree.lower()} over and over. '
        f'Just when things seemed {adjtwo.lower()}, {event.lower()} happened, making everyone {verfour.lower()} in shock. '
        f'Miraculously, that distracted the {adjone.lower()} {animone.lower()}, giving everyone time to {verfive.lower()} to safety.')

    print("Please enter the following: ")
    event = input("Random event: ")
    animone = input("Animal: ")
    exclone = input("Exclamation: ")
    place = input("Location: ")
    person = input("Family member (Mom, Dad, Brother etc.): ")
    verone = input("Verb: ")
    vertwo = input("Verb: ")
    verthree = input("Verb in past tense: ")
    verfour = input("Verb: ")
    verfive = input("Verb: ")
    adjone = input("Adjective: ")
    adjtwo = input("Adjective: ")

    madlib()
def pricecalc_code():
    def mealcalc():
        print(f"\nSubtotal: ${subtotal:0.2f}")
        print(f"Sales tax: ${salestax:0.2f}")
        print(f"Total: ${totalprice:0.2f}")

    # welcome message
    print("This is your restaurant price calculator. Please enter the following values: \n")

    # variables
    kmeal = float(input("What is the price of a kid's meal? $"))
    ameal = float(input("What is the price of an adult's meal? $"))
    nkids = int(input("How many children are eating here today? "))
    nadults = int(input("How many adults are eating here today? "))
    staxrate = float(input("What is the sales tax here? "))

    # calculations
    subtotal = kmeal*nkids+ameal*nadults
    salestax = subtotal*staxrate/100
    totalprice = subtotal+salestax

    mealcalc()

    # payment/tip amount
    tipamt = float(input("\nWhat percent would you like to tip? "))
    totalprice = totalprice*(tipamt/100)+totalprice
    print(f"Total after tip: ${totalprice:0.2f}")
    payamt = float(input("\nWhat is the payment amount? $"))
    print(f"Change: ${payamt-totalprice:0.2f}")
    print("\nThank you for using the meal price calculator!")
def cartcalc_code():
    print('Welcome to the shopping cart program!\n')

    choice = 0
    cart = []
    cprice = []
    while choice != 5:
        print('Please select one of the following:\n1. Add Item\n2. View cart\n3. Remove Item\n4. Compute total\n5. Quit')
        choice = int(input('Please enter an action: '))
        if choice == 1:
            item = input('What item would you like to add? ')
            price = float(input(f'What is the price of "{item}"? '))
            print(f"'{item}' has been added to the cart.\n")
            cart.append(item)
            cprice.append(price)
            print()
        elif choice == 2:
            print('The contents of the shopping cart are: ')
            i = 0
            while i < len(cart):
                print(f'{i+1}. {cart[i]} - ${cprice[i]}')
                i += 1
            print()
        elif choice == 3:
            rmv = int(input('Which item would you like to remove? '))
            cart.pop(rmv-1)
            cprice.pop(rmv-1)
            print('Item removed')
            print()
        elif choice == 4:
            mon = 0
            j = 0
            while j < len(cprice):
                mon += cprice[j]
                j += 1
            print(f'You have {len(cart)} items in your cart')
            print(f'The total price of the items in the shopping cart is ${mon}')
            print()
        else:
            print('Thank you, goodbye.')
def scripture_code():
    # ICE

    bchoice = input('What book would you like to see? ')
    cmax = 0
    chm = None
    with open('books_and_chapters.txt') as file:
        for i in file:
            i = i.strip()
            line = i.split(":")
            if line[2].upper() == bchoice.upper():
                b = line[0]
                c = line[1]
                t = line[2]
                c = int(c)
                print(f'Scripture: {t}, Book: {b}, Chapters: {c}')
                if cmax < c:
                        cmax = c
                        chm  = b
    print(f'\nThe book with the most chapters in the {bchoice.title()} is {chm}, with {cmax} chapters\n')
def areacalc_code():
    def compute_area(n,x,y):
        if n == 1 or n == 2:
            if x == y:
                nm = 'square'
                prs = f'length {x}'
            else:
                nm = 'rectangle'
                prs = f'lengths {x}cm and {y}'
            print(f"The area of a {nm} with sides of {prs}cm is {x*y}cm\u00B2, or {(x*y)/10000}m\u00B2")
        elif n == 3:
            print(f"The area of a circle with a radius of {x}cm is {round(math.pi*x**2,3)}cm\u00B2, or {round((math.pi*x**2)/10000,5)}m\u00B2")

    import math
    shapesk = 99
    print('welcome to the shape calculator!')
    while shapesk != 0:
        shapesk = int(input('What shape would you like to calculate? \n1. square\n2. rectangle\n3. circle\n\nType 0 to quit\n'))
        print()
        if shapesk == 0:
            print('Thank you for using shape calculator!')
        elif shapesk == 1:
            sidel = int(input('What length (in cm) would you like the side of the square to be? '))
            print()
            compute_area(shapesk, sidel, sidel)
        elif shapesk == 2:
            sideh = int(input('What length (in cm) would you like the height of the rectangle to be? '))
            sidew = int(input('What length (in cm) would you like the width of the rectangle to be? '))
            print()
            compute_area(shapesk, sideh, sidew)
        elif shapesk == 3:
            radiusl = int(input('What length (in cm) would you like the radius of the circle to be? '))
            print()
            compute_area(shapesk, radiusl, None)
        else:
            print('bruh')
        print()
def wchill_code():
    # final project
    # functions
    def ctof(t):
        far = (t*9/5) + 32
        return far
    def wchill(t, v):
        w = 35.74+0.6215*t-35.75*(v**0.16)+0.4275*t*(v**0.16)
        return w

    tempr = int(input('What is the temperature? '))
    print()
    foc  = input('Fahrenheit or Celsius (F/C)? ')
    print()

    if foc.upper() == 'C':
        tempr = ctof(tempr)

    windspeed = 5

    while windspeed <= 60:
        print(f'At temperature {tempr}.0F and wind speed {windspeed} mph, the windchill is {round(wchill(tempr, windspeed),2)}F')
        windspeed += 5

# code bits
def enum_codebit():
    # wrd = 'commitment'
    # fletter = input("\nWhat is your favorite letter? \n")
    # for i in wrd:
    #     if fletter.lower() == i.lower():
    #         # print(i.upper(), end='')
    #         print('_', end='')
    #     else:
    #         print(i.lower(), end='')
    # print()


    # play = True
    # quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
    # while play:
    #    num = int(input('\nPick a number: '))
    #     ct = 0
    #     print()
    #     for i in quote:
    #         ct += 1
    #         if ct == num:
    #             print(i.upper(), end='')
    #             ct = 0
    #         else:
    #             print(i.lower(), end='')
    #     print()
    #     redo = input('Would you like to play again? (Y/N) ')
    #     if redo.upper() == 'Y':
    #         play = True
    #     else:
    #         play = False

    num = int(input('\nPick a number: '))
    quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

    for i, letter in enumerate(quote):
        if i%num == 0:
            print(letter.upper(), end='')
        else:
            print(letter.lower(), end='')
    print()
def numguess_codebit():
    import random

    gcount = 0
    mgs = 1
    mnum = 2

    print("Welcome to the guessing game!\nTry to guess what number I'm thinking.")

    while mgs != mnum:
        if gcount == 0:
            mnum = random.randint(2,52)
        mgs = int(input("\nType your guess here: "))
        gcount += 1
        if mgs > mnum:
            print("Lower")
        elif mgs < mnum:
            print("Higher")
        else:
            print("\nCorrect!")
            print(f"\nIt took {gcount} guesses for you to guess correctly")
            restart = input("\nWould you like to play again? (Y/N): ")
            if restart.upper() == 'Y':
                mgs = 1
                gcount = 0
            else:
                print("\nThanks for playing!\n")
def gradecalc_codebit():
    grade = int(input("What's your grade? "))

    remaind = grade%10

    letterg = 'A'

    letters = ''

    word = 'a'

    if grade >= 90:
        letterg = 'A'
        word = 'an'
    elif grade >= 80:
        letterg = 'B'
    elif grade >= 70:
        letterg = 'C'
    elif grade >= 60:
        letterg = 'D'
    else:
        letterg = 'F'
        word = 'an'

    if letterg != 'F':
        if remaind >= 7:
            if letterg != 'A':
                letters = '+'
        elif remaind > 3:
            letters = ''
        else:
            letters = '-'

    print(f"\nYour grade is {word} {letterg}{letters}")

    if grade >= 70:
        print(f"\nYou passed the class! Congratulations!")
    else:
        print(f"\nUnfortunately, you did not pass the class. Better luck next time!")
def areacalc_codebit():
    # def areacalc():
    #     print(f"The area of the square is {squarel*squarel}")
    #     print(f"The area of the rectangle is {rect1*rect2}")
    #     print(f"The area of the circle is {circr*circr*math.pi}")
    # import math
    # squarel = float(input("What is the length of one side of your square? "))
    # rect1 = float(input("what is the length of the bottom of the rectangle? "))
    # rect2 = float(input("What is the length of one of the sides of the rectangle? "))
    # circr = float(input("What is the length of the radius of the circle? "))
    # areacalc()

    def areacalc():
        print(f"The area of a square with sides of a length {sidel}cm is {sidel**2}cm\u00B2, or {(sidel**2)/10000}m\u00B2")
        print(f"The area of a circle with a radius of {sidel}cm is {math.pi*sidel**2}cm\u00B2, or {(math.pi*sidel**2)/10000}m\u00B2")
        print(f"The volume of a cube with sides of a length {sidel}cm is {sidel**3}cm\u00B3, or {(sidel**3)/10000}m\u00B3")
        print(f"The area of a sphere with a radius of {sidel}cm is {math.pi*(4/3)*sidel**3}cm\u00B3, or {(math.pi*(4/3)*sidel**3)/10000}m\u00B3")
    import math
    sidel = float(input("Type a length in centimeters here: "))
    areacalc()
def math_codebit():
    import math
    def equate():
        print(f"\nThe inner value of c is: {round(c,3)}")
        print(f"The velocity after {t} seconds is: {calcc} m/s")
        print(f"The terminal velocity of the object is {terminalv}")

    print("Welcome to the velocity calculator. Please enter the following")
    m = float(input("\nMass (in kg): "))
    g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
    t = float(input("Time (In seconds): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    A = float(input("Cross sectional area (in m^2): "))
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
    cra = math.pi*float(input("Radius of sphere (in meters): "))**2

    c = (1/2)*p*A*C
    calcc = round(math.sqrt(m*g/c)*(1 - math.exp((-math.sqrt(m*g*c)/m)*t)),3)
    terminalv = round(math.sqrt(m*g/c),3)
    equate()
def ride_codebit():
    age = int(input("What is the age of the first rider? "))
    hit = int(input("What is the height of the first rider? (in inches) "))
    sec = input("Is there a second rider? (Y/N) ")
    if age >= 12 and age <= 18:
        thold = input("Do you have a golden ticket? (Y/N) ")
        if thold.upper() == 'Y':
            age = 18

    if sec.upper() == 'Y':
        age2 = int(input("What is the age of the second rider? "))
        hit2 = int(input("What is the height of the second rider? (in inches) "))
        if hit < 36 or hit2 < 36:
            canride = False
        elif age >= 18 or age2 >= 18:
            canride = True
        elif age >= 16 or age2 >= 16 and age >= 14 or age2 >= 14:
            canride = True
        elif age >= 12 and age2 >= 12 and hit >= 52 and hit2 >= 52:
            canride = True
        else:
            canride = False
    else:
        if hit >= 62 and age >= 18:
            canride = True
        else:
            canride = False


    if canride:
        print("Welcome to the ride!")
    else:
        print("Sorry, you cannot ride")
def numberavg_codebit():
    # Team activity
    print('Type a list of numbers, type 0 when finished.\n')
    numbers = []
    pnum = []
    inp = ''
    sumn = 0
    while inp != 0:
        inp = int(input('Enter Number: '))
        numbers.append(inp)
    for i in numbers:
        sumn += i
        if i > 0:
            pnum.append(i)
    numbers.sort()
    print(f'The sum is: {sumn}')
    print(f'The average is: {sumn/(len(numbers)-1)}')
    print(f'The largest number is: {max(numbers)}')
    print(f'The smallest positive number is: {min(pnum)}')
    print('The sorted list is: ')
    for i in numbers:
        print(i)
def embdata_codebit():
    with open("hr_system.txt") as fl:
        for i in fl:
            lins = i.strip()
            lines = lins.split()
            n = lines[0]
            d = lines[1]
            t = lines[2]
            s  = lines[3]
            ss = float(s)/24
            if t.upper() == 'ENGINEER':
                ss += 1000
            print(f'{n} (ID: {d}), {t} - ${ss:.2f}')
def calories_codebit():
    max_cals = 0
    min_yr = 9999
    max_food = None
    min_food = None
    with open('file.csv') as file:
        header = file.readline()
        for line in file:
            line = line.strip()
            parts = line.split(',')
            nfood = parts[0]
            ncals = int(parts[2].strip())
            if max_cals < ncals:
                max_cals = ncals
                max_food = nfood
            if min_yr > ncals:
                min_yr = ncals
                min_food = nfood
    print(f'Most calories is {max_cals} in a {max_food}')
    print(f'Least calories is {min_yr} in a {min_food}')
def ages_codebit():
    # Life expectancy database program
    # yoi = input("Input the year of interest: ")
    # max_yr = 0
    # min_yr = 9999
    # max_country = None
    # min_country = None
    # mxy = []
    # mxc = []
    # ages = []
    # years = []
    # counts = []
    # with open('life-expectancy.csv') as file:
    #     header = file.readline()
    #     for line in file:
    #         line = line.strip()
    #         parts = line.split(',')
    #         pais = parts[0]
    #         ano = int(parts[2].strip())
    #         # if max_yr < ano:
    #         #     max_yr = ano
    #         #     mxy.clear()
    #         #     mxc.clear()
    #         #     mxy.append(ano)
    #         #     mxc.append(pais)
    #         # elif max_yr == ano:
    #         #     mxy.append(ano)
    #         #     mxc.append(pais)
    # This commented section is just pure shennanigans that I was working with, ignore it please.
    yoi = int(input("Input the year of interest: "))
    ages = []
    years = []
    counts = []
    ltr = []
    aver = []
    avera = []
    ma = 0
    na = 999
    mc = None
    nc = None
    my = 0
    ny = 0
    yma = 0
    yna = 999
    ymc = None
    ync = None
    with open('life-expectancy.csv') as file:
        header = file.readline()
        for line in file:
            line = line.strip()
            parts = line.split(',')
            pais = parts[0]
            abv = parts[1]
            ano = int(parts[2].strip())
            age = float(parts[3].strip())
            counts.append(pais)
            ltr.append(abv)
            years.append(ano)
            ages.append(age)
            if ano + 1 == yoi:
                avera.append(age)
            if ano == yoi:
                aver.append(age)
                if yma < age:
                    yma = age
                    ymc = pais
                if yna > age:
                    yna = age
                    ync = pais
            if ma < age:
                ma = age
                mc = pais
                my = ano
            if na > age:
                na = age
                nc = pais
                ny = ano
    import statistics
    print()
    print(f"The overall max life expectancy is: {ma} from {mc} in {my}\nThe overall min life expectancy is: {na} from {nc} in {ny}")
    print(f'\nFor the year {yoi}: \nThe average life expectancy across all countries was {round(statistics.mean(aver),2)}, a change of {round(statistics.mean(avera) - statistics.mean(aver), 2)} years since the year before\nThe max life expectancy was in {ymc} with {yma}\nThe min life expectancy was in {ync} with {yna}')

# Current projects
def currentclass():
    # nothin babyy
    print()

# Machine
if True:
    areacalc_code()
# FIM