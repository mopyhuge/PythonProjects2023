
open_file = open("exams/exampletest.txt", "w")
open_file.write("Dylan Cowley\n")

def write_Question(list, open_file):
    for i in list:
        open_file.write(i+"\n")

question1 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question2 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question3 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question4 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question5 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question6 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question7 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question8 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question9 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question10 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question11 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question12 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question13 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question14 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question15 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question16 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question17 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question18 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question19 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]
question20 = ["category", "Question","option 1","option 2","option 3","option 4","answer","exp"]

questions = [question1,question2,question3,question4,question5,question6,question7,question8,
             question9,question10,question11,question12,question13,question14,question15,question16,
             question17,question18,question19,question20]

for question in questions:
    write_Question(question, open_file)







# open_file = open("exampletest.txt","r")
# list = open_file.readlines()
# print(list)
#
# for i in range(len(list)):
#     list[i] = list[i].strip("\n")
# open_file.close()
#
# open_file = open("exampletest.txt","w")
# open_file.write("Dylan Cowley Python Term 2 Final Exam")
# open_file.write("Question Category")
# open_file.write("What is the Question to ask?")
# open_file.write("Option 1")
# open_file.write("Option 2")
# open_file.write("Option 3")
# open_file.write("Option 4")
# open_file.write("Answer")
# open_file.write("Explanation")
#
#
#
#
# open_file.close()