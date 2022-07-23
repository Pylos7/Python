def main():
    # Get the number of players
    num_players = int(input('Enter number of players:'))

    # Open a file for writing
    golf_file = open('golf.txt', 'w')

    # Get each players data and write it to the file
    for count in range(1, num_players + 1):
        # Get the data for a player
        name = input('Enter name of player number ' + str(count) + ':')
        score = input('Enter score of player number ' + str(count) + ':')

        # Write the data as a record to the file
        golf_file.write(name + '\n')
        golf_file.write(score + '\n')

    # Close the file
    golf_file.close()

# Call the main function
main()
