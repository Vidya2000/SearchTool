from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="app.log", level=logging.DEBUG)


@app.route("/")
def hello_world():
  return render_template("home.html", saved=False)


@app.route('/save_search', methods=['POST'])
def save_search():
  query = request.form['query']
  results = request.form['results']

  # Save to search_history.txt
  with open('search_history.txt', 'a') as history_file:
    history_file.write("Query: " + query + "\nResults: " + results + "\n\n")

  # Save to search.txt if the query is not already present
  file_path = "static/Search.txt"
  with open(file_path, 'r') as search_file:
    existing_queries = search_file.readlines()

  with open(file_path, 'a') as search_file:
    if not any(query in line for line in existing_queries):
      search_file.write(query + ' ? ' + results + '\n')

  return redirect(url_for('hello_world', success=True))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
