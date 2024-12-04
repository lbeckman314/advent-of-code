def sortList(arr: list) -> list:
    """
    Sorts and returns a given list

    Args:
        arr (list): Unsorted list

    Returns:
        list: Sorted list
    """
    return sorted(arr)

def diffLists(left: list[int], right: list[int]) -> list[int]:
    """
    Compare two sorted lists and return the difference between each element: O(n)

    Args:
        left (list[int]): Sorted list
        right (list[int]): Sorted list

    Returns:
        list[int]: List of differences
    """
    diff = []
    for i in range(len(left)):
        d = abs(left[i] - right[i])
        diff.append(d)

    return diff

def sumList(arr: list) -> int:
    """
    Sum all elements in a given list

    Args:
        arr (list): List of integers

    Returns:
        int: Total sum
    """
    s = 0
    for i in arr:
        s += i
    return s

def similarLists(left: list[int], right: list[int]) -> int:
    """
    Calculate a Similarity score between two lists: O(n^2)
    https://adventofcode.com/2024/day/1#part2

    Args:
        left (list[int]): Sorted list
        right (list[int]): Sorted list

    Returns:
        int: Similarity score
    """
    similarity = 0
    for i in range(len(left)):
        occurance = right.count(left[i])
        similarity += (occurance * left[i])

    return similarity

def main():
    """
    Day 1 Advent of Code 2024
    https://adventofcode.com/2024/day/1
    """
    left = []
    right = []

    for line in open('input.txt').readlines():
        arr = line.strip().split()
        left.append(int(arr[0]))
        right.append(int(arr[1]))
    
    left = sortList(left)
    right = sortList(right)

    diff = diffLists(left, right)

    sum = sumList(diff)
    print(f"DEBUG: sum: {sum}")

    similarity = similarLists(left, right)
    print(f"DEBUG: similarity: {similarity}")

if __name__ == '__main__':
    main()
