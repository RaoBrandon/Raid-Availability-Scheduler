import csv
import os

# Opening and reading the CSV file
with open(r'Raid Availability.csv') as csvfile:
    readCSV = list(csv.reader(csvfile, delimiter=","))
    # Hard - coded time slots for availability
    availability_schedule = [["MONDAY", "8:00 AM - 12:00 NN"],
                             ["MONDAY", "12:00 NN - 4:00 PM"],
                             ["MONDAY", "4:00 PM - 8:00 PM"],
                             ["MONDAY", "8:00 PM - 12:00 MN"],
                             ["MONDAY", "12:00 MN - 4:00 AM"],
                             ["TUESDAY", "8:00 AM - 12:00 NN"],
                             ["TUESDAY", "12:00 NN - 4:00 PM"],
                             ["TUESDAY", "4:00 PM - 8:00 PM"],
                             ["TUESDAY", "8:00 PM - 12:00 MN"],
                             ["TUESDAY", "12:00 MN - 4:00 AM"],
                             ["WEDNESDAY", "8:00 AM - 12:00 NN"],
                             ["WEDNESDAY", "12:00 NN - 4:00 PM"],
                             ["WEDNESDAY", "4:00 PM - 8:00 PM"],
                             ["WEDNESDAY", "8:00 PM - 12:00 MN"],
                             ["WEDNESDAY", "12:00 MN - 4:00 AM"],
                             ["THURSDAY", "8:00 AM - 12:00 NN"],
                             ["THURSDAY", "12:00 NN - 4:00 PM"],
                             ["THURSDAY", "4:00 PM - 8:00 PM"],
                             ["THURSDAY", "8:00 PM - 12:00 MN"],
                             ["THURSDAY", "12:00 MN - 4:00 AM"],
                             ["FRIDAY", "8:00 AM - 12:00 NN"],
                             ["FRIDAY", "12:00 NN - 4:00 PM"],
                             ["FRIDAY", "4:00 PM - 8:00 PM"],
                             ["FRIDAY", "8:00 PM - 12:00 MN"],
                             ["FRIDAY", "12:00 MN - 4:00 AM"],
                             ["SATURDAY", "8:00 AM - 12:00 NN"],
                             ["SATURDAY", "12:00 NN - 4:00 PM"],
                             ["SATURDAY", "4:00 PM - 8:00 PM"],
                             ["SATURDAY", "8:00 PM - 12:00 MN"],
                             ["SATURDAY", "12:00 MN - 4:00 AM"],
                             ["SUNDAY", "8:00 AM - 12:00 NN"],
                             ["SUNDAY", "12:00 NN - 4:00 PM"],
                             ["SUNDAY", "4:00 PM - 8:00 PM"],
                             ["SUNDAY", "8:00 PM - 12:00 MN"],
                             ["SUNDAY", "12:00 MN - 4:00 AM"]]
    # Iterate through rows in the csv file
    for row in readCSV:
        # Keep track of the row number
        entry_num = 0
        # Iterate through entries of each row of the csv file
        for entry in row:
            # We want to make a potential schedule based on whether or not
            # people are potentially available
            if entry == "AVAILABLE" or entry == "PERHAPS":
                # If they are available we put their name into the
                # corresponding time slot in availability_schedule
                for slot in availability_schedule:
                    if slot[1] == row[1]:
                        if slot[0] == readCSV[0][entry_num]:
                            slot += [row[0]]
            entry_num += 1

    # Continuous loop for input to create schedules based on the day that was
    # asked to be scheduled
    while True:
        print("Type 'e' to exit")
        print("Which day would you like to schedule a raid for?: ")
        # User input is a day of the week
        day = input().upper()
        # They can exit the program by typing in 'e'
        if day == "E":
            break
        # Display result of our availability_schedule according to the day that
        # the user asked for
        print("A raid can be scheduled on " + day + " at the following times:")
        for item in availability_schedule:
            if item[0] == day:
                # Only display results that have 6 players or more because we
                # cannot have a raid with less than 6 players on a fireteam
                if len(item[2:]) >= 6:
                    print(item[1:])
