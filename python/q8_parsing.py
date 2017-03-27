# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
goal_data = dict()
with open('football.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        team = row['Team']
        goals = int(row['Goals'])
        goals_allowed = int(row['Goals Allowed'])
        Difference = abs(goals - goals_allowed)
        goal_data[team] = Difference

min_difference = min(goal_data.values())
min_team = [key for key, value in goal_data.iteritems() if value == min_difference]
print min_team
