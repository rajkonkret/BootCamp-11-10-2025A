from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, joinedload
from day_12_21_12_2025.baza_dodatkowe.baza_krok1 import User, Post
from baza_krok2_transakcja import Session

session = Session()

# users_with_posts = session.query(User).all()
#
# for user in users_with_posts:
#     print(f"Użytkownik: {user.name}")
#     for post in user.posts:
#         print(f"Post: {post.title}")
# # 2025-12-21 10:48:31,827 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# 2025-12-21 10:48:31,827 INFO sqlalchemy.engine.Engine [generated in 0.00008s] {}
# Użytkownik: Jan kowalski
# 2025-12-21 10:48:31,830 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.user_id AS posts_user_id
# FROM posts
# WHERE %(param_1)s = posts.user_id
# 2025-12-21 10:48:31,830 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {'param_1': 1}
# Post: Pierwszy post
# Problem N + 1

# eager
# ominiecie problemu N + 1
users_with_posts = session.query(User).options(joinedload(User.posts)).all()
for user in users_with_posts:
    print(f"Użytkownik: {user.name}")
    for post in user.posts:
        print(f"Post: {post.title}")
# 2025-12-21 10:53:00,722 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, posts_1.id AS posts_1_id, posts_1.title AS posts_1_title, posts_1.content AS posts_1_content, posts_1.user_id AS posts_1_user_id
# FROM users LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.user_id
# 2025-12-21 10:53:00,722 INFO sqlalchemy.engine.Engine [generated in 0.00006s] {}
# Użytkownik: Jan kowalski
# Post: Pierwszy post
