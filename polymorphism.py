class Student:
    # Delete this and write your code here
    def __init__ (self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.gpa_for_semesters = gpa_for_semesters
    def __str__ (self):
        return f"{self.name} is studying {self.major}."
    def get_gpa (self):
        return self.gpa_for_semesters
    def set_gpa (self, new_gpa):
        self.gpa_for_semesters = new_gpa
    def calculate_average_gpa (self):
        return sum(self.gpa_for_semesters) / len(self.gpa_for_semesters)
    def is_in_good_standing (self):
        return f"{self.name} is a student."
student1 = Student("John", "Computer Science", [3.5, 4.0, 3.9])
student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.75])

class UndergraduateStudent(Student):
    # Delete this and write your code here
    def __str__ (self):
        return f"{self.name} is an undergraduate student studying {self.major}."
    def is_in_good_standing (self):
        return f"{self.name} is in good academic standing."
undergrad1 = UndergraduateStudent("Grey", "Business", [3.0, 3.5, 3.4])

class GraduateStudent(Student):
    # Delete this and write your code here
    def __str__ (self):
        return f"{self.name} is a graduate student studying {self.major}."
    def is_in_good_standing (self):
        return f"{self.name} is not in good academic standing."
grad1 = GraduateStudent("Jake", "Biology", [2.0, 2.3, 1.8])