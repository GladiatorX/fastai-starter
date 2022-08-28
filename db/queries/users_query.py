#from sqlalchemy.orm import Session

#from db.models.user import User
from pydantic_schemas.user import UserCreate

DBConn = "Some obj of db to query"

def get_user(db: DBConn, user_id: int):
    #return "select * etc.."#db.query(User).filter(User.id == user_id).first()
    pass


def get_user_by_email(db: DBConn, email: str):
    #return db.query(User).filter(User.email == email).first()
    pass

# skip limit for pagination
def get_users(db: DBConn, skip: int = 0, limit: int = 100):
    #return db.query(User).offset(skip).limit(limit).all()
    pass


def create_user(db: DBConn, user: UserCreate):
    # db_user = User(email=user.email, role=user.role)
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user
    pass
