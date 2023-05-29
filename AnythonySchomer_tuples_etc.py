"""
Author: Anythony Schomer

Purpose: Demonstrate knowledge of tuples and dictionaries

Domain: Music
"""

# Setting up logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Creating some tuples
# Tuple setup = (Band Member Names, Positions, years in the band)
pg_tuple = ("Gerard Way", "Lead_singer", 22)
sg_tuple = ("Mikey Way", "Bass guitar", 22)
sf_tuple = ("Frank Iero", "Rhythm guitar", 22)
pf_tuple = ("Ray Del Toro", "Lead Guitar", 22)
c_tuple = ("Bob Bryar", "Drummer", 22)
# Logging the tuples
logger.info(f"Below I have the band mebers names, positions, years in the band:")
logger.info(f"{pg_tuple}")
logger.info(f"{sg_tuple}")
logger.info(f"{sf_tuple}")
logger.info(f"{pf_tuple}")
logger.info(f"{c_tuple}")
# Creating some functions to demonstrate knowledge of tuples
# First name finder - demonstrates knowledge of index positions
def first_name_finder(my_tuple):
    name = my_tuple[0]
    return name
# Running the first name finder
sg_name = first_name_finder(sg_tuple)
logger.info(f"Does the first name finder work? Is your lead singer named {sg_name}?")

# Membership testing
def pf_position_test(another_tuple):
    if another_tuple[1] == "Lead Guitar":
        return True
    else:
        return False
# Running the power forward position test
pf_test_fail = pf_position_test(sf_tuple)
logger.info(f"Does Frank Iero play Lead Guitar? {pf_test_fail}")
logger.info(f"Sorry! I will try again!")
pf_test = pf_position_test(pf_tuple)
logger.info(f"Does Ray Del Toro play Lead Guitar? {pf_test}")

# Task 5-5 Creating 2 Sets
# The Sets are list of song titles the Bands played on tour
# Tour 1 Set
set_Blink = {"What's My Age Again?", "Stay Together for the Kids", "Girl at the Rock Show", "All the Small Things", "Man Overboard", "Feelin This", "Always", "Shutup", "Down"}
set_Yellowcard = {"Only One", "Ocean Ave", "Rest in Peace", "Hang You Up", "Paper Walls", "Sing For Me", "Believe"}
# Logging the Sets
logger.info(f"Here is a list of the songs this band sings on this Tour: {set_Blink}")
logger.info(f"Here is a list of the songs this band sings on this Tour: {set_Yellowcard}")
# Finding the Unior of the 2 sets
union_set = set_Blink | set_Yellowcard
# Logging the new set
logger.info(f"Here is a combined list of all songs both recorded throughout their careers: {union_set}")
# Finding the Intersection of the 2 sets
common_set = set_Blink & set_Yellowcard
logger.info(f"Here is a list of all songs from both bands: {common_set}")

with open("text_zen_of_python.txt") as file_object:
        word_list = file_object.read().split()

# Create a dictionary of word counts from a list of words
# A dictionary is always key:value pairs
# Say "I want word:count for each word in word_list"
# Cast the result to a dictionary by using curly braces {}
word_counts_dict2 = {word: word_list.count(word) for word in word_list}

# Logging the information
logger.info("Given text_simple.txt and comprehensions,")
logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
