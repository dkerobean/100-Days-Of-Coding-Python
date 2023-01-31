#dictionaries

dictionary = {
    1: "one",
    2: "two",
    3: "threee"
}

print(dictionary[1])

dictionary[4] = "four"

#update
dictionary[3] = "three"

#wipe a dictionary
#dictionary = {}

#loop
for key in dictionary:
    print(dictionary[key])

#exercise

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectation"
    elif score >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)


#nesting

travel_log1 = {
    "France": {"cities_visited": ["Paris", "Accra", "Abuja"], "total_visits":12},
    "Germany": ["Berlin", "Hamburg"]

}

#excersie

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]

    }
]

def add_country(country, visits, cities):

    new_country = {}

    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities

    travel_log.append(new_country)


add_country("Russia", 2, ["Moscow","ukraine"])





