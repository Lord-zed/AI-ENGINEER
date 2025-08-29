import csv
from pathlib import Path

def save_participant(path, participant_dict):
    # Check if file exists
    file_exists = path.exists()
    
    # Open file in append mode
    with open(path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'age', 'phone', 'track'])
        
        # Write header if file is new
        if not file_exists:
            writer.writeheader()
        
        # Write participant data
        writer.writerow(participant_dict)

def load_participants(path):
    participants = []
    
    # Check if file exists
    if not path.exists():
        return participants
    
    # Read all participants from file
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            participants.append(row)
    
    return participants


# # MAIN
# from pathlib import Path
# from participant_pkg import file_ops

# def get_valid_input(prompt, validation_func, error_msg):
#     while True:
#         value = input(prompt)
#         if validation_func(value):
#             return value
#         print(error_msg)

# def main():
#     # Define file path
#     csv_path = Path("workspace/contacts.csv")
    
#     # Create directory if it doesn't exist
#     csv_path.parent.mkdir(parents=True, exist_ok=True)
    
#     participants = []
    
#     print("Welcome to Contact Saver!")
#     print("Enter participant details (or type 'quit' to exit):")
    
#     while True:
#         # Get name
#         name = get_valid_input(
#             "\nEnter name: ",
#             lambda x: x.strip() != "" and x.lower() != 'quit',
#             "Name cannot be empty. Please try again."
#         )
        
#         if name.lower() == 'quit':
#             break
        
#         # Get age with validation
#         while True:
#             age_input = input("Enter age: ")
#             if age_input.lower() == 'quit':
#                 break
#             try:
#                 age = int(age_input)
#                 if age <= 0:
#                     print("Age must be a positive number. Please try again.")
#                 else:
#                     break
#             except ValueError:
#                 print("Invalid age. Please enter a number.")
        
#         if age_input.lower() == 'quit':
#             break
        
#         # Get phone number
#         phone = get_valid_input(
#             "Enter phone number: ",
#             lambda x: len(x.strip()) >= 7,  # Basic validation
#             "Phone number seems too short. Please try again."
#         )
        
#         # Get track
#         track = get_valid_input(
#             "Enter track: ",
#             lambda x: x.strip() != "",
#             "Track cannot be empty. Please try again."
#         )
        
#         # Create participant dictionary
#         participant = {
#             'name': name,
#             'age': age,
#             'phone': phone,
#             'track': track
#         }
        
#         # Save participant
#         try:
#             file_ops.save_participant(csv_path, participant)
#             print("Participant saved successfully!")
#         except Exception as e:
#             print(f"Error saving participant: {e}")
        
#         # Ask if user wants to add another participant
#         another = input("\nAdd another participant? (y/n): ").lower()
#         if another != 'y':
#             break
    
#     # Load and display all participants
#     try:
#         all_participants = file_ops.load_participants(csv_path)
#         print(f"\nSummary: {len(all_participants)} participants saved:")
#         for p in all_participants:
#             print(f"- {p['name']} ({p['age']}), Phone: {p['phone']}, Track: {p['track']}")
#     except Exception as e:
#         print(f"Error loading participants: {e}")

# if __name__ == "__main__":
#     main()