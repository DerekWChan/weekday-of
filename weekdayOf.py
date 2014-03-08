def main():
    interface()
         
def interface():
    userInput = raw_input("Enter the date (XX/XX/XXXX):")

    if userInput.count("/") != 2:
        print "Invalid input, try again?"
        interface()
    else:
        date = [int(s) for s in userInput.split("/")]
        
        if 0 in date or date[0] > 12 or date[1] > 31:
            print "Invalid date, try again?"
            interface()
        else:
            print "The date " + userInput \
                   + " falls on a " + weekdayOf(date)
            
            userChoice = raw_input("Restart? (Y/N)")
            if userChoice.lower() == 'y':
                interface()

def weekdayOf(date):
    dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", 
                "Wednesday", "Thursday", "Friday"]
    monthTable = [0, 31, 59.25, 90.25, 120.25, 151.25, 181.25, 
                  212.25, 243.25, 273.25, 304.25, 334.25, 365.25]

    day = date[1]
    month = date[0]-1
    year = date[2]-1

    dayCount = day + monthTable[month] + (year)*365.25
    
    return dayNames[int(dayCount%7)]

if __name__ == "__main__":
    main()
