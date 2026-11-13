def parse_request(text):
    if not isinstance(text, str) or '->' not in text:
        return None
    parts = text.split('->')
    if len(parts) != 2:
        return None
    start_str, end_str = parts[0].strip(), parts[1].strip()
    if not start_str or not end_str:
        return None
    try:
        return int(start_str), int(end_str)
    except ValueError:
        return None


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        return 0
    floors = []
    for item in floors_csv.split(','):
        cleaned = item.strip()
        if not cleaned:
            return 0
        try:
            floors.append(int(cleaned))
        except ValueError:
            return 0
    if len(floors) < 2:
        return 0
    return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))


def load_percent(text):
    if not isinstance(text, str) or ' of ' not in text:
        return None
    parts = text.split(' of ')
    if len(parts) != 2:
        return None
    load_str, cap_str = parts[0].strip(), parts[1].strip()
    if not load_str or not cap_str:
        return None
    try:
        load = int(load_str)
        capacity = int(cap_str)
    except ValueError:
        return None
    if load < 0 or capacity <= 0:
        return None
    return load * 100 // capacity


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()