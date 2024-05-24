from sys import argv, exit
import csv
from tabulate import tabulate

# Read students into memory as a list
students = []

# Start the main programme
def main():
    # Expects two command-line arguments exactly (if not sys.exit)
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if len(argv) > 3:
        exit("Too many command-line arguments")


    # Expects name of an existing CSV file to read as input, 
    # whose columns are assumed to be, in order, name and house
    # if not read sys.exit   
    try:
        with open(argv[1]) as file:  
            reader =csv.DictReader(file)                       
            for row in reader:    
                students.append(row)                 
    except FileNotFoundError:
            exit("Could not read invalid_file.csv")

    # and the name of a new CSV to write as output, whose 
    # columns should be, in order, first, last, and house.    
    with open("after.csv", "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Converts that input to that output, splitting each name into
        # first name and last name. 
        writer.writeheader()  
        for student in students:
            last, first = student["name"].split(",")
            house = student["house"]          
            writer.writerow({"first": first, "last": last, "house": house})   
    
    

  
if __name__ == "__main__":
    main()
