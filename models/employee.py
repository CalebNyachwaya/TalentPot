#!/usr/bin/python3
""" holds class employee"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from hashlib import md5


class Employee(BaseModel, Base):
    """Representation of a employee """
    if models.storage_t == 'db':
        __tablename__ = 'employees'
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone = Column(String(128), nullable=True)
        dept = Column(String(128), nullable=True)
        position = Column(String(128), nullable=True)
        DOB = Column(String(128), nullable=True)
        company = Column(String(128), nullable=True)
        address = Column(String(128), nullable=True)
        city = Column(String(128), nullable=True)
        country = Column(String(128), nullable=True)
        email = Column(String(250), nullable=False)
        hashed_password = Column(String(250), nullable=False)
        session_id = Column(String(250), nullable=True)
        session_created_at = Column(DateTime, default=datetime.utcnow)
        reset_token = Column(String(250), nullable=True)
    else:
        first_name = ""
        last_name = ""
        phone = ""
        dept = ""
        position = ""
        DOB = ""
        company = ""
        address = ""
        city = ""
        country = ""
        email = ""
        hashed_password = ""
        session_id = ""
        reset_token = ""


    def __init__(self, *args, **kwargs):
        """initializes employee"""
        super().__init__(*args, **kwargs)
