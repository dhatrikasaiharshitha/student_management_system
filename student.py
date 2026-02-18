# -------------------------------
# Student Management System
# -------------------------------

students = []


def add_student():
    print("\n--- Add Student ---")
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    phone = input("Enter Phone Number: ")
    marks = float(input("Enter Marks: "))

    # Check if ID already exists
    for s in students:
        if s["id"] == sid:
            print("❌ Student ID already exists!")
            return

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "branch": branch,
        "phone": phone,
        "marks": marks
    }

    students.append(student)
    print("✅ Student Added Successfully!")


def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("⚠️ No students found!")
        return

    print("\nID   Name        Age   Branch     Phone        Marks")
    print("------------------------------------------------------")

    for s in students:
        print(f"{s['id']}   {s['name']}     {s['age']}    {s['branch']}     {s['phone']}     {s['marks']}")


def search_student():
    print("\n--- Search Student ---")
    sid = int(input("Enter Student ID to search: "))

    for s in students:
        if s["id"] == sid:
            print("\n✅ Student Found!")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Branch:", s["branch"])
            print("Phone:", s["phone"])
            print("Marks:", s["marks"])
            return

    print("❌ Student Not Found!")


def update_student():
    print("\n--- Update Student ---")
    sid = int(input("Enter Student ID to update: "))

    for s in students:
        if s["id"] == sid:
            print("\nStudent Found. Enter new details:")

            s["name"] = input("Enter New Name: ")
            s["age"] = int(input("Enter New Age: "))
            s["branch"] = input("Enter New Branch: ")
            s["phone"] = input("Enter New Phone: ")
            s["marks"] = float(input("Enter New Marks: "))

            print("✅ Student Updated Successfully!")
            return

    print("❌ Student Not Found!")


def delete_student():
    print("\n--- Delete Student ---")
    sid = int(input("Enter Student ID to delete: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("✅ Student Deleted Successfully!")
            return

    print("❌ Student Not Found!")


# Main Program
while True:
    print("\n===============================")
    print("  Student Management System")
    print("===============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice! Please enter 1-6.")
