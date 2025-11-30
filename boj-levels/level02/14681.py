x = int(input())
y = int(input())

def find_quadrant(x:int, y:int) -> None:
    if x and y:
        if x > 0 and y > 0:
            print(1)
        if x < 0 and y > 0:
            print(2)
        if x < 0 and y < 0:
            print(3)
        if x > 0 and y < 0:
            print(4)

find_quadrant(x, y)