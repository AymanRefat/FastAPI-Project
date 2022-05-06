from fastapi import  FastAPI , status , HTTPException
from models import Post , PostModel



app = FastAPI()

model = PostModel

# get all Posts 
@app.get('/posts',status_code=status.HTTP_200_OK)
def get_posts():
    posts = [ post.dict() for post in model.posts ]
    return {'posts':posts}


# Get Specific post
@app.get('/posts/{post_id}')
def get_post(post_id:int):
    post = model.find_post(post_id)
    if post:
        return post.dict()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the Post With Id({post_id}) NOT Found")


# Create post 
@app.post('/posts/create',status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    model.add_post(post)
    return {"massage":"Post Created"}


# Update post 
@app.put('/posts/update/{post_id}',status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id:int,post:Post):
    if model.find_post(post_id):
        model.delete_post(post_id)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There Is NO Post With Id ({post_id})")
    model.add_post(post)
    return {"massage":"Post Updated"}

# Delete  post 
@app.delete('/posts/delete/{post_id}',status_code=status.HTTP_200_OK)
def delete_post(post_id:int):
    if model.delete_post(post_id) == 0 :
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"this is no Post with id ({post_id})")
    return {"massage":"Post Deleted"}