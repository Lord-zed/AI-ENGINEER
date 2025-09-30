from pathlib import Path
import file_ops


def work_path():
    workspace = Path("participant_pkg")
    file_path = workspace / 'participants.csv'
    return file_path

def participant():

    while True:
        participant_data = {}

        while True:
            name = input("Enter name: ").strip()
            if (name.isalpha()) or len(name) != 0 and not name.isdigit():
                participant_data['name'] = name
                break
            print("Name must be alphabet and not empty")
            
        while True:
            age = input("Enter age: ")
            try:
                new_age = int(age)
                if new_age <= 150:
                    participant_data['age'] = new_age
                    break
                else:
                    print("Age cannot be creater than 150")
            except ValueError:
                print('Age must be number')
                    
        while True:
            phone = input("Enter phone number: ")
            if phone.isdigit() and len(phone) == 11:
               participant_data['phone'] = phone
               break
            print("Phone number must be numbers and 11 digits")
                    
        while True:
            track = input("Enter track: ")
            if len(track) != 0 and not track.isnumeric():
                participant_data['track'] = track
                break
            print("Track cannot not be empty and cannot contain letters")

        return participant_data


def participant_list(n):
    localpath = work_path()
    for i in range(n):
        participant_dict = participant()
        file_ops.save_participant(localpath, participant_dict)

def participant_details():
    path = work_path()
    return file_ops.load_participant(path)


def main():
    try:
        choice = int(input("Input 1 to Save Participant Details and Input 2 to View Participant Details and Input 3 to Exit: " ))
        if choice == 1:
            participant_num = int(input("Input the number of Participant's to save: "))
            participant_list(participant_num)
        elif choice == 2:
            print("\nParticipant Details:")
            print(participant_details())
        elif choice == 3:
            print("Exiting program... Thank you!")
            return 
            
    except ValueError as ve:
        print("Error: Input correct option!", ve)
        
main()
