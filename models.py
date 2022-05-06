from pydantic import BaseModel , validate_arguments
from datetime import datetime 




class Post(BaseModel):
  id:int 
  title:str
  content:str 
  created_time:datetime = datetime.now()




class PostModel:
  posts:list[Post] = []

  @classmethod
  @validate_arguments
  def add_post(cls,post:Post)->None:
      cls.posts.append(post)

  
  @classmethod
  @validate_arguments
  def find_post(cls,id:int)->Post:
    """Search for the Post By id and return the Post Object if we don't found it, will return 0  """
    for post in cls.posts:
        if post.id == id:
            return post
    else:
      return 0 


  @classmethod
  @validate_arguments
  def delete_post(cls,id:int)->None:
    """Delete Post from the Model, or Return 0"""
    try:
      cls.posts.remove(cls.find_post(id))
    except: 
      return 0 