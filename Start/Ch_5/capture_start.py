# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
    case "":
        print("Hello, anonymous!")
    case "Omer" | "Gamie" as og:
        print(f"Hallo, Bruder, wie läuft bei dir, {og}")
    case name:
        print(f"Hello, {name}!")
