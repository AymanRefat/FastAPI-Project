from fastapi import  FastAPI
from fastapi.params import Body


from models import Post


app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Hello World"}


@app.get('/posts')
def get_posts():
    return {'posts':[{'post_id':1}]}


@app.get('/posts/{post_id}')
def get_post(post_id:int):
    print(post_id)
    return {}



@app.post('/create')
def create_post(data:Post):
    return {'msg':"Data Created Successfully"}