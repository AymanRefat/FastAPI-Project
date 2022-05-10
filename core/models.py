from pydantic import BaseModel , validate_arguments , validator
from datetime import datetime 




class Post(BaseModel):
  title:str
  content:str 
  published:bool = True

