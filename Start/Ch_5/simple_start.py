# Simple pattern matching using literal values

x = None

# Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case "Zero":
        print(0)
    case None:
        print("Nee")
