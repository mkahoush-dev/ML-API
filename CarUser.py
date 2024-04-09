from pydantic import BaseModel
 
class CarUser(BaseModel):
  age: int
  gender: int