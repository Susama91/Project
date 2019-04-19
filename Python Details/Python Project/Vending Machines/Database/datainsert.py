# 1 - imports
from Database.Models import VendingMachines, DrugsRequestRecords, DrugDispenseRecords
from Database.base import Session, Base, engine
from datetime import time

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create vending machines
vending_id1= VendingMachines('5123a', "nello")
vending_id2= VendingMachines('5124b', "nel")
vending_id3= VendingMachines('5124c', "guntu")

# 4 - create Drugs Request Records
vmid1 = DrugsRequestRecords(1101,82145,15,'10:00:00')
vmid2 = DrugsRequestRecords(1102,82146,10,'11:00:00')

session.add(vending_id1)
session.add(vending_id2)
session.add(vending_id3)

session.commit()
session.close()



