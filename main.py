import random
numbers = []


def generateArray():
    l = int(input("Insert the desired length: "))
    for i in range(0, l):
        numbers.append(random.randint(0, 10))


def sort(numbers):
    for j in range(0, len(numbers) - 1):
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]


def main():
    print("Welcome to bubble sort, a random array will be generated and then sorted")
    generateArray()
    print("The generated array: ", numbers)
    sort(numbers)
    print("The sorted array: ", numbers)


main()
