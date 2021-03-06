from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from blog.model import *

class DBManager:

    __engine = None
    __session = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        DBManager.__session = scoped_session(
                                    sessionmaker(autocommit=False,
                                    autoflush=False,
                                    bind=DBManager.__engine)
                                )

        global dao
        dao = DBManager.__session

    @staticmethod
    def init_db():
        from blog.model import Base
        Base.metadata.create_all(bind=DBManager.__engine)

dao = None