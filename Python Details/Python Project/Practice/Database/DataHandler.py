import  time
from sqlalchemy import and_, func

from Database.base import Session, engine, Base

from Database.Models import VendingMachines, DrugsRequestRecords, DrugDispenseRecords

class DataHandler(object):
    def __init__(self):
        self.session = Session()

    def addVendingMachine(self, id, location):
        try:
            v = VendingMachines(id, location)
            self.session.add(v)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("vending machines already persisted in database")
        finally:
            self.session.close()

    def getVendingMachine(self, id):
        try:
            vm = self.session.query(VendingMachines).filter(VendingMachines.uid==id).first()
            return vm
        except:
            self.session.rollback()
            raise Exception("no vending machine exists with id {}.".format(id))
        finally:
            self.session.close()

    def setAllVmsAvailable(self):
        try:
            self.session.query(VendingMachines.uid).update(dict(status=0))
            self.session.commit()
            print("all vm status updated 0")
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def listAllAvailableVendingMachines(self,):
        try:
            vms = self.session.query(VendingMachines) \
                    .filter(VendingMachines.status==0).all()
            return vms
        except:
            self.session.rollback()
        finally:
            self.session.close()

    def getDrugsRequestRecord(self, casenumber):
        try:
            ReqRecord = self.session.query(DrugsRequestRecords).filter(DrugsRequestRecords.case_number==casenumber).first()
            return ReqRecord
        except:
            self.session.rollback
            raise Exception("no drugs available with casenumber{}.".format(casenumber))
        finally:
            self.session.close()








