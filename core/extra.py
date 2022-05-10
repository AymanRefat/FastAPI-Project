from pathlib import Path 
import json as js 


def read_json_file(path:Path,**kwargs)->dict:
  with open(path,errors='ignore')as file:
    data = js.load(file,**kwargs)
    return data 