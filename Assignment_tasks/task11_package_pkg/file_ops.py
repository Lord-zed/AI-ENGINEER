from pathlib import Path


import csv 


def save_participant(path, participant_dict):
    if path.exists():
        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())
    else:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("Name, Age, Phone, Track\n")
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())
    
def load_participant(path):
    with open(path, "r", encoding="utf-8") as f:
        participants = []
        reader = csv.reader(f)
        for row_number, row in enumerate(reader):
            if row_number == 0:
                print(f"Headers: {"\t|".join(row)}")
                print("-"*60)
            else:
                name, age, phone, track = row 
                print(f"{name} \t| {age} \t| {phone} \t| {track}")

    return participants