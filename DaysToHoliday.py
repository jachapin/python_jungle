from datetime import date

# This program counts down the days until Christmas or New Year's. User selects which holiday.

def main():

    print("Let's count down the days until your favorite holiday! Enter 1 for Christmas or 2 for New Year\'s")
    holiday = input()

    if holiday == "1":
        daysTillChristmas()
    else:
        daysTillNewYear()


# Calculate days until Christmas. 
def daysTillChristmas():
    today = date.today()
    print("The current date and time is", today)
    christmasDay = date(today.year, 12, 25)
    if christmasDay < today:
        christmasDay = christmasDay.replace(year = today.year + 1)
    daysUntilChristmas = christmasDay - today
    print("It is", daysUntilChristmas.days, "days until Christmas!")

# Calculate the number of days until New Year's Day. 
def daysTillNewYear():
    today = date.today()
    print("The current date and time is", today)
    newYearsDay = date(today.year + 1, 1, 1)
    daysUntilNewYears = newYearsDay - today
    print("It is", daysUntilNewYears.days, "days until New Year's!")

if __name__ == "__main__":
    main()