class Professor:
    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name
    
class Department:
    def __init__(self, name, professor):
        self.name = name
        self.professor = professor

    def print_professor(self):
        print(f"Professor in {self.name} department: ")
        for professor in self.professor:
            print(f"- {professor.get_name()}")
        

if __name__ == "__main__":
    prof1 = Professor("Dr. Smith")
    prof2 = Professor("Dr. Johnson")
    prof3 = Professor("Dr. Williams")

    cs_department = Department("Computer Science", [prof2])
    math_department = Department("Mathematics", [prof1, prof3])

    cs_department.print_professor()
    print("-----------------------")
    math_department.print_professor()