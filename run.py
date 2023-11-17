from hospital import *

while True:
    print("""
Enter 1 for Add a New patient
Enter 2 for Show All patients
Enter 3 for search a specific Patient
Enter 4 for delete a patient
Enter 5 to delete the all data
Enter 6 for exit
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
    if option == 6:
        print("See You Next Time.")
        break


