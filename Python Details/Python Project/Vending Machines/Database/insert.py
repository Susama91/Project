from Database.DataHandler import DataHandler
from sqlalchemy import and_, func
import time
from Database.base import Session, engine, Base

Base.metadata.create_all(engine)
session = Session()


vending_id1 = DataHandler.addVendingMachine("5123a", "nel")
vending_id2 = DataHandler.addVendingMachine('5123b', "hyd")
vending_id3 = DataHandler.addVendingMachine('5123c', "sec")

