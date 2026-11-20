def view_slots(slots):
    print("\n--- Available Parking Slots ---")

    for slot, vehicle in slots.items():
        if vehicle is None:
            print(f"Slot {slot}: Available")
        else:
            print(f"Slot {slot}: Occupied by {vehicle}")