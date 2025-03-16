class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grades):
        self.grades.clear()
        self.grades.extend(grades)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class GradeManager:
    def __init__(self):
        self.students = {}
        self.load_data("grade.md")

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)

    def record_grade(self, name, grades):
        if name in self.students:
            self.students[name].add_grade(grades)
        else:
            print(f"Error: Student '{name}' not found. Please add the student first.")

    def calculate_average_all(self):
        total_average = 0
        student_count = len(self.students)
        for student in self.students.values():
            total_average += student.calculate_average()
        if student_count == 0:
            return 0
        return total_average / student_count

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for student in self.students.values():
                grades_str = ', '.join(map(str, student.grades))
                file.write(f"{student.name}: {grades_str}\n")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, grades_str = line.strip().split(': ')
                    grades = list(map(float, grades_str.split(', ')))
                    student = Student(name)
                    student.grades = grades
                    self.students[name] = student
        except FileNotFoundError:
            print("No existing data file found. Starting fresh.")

def main():
    manager = GradeManager()
    while True:
        print("1. Add a new student")
        print("2. Record grades for a student")
        print("3. Calculate the average grade of all students")
        print("4. Save the data to a file")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            manager.add_student(name)
        elif choice == '2':
            name = input("Enter the student's name: ")
            grades_input = input("Enter the grades separated by commas: ")
            grades = [float(grade.strip()) for grade in grades_input.split(',')]
            manager.record_grade(name, grades)
        elif choice == '3':
            average = manager.calculate_average_all()
            print(f"The average grade of all students is: {average}")
        elif choice == '4':
            manager.save_data("grade.md")
            print("Data saved successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
