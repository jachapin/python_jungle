from datetime import datetime

def main():
    chooseHoliday()
    print(holiday)
    if holiday == "1":
        daysTillChristmas()
    else:
        print("New Year's")

# User chooses holiday
def chooseHoliday():
    print("Let's count down the days until your favorite holiday! Enter 1 for Christmas or 2 for New Year\'s")
    global holiday
    holiday = input()

# Calculate days until Christmas. Return number of days until Christmas
def daysTillChristmas():
    today = datetime.now()
    print("The current date and time is ", today)
    christmasDay = date(today.year, 12, 25)
    if christmasDay < today:
        christmasDay = christmasDay.replace(year = today.year + 1)
    daysUntilChristmas = christmasDay - today
    print("It is ", daysUntilChristmas, " days until Christmas!")

if __name__ == "__main__":
    main()