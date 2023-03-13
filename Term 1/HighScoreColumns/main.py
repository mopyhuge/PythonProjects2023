






name1 = "Bob"
name2 = "Pop"
name3 = "Lob"
# create and initialize three score variables
# (score1, score2, score3)
score1 = 10003345
score2 = 995357
score3 = 85023
# print a title for the high scores list
print(str.format("{0:^26}","High Scores"))
print(str.format("{0:^15} {1:^10}","Player Name","High Score"))
print("---------------------------")
print(str.format("{0:^15} {1:^10}",name1,score1))
print(str.format("{0:^15} {1:^10}",name2,score2))
print(str.format("{0:^15} {1:^10}",name3,score3))