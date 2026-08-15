from sqlalchemy.orm import Session

from db.hash import Hash
from schemas import UserBase
from db.models import DbUser

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username, 
        email=request.email, 
        password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if user:
        return user
    else:
        return {"error": "User not found"} 

def get_all_users(db: Session):
    return db.query(DbUser).all()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        return None
    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt(request.password)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    #handle the case where the user is not found
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        return {"error": "User not found"}