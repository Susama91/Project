from Database.Models import DrugsRequestRecords, DrugDispenseRecords, VendingMachines
from base import Session

# 2 - extract a session
session = Session()

# 3 - extract all machines
vm = session.query(VendingMachines).all()
#vm1=session.query(DrugsRequestRecords).all()

# 4 - print machies details
print('\n### All machines:')
for p in vm:
    print(f'{p.uid} located in {p.location}')
print('')

