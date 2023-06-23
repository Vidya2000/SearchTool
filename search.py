import sys

# Get the search keyword from the command line arguments
if len(sys.argv) > 1:
  keyword = sys.argv[1]
else:
  print("Please provide a search keyword.")
  sys.exit(1)

# Get the file path
file_path = "static/Search.txt"

# Read the content of the file
try:
  with open(file_path, 'r') as file:
    content = file.readlines()
except FileNotFoundError:
  print("File not found.")
  sys.exit(1)

# Perform the case-insensitive search and display the matching results
matches = []
for line in content:
  if keyword.lower() in line.lower(
  ):  # Convert both keyword and line to lowercase for case-insensitive comparison
    matches.append(line.strip())

if matches:
  print("Matching results:")
  for match in matches:
    print(match)
else:
  print("No matches found.")
