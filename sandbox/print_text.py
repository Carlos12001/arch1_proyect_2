def my_abs(x:int)->int:
    mask = x >> 31
    return (x + mask) ^ mask

def bresenham(x1, y1, x2, y2, points_count):
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
            points_count += 1  # Increment counter
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy >> 1 # Use logical right shift to divide by 2
        while y != y2:
            points.append((x, y)) # In Assembly this will be save on memory
            points_count += 1  # Increment counter
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points.append((x2, y2))  # Make sure the endpoint is included
    points_count += 1
    return (points, points_count)

def points2pixel(letter,points,points_count):
    for i in range(points_count):
        x = points[i][0]
        y = points[i][1]
        if x == 0:
            letter[y] = 1
        elif x == 1:
            letter[y+6] = 1
        elif x == 2:
            letter[y+12] = 1
        elif x == 3:
            letter[y+18] = 1
        elif x == 4:
            letter[y+24] = 1
        else:
            return

def generate_letter(char):
    letter = [
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0
                ]
    if char == 32: # SPACE
        counter_points = 0
        points = []
        # bresenham
        points2pixel(letter,points,counter_points)
    elif char == 44: # COMMA
        counter_points = 0
        points = []
        
        result =  bresenham(4,1,3,2, counter_points)
        points += result[0]
        counter_points = result[1]


        
        points2pixel(letter,points,counter_points)
        
    elif char == 46: # POINT
        counter_points = 0
        points = []
        
        result =  bresenham(3,2,3,2, counter_points)
        points += result[0]
        counter_points = result[1]


        
        points2pixel(letter,points,counter_points)
        
        
    elif char == 65: # A
        counter_points = 0
        points = []

        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]

        result = bresenham(1,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]

        result =  bresenham(1,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]

        result = bresenham(3,1,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
        
        
    elif char == 66:#B
        counter_points = 0
        points = []
        
        result =  bresenham(1,4,1,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,1,2,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]

        points2pixel(letter,points,counter_points)
        
        
    elif char == 67:#C
        counter_points = 0
        points = []
        
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(4,1,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        points2pixel(letter,points,counter_points)
    elif char == 68:#D
        counter_points = 0
        points = []
        
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 69:#E
        counter_points = 0
        points = []
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(2,1,2,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(4,1,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 70:#F
        counter_points = 0
        points = []
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(2,1,2,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        points2pixel(letter,points,counter_points)
    elif char == 71:#G
        counter_points = 0
        points = []
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(1,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(4,1,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,2,2,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 72:#H
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(2,1,2,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(0,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        

        points2pixel(letter,points,counter_points)
    elif char == 73:#I
        counter_points = 0
        points = []
        result =  bresenham(0,0,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(1,2,3,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(4,0,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        points2pixel(letter,points,counter_points)
    elif char == 74:#J
        counter_points = 0
        points = []
        result =  bresenham(0,0,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
                
        result =  bresenham(1,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 75:#K
        counter_points = 0
        points = []
        
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        result =  bresenham(2,1,2,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,3,1,3, counter_points)
        points += result[0]
        counter_points = result[1]  
              
        result =  bresenham(0,4,0,4, counter_points)
        points += result[0]
        counter_points = result[1]       
        
        result =  bresenham(3,3,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        points2pixel(letter,points,counter_points)
    elif char == 76:#L
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 77:#M
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,1,1,1, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,2,2,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,3,1,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        points2pixel(letter,points,counter_points)
    elif char == 78:#N
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,1,1,1, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,2,2,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,3,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 79:#O
        counter_points = 0
        points = []
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        

        points2pixel(letter,points,counter_points)
    elif char == 80:#P
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,1,2,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,1,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 81:#Q
        counter_points = 0
        points = []
        
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,2,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,3,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 82:#R
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,1,2,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,1,0,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,1,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,3,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        points2pixel(letter,points,counter_points)
        
        
        
    elif char == 83:#S
        counter_points = 0
        points = []
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,0,2,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,1,2,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,4,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,0,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 84:#T
        counter_points = 0
        points = []
        
        result =  bresenham(0,0,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,2,4,2, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 85:#U
        counter_points = 0
        points = []

        result =  bresenham(0,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    elif char == 86:#V
        counter_points = 0
        points = []
        
        result =  bresenham(0,0,1,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,1,3,1, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,2,4,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,4,1,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,3,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        points2pixel(letter,points,counter_points)
    elif char == 87:#W
        counter_points = 0
        points = []
        result =  bresenham(0,0,3,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,2,3,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        points2pixel(letter,points,counter_points)
    elif char == 88:#X
        counter_points = 0
        points = []
        
        
        result =  bresenham(0,0,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        result =  bresenham(4,0,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        

        points2pixel(letter,points,counter_points)
    elif char == 89:#Y
        counter_points = 0
        points = []
        result =  bresenham(0,0,1,1, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,3,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,2,4,2, counter_points)
        points += result[0]
        counter_points = result[1]
        
        
        points2pixel(letter,points,counter_points)
    elif char == 90:#Z
        counter_points = 0
        points = []
        
        
        result =  bresenham(0,0,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(3,1,1,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,0,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    else:
        counter_points = 0
        points = []
        result =  bresenham(0,0,4,0, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(4,1,4,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(0,1,0,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,3,3,3, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(1,4,3,4, counter_points)
        points += result[0]
        counter_points = result[1]
        
        result =  bresenham(2,2,2,2, counter_points)
        points += result[0]
        counter_points = result[1]
        points2pixel(letter,points,counter_points)
    return letter

if __name__ == "__main__":
    l = [ord(" "),ord(","),ord(".")] + list(range(ord("A"),ord("Z")+1))
    print(f"cases total: {len(l)}")
    
    letter = generate_letter(ord("A"))
    
    s = ""


    
    for i,pixel in enumerate(letter,1):
        s += str(pixel) if pixel==1 else " "
        s += "\n" if i%6==0 else " "
    print(s)
