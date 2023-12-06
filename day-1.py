# Advent of Code 2023 - Day 1

# --- Part One ---

# The newly-improved calibration document consists of lines of text;
#each line originally contained a specific calibration value that the Elves now need to recover.
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python module (csv) to read in CSV data
from csv import reader, DictReader
# Python module (re) to use regex to find digits in strings
import re

# Creating an empty list called data to hold all the puzzle input data
data = []

# reading data in using reader() method
# reader() creates a list for each row of data in the CSV file
with open("input-day-1.csv") as file:
	csv_reader = reader(file) # creates a csv_reader object, which is an iterator
	for row in csv_reader:
		data.extend(row) # adding each row to the data list so all input is contained to the data list


# --- Part One Solution ---

def extract_and_sum_all_nums(list1):
	"""
	this function:
	 - extracts all the numbers from individual string items in a list using regex
	 - concatenates the first and last digits while they are still strings
	 - converts the concatenated string to an int then adds it to the total
	 - returns the total once the whole list has completed iterating
	 """
	total = 0
	for value in list1:
		extracted_nums = re.findall(r'[0-9]{1}', value)
		total += int(extracted_nums[0] + extracted_nums.pop())
	return total

print(extract_and_sum_all_nums(data)) # The sum of all the calibration values is: 54927


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# --- Part Two ---
# Your calculation isn't quite right.
# It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TO-DO
