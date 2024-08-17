import sys
import calendar
import csv
from datetime import datetime

# Check if a month argument is provided
if len(sys.argv) != 2:
    print("Usage: python dates.py <month>")
    sys.exit(1)

month_arg = sys.argv[1]

# Validate the provided month
try:
    month = int(month_arg)
    if month < 1 or month > 12:
        raise ValueError
except ValueError:
    print("Month must be a number between 01 and 12.")
    sys.exit(1)

year = datetime.now().year
weekday_dates = []

# Calculate weekdays for the given month
for day in range(1, calendar.monthrange(year, month)[1] + 1):
    if calendar.weekday(year, month, day) < 5:  # Monday to Friday are 0-4
        weekday_dates.append(f"{year}-{month:02d}-{day:02d}")

# Write the dates to a CSV file
with open('weekday_dates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for date in weekday_dates:
        writer.writerow([date])

print(f"Weekday dates for {calendar.month_name[month]} {year} written to weekday_dates.csv")
