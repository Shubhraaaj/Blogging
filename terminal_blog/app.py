# from models.Blog import Blog
# from models.post import Post
from terminal_blog.database import Database
from terminal_blog.menu import Menu

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

# blog = Blog(author="Shubhraj",
#             title="Sample Title",
#             description="Sample Description")
#
# blog.new_post()
# blog.save_to_mongo()
# from_database = Blog.get_from_mongo(blog.id)
# print(blog.get_posts()) #Post.from_blog(id)

menu = Menu()


def exit_status():
    status = input("Do you want to exit the application (Y/N): ");
    if status == "Y":
        exit(0)
    elif status == "N":
        return True
    else:
        print("Wrong option selected. Try Again")
        exit_status()


while True:
    menu.run_menu()
    while exit_status():
        menu.run_menu()

