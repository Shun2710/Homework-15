# Task 15.1

class GroupOverflowError(Exception):
    pass

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupOverflowError("Group is full")
        self.students.append(student)

    def __str__(self):
        return f"Group {self.name}: {', '.join(self.students)}"

group = Group("AI-1")

try:
    for i in range(1, 12):
        group.add_student(f"Student {i}")
        print(f"Student {i} successfully added to group")
except GroupOverflowError as e:
    print(f"Error occurred: {e}")

print("\nGroup status:")
print(group)