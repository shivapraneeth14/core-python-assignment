def book_seat(booked_seats, seat_number, total_seats):
    if seat_number < 1 or seat_number > total_seats:
        print("Invalid seat number")
    elif seat_number in booked_seats:
        print("Seat already booked")
    else:
        booked_seats.append(seat_number)


def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
    else:
        print("Seat not booked")


def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


# Example usage
total_seats = 10
booked_seats = [2, 5, 7]

book_seat(booked_seats, 3, total_seats)
cancel_seat(booked_seats, 5)

available_seats = get_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)
