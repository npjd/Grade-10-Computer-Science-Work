# Nima
# December 6th 2020

# variable will be defined as which operation user wants to execute
choice = str(input(
    "1. Count a pattern \n 2. Eliminate a pattern \n 3. Substitute a pattern \n4. Exit\n Please enter 1,2,3, or 4: "))
# Loop only occurs if user does not pick the exit option.
while choice != "4":
    # First choice conditional statement
    if choice == "1":
        # Option 1
        # defining the original string
        string = str(input("Enter string: "))
        # defining the substring pattern
        pattern = str(input("Enter pattern: "))
        # counter to keep track of occurrences of substring
        res = 0
        # loop that goes over every index in the original string
        for i in range(len(string)):
            # checks to see if a substring the length of the pattern matches the pattern.
            if string[i:i + len(pattern)].lower() == pattern.lower():
                # adds to counter if occurrence happens
                res += 1
        # prints result
        print(res)
    elif choice == "2":
        # Option 2
        # defining the original string
        string = str(input("Enter string: "))
        # defining the substring pattern
        pattern = str(input("Enter pattern: "))
        # length variable for our loop
        length = len(string)
        # index variable
        i = 0
        # we use a while variable so that we are able to change our index, the loop occurs until the index
        # is greater than the length of the string
        while i <= length:
            # checks to see if a substring matches with our pattern variable
            if string[i:i + len(pattern)].lower() == pattern.lower():
                # modifies string to remove the pattern
                string = string[0:i] + string[i + len(pattern):]
                # decrease index by the length of pattern to account for consecutive occurrences
                i -= len(pattern) - 1
                # decreases the length variable to account for the removal of the pattern
                length -= len(pattern) - 1
                # we subtract each variable by one because we automatically increase i by 1
            # index increases by one
            i += 1
        # print result
        print(string)
    # option 3
    elif choice == "3":
        # defines original string
        string = str(input("Enter string: "))
        # defines substring pattern
        pattern = str(input("Enter pattern: "))
        # defines the string we want to use to replace
        replace = str(input("Enter the replacement: "))
        # length of the original string before modification
        length = len(string)
        # index variable
        i = 0
        # we use a while variable so that we are able to change our index, the loop occurs until the index
        # is greater than the length of the string
        while i <= length:
            # checks to see if a substring matches with our pattern variable
            if string[i:i + len(pattern)].lower() == pattern.lower():
                # modifies string to add the replacement
                string = string[0:i] + replace + string[i + len(pattern):]
                # increases index by the length of the replace var to skip repeating it
                i += len(replace) - 1
                # increases the length variable so the loop goes longer
                length += len(replace) - 1
                # we subtract each variable by one because we automatically increase i by 1
            # index increases by one
            i += 1
        # print result
        print(string)
    else:
        # error check
        print('Invalid Input, try again')
    # asks for input again
    choice = str(input(
        "1. Count a pattern \n 2. Eliminate a pattern \n 3. Substitute a pattern \n4. Exit\n Please enter 1,2,3, or 4: "))
