class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}

    def mark_attendance(self, date):
        if date not in self.attendance:
            self.attendance[date] = True

    def get_attendance(self, date):
        return self.attendance.get(date, False)

class AttendanceManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            print("Student already exists.")

    def mark_student_attendance(self, student_id, date):
        student = self.students.get(student_id)
        if student:
            student.mark_attendance(date)
        else:
            print("Student not found.")

    def view_student_attendance(self, student_id, date):
        student = self.students.get(student_id)
        if student:
            attendance_status = "Present" if student.get_attendance(date) else "Absent"
            print(f"{student.name} ({student.student_id}) was {attendance_status} on {date}")
        else:
            print("Student not found.")

if __name__ == "__main__":
    attendance_system = AttendanceManager()

    while True:
        print("\nAttendance Management System")
        print("1. Add Student")
        print("2. Mark Student Attendance")
        print("3. View Student Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            attendance_system.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            attendance_system.mark_student_attendance(student_id, date)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            attendance_system.view_student_attendance(student_id, date)
        elif choice == "4":
            print("Exiting the Attendance Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
