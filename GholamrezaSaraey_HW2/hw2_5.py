def binary_search(
        item: int, 
        *args: int, 
        start: int = 0,
        end: int = None) -> int | None:
    
    end = end if end is not None else len(args) -1
    if start > end: 
        raise ValueError ("Item not found!!!!!")

    middle = (start + end) // 2
    if item < args[middle]:
        return binary_search(item, *args, start=start, end=middle-1)
    elif item > args[middle]:
        return binary_search(item, *args, start=middle+1, end=end)
    
    return middle

print (binary_search(4, 1, 2, 3, 5, 7, 11, 13))