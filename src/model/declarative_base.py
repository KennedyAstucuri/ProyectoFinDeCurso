from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

driverr = 'ODBC Driver 17 for SQL Server'
server = r'SRVJEAN\SQLEXPRESS'
database = 'DBHorizonte'
username = 'sa'
password = '123'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driverr}'

engine = create_engine(connection_string, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()