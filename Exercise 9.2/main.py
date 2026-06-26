travel_log = [
{
    "State": "HP",
    "places_visited" : ["Shimla", "Manali", "Sanga Valley"],
    "total_visited" : 3,
},
{
    "State": "UP",
    "places_visited" : ["Kanpur", "Ayodhya"],
    "total_visited" : 2,
},
]
# do not change code above this line
# Task 1: Write a function that will allow you to add a new state to the travel_log. 
def add_new_state(state_visited,palces_visits,total_visits):
    new_state = {}
    new_state["State"] = state_visited
    new_state["places_visited"] = palces_visits
    new_state["total_visited"] = total_visits
    travel_log.append(new_state)

# do not change code below this line
add_new_state("MP",["Bhopal","Ujjain","Indore","Gwalior"],4)
print(travel_log)