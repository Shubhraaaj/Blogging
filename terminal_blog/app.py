from models.Blog import Blog
from models.post import Post
from terminal_blog.database import Database

Database.initialize()

# post = Post(blog_id="123",
#             title="First Post",
#             content="This is the first post made by Python for MongoDB",
#             author="Shubhraj")
# post.save_to_mongo()
# post = Post.from_mongo("_id_")
# posts = Post.from_blog("123")
#
# for post in posts:
#     print(post)

blog = Blog(author="Shubhraj",
            title="Sample Title",
            description="Sample Description")

blog.new_post()
blog.save_to_mongo()
Blog.from_mongo()
blog.get_post() #Post.from_blog(id)

