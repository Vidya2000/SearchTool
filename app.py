from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html", saved=False)


@app.route('/save_search', methods=['POST'])
def save_search():
  query = request.form['search']
  results = request.form.get('results', '')

  # Remove HTML tags from results
  results = re.sub(r'<[^>]+>', '', results)

  # Save to search_history.txt
  with open('search_history.txt', 'a') as history_file:
    history_file.write("Query: " + query + "\nResults: " + results.strip() +
                       "\n\n")

  # Save to search.txt and update the existing query if found
  file_path = "static/Search.txt"
  updated = False

  lines = []
  with open(file_path, 'r+') as search_file:
    for line in search_file:
      parts = line.split(" ? ")
      existing_query = parts[0].strip()
      if query.lower() in existing_query.lower():
        # Update the existing query by adding the new word
        updated_query = existing_query + query.strip()
        line = updated_query + ' ? ' + parts[1].strip() + '\n'
        updated = True
        break  # Stop processing further lines since the query is updated
      lines.append(line.rstrip('\n'))

    if not updated:
      lines.append(query + ' ? ' + results.strip())

    search_file.seek(0)  # Move the file pointer to the beginning
    search_file.truncate()  # Clear the file content

    for line in lines:
      search_file.write(line + '\n')

  return redirect(url_for('hello_world', success=True))


@app.route('/search', methods=['POST'])
def perform_search():
  query = request.form.get('search')
  results = []

  # Search in the text file
  file_path = "static/Search.txt"
  with open(file_path, 'r') as search_file:
    for line in search_file:
      parts = line.split(" ? ")
      if len(parts) >= 2:
        line_query = parts[0].strip()
        line_result = parts[1].strip()
        if query.lower() in line_query.lower():
          results.append(line_result)

  return render_template('search_results.html', results=results)


@app.route('/remove', methods=['POST'])
def remove_search():
  query = request.form.get('query')

  # Remove the results associated with the query from search.txt
  file_path = "static/Search.txt"
  lines = []
  with open(file_path, 'r') as search_file:
    for line in search_file:
      parts = line.split(" ? ")
      if query.lower() in parts[0].lower():
        # Remove the results for this query
        line = parts[0] + " ?\n"  # Retain the query without results
      lines.append(line)

  with open(file_path, 'w') as search_file:
    search_file.writelines(lines)

  return redirect(url_for('hello_world', removed=True))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
