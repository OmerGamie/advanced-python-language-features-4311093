# Use special methods to compare objects to each other

class Employee():
    def __init__(self, fname, lname, level, years_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = years_service

    # Implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


# define some employees
dept = []
dept.append(Employee("Omer", "Gamie", 8, 9))
dept.append(Employee("Mona", "Ahmed", 5, 11))
dept.append(Employee("John", "Cena", 7, 7))
dept.append(Employee("Ibrahim", "Sharief", 6, 14))
dept.append(Employee("Ali", "Hassan", 6, 13))

# Who's more senior?
print(dept[1] > dept[3])
print(dept[2] < dept[4])

# Sort the items
for emp in dept:
    print(emp.lname)
print("-----------")

emps = sorted(dept)
for emp in emps:
    print(emp.lname)
