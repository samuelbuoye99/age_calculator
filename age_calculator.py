from datetime import datetime, date

# Helper functions

def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    # check for leap year(february)
    elif(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 29
    return 28 


def previous_month(ref_day):
    if ref_day.month == 1:
        return ref_day.year - 1, 12   # January goes to December of last year
    return ref_day.year, ref_day.month - 1

# Valid birthdate

today = date.today()

while True:
    raw_input = input("Enter your birthdate (YYYY-MM-DD): ")
    raw_input = raw_input.strip()
    try:
        birth = datetime.strptime(raw_input, "%Y-%m-%d").date()
    except ValueError:
        print("That is not a valid date. Please try again.")
        continue

    if birth > today:
        print("Birthdate cannot be in the future. Try again.")
        continue

    break

# 1. Exact age in years, months, days

years  = today.year  - birth.year
months = today.month - birth.month
days   = today.day   - birth.day

if days < 0:
    pre_year, pre_month = previous_month(today)
    days += days_in_month(pre_year, pre_month)
    months -= 1

if months < 0:
    #1 year = 12 months
    months += 12
    years  -= 1

# Output

print(f"You are {years} year(s), {months} month(s), and {days} day(s) old.")
print(f"You were born on a {birth.strftime('%A')}.")

# 2. Zodiac sign

def zodiac_sign(birth):
    signs = [
        (1, 19, "Capricorn"),
        (2, 18, "Aquarius"),
        (3, 20, "Pisces"),
        (4, 19, "Aries"),
        (5, 20, "Taurus"),
        (6, 20, "Gemini"),
        (7, 22, "Cancer"),
        (8, 22, "Leo"),
        (9, 22, "Virgo"),
        (10, 22, "Libra"),
        (11, 21, "Scorpio"),
        (12, 21, "Sagittarius"),
    ]
    for last_month, last_day, sign in signs:
        if (birth.month, birth.day) <= (last_month, last_day):
            return sign
    return "Capricorn" # december 22 - 31

print(f"Your zodiac sign is {zodiac_sign(birth)}.")

# 3. Total time alive

now = datetime.now()
birth_dt = datetime.combine(birth, datetime.min.time())
time_delta = now - birth_dt

total_days    = time_delta.days
total_seconds = time_delta.total_seconds()
total_hours   = int(total_seconds // 3600)
total_minutes = int(total_seconds // 60)

print(f"You have been alive for {total_days:,} days, {total_hours:,} hours, or {total_minutes:,} minutes.")

# 4. Days until next birthday
try:
    next_bday = birth.replace(year=today.year)
except ValueError:
    next_bday = date(today.year, 3, 1)   # Feb 29 birthday in non-leap year

if next_bday < today:
    try:
        next_bday = birth.replace(year=today.year + 1)
    except ValueError:
        next_bday = date(today.year + 1, 3, 1)

days_left = (next_bday - today).days
if days_left == 0:
    print("Today is your birthday! Happy birthday to you.")
else:
    print(f"{days_left:,} days until your next birthday.")