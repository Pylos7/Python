"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Chapter 8: Programming Project 1
Program Name: Alpha Phone Number
"""
def main():
    tupple2 = ["A", "B", "C", "2"]
    tupple3 = ["D", "E", "F", "3"]
    tupple4 = ["G", "H", "I", "4"]
    tupple5 = ["J", "K", "L", "5"]
    tupple6 = ["M", "N", "O", "6"]
    tupple7 = ["P", "Q", "R", "S", "7"]
    tupple8 = ["T", "U", "V", "8"]
    tupple9 = ["W", "X", "Y", "Z", "9"]

    mix_num = input("Enter a phone number to be translated:")

    final_num = ""
    for number in mix_num:
        if number.isalpha():
            if number.upper() in tupple2:
                final_num += (tupple2[-1])
            elif number.upper() in tupple3:
                final_num += (tupple3[-1])
            elif number.upper() in tupple4:
                final_num += (tupple4[-1])
            elif number.upper() in tupple5:
                final_num += (tupple5[-1])
            elif number.upper() in tupple6:
                final_num += (tupple6[-1])
            elif number.upper() in tupple7:
                final_num += (tupple7[-1])
            elif number.upper() in tupple8:
                final_num += (tupple8[-1])
            elif number.upper() in tupple9:
                final_num += (tupple9[-1])
        else:
            final_num += (number)

    print(final_num)
# Call the main function.
main()
