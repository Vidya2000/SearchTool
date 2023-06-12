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
        history_file.write("Query: " + query + "\nResults: " + results.strip() + "\n\n")

    # Save to search.txt if the query is not already present
    file_path = "static/Search.txt"
    with open(file_path, 'r') as search_file:
        existing_queries = search_file.readlines()

    with open(file_path, 'a') as search_file:
        if not any(query in line for line in existing_queries):
            search_file.write(query + ' ? ' + results.strip() + '\n')

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
      if query.lower() in parts[0].lower():
        results.append(parts[1])

  return render_template('search_results.html', results=results)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
