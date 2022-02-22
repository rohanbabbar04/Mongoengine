from flask_app import db


class Book(db.Document):
    bookID = db.IntField(primary_key=True)
    name = db.StringField(required=True)
    author = db.StringField(required=True)
    price = db.FloatField(required=True)

    def __repr__(self):
        return f'Book({self.bookID},{self.name},{self.author},{self.price}'

    def to_json(self):
        return {
            'bookID': self.bookID,
            'name': self.name,
            'author': self.author,
            'price': self.price
        }
