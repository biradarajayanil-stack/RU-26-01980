from collections import deque

# Bus network (Dictionary of Dictionaries)

bus_network = {
    "Durg": {
        "Bhilai": 10,
        "Raipur": 40,
        "Rajnandgaon": 45
    },
    "Bhilai": {
        "Durg": 10,
        "Raipur": 30
    },
    "Raipur": {
        "Bhilai": 30,
        "Bilaspur": 110,
        "Dhamtari": 80,
        "Durg": 40
    },
    "Bilaspur": {
        "Raipur": 110
    },
    "Dhamtari": {
        "Raipur": 80
    },
    "Rajnandgaon": {
        "Durg": 45
    },
    "Jagdalpur": {
        "Kondagaon": 75
    },
    "Kondagaon": {
        "Jagdalpur": 75
    }
}

FARE_PER_KM = 1.50


# Find correct stop name
def find_stop(name):
    for stop in bus_network:
        if stop.lower() == name.strip().lower():
            return stop
    return None


# Show all bus stops
def show_all_stops():
    print("\nAvailable Bus Stops:")
    for stop in bus_network:
        print(stop)


# Show direct connections
def show_connections(name):
    stop = find_stop(name)

    if stop is None:
        print(f"Stop '{name.strip()}' not found.")
        return

    connections = bus_network[stop]

    details = ", ".join(
        f"{neighbour} ({distance} km)"
        for neighbour, distance in connections.items()
    )

    print(f"{stop} connects to: {details}")


# Find shortest route using BFS
def bfs(source, destination):

    if source == destination:
        return [source]

    queue = deque([[source]])
    visited = {source}

    while queue:
        route = queue.popleft()
        current = route[-1]

        for neighbour in bus_network[current]:

            if neighbour not in visited:
                new_route = route + [neighbour]

                if neighbour == destination:
                    return new_route

                visited.add(neighbour)
                queue.append(new_route)

    return None


# Find route and calculate fare
def find_route(from_stop, to_stop):

    source = find_stop(from_stop)
    destination = find_stop(to_stop)

    if source is None:
        print(f"Stop '{from_stop.strip()}' not found.")
        return

    if destination is None:
        print(f"Stop '{to_stop.strip()}' not found.")
        return

    if source == destination:
        print("Source and destination are the same.")
        print("Distance: 0 km.")
        print("Fare: Rs. 0.00")
        return

    route = bfs(source, destination)

    if route is None:
        print(f"No route available between {source} and {destination}.")
        return

    distance = 0

    for i in range(len(route) - 1):
        distance += bus_network[route[i]][route[i + 1]]

    fare = distance * FARE_PER_KM

    print("Route:", " -> ".join(route))
    print(f"Stops: {len(route)} | Distance: {distance} km | Fare: Rs. {fare:.2f}")


# Main menu
def main():

    while True:

        print("\n================================")
        print("   BUS ROUTE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Show all stops")
        print("2. Show connections")
        print("3. Find route")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_stops()

        elif choice == "2":
            stop = input("Enter stop name: ")
            show_connections(stop)

        elif choice == "3":
            from_stop = input("From: ")
            to_stop = input("To: ")
            find_route(from_stop, to_stop)

        elif choice == "4":
            print("Thank you for using Bus Route Management System!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()