def parking_status(slots):
    total = len(slots)

    occupied = sum(
        1 for vehicle in slots.values()
        if vehicle is not None
    )

    available = total - occupied

    print("\n--- Parking Status ---")
    print("Total Parking Slots:", total)
    print("Occupied Slots:", occupied)
    print("Available Slots:", available)