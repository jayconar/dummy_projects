def print_theatre(theatre):
    for row_idx, row in enumerate(theatre, start=1):
        row_label = chr(ord('A') + row_idx - 1)
        seats = ['X' if status == 'X' else f"{seat + 1}" if status == 'O'
                 else 'X ' for seat, status in enumerate(row)]
        print(f"{row_label}   {'   '.join(seats)}   {row_label}")


def get_available_seats(theatre, row):
    row_index = ord(row) - ord('A')
    return [seat + 1 for seat, status in enumerate(theatre[row_index])
            if status == 'O']


def calculate_price(row, seat):
    if row in ['A', 'B', 'C']:
        price = 100
    elif row in ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
        price = 200
    else:
        price = 300

    if seat in [1, 2, 3, 16, 17, 18]:
        price -= 30

    return price


def reserve_seats(theatre, row, selected_seats, reserved_seats):
    row_index = ord(row) - ord('A')
    total_price = 0
    [reserved_seats.append(f"{row}{seat}") for seat in selected_seats]
    for seat in reserved_seats:
        price = calculate_price(seat[0], int(seat[1:]))
        total_price += price
        theatre[row_index][int(seat[1:]) - 1] = 'X ' if int(seat[1:]) > 9 else 'X'

    return total_price


def main():
    rows = 18
    seats_per_row = 18
    theatre = [["O"] * seats_per_row for _ in range(rows)]
    reserved_seats = []

    while True:
        print_theatre(theatre)
        user_row = input("\nEnter the row (A-R): ").upper()

        if user_row not in "ABCDEFGHIJKLMNOPQR":
            print("Invalid row. Please enter a valid row (A-R).")
            continue

        available_seats = get_available_seats(theatre, user_row)

        if not available_seats:
            print(f"No available seats in row {user_row}. Please choose another row.")
            continue

        print(f"Available seats in row {user_row}: {', '.join(map(str, available_seats))}")

        try:
            selected_seats = set(
                int(seat) for seat in input("Enter the seat numbers (comma-separated): ").split(',')
            )
            list(selected_seats)
        except ValueError:
            print("Invalid seat number. Please enter valid seat numbers.")
            continue

        if any(seat not in available_seats for seat in selected_seats):
            print("Invalid seat selection. Please choose from the available seats.")
            continue

        total_price = reserve_seats(theatre, user_row, selected_seats, reserved_seats)

        print(f"Reserved seats: {', '.join(reserved_seats)}")
        print(f"Total Price: {total_price} currency units")

        another_transaction = input("Do you want to make another reservation? (yes/no): ").lower()
        if another_transaction != 'yes':
            break

    print("Thank you for using the seat reservation system!")


if __name__ == "__main__":
    main()
