"""
Author: Anythony Schomer

Purpose: Demonstrate knowledge of string files and functions

Domain: Music

"""

# imports first
import random

# Setting up logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Task 4 - Setting up some string lists
band_members_names = ["Tom", "Mark", "Travis", "Matt", "Derrick", "Bert", "Josh", "Gerard"]
guitar_types = ["Gibson", "Taylor", "Fender", "Ibanez", "Yamaha"]
guitar_descriptors = ["palm muting", "strumming", "hammeron", "fingerpicking"]
opening_band_names = ["Royal Blood", "Badflower", "ConMan Economy", "The Architects", "Flyleaf", "The Starting Line", "McFly", "Josephine Collective"]
Headliner_bands = ["MCR", "Blink182", "AVA", "Foo Fighters", "Sum41", "Yellowcard"]

# Task 4 Lists 1 - Use the len(), set(), and zip() to combine two tuples
# Find a set of opening band names
open_names = set(opening_band_names)
# Using zip() that combines opening bands names and headliners bands
combined_names = zip(open_names, Headliner_bands)
printable_combined_names = list(combined_names)

# Loggin all the info
logger.info(f"Here is your list of opening bands names: {opening_band_names}.")
logger.info(f"Here is your list of guitar types: {guitar_types}.")
logger.info(f"Here is your list of Headliner bands: {Headliner_bands}.")
logger.info(f"Here is your list of opening band names and headliner band names combined together: {printable_combined_names}")
logger.info(f"Oops I made a mistake! Let me correct that!")
# Function that removes duplicates from a list and preserves order. Found on geeksforgeeks.org .
def removeduplicate(data):
    countdict = {}
    for element in data:
        if element in countdict.keys():
             
            # increasing the count if the key(or element)
            # is already in the dictionary
            countdict[element] += 1
        else:
            # inserting the element as key  with count = 1
            countdict[element] = 1
    data.clear()
    for key in countdict.keys():
        data.append(key)
# Running the function
removeduplicate(opening_band_names)
# Using zip() to creat a correct combination of opening bands and headliners
correct_combined_names = zip(opening_band_names, Headliner_bands)
print_friendly_names = list(correct_combined_names)
# Logging the new info
logger.info(f"Does this look better?")
logger.info(f"Here is the correct list of opening bands and headliners: {print_friendly_names}")

# Task 4 Lists 2 - Random Choice
# Creating a random sentence using my lists
# This sentence will be a random statement about bands performing at a show
# 
# 
# 
# 
sentence = (
        f"{random.choice(band_members_names)} {random.choice(guitar_descriptors)} a {random.choice(guitar_types)} LET'S ROCK THIS PLACE {random.choice(print_friendly_names)}!!!!"
    )
# Logging the sentence
logger.info(f"Random sentence: {sentence}")

# Task 4 Lists 3 - Get unique words
# I Found a few music files on github but they were not working when i tried to include them so I'm using the Zen of Python text file instead
# Opening the text file
full_text = open("text_zen_of_python.txt")
# Reading and logging the file
read_full_text = full_text.read()
logger.info(f"{read_full_text}")
# Creating a list of the strings in the text file
text_list = read_full_text.split()
# Find the unique words in the text file
unique_text_list = set(text_list)
# Order the unqie list alphabetically
alpha_text_list = sorted(unique_text_list)
numb_words = len(alpha_text_list)
# Logging the number of words and the alphabetically list
logger.info(f"Here is a list of the {numb_words} unique words in the Zen of Python file: {alpha_text_list}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())



