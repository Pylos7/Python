"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Chapter 8: Lab Part B
Program Name: Guess the State Capital Game
"""

# create a dictionary, key is the state and value is the capital
capitals_dic = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
# print(capitals_dic['Wyoming'].lower())
# Define correct and
correct_guesses = 0
incorrect_guesses = 0

game_length = 3

for x in range(0, game_length):
    k, v = capitals_dic.popitem()
    capital_guess = input('Enter the capital of ' + k + ': ')
    if capital_guess.lower() == v.lower():
        print('Correct, Good Job!')
        correct_guesses += 1
    else:
        print('Incorrect, Try Again...')
        incorrect_guesses += 1

# Print correct/incorrect guesses
print('Correct Guesses: ' + str(correct_guesses) + '\nIncorrect Guesses: ' + str(incorrect_guesses))
