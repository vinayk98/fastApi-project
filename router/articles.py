from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import oauth2_scheme
from db import db_articles
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(
    prefix="/article",
    tags=["article"]
)

@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_articles.create_article(db, request)      

@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db_articles.get_article(db, id)
