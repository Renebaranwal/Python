flights = (
    ("AA123", "NYC", "LAX", 360),
    ("BA456", "LAX", "CHI", 270),
    ("CA789", "CHI", "NYC", 120),
    ("DA012", "NYC", "MIA", 180),
    ("EA345", "MIA", "LAX", 330)
)


print("Flights originating from NYC:")
for flight in flights:
    if flight[1] == "NYC":
        print(flight)


sorted_flights = sorted(flights, key=lambda x: x[3])
print("\nFlights sorted by duration:")
for flight in sorted_flights:
    print(flight)


longest_flight = max(flights, key=lambda x: x[3])
print(f"\nFlight with longest duration: {longest_flight}")
