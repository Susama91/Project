from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from Database.base import Base


class VendingMachines(Base):
    __tablename__ = 'vending_machines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(20), unique=True)
    location = Column(String(100), nullable=True)
    status = Column(Integer, default=0)
    drugs_request_records = relationship("DrugsRequestRecords", back_populates="vending_machine")

    def __init__(self, uid, location):
        self.uid = uid
        self.location = location


class DrugsRequestRecords(Base):
    __tablename__ = 'drugs_request_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    case_number = Column(String(20), unique=True)
    vending_machine_id = Column(Integer, ForeignKey('vending_machines.id'))
    vending_machine = relationship("VendingMachines", back_populates="drugs_request_records")
    drug_dispense_records = relationship("DrugDispenseRecords", back_populates="drugs_request_record")
    total_drugs_record = Column(Integer)
    total_drugs_dispensed = Column(Integer, default=0)
    creation_time = Column(DateTime)

    def __init__(self, vending_machine_id, case_number, total_drugs_record, creation_time):
        self.vending_machine_id = vending_machine_id
        self.case_number = case_number
        self.total_drugs_record = total_drugs_record
        self.creation_time = creation_time


class DrugDispenseRecords(Base):
    __tablename__ = 'drug_dispense_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    case_number = Column(String(20))
    drugs_request_record_id = Column(Integer, ForeignKey('drugs_request_records.id'))
    drugs_request_record = relationship("DrugsRequestRecords", back_populates="drug_dispense_records")
    drug_slot = Column(String(20))
    quantity = Column(Integer)
    total_dispensed = Column(Integer, default=0)

    def __init__(self, case_number, drugs_request_record_id, drug_slot, quantity):
        self.case_number = case_number
        self.drugs_request_record_id = drugs_request_record_id
        self.quantity = quantity
        self.drug_slot = drug_slot


