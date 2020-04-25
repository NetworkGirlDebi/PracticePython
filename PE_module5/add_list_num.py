# Numbers Processor

line = None

while line != "q":

    line = input("Enter a line of numbers - separate them with spaces: (q to quit)")
    strings = line.split()

    if line != "q":

        if len(strings) > 0:
            
            total = 0
            try:
                for substr in strings:
                    total += float(substr)
                print("The total is:", total)
            except:
                print(substr, "is not a number.")
        else:
            print("You haven't entered anything...")

