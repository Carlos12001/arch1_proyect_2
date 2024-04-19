def generate_letter(char: int):
    if char == 32:
        return " "
    elif char == 44:
        return ","
    elif char == 46:
        return "."
    elif char == 65:
        return "A"
    elif char == 66:
        return "B"
    elif char == 67:
        return "C"
    elif char == 68:
        return "D"
    elif char == 69:
        return "E"
    elif char == 70:
        return "F"
    elif char == 71:
        return "G"
    elif char == 72:
        return "H"
    elif char == 73:
        return "I"
    elif char == 74:
        return "J"
    elif char == 75:
        return "K"
    elif char == 76:
        return "L"
    elif char == 77:
        return "M"
    elif char == 78:
        return "N"
    elif char == 79:
        return "O"
    elif char == 80:
        return "P"
    elif char == 81:
        return "Q"
    elif char == 82:
        return "R"
    elif char == 83:
        return "S"
    elif char == 84:
        return "T"
    elif char == 85:
        return "U"
    elif char == 86:
        return "V"
    elif char == 87:
        return "W"
    elif char == 88:
        return "X"
    elif char == 89:
        return "Y"
    elif char == 90:
        return "Z"
    else:
        return "*"

def my_abs(x:int)->int:
    mask = x >> 31
    return (x + mask) ^ mask

def bresenham(x1:int, y1:int, x2:int, y2:int)->list[(int, int)]:
    points = []
    dx = my_abs(x2 - x1)
    dy = my_abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    if dx > dy:
        err = dx >> 1 # Use logical right shift to divide by 2
        while x != x2:
            points.append((x, y)) # In Assembly this will be save on memory
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy >> 1 # Use logical right shift to divide by 2
        while y != y2:
            points.append((x, y)) # In Assembly this will be save on memory
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x2, y2))  # Make sure the endpoint is included
    return points

if __name__ == "__main__":
    l = [ord(" "),ord(","),ord(".")] + list(range(ord("A"),ord("Z")+1))
    assert all(generate_letter(i)==chr(i) for i in l),"failed"   
    


