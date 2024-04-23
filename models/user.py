from sqlalchemy import Column, Integer, String, DateTime, Boolean

from config import Config
from models.database import db

config = Config()


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    last_login = Column(DateTime, default=None, nullable=True)
    token = Column(String(256))
    token_expires = Column(DateTime, default=None, nullable=True)
    enabled = Column(Boolean)

    # User roles
    # Sample relationship (See SQLAlchemy Documentation)
    # roles = relationship("Profiling", back_populates="user")

    def roles_list(self):
        return [role.to_dict() for role in self.roles]

    def __init__(self, username, first_name, last_name, password, email, token=None, enabled=True, recovery_token=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.token = token
        self.enabled = enabled
