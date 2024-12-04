def checkSafety(arr: list) -> bool:
    """
    Check if the given list is Safe or Unsafe

    Args:
        arr (list): Level reports

    Returns:
        bool: True if the given list is safe, False otherwise
    """
    direction = None
    for prev, curr in zip(arr, arr[1:]):
        prev = int(prev)
        curr = int(curr)
        
        if prev < curr:
            if direction == "decreasing":
                return False
            direction = "increasing"
        elif prev > curr:
            if direction == "increasing":
                return False
            direction = "decreasing"
        else:
            return False

        diff = abs(prev - curr)
        if diff < 1 or diff > 3:
            return False

    return True


def main():
    numSafe = 0
    for line in open('input.txt').readlines():
        arr = line.strip().split() 
        if not arr:
            continue
        safe = checkSafety(arr)
        if safe:
            numSafe += 1
        else:
            for i in range(len(arr)):
                list = arr.copy()
                list.pop(i)
                safe = checkSafety(list)

                if safe:
                    numSafe += 1
                    break
    print("DEBUG: numSafe:", numSafe)
       

if __name__ == "__main__":
    main()
