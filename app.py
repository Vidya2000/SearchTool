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
  with open('search_history.txt', 'a') as file:
    file.write("Query: " + query + "\nResults: " + results + "\n\n")
  return redirect(url_for('hello_world', success=True))


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
