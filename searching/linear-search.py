def linear(num):
    array = [12,52,63,96,85,74,125];
    for i, value  in enumerate(array):
        if num == value:
            print(f"Found {num} at index {i}")
            return True;
    return False

print(linear(56))