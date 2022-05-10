from fastapi import FastAPI,  status, HTTPException
from pathlib import Path
from retry.api import retry_call


# my local Imports
from core.models import Post
from core.extra import read_json_file
from core.controller import DBManager


app = FastAPI()


# geting the database info from json file
DATABASE_INFO: dict = read_json_file(
    Path(__file__).parent / "data_info.json").get('database_info')

database_manager = DBManager(dbname=DATABASE_INFO.get(
    'dbname'), user=DATABASE_INFO.get('user'), password=DATABASE_INFO.get('password'))

con = retry_call(database_manager.connect, tries=5, delay=2)

if con.cursor:
    print("Connected To Database")
else:
    print("Cann't Connect to Database")
    exit(-1)


@app.get('/posts', status_code=status.HTTP_200_OK)
def get_posts():
    """Get All Posts in the Model"""
    con.cursor.execute("""SELECT * FROM posts """)
    posts = con.cursor.fetchall()
    return {'posts': posts}


# Get Specific post
@app.get('/posts/{post_id}')
def get_post(post_id: int):
    con.cursor.execute(f"""SELECT * FROM posts WHERE id={post_id}""")
    post = con.cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the Post With Id({post_id}) NOT Found")
    return {'post': post}


# Create post
@app.post('/posts/create', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):

    con.cursor.execute(
        f"""INSERT INTO posts (title,content) VALUES(%s , %s) """, (post.title, post.content))

    con.database.commit()

    return {"massage": "Post Created"}


# Update post
@app.put('/posts/update/{post_id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id: int, post: Post):
    con.cursor.execute(
        f"UPDATE posts SET title = %s , content = %s WHERE id= {post_id};", (post.title, post.content))
    con.database.commit()
    return {"massage": "Post Updated", 'NewPost': post.dict()}


# Delete  post


@app.delete('/posts/delete/{post_id}', status_code=status.HTTP_200_OK)
def delete_post(post_id: int):
    con.cursor.execute(
        f"DELETE FROM posts WHERE id= {post_id};")
    con.database.commit()

    return {"massage": "Post Deleted"}
