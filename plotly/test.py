# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Integer, String, DateTime, DECIMAL, text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:123456@192.168.1.15:3306/weather?charset=utf8", encoding='utf-8', echo=True)

metaData = MetaData()
Base = declarative_base()


class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    date = Column(Date)
    highest_temperature = Column(DECIMAL)
    lowest_temperature = Column(DECIMAL)
    weather = Column(String(20))
    wind_vane = Column(String(20))
    wind_power = Column(String(20))

    def __init__(self):
        self.session_class = sessionmaker(bind=engine)  # 返回的是类
        self.session = self.session_class()  # 创建实例

    @staticmethod
    def create_table():
        Base.metadata.create_all(engine)


class KunMing(Base):
    __tablename__ = "kunming"
    temperature = Column(DECIMAL)
    date = Column(DateTime)
    mois = Column(DECIMAL)
    wind_dire = Column(String(50))
    wind_speed = Column(String(50))
    id = Column(Integer, primary_key=True)

    def __init__(self, keylist):
        self.session_class = sessionmaker(bind=engine)  # 返回的是类
        self.session = self.session_class()  # 创建实例
        self.temperature = keylist['摄氏度']
        self.date = keylist['时间']
        self.mois = keylist['相对湿度']
        self.wind_dire = keylist['风向']
        self.wind_speed = keylist['风速']

    @staticmethod
    def create_table():
        Base.metadata.create_all(engine)


db = Weather()
# km = KunMing(1).create_table()

if __name__ == "__main__":
    result_list = db.session.query(Weather).from_statement(text("select * from weather")).params().all()
    _list = list()
    weather_type = set()
    for result in result_list:
        _list.append(result)
        weather_type.add(result.weather)
    for weather in iter(weather_type):
        print weather
    print len(_list)
