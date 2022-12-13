a = 2
b = [2,3,4]

match (type(a), type(b)):
    case (type(0), type([])):
        print("OK")

