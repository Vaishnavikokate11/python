d = {} # empty dictonary
marks = {
    "Raj": 90,
    "Sham": 86,
    "vaishu": 67
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sham": 88, "harry": 94})
print(marks)
print(marks.get("Raj"))

print(marks.get("harry2")) #return none if not present
# print(marks["Raj2"]) #give error if not present

marks.pop("Sham")
print(marks)

marks.popitem()
print(marks)