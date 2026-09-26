"""
name: Mary Zhou
andrewID: maryzhou
"""

def parse_record(record: str) -> dict:
    fields = record.strip().split(",")
    if len(fields) != 4:
        return None
    for item in fields:
        if item.strip() == "":
            return None

    name = fields[0].strip()
    year = fields[1].strip()
    event = fields[2].strip()
    hours = fields[3].strip()

    if not year.isdigit():
        return None
    else:
        year = int(year)

    if year < 1 or year > 4:
        return None

    try:
        hours = float(hours)
    except ValueError:
        return None

    if hours <= 0:
        return None

    return {
        "name": name,
        "year": year,
        "event": event,
        "hours": hours
    }


def participation_points(hours: float) -> int:
    if hours >= 1 and hours <= 2:
        return 10
    elif hours <= 5:
        return 20
    elif hours >= 6:
        return 30


def participation_standing(hours:float) -> str:
    if hours >=1 and hours <= 5:
        return "Bronze"
    elif hours <= 10:
        return "Silver"
    elif hours <= 20:
        return "Gold"
    elif hours >= 21 :
        return "Diamond"

def run_menu(student_data: list) -> None:
    search = ""
    while search != "d":
        print("a. Search for a student by name.")
        print("b. Display all students who participated in a specific event.")
        print("c. Display all students in a specific participation standing.")
        print("d. Quit the program.")
    
        search = input("Please enter your choice: ").loewr().strip()
        if search == "a":
            name = input("Please enter student name: ").strip()
            check = 0
            for student in student_data:
                if student["name"].lower() == name.lower():
                    print(student)
                    check = 1
                    break
            if check == 0:
                print("Student not found.")

        elif search == "b":
            event = input("Please enter a specific event name: ").strip()
            check = 0
            for student in student_data:
                if student["event"].lower() == event.lower():
                    print(student)
                    check +=1
            if check == 0:
                print("No students found for that event.")

        elif search == "c":
            standing = input("Please enter a specific participation standing (Bronze, Silver, Gold, Diamond): ").strip()
            check = 0
            for student in student_data:
                if participation_standing(student["hours"]).lower() == standing.lower():
                    print(student)
                    check +=1
            if check == 0:
                print("No students found for that participation standing.")
                
        elif search == "d":
            print("You are quitting the program")

        else:
            print("Invalid choice, please try again.")

def filter_high_participation(student_data: list)-> list:
    student_list = []
    for student in student_data:
        if student["hours"] >=10:
            student_list.append(student)
    return student_list


def filter_high_participation_comprehension(student_data:list) ->list:
    student_list_comp = [student for student in student_data if student["hours"]>=10]
    return student_list_comp

def get_names_loop(student_data: list)->list:
    name_list = []

    for student in student_data:
        name_list.append(student["name"])

    return name_list

def get_names_map(student_data: list)->list:
    name_list_map = list(map(lambda student: student["name"], student_data))
    return name_list_map

def get_hours_loop(student_data: list)->list:
    hours_list = []

    for student in student_data:
        hours_list.append(student["hours"])

    return hours_list

def get_hours_map(student_data: list)->list:
    hours_list_map = list(map(lambda student: student["hours"], student_data))
    return hours_list_map

def  event_statistics(student_data: list)->dict:
    statistics = {}

    for student in student_data:
        event = student["event"]
        if event in statistics:
            statistics[event] +=1
        else:
            statistics[event] = 1

    return statistics

def most_popular_event(statistics:dict) ->str:
    event_name = max(statistics, key=statistics.get)
    return event_name

def least_popular_event(statistics:dict)->str:
    event_name = min(statistics, key=statistics.get)
    return event_name

def generate_report(student_data:list) -> None:
    for student in student_data:
        print(f"Student: {student['name']}")
        print(f"Year: {student['year']}")
        print(f"Event: {student['event']}")
        print(f"Hours: {student['hours']}")
        print(f"Points: {participation_points(student['hours'])}")
        print(f"Standing: {participation_standing(student['hours'])}")

def main():
    student_data = []
    with open("students.csv", "r") as file:
        f = file.readlines()

    for line in f: 
        student = parse_record(student)

        if student is not None:
            student_data.append(student)

        statistics = event_statistics(student_data)

        print("Event Statistics:")
        print(statistics)

        print("Most Popular Event:")
        print(most_popular_event(statistics))

        print("Least Popular Event:")
        print(least_popular_event(statistics))
        
        generate_report(student_data)

        run_menu(student_data)

if __name__ == "__main__":
    main()