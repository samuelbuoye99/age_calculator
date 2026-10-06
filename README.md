# Age Calculator

A simple command-line Python program that takes a birthdate and tells you
a few things about it.

## Features

- Validates input (`YYYY-MM-DD`), rejecting invalid dates, bad formats, and future dates
- Calculates your age in years, months, and days
- Shows the day of the week you were born
- Finds your zodiac sign
- Shows how long you've been alive in days, hours, and minutes
- Counts the days until your next birthday, including Feb 29 birthdays

## Usage

    python age_calculator.py

Example:

    Enter your birthdate (YYYY-MM-DD): 2000-01-01
    You are 26 year(s), 9 month(s), and 1 day(s) old.
    You were born on a Saturday.
    Your zodiac sign is Capricorn.
    You have been alive for 9,775 days, 234,600 hours, or 14,076,000 minutes.
    91 days until your next birthday.

## Requirements

- Python 3.6+
- No external libraries (uses only the standard `datetime` module)

## What I practiced

- Input validation with `try/except`
- Working with `datetime` and `date` objects
- Leap year logic and edge-case handling
- Writing helper functions and testing edge cases
