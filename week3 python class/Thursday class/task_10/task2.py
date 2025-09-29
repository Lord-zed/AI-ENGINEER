# Create a Unique Voters Registration System







voters = set()  # Set to store unique voter names

while True:
        name = input("Enter voter name (or type 'done' to finish): ").strip()

        try:
             name = str(name)
        except:
             print("Name cannot be an integer")

        if name.lower() == 'done':
            break

        if name in voters:
            print(f" Warning: {name} has already registered!")
        else:
            voters.add(name)
            print(f"✅ {name} registered successfully.")

print(f"\nTotal unique voters registered: {len(voters)}")

# Run the registration function
