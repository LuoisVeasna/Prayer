from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import User, Prayer, Journal
from schemas import UserCreate, PrayerCreate, JournalCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------
# 🔐 USERS
# -------------------

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# -------------------
# 🙏 PRAYERS
# -------------------

def get_prayers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Prayer).offset(skip).limit(limit).all()

def create_prayer(db: Session, prayer: PrayerCreate):
    db_prayer = Prayer(title=prayer.title, content=prayer.content, audio_url=prayer.audio_url)
    db.add(db_prayer)
    db.commit()
    db.refresh(db_prayer)
    return db_prayer


# -------------------
# 📓 JOURNALS
# -------------------

def get_user_journals(db: Session, user_id: int):
    return db.query(Journal).filter(Journal.user_id == user_id).all()

def create_journal_entry(db: Session, journal: JournalCreate, user_id: int):
    db_entry = Journal(entry=journal.entry, user_id=user_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_journal_entry(db: Session, journal_id: int, user_id: int):
    journal = db.query(Journal).filter(Journal.id == journal_id, Journal.user_id == user_id).first()
    if journal:
        db.delete(journal)
        db.commit()
    return journal
