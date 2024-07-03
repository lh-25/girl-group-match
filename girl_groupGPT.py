# This program will be used to help the user figure out which k-pop girl group they would like more.

enter = input("Enter 1 - start or 2 - stop ")

while enter != "2":
    concept = input("Which concept do you prefer? Girl Crush, Teen Crush or High Teen? ").lower()
    if concept == "girl crush":
        girl_crush = input("Do you prefer powerful or energetic? ").lower()
        if girl_crush == "powerful":
            print("Blackpink in your area!")
            print("You would love Blackpink 🖤💖")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "boombayah":
                bonus = input("What was Blackpinks Debut song? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "boombayah":
                print("Congratulations! You are a true Blink")
            
        else:
            print("your very Dalla Dalla")
            print("You would love ITZY🎂")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "mitzy":
                bonus = input("What are ITZY's fans called? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "mitzy":
                print("Congratulations! You are sooo ICY")
    elif concept == "teen crush":
        teen_crush = input("Do you prefer bright and cheerfull or fresh and lively? ").lower()
        if teen_crush == "bright and cheerfull":
            print("We just wanna have some FUN!")
            print("You would love Fromis_9")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "dm":
                bonus = input("What song has the lyrics 'gakkai gallae I want to'? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "dm":
                print("joh-ahae neol nae mam-eun I want you!😘")
        else:
            print("I'm~ so good~ with you~~~")
            print("You would love Weeekly!📅")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "after school":
                bonus = input("What was Weeekly's most popular song? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "after school":
                print("Congratulations! You got it right")
    else:
        high_teen = input("Do you prefer trendy or cute ?").lower()
        if high_teen == "trendy":
            print("STAYC girls its going down!")
            print("You would like STAYC")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "j":
                bonus = input("Who is the rapper of the group? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "j":
                print("Congratulations! You got it right")
        else:
            print("You would like Cherry Bullet!🍒🚄")
            bonus = ""
            guess = 0
            while guess < 2 and bonus != "7":
                bonus = input("How many members does Cherry Bullet have? ").lower()
                guess += 1
                print("Wrong answer")
                bonus = input("Please try again: ")
            if bonus == "after school":
                print("Congratulations! You got it right")
        

    