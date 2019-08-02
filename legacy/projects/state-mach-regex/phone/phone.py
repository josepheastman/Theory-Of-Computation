import re  # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
phone_regex = re.compile(r"/[^0-9 +\-]/")


def phone_format(phone_number):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub(
        "(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number


while line != "exit":
    # TODO Find matches
    for element in line:
        matches = re.match("/[^0-9 +\-]/", element)
        if matches:
            print((matches.groups()))

    # TODO If no match found, print that no number was found
        elif matches != matches:
            print("No number was found.")

    # TODO Else, break number up into area code, prefix, and suffic
        else:
            phone_format(matches)
            # format(int(n[:-1]), ",").replace(",", "-") + n[-1]

    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
