#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import models
from models.base_model import BaseModel, Base
from models.employee import Employee
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine, tuple_
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Employee": Employee}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        TP_MYSQL_USER = getenv('TP_MYSQL_USER')
        TP_MYSQL_PWD = getenv('TP_MYSQL_PWD')
        TP_MYSQL_HOST = getenv('TP_MYSQL_HOST')
        TP_MYSQL_DB = getenv('TP_MYSQL_DB')
        TP_ENV = getenv('TP_ENV')
        sess_dur = getenv("SESSION_DURATION")
        if sess_dur is None:
            self.session_duration = 0
        else:
            try:
                sess_val = int(sess_dur)
                self.session_duration = sess_val
            except Exception:
                self.session_duration = 0
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(TP_MYSQL_USER,
                                             TP_MYSQL_PWD,
                                             TP_MYSQL_HOST,
                                             TP_MYSQL_DB))
        if TP_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        try:
            self.__session.add(obj)
        except Exception:
            self.__session.rollback()

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def add_user(self, email: str, hashed_password: str) -> User:
        """method to add user via email and hashd
password and saved to db"""
        usr = Employee(email=email, hashed_password=hashed_password)
        try:
            self.__session.add(usr)
            self.__session.commit()
            return usr
        except Exception:
            self._session.rollback()
        return None

    def find_user_by(self, **kwargs) -> User:
        """find a user by their email or entered keywrd"""
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(User, key):
                fields.append(getattr(User, key))
                values.append(value)
            else:
                raise InvalidRequestError()
        result = self._session.query(User).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """method to update user"""
        """Updates a user based on a given id.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_source[getattr(User, key)] = value
            else:
                raise ValueError()
        self.__session.query(User).filter(User.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self.__session.commit()
