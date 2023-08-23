# Demonstrate template string functions
from string import Template

# Usual string formatting with f-strings
str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# Create a template with placeholders
templ = Template("You're watching ${title} by ${author}")

# The substitute method with keyword arguments
str2 = templ.substitute(title="Advanced Python: Language Features",
                        author="Joe Marini")
print(str2)

# The substitute method with a dictionary
data = {
    "author": "Joe Marini",
    "title": "Advanced Python: Language Features"
}

str3 = templ.substitute(data)
print(str3)
