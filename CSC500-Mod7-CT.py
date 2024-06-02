# Module 7: Critical Thinking Assignment
# Design a program allowing a user to enter a course number and return course's room number, instructor, and meeting time.

# Creates a dictionary containing course numbers as keys and the corresponding room numbers as values.
course_rooms = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Creates a dictionary containing course numbers as keys and the corresponding instructors as values.
course_instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Creates a dictionary containing course numbers as keys and the corresponding meeting times as values.
course_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Ask user to input course number.
course_number = input("For detailed course info\nEnter a course number: ")

# Check if the course is offered this term.
# If the course is offered return details, else prompt user to try again.
valid_course = False

while not valid_course:
    course_number = input("For detailed course info\nEnter a course number: ")

    if course_number in course_rooms and course_number in course_instructors and course_number in course_times:
        valid_course = True
        room_number = course_rooms[course_number]
        instructor = course_instructors[course_number]
        meeting_time = course_times[course_number]

        print(f'Course Number: {course_number}')
        print(f'Room Number: {room_number}')
        print(f'Instructor: {instructor}')
        print(f'Meeting Time: {meeting_time}')
    else:
        print("Course number not found. Please enter a valid course number.")
        print("Courses offered this term:")
        for course in course_rooms:
            print(course)