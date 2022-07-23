def main():
    # Open the golf.txt file.
    golf_file = open('golf.txt', 'r')

    # Read the first line from the file, which is
    # the name field of the first record.
    name = golf_file.readline()

    # If a field was read, continue processing.
    while name != '':
        # Read the score field.
        score = golf_file.readline()

        # Strip the newlines from the fields.
        name = name.rstrip('\n')
        #score = score.rstrip('\n')

        # Display the record.
        print('Name:' + str(name))
        print('Score:' + str(score))
        #print()
        # Read the name field of the next record.
        name = golf_file.readline()

    # Close the file.
    golf_file.close()

# Call the main function.
main()
