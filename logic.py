def average(marks):
    return sum(marks)/len(marks)
def grade(avg):
    if avg>=90:
        return "A+"
    if avg>=80 and avg<=89:
        return "A"
    if avg>=70 and avg<=79:
        return "B"
    if avg>=60 and avg<=69:
        return "C"
    if avg>=50 and avg<=59:
        return "D"
    if avg<50:
        return "F"