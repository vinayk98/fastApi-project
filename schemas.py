from pydantic import BaseModel

#articles inside user display is a list of articles, so we need to create a schema for articles as well
class Articles(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
            from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
class UserDisplay(BaseModel):
    username: str
    email: str
    items: list[Articles] = []
    class Config:
        from_attributes = True
        
#user inside article display is a single user, so we need to create a schema for user as well
class User(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int
    
class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config:
        from_attributes = True