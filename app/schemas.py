from pydantic import BaseModel

class Zap_input(BaseModel):
    url: str
    class Config:
        orm_mode = True