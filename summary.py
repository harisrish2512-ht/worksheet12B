import sys                              # Access command line arguments
from collections import Counter         # Count occurrences of items in a list and store them in a dictionary

filename = sys.argv[1]                  # Get the log file name from the command line
position = int(sys.argv[2])             # Get the field position from the command line and convert it to an integer
word = sys.argv[3]                      # Get the word to search for from the command line
lower_word = word.lower()               # Convert the word to lowercase for case-insensitive comparison

with open(filename) as f:               # Open the log file
    lines = f.readlines()               # Read all lines from the log file into a list

print("Total lines:", len(lines))       # Print the total number of lines in the log file

counts = Counter()                      # Create an empty Counter object to store the counts of items
for line in lines:                      # Iterate over each line in the log file
    fields = line.split()               # Split the line into fields using whitespace as the delimiter
    if len(fields) > position:          # Check if the line has more than the specified position fields
        key = fields[position]          # Get the field at the specified position as the key for counting
        counts[key] += 1                # Increment the count for the key in the Counter object



print("Top 5 most common items:")       # Print a header for the top 5 most common items
for item, n in counts.most_common(5):   # Iterate over the top 5 most common items in the Counter object
    print(item, n)                      # Print the item and its count