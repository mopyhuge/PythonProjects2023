score = int(input("What is the score? "))
health = int(input("What is the health? "))
powerups = int(input("How many powerups? "))
lives = 3
if score > 100 and health > 50:
    print("First condition met")
    lives = lives + 1
elif score > 1000 or powerups >= 1:
    print("Second condition met")
    lives = lives + 1
print("Final number of lives:",lives)