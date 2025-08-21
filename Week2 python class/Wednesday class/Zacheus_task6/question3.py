seats= set( range(1,51))
print(seats)
for seat in range(1,51):
    user_seat= int(input("pick any seat number of your choice:"))
    seats.discard(user_seat)
    print("Remaining seat:",seats)