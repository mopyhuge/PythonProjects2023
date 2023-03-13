class Person(object):
    people_count = 0
    languages = ["Eng","Spa","Chi","Ger", "Fre"]
    def __init__(self,name,alive=True,happy=False,mad=False,eyeColor="Brown",gender="M",height= 0,weight= 0,age=0,bloodtype = "o",haircolor= "brown",race="n/a"):
        Person.people_count += 1
        self.name = name
        self.isAlive = alive
        self.happy = happy
        self.mad = mad
        self.language = ""
        self.eyeColor = eyeColor
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.bloodType = bloodtype
        self.allergies = []
        self.hairColor = haircolor
        self.race = race

    def speak(self,speech):
        print(speech)

    def walk(self):
        print("walking")

    def run(self):
        print("running")

    def die(self):
        self.isAlive = False
        Person.people_count -= 1

    def breath(self):
        pass

    def sleep(self):
        pass

    def jump(self):
        pass

    def grow(self, amount):
        self.height += amount

    def gainWeight(self,amount):
        self.weight+= amount

    def loseWeight(self,amount):
        self.weight-=amount

    def __str__(self):
        des = self.name + "\n"
        des+= str(self.height) + " inches tall\n"
        des+= str(self.weight) + " pounds\n"
        des+= self.gender + "\n"
        des+= self.eyeColor + " eyes\n"
        des+= self.hairColor + " hair"

        return des