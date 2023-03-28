class Person:
    count_of_object = 0
    def __init__(self, fisrt_name, last_name, age, occupation, gender, nationality):
        self.fisrt_name = fisrt_name
        self.last_name = last_name 
        self.age = age 
        self.occupation = occupation 
        self.gender = gender 
        self.nationality = nationality
        Person.count_of_object += 1
    
    def year_born(self, cur_year):
        print(cur_year - self.age)
    def get_name(self):
        print("First name is", self.first_name, "last name is", self.last_name)
    def get_nationality(self): 
        print(self.nationality)
    def get_age(self):
        print(self.age)
    def get_occupation(self):
        print(self.occupation)

actor1 = Person(fisrt_name="Brad", last_name="Pitt", age=50, occupation="Actor", gender="Man", nationality="American")

actor1.year_born(cur_year=2023)

print(actor1.count_of_object)


actor2 = Person(fisrt_name="Tom", last_name="Cruise", age=61, occupation="Actor", gender="Man", nationality="American")

actor2.year_born(cur_year=2023)

print(actor2.count_of_object)