def main():
    stops_bus1_start, stops_bus1_end, stops_bus2_start, stops_bus2_end = map(int, input().split())

    stops_set_bus1 = set(range(min(stops_bus1_start, stops_bus1_end), max(stops_bus1_start, stops_bus1_end) + 1))
    stops_set_bus2 = set(range(min(stops_bus2_start, stops_bus2_end), max(stops_bus2_start, stops_bus2_end) + 1))

    intersection = stops_set_bus1.intersection(stops_set_bus2)

    print(len(intersection))

if __name__ == "__main__":
    main()
