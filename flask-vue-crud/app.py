from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration
DEBUG = True

# instantiate the app

# List of Books :
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    },
]


app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route


@app.route('/ping', methods=['GET'])
def ping_pong():
    """[Ping pong Route Testing]

    Returns:
        [Methods] -- [GET]
    """

    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    """This route for all books and use GET and POST methods:"""

    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS

    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
