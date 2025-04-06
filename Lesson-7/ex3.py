class Student:
    def __init__(self, student_id, name, gpa):
        self.id = student_id
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, GPA: {self.gpa}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, gpa):
        self.students.append(Student(student_id, name, gpa))

    def display_students(self):
        if not self.students:
            print("No students in the list.")
        else:
            for student in self.students:
                print(student)

    def bubble_sort_by_gpa(self):
        n = len(self.students)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.students[j].gpa > self.students[j + 1].gpa:
                    self.students[j], self.students[j + 1] = self.students[j + 1], self.students[j]

    def binary_search_by_id(self, student_id):
        self.students.sort(key=lambda x: x.id)  # Ensure sorted order
        low, high = 0, len(self.students) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.students[mid].id == student_id:
                return self.students[mid]
            elif self.students[mid].id < student_id:
                low = mid + 1
            else:
                high = mid - 1
        return None


def main():
    manager = StudentManager()
    while True:
        print("\n1. Add student")
        print("2. Display students")
        print("3. Sort students by GPA")
        print("4. Search student by ID")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            gpa_input = input("Enter GPA (comma-separated if multiple): ")
            gpa_list = [float(gpa.strip()) for gpa in gpa_input.split(',')]
            average_gpa = sum(gpa_list) / len(gpa_list)
            manager.add_student(student_id, name, average_gpa)
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.bubble_sort_by_gpa()
            print("Students sorted by GPA.")
        elif choice == "4":
            student_id = int(input("Enter ID to search: "))
            result = manager.binary_search_by_id(student_id)
            print(result if result else "Student not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
