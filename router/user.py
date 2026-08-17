from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

#with this router we mention common prefix and tags for all the routes in this router
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

#create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#read all user
@router.get("/all", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)
        

#read user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user(db, id)

# update user
@router.put("/update/{id}",response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db, id, request)

#delete user
@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db, id)
