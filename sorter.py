"""Module to perform a bubble sort on a list."""


def sorter(data, first_count):
    """Sort the array in descending order using bubble sort."""
    for count in range(first_count):
        if data[count + 1] > data[count]:
            data[count], data[count + 1] = data[count + 1], data[count]
            print(data)


def main():
    """Main execution of the sorter script."""
    data = [1, 2, 3, 4, 5, 6]
    for first_count in range(len(data) - 1, 0, -1):
        print(first_count)
        sorter(data, first_count)
        print(data)


if __name__ == "__main__":
    main()
