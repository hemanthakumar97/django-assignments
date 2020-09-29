from django import template

register = template.Library()

def is_lower(name):
    for i in name:
        if "A"<=i<="Z":
            return False
    return True
    
def is_upper(name):
    for i in name:
        if "a"<=i<="z":
            return False
    return True

register.filter("islower",is_lower)
register.filter("isupper",is_upper)




