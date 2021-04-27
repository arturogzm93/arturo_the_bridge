
from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
    return '<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>'

@app.route('/api/v1/resources/books/all', methods = ['GET'])
def get_all():
    return jsonify(books)

@app.route('/api/v1/resources/book', methods = ['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id field provided'

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

@app.route('/api/v1/resources/book/<string:title>', methods = ['GET'])
def get_by_title(title):
    for book in books:
        if book['title'] == title:
            return jsonify(book)
    return 'Book title not found'

@app.route('/api/v2/resources/book', methods = ['GET'])
def get_by_id_body():
    id = int(request.get_json()['id'])

    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return 'Book id in body not found'

@app.route('/api/v1/resources/book', methods = ['POST'])
def post_book():
    data = request.get_json()
    books.append(data)
    return data

@app.route('/api/v1/resources/published/<string:title>', methods = ['PUT'])
def put_book_published(title):
    data = request.get_json()

    for book in books:
        if book['title'] == title:
            book['published'] = data['published']
            return book

    return 'Book not found in published PUT'

@app.route('/api/v1/resources/<string:title>/<int:published>', methods = ['PUT'])
def put_book_published2(title, published):
    for book in books:
        if book['title'] == title:
            book['published'] = published
            return book

    return 'Book not found in published PUT'

app.run()