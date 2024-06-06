from datetime import datetime
dt = datetime.strptime('2021-07-01','%Y-%m-%d')
print(dt)

date_time_formatting_args = {
    "%A" : "Weekday name, such as Monday",
    "%B" : "Month name, such as January",
    "%m" : "Month, as a number (01 to 12)",
    "%d" : "Day of the month, as a number (01 to 31)",
    "%Y" : "Four-digit year, such as 2020",
    "%y" : "Two-digit year, such as 23",
    "%H" : "Hour, in 24-hour format(00 to 23)",
    "%I" : "Hour, in 12-hour format(01 to 12)",
    "%p" : "AM or PM",
    "%M" : "Minutes (00 to 59)",
    "%S" : "Seconds (00 to 61)"
}

for i,j in date_time_formatting_args.items():
    print(f"{i} = {j}\n\n")