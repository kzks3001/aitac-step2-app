from .setting import Base,Engine,session
from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Numeric, Boolean, JSON
from sqlalchemy.dialects.mysql import INTEGER


def create_data_record():
    try:
        print('create tables start')
        Base.metadata.create_all(bind=Engine)
    except:
        print('exception!!')
        session.rollback()
        raise
    finally:
        print('fin')
        session.close()


class Data(Base):
    __tablename__ = 'data'
    __table_args__ = {'extend_existing': True,"mysql_charset": "utf8mb4"} # テーブル定義時に実行で再定義可

    # カラム
    data_id = Column(INTEGER(unsigned=True),nullable=False,autoincrement=True,primary_key=True)
    date = Column(DateTime, nullable=False)
    temperature = Column(Numeric(10,2))
    humid = Column(Numeric(10,2))
    data1 = Column(Numeric(10,2))
    data2 = Column(Numeric(10,2))
    data3 = Column(Boolean)

    def create_data_record(
        self,
        date,
        temperature,
        humid,
        data1,
        data2,
        data3
    ):
        self.date = date
        self.temperature = temperature
        self.humid = humid
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3


