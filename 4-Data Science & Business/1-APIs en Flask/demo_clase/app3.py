
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
    return '<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>'

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    select_books = 'SELECT * FROM books'

    result = cursor.execute(select_books).fetchall()

    connection.close()

    return {'books': result}

@app.route('/api/v1/resources/books/<string:author>', methods = ['GET'])
def get_by_author(author):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    select_books = 'SELECT * FROM books WHERE author=?'

    result = cursor.execute(select_books, (author,)).fetchall()

    connection.close()

    return {'books': result}

@app.route('/api/v1/resources/books/filter', methods = ['GET'])
def filter_table():
    query_parameters = request.get_json()

    published = query_parameters.get('published')
    author = query_parameters.get('author')

    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    query = 'SELECT * FROM books WHERE'
    to_filter = []

    if published:
        query += ' published=? AND'
        to_filter.append(published)

    if author:
        query += ' author=? AND'
        to_filter.append(author)

    query = query[:-4] + ';'

    print(query)

    result = cursor.execute(query, to_filter).fetchall()

    connection.close()

    return {'books': result}

app.run()