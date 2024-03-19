import secrets

# num = secrets.randbelow(3)

# def http_error(status):
#     match status:
#         case 0:
#             return 'hi'
#         case 1:
#             return 'bye'
#         case 2:
#             return 'ok'
        
# print(f"{num} / {http_error(num)}")

class Point:
    x: int
    y: int

    def __init__(self, x,y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("origin")
        case Point(x=0, y=y):
            print(f"Y = {y}")

point = Point(0,1)
where_is(point)