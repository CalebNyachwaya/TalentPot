#!/usr/bin/python3
""" holds class employee"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Employee(BaseModel, Base):
    """Representation of a employee """
    if models.storage_t == 'db':
        __tablename__ = 'employees'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        phone = Column(String(128), nullable=False)
        dept = Column(String(128), nullable=False)
        position = Column(String(128), nullable=False)
        DOB = Column(String(128), nullable=False)
        company = Column(String(128), nullable=False)
        address = Column(String(128), nullable=False)
        city = Column(String(128), nullable=False)
        country = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
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

    def __init__(self, *args, **kwargs):
        """initializes employee"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
