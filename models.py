from pydantic import BaseModel
from datetime import datetime 




class Post(BaseModel):
  title:str
  content:str 
  created_time:datetime = datetime.now()


