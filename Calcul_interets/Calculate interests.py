#réponse simple
def epargne():
    total=float(input("combien d'argent je dépose sur mon compte ? (uniquement numérique): "))
    year=int(input("combien d'année je laisse l'argent sur mon compte ? (uniquement numérique): "))
    rate=float(input("quel est le tx d'intérêt ? (numérique séparé par un point ou 10% = 0.1) ; "))
    totalrate = total *(1+rate)**(year)
    print(totalrate)
# epargne()

#réponse 2
def savings():
    try:
        initial_amount = float(input("Give us the total amount you wish to invest : \n"))
        print(initial_amount)
        duration = float(input("How many years are you going to invest that money ? \n"))
        print(duration)
        interest_rate = float(input("At what rate would you like to see interest ?\n \
              WARNING: You will have to put a decimal value \n Ex: 10% --> 0.10 \n"))
        print(interest_rate)
    except ValueError:
        # We enter this except only if the user types something other than numbers.
        raise ValueError("Please enter only numbers !") # makes it possible to explain the error
    else:
        # We enter this else if the user has typed numbers correctly.
        # We're going to run successive tests to create the other errors
        
        if (initial_amount < 0) or (duration < 0) or (interest_rate < 0):
            raise ValueError("You have entered one or more negative values. \n \
            Please type only positive values !")
        
        if interest_rate > 1:
            raise ValueError("You have entered an interest rate greater than 1%. \n \
            Please enter an interest rate as a decimal value !")
        
# The following code will be executed if no errors occurred upstream
    total = initial_amount*(1+interest_rate)**(duration)
    print("The total amount of money you will have after you deposit {:.2f} at the end of {} years will be {:.2f} €".format(initial_amount, duration, total))

savings()