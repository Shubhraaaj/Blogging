import datetime
import uuid
from terminal_blog.database import Database

class Post(object):

    def __init__(self, blog_id, title, content, author, created_date = datetime.datetime.utcnow(), id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
       postdata = Database.find_one(collecion = 'posts', query = {'id': id})
       return cls(blog_id=postdata['blog_id'],
                  title=postdata['title'],
                  content=postdata['content'],
                  author=postdata['author'],
                  date=postdata['created_date'],
                  id=postdata['id'])

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection = 'posts', query = {'blog_id': blog_id})]