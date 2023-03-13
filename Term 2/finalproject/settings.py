from tkinter import *
from os import path

HEIGHT = 420
WIDTH = 640
create_app = False
TITLE = "Term 2 Final Exam"

SCREENSIZE = str(HEIGHT)+"x"+str(WIDTH)

file_name = "exampletest.txt"

location = path.dirname(__file__)
exams_folder = path.join(location, "exams")
reports_folder = path.join(location,"reports")
errorLogs = path.join(reports_folder,"errorLogs")
reportCards = path.join(reports_folder,"reportCards")

test = path.join(exams_folder,file_name)