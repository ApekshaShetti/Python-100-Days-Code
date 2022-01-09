# students_scores = {
#     "Apeksha": 88,
#     "Neha": 75,
#     "Zaid": 91,
#     "Vinay": 69,
# }
# students_grades = {}
# for i in students_scores:
#     score = students_scores[i]
#     if score > 90:
#         students_grades[i] = "Outstanding"
#     elif score > 80:
#         students_grades[i] = "Exceeds Expectation"
#     elif score > 70:
#         students_grades[i] = "Acceptable"
#     else:
#         students_grades[i] = "fail"

# print(students_grades)


# Nesting dictionary in dictionary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille"], "total_visits": 12},
#     "Germany": {"Berlin": 2, "Hamburg": 1},
# }
# print(travel_log)


# Nesting dictionary in list

# travel_log = [
#     {
#         "country_visited": "France",
#         "cities_visited": ["Paris", "Lille"],
#         "total_visits": 12,
#     },
#     {
#         "country_visited": "Germany",
#         "cities_visited": ["Berlin", "hamburg"],
#         "total_visits": 15,
#     },
# ]


# def add_new_country(country_visited, cities_visited, total_visits):
#     new_country = {}
#     new_country["country_visited"] = country_visited
#     new_country["cities_visited"] = cities_visited
#     new_country["total_visits"] = total_visits
#     travel_log.append(new_country)


# add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
# print(travel_log)

import os

logo = (
    """)
                         ___________
                         \         /
                          )_______(
                          |"""
    """"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""
    """"(
                         /_________\
                         `'-------'`
                       .-------------.
                       /_______________\
"""
)

print(logo)

dict = {}


def highest_bid(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}")


bidding_finished = False

while not bidding_finished:
    name = input("What is your name: \n")
    bidding_amt = int(input("What's your bid?:  \n$"))
    dict = [name] = bidding_amt
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.  \n")
    if should_continue == "yes":
        os.system("cls")
    elif should_continue == "no":
        bidding_finished = True
        highest_bid(dict)
