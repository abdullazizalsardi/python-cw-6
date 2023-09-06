person = {

        "name": "abdulaziz",
        "age": 17,
        "hobbies": ["running","shoting","mma"],

}
print(person["name"])
print(person["age"])
person["age"] = 18
person["country"] = "kuwait"
print(person)
print(len(person))
person["hobbies"].append("sleeping")
def check_hobbies(person) :
    if len(person["hobbies"]) > 3 :
        print("WOW YOU ARE AMAZING")
check_hobbies(person)
    