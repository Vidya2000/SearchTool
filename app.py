import os
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="app.log", level=logging.DEBUG)


@app.route("/")
def hello_world():
  return render_template("home.html")


@app.route('/search', methods=['POST'])
def search():
  keyword = request.form['keyword']
  with open('search_history.txt', 'a') as file:
    file.write(keyword + '\n')
  return render_template('result.html', keyword=keyword)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
