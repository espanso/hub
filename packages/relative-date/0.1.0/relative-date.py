import sys
import datetime
from dateutil.relativedelta import relativedelta

input_str = sys.argv[1]

# Extract the operator (+ or -) and the number from the input
operator = input_str[0]
number = int(input_str[1:-1])

# Determine the time unit based on the last character of the input
unit = input_str[-1]

# Perform the date calculation and print the result
current_date = datetime.date.today()
if operator == '+':
    if unit == 'd':
        new_date = current_date + datetime.timedelta(days=number)
    elif unit == 'w':
        new_date = current_date + datetime.timedelta(weeks=number)
    elif unit == 'm':
        new_date = current_date + relativedelta(months=number)
    elif unit == 'y':
        new_date = current_date + relativedelta(years=number)
    else:
        print("Invalid input format. Please use +2d, +2w, +2m, or +2y.")
        sys.exit(1)
else:
    if unit == 'd':
        new_date = current_date - datetime.timedelta(days=number)
    elif unit == 'w':
        new_date = current_date - datetime.timedelta(weeks=number)
    elif unit == 'm':
        new_date = current_date - relativedelta(months=number)
    elif unit == 'y':
        new_date = current_date - relativedelta(years=number)
    else:
        print("Invalid input format. Please use +2d, +2w, +2m, or +2y.")
        sys.exit(1)

print(new_date.strftime("%Y-%m-%d"))