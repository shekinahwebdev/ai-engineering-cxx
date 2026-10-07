import os

def studentRecordSystem():
    # Automatically get the correct path for students.txt in the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
    file_path = os.path.join(script_dir, "students.txt")

    while True:
        print("\n========================")
        print("  STUDENT RECORD SYSTEM")
        print("========================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Count Students")
        print("5. Exit")
        
        try:
            choice = int(input("Enter any option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        # 1. ADD STUDENT
        if choice == 1:
            name = input("Name: \n").strip()
            age = input("Age: \n").strip()
            score = input("Score: \n").strip()

            # "a" (append) mode creates the file if missing, and won't overwrite existing text
            with open(file_path, "a") as file:
                file.write(f"{name},{age},{score}\n")
            
            print(f"\nSuccessfully added {name} to the system!")

        # 2. VIEW STUDENTS
        elif choice == 2:
            print("\n--- Current Student Records ---")
            if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
                print("No records found.")
            else:
                with open(file_path, "r") as file:
                    for line in file:
                        # Split commas to display neatly
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            print(f"Name: {parts[0]} | Age: {parts[1]} | Score: {parts[2]}")

        # 3. SEARCH STUDENT
        elif choice == 3:
            search_name = input("Enter student name to search: \n").strip().lower()
            found = False
            
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    for line in file:
                        parts = line.strip().split(",")
                        if len(parts) == 3 and parts[0].lower() == search_name:
                            print(f"\nStudent Found:\nName: {parts[0]}\nAge: {parts[1]}\nScore: {parts[2]}")
                            found = True
                            break
            
            if not found:
                print(f"Student '{search_name}' not found.")

        # 4. COUNT STUDENTS
        elif choice == 4:
            count = 0
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    # Count non-empty lines
                    count = sum(1 for line in file if line.strip())
            print(f"\nTotal students registered: {count}")

        # 5. EXIT
        elif choice == 5:
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

# Run the project
if __name__ == "__main__":
    studentRecordSystem()
