

# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer")


def instruction():
    print("****How to Play****")
    print()
    print("***About the game***")
    print("write rules here")
    return ""

# Main routine goes here...
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instruction()

print("Programs Continues")
