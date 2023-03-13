from asciiArt import *
from settings import *
import winsound


playerName = ""
partyNumber = 0



def clearScreen():
    print("\n"*10000)



def displayMenu(options,question):
    print(RIBBON)
    print(" "*50 + question)
    for i in range(len(options)):
        print(str.format("\t\t\t\t\t\t\t\t\t\t\t\t\t\t({0}.)- -{1:<30}",i+1,options[i]))
    print(RIBBON)
    while True:
        choice = input("What would you like to do? ")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= len(options) and choice > 0:
                return choice
            else:
                print("Not a number in range")
        else:
            print("You need a number between 1 and "+str(len(options)))

def titleScreen():
    clearScreen()
    print(title)
    while True:
        choice = displayMenu(["Travel the Oregon Trail", "Learn about the trail", "Top Ten",
                              "Sound Options", "Choose Management Options", "Quit"], "You may:")
        if choice == 1:
            return
            idenityChoice()

        if choice == 2:
            print("""
            Enter Lore here
            """)
            input("Press Enter to continue")
        if choice == 3:
            print("In development...")
            input("Press Enter to continue")
        if choice == 4:
            winsound.Beep(5000,50000)
            input("Press Enter to continue")
        if choice == 5:
            print("In development...")
            input("Press Enter to continue")
        if choice == 6:
            quitGame()


def idenityChoice():
    clearScreen()
    while True:
        print(jobTitle)
        choice = displayMenu(["Be a banker from Mountain America Credit Union",
                              "Be a carpenter from Home Depot", "Be a farmer from FarmersOnly.com",
                              "Be an average poor person from the streets of Chicago", "Learn about each job"], "You may:")
        if choice == 1:
            money = 1500
            job = "banker"
            diff = "easy"
            break
        elif choice == 2:
            money = 1000
            job = "car"
            diff = "Medium"
            break
        elif choice == 3:
            money = 500
            job = "carpenter"
            diff = "Hard"
            break
        elif choice == 4:
            money = 1
            job = "Poor person"
            diff = "Hell"
            break
        elif choice == 5:
            print("Traveling to Oregon isn't easy! But if you're a banker, "
                  " you'll have more money for supplies and services than a carpenter"
                  " or a farmer."
                  ""
                  " However, the harder you have to try, the more points you deserve!"
                  " Therefore, the farmer earns the greatest number of points and the banker earns"
                  " the least.")
            break
    return money, job, diff

def partyNaming():
    clearScreen()
    partyMembers = []
    randomnames = ["Bob", "Saul", "Henry", "Ronald", "Harold"]
    while True:
        playerName = input("What is the leader's name?")

        if len(playerName) >= 3:
            break
        else:
            print("Not a good name")

    while True:
        partyNumber = input("How many people are in your party?")
        if partyNumber.isnumeric():
            partyNumber = int(partyNumber)
            if partyNumber >= 1 and partyNumber <= 5:
                break
            else:
                print("Not a number")
        else:
            print("Not a number")
    for i in range(partyNumber):
        name = input("Enter party numbers name")
        if len(name) < 3:
            name = random.choice(randomnames)
            randomnames.remove(name)
        partyMembers.append(name)
    partyMembers.insert(0,playerName)
    return playerName, partyMembers
    startmonthselection()

def startmonthselection(options):
    startMonth = ""
    clearScreen()
    print()
    while True:
        choice = displayMenu([])
        if choice == 1:
            month = 3
            day = 1
            year = 1867
            break
        elif choice == 2:
            month = 4
            day = 1
            year = 1867
            break
        elif choice == 3:
            month = 5
            day = 1
            year = 1867
            break
        elif choice == 4:
            month = 6
            day = 1
            year = 1867
            break
        elif choice == 5:
            month = 7
            day = 1
            year = 1867
            break
        elif choice == 6:
            print("to be continued")

def shop(money):
    inventory = []
    bill = 0.00
    spentOnItems = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    choices = ["Oxen","Food","Clothes","Ammo","Wagon Parts","Check Out"]
    messages = ["""
        There are 2 oxen in a yoke;
        I recommend at least 3 yokes.
        I charge $40 a yoke""", """
            I recommend you take at least 200 pounds of food for each person in your family. 
            My price is 20 cents a pound.""","""
            You'll need warm clothing in the mountains. 
            I recommend taking at least 2 sets of clothes per person. 
            Each set is $10.00.""", """
            I sell ammunition in boxes of 20 bullets.
            Each box costs $2.00."""]
    questions = ["How many yokes would you like to buy?",
                 "How many pounds of food would you like to buy?",
                 "How many sets of clothes would you like to buy?",
                 "How many boxes of ammo would you like to buy?"
                 ]
    print("Before leaving Independence you should buy Equipment and Supplies.")
    print(str.format("You have ${:.2f} in cash to make this trip", money))
    print(" ")
    input("Press Enter to Continue")
    print(" ")
    print("Remember you can buy supplies along the way so you don't have to spend it all now.")
    print(" ")
    input("Press Enter to Continue")
    while True:
        spentOnItems[len(spentOnItems)-1] = bill
        print("Welcome to the General Store")
        print("Here is a list of things you can buy")
        print(RIBBON)
        for i in range(len(choices)):
            print(str.format("\t{}:{:<20} ${:<10.2f}",i+1,choices[i],spentOnItems[i]))
        print (" ")
        print(str.format("Total bill so far   ${:.2f}", bill))
        print(str.format("Total funds available:    {:.2f}", money - bill))
        print(RIBBON)
        choice = getNumberInRange("What would you like to buy?",1,len(choices))
        if choice == 1:
            oxen,spentOnItems = buyGoods(spentOnItems,money,"ox", messages, questions)
            inventory.insert(oxen, 0)
        elif choice == 2:
            food,spentOnItems = buyGoods(spentOnItems,money,"food", messages, questions)
            inventory.insert(food, 1)
        elif choice == 3:
            clothes = buyGoods(spentOnItems,money,"clothes", messages, questions)
            inventory.insert(2,clothes)
        elif choice == 4:
            ammo = buyGoods(spentOnItems,money,"ammo", messages, questions)
            inventory.insert(3, ammo)
        elif choice == 5:
            parts = buyParts(spentOnItems, money)
            inventory.insert(4, parts)
        elif choice == 6:
            if spentOnItems[len(spentOnItems)-1] <= money:
                if inventory[0] >= 1:
                    total_Wheels = 0
                    total_axles = 0
                    total_tongues = 0
                    total_tarps = 0
                    for part in inventory[4]:
                        if part == "Wagon Wheel":
                            total_Wheels += 1
                        elif part == "Wagon axle":
                            total_axles += 1
                        elif part == "Wagon Tongue":
                            total_tongues += 1
                        elif part == "Wagon Tarp":
                            total_tarps += 1
                    print(str.format("""
                                        you have purchased 
                                        {} yokes of oxen
                                        {} pounds of food
                                        {} sets of clothing
                                        {} boxes of ammo
                                        and the following wagon parts
                                        {} Wheels
                                        {} Axles
                                        {} Tongues
                                        {} Tarps                 

    """, inventory[0] / 2, inventory[1], inventory[2], inventory[3] / 20, total_Wheels, total_axles, total_tongues, total_tarps))
                    choice = displayMenu(["yes", "no"], "is this correct")
                    if choice == 1:
                        money -= spent_on_items[len(spent_on_items) - 1]
                        return inventory
                    else:
                        print("Start over then")
                        inventory = []
                        bill = 0.00
                        spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                        continue
                else:
                    print("you must have at least 1 oxen to travel Start shoping over")
                    inventory = []
                    bill = 0.00
                    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                    continue
            else:
                print("you dont have enough money Start over")
                inventory = []
                bill = 0.00
                spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                continue

def buyGoods(spentOnItems,money,good,messages,questions,):
    if good == "ox":
        index = 0
        price = 40
        multiplyer = 2
    elif good == "food":
        index = 1
        price = 0.20
        multiplyer = 1
    elif good == "clothes":
        index = 2
        price = 10
        multiplyer = 1
    elif good == "ammo":
        index = 3
        price = 2
        multiplyer = 20
    # clear the amount spent on goods from the current bill
    currentbill = spentOnItems[len(spentOnItems) - 1]
    currentbill = currentbill - spentOnItems[index]
    # update the spent on items list with updated values
    spentOnItems[len(spentOnItems) - 1] = currentbill
    spentOnItems[index] = 0.00
    goods = 0
    print(messages[index])

    print(str.format("Total Bill so far:        ${:.2f}",
spentOnItems[len(spentOnItems) - 1]))
    answer = getNumberInRange(questions[index], 1, money / price)
    cost = answer * price
    goods = answer * multiplyer
    currentbill += cost
    spentOnItems[index] = cost
    spentOnItems[len(spentOnItems) - 1] = currentbill
    return goods, spentOnItems
# def buyOxen(spentOnItems,money,good,message,question):
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1]-spentOnItems[0]
#     spentOnItems[0]= 0.00
#
#
#
#
#     oxen = 0
#     print("""
#         There are 2 oxen in a yoke;
#         I recommend at least 3 yokes.
#         I charge $40 a yoke""")
#     print(" ")
#     print(str.format("Total bill so far   ${:.2f}",spentOnItems[len(spentOnItems)-1]))
#     print(" ")
#     answer = getNumberInRange("How many yokes would you like to buy?",1,money/40)
#     cost = answer * 40
#     oxen - answer * 2
#     spentOnItems[0] = cost
#     spentOnItems[len(spentOnItems)-1] = spentOnItems[len(spentOnItems)-1]+cost
#
#     return oxen, spentOnItems
# def buyFood(spentOnItems,money):
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] - spentOnItems[1]
#     spentOnItems[1] = 0.00
#
#     food = 0
#     print("""
#             I recommend you take at least 200 pounds of food for each person in your family.
#             My price is 20 cents a pound.""")
#     print(" ")
#     print(str.format("Total bill so far   ${:.2f}", spentOnItems[len(spentOnItems) - 1]))
#     print(" ")
#     answer = getNumberInRange("How many pounds of food would you like to buy?", 1, money )
#     cost = answer * .2
#     food - answer * 2
#     spentOnItems[1] = cost
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] + cost
#     return food, spentOnItems
# def buyClothes(spentOnItems,money):
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] - spentOnItems[2]
#     spentOnItems[2] = 0.00
#
#     clothes = 0
#     print("""
#             You'll need warm clothing in the mountains.
#             I recommend taking at least 2 sets of clothes per person.
#             Each set is $10.00.""")
#     print(" ")
#     print(str.format("Total bill so far   ${:.2f}", spentOnItems[len(spentOnItems) - 1]))
#     print(" ")
#     answer = getNumberInRange("How many sets of clothes would you like to buy?", 1, money)
#     cost = answer * 10
#     clothes - answer * 2
#     spentOnItems[2] = cost
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] + cost
#     return clothes, spentOnItems
# def buyAmmo(spentOnItems,money):
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] - spentOnItems[0]
#     spentOnItems[3] = 0.00
#
#     ammo = 0
#     print("""
#             I sell ammunition in boxes of 20 bullets.
#             Each box costs $2.00.""")
#     print(" ")
#     print(str.format("Total bill so far   ${:.2f}", spentOnItems[len(spentOnItems) - 1]))
#     print(" ")
#     answer = getNumberInRange("How many boxes of ammo would you like to buy?", 1, money / 40)
#     cost = answer * 2
#     ammo - answer * 2
#     spentOnItems[3] = cost
#     spentOnItems[len(spentOnItems) - 1] = spentOnItems[len(spentOnItems) - 1] + cost
#     return ammo, spentOnItems
def buyParts(spentOnItems,money):
    print("""
    It is a good idea to have a few
    Spare parts for your wagon on hand
    you never know what can happen on
    the trail and a broken down 
    wagon can be a death sentence.
    """)
    partsInventory=[]
    currentbill = spentOnItems[len(spentOnItems) - 1]
    currentbill = currentbill - spentOnItems[4]

    spentOnItems[4] = 0.00
    partsBill = 0.00
    options = ["Wagon Wheel","Wagon Axle","Wagon Tongue", "Wagon Tarp", "Back to Main Shop"]
    partsCost= [10.00,20.00,50.00,12.75,partsBill]
    while True:
        partsCost[len(partsCost)-1] = partsBill
        print("Here is a list of things you can buy.")
        for i in range(len(options)):
            print(str.format("{}.    {:20}    ${:.2f}",i+1,options[i],partsCost[i]))
        print(str.format("Total bill so far:       ${:.2f}", partsBill))
        print(str.format("Total funds available:   ${:.2f}", money))

        choice = getNumberInRange("What is your choice",1,len(options))
        if choice == 1:
            parts = getNumberInRange("how many wagon wheels do you want?",0,3)
            for i in range(parts):
                partsInventory.append(options[0])
            partsBill += partsCost[0] * parts
        elif choice == 2:
            parts = getNumberInRange("how many wagon axle do you want?", 0,3)
            for i in range(parts):
                partsInventory.append(options[1])
            partsBill += partsCost[1] * parts
        elif choice == 3:
            parts = getNumberInRange("how many wagon tongue do you want?", 0,3)
            for i in range(parts):
                partsInventory.append(options[2])
            partsBill += partsCost[2] * parts
        elif choice == 4:
            parts = getNumberInRange("how many tarps do you want?", 0,3)
            for i in range(parts):
                partsInventory.append(options[3])
            partsBill += partsCost[3] * parts
        elif choice == 5:
            currentbill += partsBill
            spentOnItems[4] = partsBill
            break
    return partsInventory, spentOnItems

def currentDay(day, month):
    month = month
    MONTHS = ["January","February","March","April","May","June","July","August","September","October",
    "November","December"]
    monthIndex = 0
    for m in range(len(MONTHS)):
        if MONTHS[m] == month:
            monthIndex =  m
    day += 1
    if(month in ["March","May","July","August","October","December"]):
        if day > 31:
            month = MONTHS[monthIndex + 1]
            day = 1
    elif month == "February":
        if day > 28:
            month = MONTHS[monthIndex + 1]
    else:
        if day > 30:
            month = MONTHS[monthIndex + 1]
            day = 1
    date = str(month)+"/"+str(day)+"/"+str(year)

    return day,month,date

def getWeather():
    WEATHER = ["Good","Good","Fair","Fair","Fair","Fair","Fair","Fair","Poor","Poor","Poor"]
    weather = random.choice(WEATHER)
    if weather == "Good":
        mod = 2
    elif weather == "Poor":
        mod = .5
    else:
        mod = 1
    return weather, mod

def eat(rations,food,members):
    food-= (3* members) * rations
    return food

# def getHealth():
#     number =random.randint(1, 100)
#     if number >= 90:
#         health = "Sick"
#     else:
#         if healthvalue > 80:
#             health = "Good"
#         elif healthValue < 45:
#             health = "Poor"
#         else:
#             health = "Fair"

def rest(health_value,food,day,rations,members):
    day = day
    food = food
    health_value = health_value
    x = getNumberInRange("How many days do you want to rest for?",1,9)
    for i in range(x):
        day += 1
        food = eat(rations,food,members)
        health_value += random.randint(5,15)
    return health_value, food, day

def checkSupplies(food, bullets, oxen, inventory):
    total_wheels = 0
    total_axles = 0
    total_tongues = 0
    total_tarps = 0

    for part in inventory[4]:
        if part == "Wagon Wheel":
            total_wheels += 1
        elif part == "Wagon axle":
            total_axles += 1
        elif part == "Wagon Tongue":
            total_tongues += 1
        elif part == "Wagon Tarp":
            total_tarps += 1

    print(str.format("""
        you have purchased
        {} yokes of oxen
        {} pounds of food
        {} sets of clothing
        {} boxes of ammo
        and the following wagon parts
        {} Wheels
        {} Axles
        {} Tongues
        {} Tarps

        """, oxen, food, inventory[2], bullets, total_wheels, total_axles,
                     total_tongues, total_tarps))

def get_health(health_value,members):
    number = random.randint(1, 100)
    health_value -= 10
    sick = ""
    if number >= 90:
        health = "sick"
        conditions = ["the *#*^'s","Drowding","Cold","covid","flu","Exaustion"]
        sick = random.choice(conditions)
        if sick == conditions[0]:
            health_value -=15
        elif sick == conditions[1]:
            health_value -= 100
        elif sick == conditions[2]:
            health_value -= 10
        elif sick == conditions[3]:
            health_value -= 50
        elif sick == conditions[4]:
            health_value -= 20
        elif sick == conditions[5]:
            health_value -= 5

    if health_value <= 0:
        if sick =="":
            "Starvation"
        if len(members)>1:
            number = random.randint(1,len(members)-1)
            print(members[number]+" Has died from "+sick)
            members.remove(members[number])
            health_value = 100
        else:
            #game over
            print("you have Died")
            input()
            quitGame()

    if health_value > 80:
        health = "Good"
    elif health_value < 45:
        health = "Poor"
    else:
        health = "Fair"
    if health == "Good":
        health_mod = 1
    elif health == "Poor":
        health_mod = .25
    else:
        health_mod = .5
    return health, health_value, members,health_mod

def todays_travel(weather_mod,health_mod,pace):
    miles = 0
    high = int((25)*weather_mod+health_mod)
    low = int((5)*weather_mod+health_mod)
    miles = random.randint(low,high)*pace

    return miles


def change_pace():
    pace = 1
    choice = displayMenu(["Fast pace","Normal pace","Slow pace"],"what Pace wuould you like to set?")
    if choice == 1:
        pace = 1
    elif choice  == 2:
        pace = .5
    else:
        pace = .25

    return pace

def change_rations():
    rations = 1
    choice = displayMenu(["Double rations", "Normal rations", "Half rations"], "How good would you like to eat?")
    if choice == 1:
        pace = 1
    elif choice == 2:
        pace = .5
    else:
        pace = .25
    return rations

def travel(day,month,rations,members,health_value,food,oxen,total_miles,pace):
    if oxen >= 1:
        day, month, date = currentDay(day, month)
        weather,weather_mod = getWeather()
        food = eat(rations,food,members)
        health,health_value,members,health_mod = get_health(health_value,members)
        miles_travled = todays_travel(weather_mod,health_mod,pace)
        total_miles = total_miles - miles_travled

        print(str.format("""
           .....                                        ..'..                              ..',,,'..
        ..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..
        ,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
        ;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                              ........        ...............            ...
         +-----------------------------+
         |Date:{:_>24}|
         |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.
         |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.
         |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.
         |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.
         |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.
         +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'
                         ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,
                  .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'
                   .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.
                 .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.
                  ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.
                        .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.
                         .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.
                          .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.
                        .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.
        '..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
        ;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
        ;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
        ;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;
        """, date, weather, health, miles_travled, total_miles, food))
        return day, month, date,weather,weather_mod,food,health,health_value,members,health_mod,total_miles
    else:
        quitGame()



def hunt(food,bullets):
    number = random.randint(1,2)
    if number == 1:
        print("good Hunt")
        food += random.randint(25,100)
        bullets -= random.randint(10,30)
        return food,bullets
    else:
        print("bad hunt")
        bullets -= random.randint(10, 30)
        return food, bullets


def getNumberInRange(question, min, max,):
    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min and x <= max:
            return x
        else:
            print("Not in range")




def quitGame():
    clearScreen()
    choice = displayMenu(["Yes","No"],"Are you sure you want to quit?")
    if choice == 1:
        print("Goodbye")
        input("Press enter to continue")
        quit()
    else:
        return

    alive = True
def game():
    alive = True
    miles_travled = 0
    weather = "good"
    healthValue = 100
    alive = True
    day = 0
    year = 2022
    money = 1000000
    inventory = shop(money)
    titleScreen()
    money, job, diff = idenityChoice()
    playerName, partyMembers = partyNaming()
    startMonth = "March"
    date = str(startMonth)+"/"+str(day)+"/"+str(year)
    food = inventory[1]
    oxen = inventory[0]
    bullets = inventory[3]

    while miles_travled < total_miles and alive:
        choice = displayMenu(
            ["Travel trail", "Change Pace", "Change Rations", "Check Supplies", "Rest", "Hunt", "Trade"],
            "What would you like to do?")
        if choice == 1:
            day, month, date, weather, weather_mod, food, health, health_value, members, health_mod, total_miles = travel(day,month,rations,members,health_value,food,oxen,total_miles,pace)
        elif choice == 2:
            pace = change_pace()
        elif choice == 3:
            rations = change_rations()
        elif choice == 4:
            checkSupplies(food, bullets, oxen, inventory)
        elif choice == 5:
            health_value, food, day = rest(health_value, food, day, rations, members)
        elif choice == 6:
            pass  # hunt
        elif choice == 7:
            pass

    if alive:
        print("Congrats you win")
    else:
        print("you have died")



