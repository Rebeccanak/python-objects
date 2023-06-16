from datetime import date
class Student:
    school = "Akirachix"
    def __init__(self,first_name,second_name,age,country):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.country = country

    def greet_student(self):
        return f"Hello {self.first_name},{self.second_name} from {self.country}. Welcome to {self.school}"

    def show_full_name(self):
        return f"{self.first_name} {self.second_name}"

    # def year_of_birth(self,current_year=2023):
    #     return current_year - self.age

    def year_of_birth(self):
        current_year=date.today().year
        return current_year-self.age

    def show_initials(self):
        return f"{self.first_name[0]}.{self.second_name[0]}"
    

    