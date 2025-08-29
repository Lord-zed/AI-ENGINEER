#This is the first line in notes.txt
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
    participants = []n
    
    # Check if file exists
    if not path.exists():
        return participants
    
    # Read all participants from file
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            participants.append(row)
    
    return participants