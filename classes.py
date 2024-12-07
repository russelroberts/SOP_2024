class Person:
    status="Alive"
    def __init__(self,name,sex,race): #instance parameters
        self.name=name
        self.sex = sex
        self.race =race

jane=Person("JAne Doe","Female","LatinX")
mildred= Person("mildred Ojomah","Female","African American")

print(f"my name is {jane.name} and I am of {jane.race}")