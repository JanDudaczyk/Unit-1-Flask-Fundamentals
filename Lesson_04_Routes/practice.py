from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
 return '''
<ul>
<li>
<a href = /book_id?books=Harry_Potter&id=10224>
See Harry Potter Book
</a>
</li>
</ul>
'''

@app.route('/books')
def book_genre():
    genre = request.args.get('genre', 'no genre')
    books = request.args.getlist('book') or ["no book"]
    return f'{genre} has the books {books}'
@app.route('/book_id/<int:book_id>')
def book_id(book_id):
    books = request.args.getlist('books') or ["no book"]
    return f'{books} has the id {book_id}'

if __name__ == '__main__':
 app.run(debug=True)