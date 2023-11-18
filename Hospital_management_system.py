import datetime as dt

file_name = "hospital.txt"


def get_max_patient_id():
    try:
        max_id = 0
        with open(file_name, 'r') as file:
            for line in file:
                patient_id = int(line.split(" | ")[0])
                if patient_id > max_id:
                    max_id = patient_id
        return max_id
    except FileNotFoundError:
        return 0

def create_patient():
    max_pid = get_max_patient_id()
    next_pid = max_pid + 1

    print(f"Suggested patient ID: {next_pid}")

    while True:
        pid = input("Enter patient id (or press Enter to use the suggested ID): ")
        if pid:
            upid = int(pid)
        else:
            upid = next_pid

        if upid <= max_pid:
            print("Please enter a unique patient id.")
        else:
            break

    name = input("Enter patient name: ")
    dob = input("Enter patient's dob: ")
    gender = input("Enter patient's gender: ")
    cr_dt = dt.datetime.now()
    date_time = str(cr_dt)
    date = date_time.split(" ")[0]
    time = date_time.split(" ")[1]
    imp_abt_pt = input("Important Points about patient's Health: ")


    with open(file_name, 'a') as file:
        line = f"{upid} | {name} | {dob} | {gender} | {date} | {time} | {imp_abt_pt}"
        file.write(line + '\n')
        print("Patient's Data Added Successfully.")
def show_patient_data():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.split(" | "))
    except FileNotFoundError:
        print("No patient data found.")

def search_patient_by_id():
    search_id = int(input("Enter patient ID to search: "))
    found = False
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if int(line.split(" | ")[0]) == search_id:
                    print(line.split(" | "))
                    found = True
                    break
    except FileNotFoundError:
        print("No patient data found.")
    if not found:
        print(f"No patient with ID {search_id} found.")

def delete_patient():
    show_patient_data()
    search_id = int(input("Enter patient ID to delete: "))
    found = False
    patient_data = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                if int(line.split(" | ")[0]) == search_id:
                    print("Patient found:")
                    print(line.split(" | "))
                    found = True
                else:
                    patient_data.append(line)

    except FileNotFoundError:
        print("File not found")

    if not found:
        print(f"No patient with ID {search_id} found.")
    else:
        confirm = input("Are you sure you want to delete this patient? (yes/no): ").lower()
        if confirm == 'yes':
            with open(file_name, 'w') as file:
                file.writelines(patient_data)
            print(f"Patient with ID {search_id} has been deleted.")
        else:
            print("Deletion canceled.")

def delete_all_data():
    show_patient_data()
    confirm = input("Are you sure you want to delete all data? (yes/no): ").lower()
    if confirm == 'yes':
        with open(file_name, 'w') as file:
            file.writelines("")
        print("All data has been deleted.")
    else:
        print("Deletion canceled.")

def update_patient():
    show_patient_data()

    search_id = int(input("Enter patient ID to update: "))
    found = False
    patient_data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if int(line.split(" | ")[0]) == search_id:
                    print("Patient found:")
                    print(line.split(" | "))
                    found = True

                    name = input("Enter new patient's name: ")
                    dob = input("Enter new patient's dob: ")
                    gender = input("Enter new patient's gender: ")
                    cr_dt = dt.datetime.now()
                    date_time = str(cr_dt)
                    date = date_time.split(" ")[0]
                    time = date_time.split(" ")[1]
                    imp_abt_pt = input("Important Points about patient's Health: ")

                    line = f"{search_id} | {name} | {dob} | {gender} | {date} | {time} | {imp_abt_pt}\n"
                    patient_data.append(line)
                else:
                    patient_data.append(line)
    except FileNotFoundError:
        print("Files not found")

    if not found:
        print(f'No patient id {search_id} found')
    else:
        with open(file_name, 'w') as file:
            file.writelines(patient_data)
            print(f"Patient with ID {search_id} has been updated.")




if __name__ == "__main__":
    while True:
        print("""
    Enter 1 for Add a New patient
    Enter 2 for Show All patients
    Enter 3 for search a specific Patient
    Enter 4 for delete a patient
    Enter 5 to delete the all data
    Enter 6 to update a patient
    Enter 7 for exit
        """)

        option = int(input("Choose a option: "))
        if option == 1:
            create_patient()
        elif option == 2:
            show_patient_data()
        elif option == 3:
            search_patient_by_id()
        elif option == 4:
            delete_patient()
        elif option == 5:
            delete_all_data()
        elif option == 6:
            update_patient()
        if option == 7:
            print("See You Next Time.")
            break

