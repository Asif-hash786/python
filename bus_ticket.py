# Bus Ticket Reservation System

bus = {
    "bus_number": "KA01AB1234",
    "route": ("Bangalore", "Mysore"),
    "fare": 250
}

total_seats = 10

booked_seats = set()

passengers = []

while True:

    print("\n========== BUS RESERVATION ==========")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Passenger List")
    print("5. Exit")
    print("=====================================")

    choice = int(input("Enter choice: "))

    if choice == 1:

        print("\nSeat Status:")

        for seat in range(1, total_seats + 1):

            if seat in booked_seats:
                print(f"Seat {seat}: BOOKED")
            else:
                print(f"Seat {seat}: AVAILABLE")


    elif choice == 2:

        seat = int(input("Enter seat number: "))

        if seat < 1 or seat > total_seats:
            print("Invalid seat number.")

        elif seat in booked_seats:
            print("Seat already booked.")

        else:

            name = input("Enter passenger name: ")

            passenger = {
                "name": name,
                "seat": seat
            }

            passengers.append(passenger)
            booked_seats.add(seat)

            print("Seat booked successfully.")


    elif choice == 3:

        seat = int(input("Enter seat number: "))

        if seat in booked_seats:

            booked_seats.remove(seat)

            for passenger in passengers:

                if passenger["seat"] == seat:
                    passengers.remove(passenger)
                    break

            print("Booking cancelled.")

        else:
            print("Seat is not booked.")


    elif choice == 4:

        print("\n========== PASSENGERS ==========")

        if len(passengers) == 0:
            print("No passengers.")

        else:

            for passenger in passengers:

                print(
                    f"Seat {passenger['seat']} - "
                    f"{passenger['name']}"
                )


    elif choice == 5:

        print("Thank you for using the reservation system.")
        break

    else:

        print("Invalid choice.")