def book_slot(slots, slot, vehicle):
    # Check whether slot exists
    if slot not in slots:
        print("Invalid parking slot!")
        return False

    # Check whether slot is already occupied
    if slots[slot] is not None:
        print("Sorry! This parking slot is already occupied.")
        return False

    # Check vehicle number
    if not vehicle.strip():
        print("Please enter a valid vehicle number.")
        return False

    # Book the parking slot
    slots[slot] = vehicle.strip().upper()

    print("\nParking slot booked successfully!")
    print("Slot Number:", slot)
    print("Vehicle Number:", slots[slot])

    return True


def book_first_available(slots, vehicle):
    # Find the first available slot
    for slot, occupied in slots.items():
        if occupied is None:
            return book_slot(slots, slot, vehicle)

    print("Sorry! No parking slots available.")
    return False


def cancel_booking(slots, slot):
    # Check whether slot exists
    if slot not in slots:
        print("Invalid parking slot!")
        return False

    # Check whether slot is booked
    if slots[slot] is None:
        print("This parking slot is already empty.")
        return False

    vehicle = slots[slot]

    # Cancel booking
    slots[slot] = None

    print("\nBooking cancelled successfully!")
    print("Slot Number:", slot)
    print("Vehicle Number:", vehicle)

    return True


if __name__ == "__main__":
    slots = {
        1: None,
        2: None,
        3: "KA01AB1234",
        4: None
    }

    print("SMART PARKING BOOKING SYSTEM")

    print("\nInitial Parking Slots:")
    print(slots)

    # Test booking
    book_slot(slots, 1, "KA05CD5678")

    # Test automatic booking
    book_first_available(slots, "KA03EF1234")

    # Test cancellation
    cancel_booking(slots, 1)

    # Final parking status
    print("\nFinal Parking Slots:")
    print(slots) 

    

    