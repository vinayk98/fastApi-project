from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user, oauth2_scheme
from db import db_articles
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay, UserBase

router = APIRouter(
    prefix="/article",
    tags=["article"]
)

@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_articles.create_article(db, request)      

@router.get("/{id}")
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        "data": db_articles.get_article(db, id),
        "current_user": current_user
    }
