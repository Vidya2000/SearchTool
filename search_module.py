import requests


def search(query):
  response = requests.get(
    "static/Search.txt")  # Fetch the data from the text file
  data = response.text

  results = processData(data, query)  # Process the data and get the results
  return results


def processData(data, query):
  lines = data.split("\n")
  results = []

  for line in lines:
    line = line.strip()
    parts = line.split(" ? ")

    prompt = parts[0]
    response = parts[1]

    words = prompt.lower().split(" ")

    if query.lower() in prompt.lower() or any(query.lower() in word for word in words):
      results.append(response)

  return results

