from pydantic import BaseModel
from typing import Optional


# -------------------
# 🔐 USERS
# -------------------

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # ✅ Pydantic v2 compatible


# -------------------
# 🙏 PRAYERS
# -------------------

class PrayerBase(BaseModel):
    title: str
    content: str
    audio_url: Optional[str] = None

class PrayerCreate(PrayerBase):
    pass

class PrayerOut(PrayerBase):
    id: int

    class Config:
        from_attributes = True  # ✅ Pydantic v2 compatible


# -------------------
# 📓 JOURNALS
# -------------------

class JournalBase(BaseModel):
    entry: str

class JournalCreate(JournalBase):
    pass

class JournalOut(JournalBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # ✅ Pydantic v2 compatible
