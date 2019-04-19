import time

from sqlalchemy import and_, func

from Database.base import Session, engine, Base
from Database.Models import VendingMachines, DrugsRequestRecords, DrugDispenseRecords

Base.metadata.create_all(engine)

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
            print("Vending machine already persisted in database.")
        finally:
            self.session.close()

    def getVendingMachine(self, id):
        try:
            VM = self.session.query(VendingMachines).filter(VendingMachines.uid == id).first()
            return VM
        except:
            self.session.rollback()
            raise Exception("No Vending Machine exists with id {}.".format(id))
        finally:
            self.session.close()

    def setAllVmsAvailable(self):
        try:
            self.session.query(VendingMachines.uid).update(dict(status=0))
            self.session.commit()
            print("Updated all Vms status to 0")
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def listAllAvailableVendingMachines(self):
        try:
            vms = self.session.query(VendingMachines) \
                    .filter(VendingMachines.status == 0).all()
            return vms
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def getDrugsRequestRecord(self, caseNumber):
        try:
            ReqRecord = self.session.query(DrugsRequestRecords).filter(DrugsRequestRecords.case_number == caseNumber).first()
            return ReqRecord
        except:
            self.session.rollback()
            raise Exception("No Drugs request exists with caseNumber {}.".format(caseNumber))
        finally:
            self.session.close()

    def isVmBusy(self, vmId):
        try:
            vm = self.session.query(VendingMachines).filter(VendingMachines.uid == vmId).first()
            if vm.status == 1:
                return True
            else:
                return False
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def isVmPersisted(self, uid):
        try:
            s = self.session.query(VendingMachines).filter(VendingMachines.uid == uid).first()
            if s != None:
                return True
            else:
                return False
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def updateVmStatus(self, vmId, status):
        try:
            self.session.query(VendingMachines.uid).filter_by(uid=vmId).update(dict(status=status))
            self.session.commit()
            # print("Updated Vm id {} status {}".format(vmId, status))
        except:
            self.session.rollback()
            print("failed to update Vm {} status".format(vmId))
            raise
        finally:
            self.session.close()

    def getDrugRequestRecord(self, caseNumber):
        try:
            dr = self.session.query(DrugsRequestRecords) \
                .filter(DrugsRequestRecords.case_number == caseNumber).first()
            return dr
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def getDrugDispenseRecord(self, caseNumber, slot):
        try:
            dr = self.session.query(DrugDispenseRecords) \
                .filter(and_(DrugsRequestRecords.case_number == caseNumber),
                             DrugDispenseRecords.drug_slot == slot).first()
            return dr
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def validateCaseNumber(self, caseNumber):
        dr = self.getDrugRequestRecord(caseNumber)
        if dr is not None:
            if dr.total_drugs_dispensed != dr.total_drugs_record:
                return True
            else:
                print("All drugs for case number {} already dispensed".format(caseNumber))
                return False
        else:
            return True

    def drugsRequestQuantityStatus(self, oldDispenseQty, caseNumber, slotNumber):
        try:
            d = self.session.query(DrugDispenseRecords)\
                .filter(and_(DrugDispenseRecords.case_number == caseNumber,
                             DrugDispenseRecords.drug_slot == slotNumber)).first()
            newDispenseQty = d.total_dispensed
            # print("old: {} , new: {}".format(oldDispenseQty, newDispenseQty))
            if oldDispenseQty == newDispenseQty:
                return False
            elif oldDispenseQty < newDispenseQty:
                # drugs quantity has been increased by 1, which means VM is actively responding
                # check if all the requested drugs are completed ?
                requestStatus = self.getDrugRequestRecord(caseNumber)
                if requestStatus.total_drugs_record == requestStatus.total_drugs_dispensed:
                    return "Completed"
                else:
                    return True
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def updateDrugDispenseQuantity(self, caseNumber, slot):
        try:
            self.session.query(DrugDispenseRecords) \
                .filter(and_(DrugDispenseRecords.case_number == caseNumber,
                             DrugDispenseRecords.drug_slot == slot)) \
                .update({'total_dispensed': DrugDispenseRecords.total_dispensed + 1})
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def getCompleteDrugRecord(self, caseNumber, slot):
        try:
            result = self.session.query(DrugDispenseRecords, VendingMachines, DrugsRequestRecords) \
                .filter(and_(DrugDispenseRecords.case_number == caseNumber,
                             DrugDispenseRecords.drug_slot == slot))\
                .join(DrugsRequestRecords, DrugsRequestRecords.case_number == DrugDispenseRecords.case_number)\
                .join(VendingMachines, VendingMachines.id == DrugsRequestRecords.vending_machine_id).first()
            drugDispenseRecord = result[0]
            vendingMachine = result[1]
            drugRequestRecord = result[2]
            return drugDispenseRecord, vendingMachine, drugRequestRecord
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def updateDrugsRequestQuantity(self, caseNumber):
        try:
            self.session.query(DrugsRequestRecords) \
                .filter(DrugsRequestRecords.case_number == caseNumber) \
                .update({'total_drugs_dispensed': DrugsRequestRecords.total_drugs_dispensed + 1})
            self.session.commit()
            return self.session.query(DrugsRequestRecords) \
                .filter(DrugsRequestRecords.case_number == caseNumber).first()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def isReqIdValidForGivenDrug(self, vmId, caseNumber, slot):
        try:
            result = self.session.query(DrugDispenseRecords, VendingMachines) \
                .filter(and_(DrugDispenseRecords.case_number == caseNumber,
                             DrugDispenseRecords.drug_slot == slot))\
                .join(DrugsRequestRecords, DrugsRequestRecords.case_number == DrugDispenseRecords.case_number)\
                .join(VendingMachines, VendingMachines.id == DrugsRequestRecords.vending_machine_id).first()
            drugRecord = result[0]
            vendingMachine = result[1]
            if drugRecord is not None:
                if vendingMachine.status == 1:
                    if not self.isAllQuantityDispensed(drugRecord):
                        # drug_code for this reqId has not meet total_quantity, so this reqId is still valid
                        return True
                    else:
                        print("drug_slot {} for caseNumber {} has already been fully dispensed to total "
                              "quantity requested. This means, we have received and OLD or INVALID case number from VM id {}."
                              "This should never happen!".format(drugRecord.drug_slot, caseNumber, vmId))
                        return False
                else:
                    print("Received response for drug_slot {}, caseNumber {}, for non-busy VM {}."
                          "This means that VM took too long to respond, and python script timedOut and aborted the "
                          "transaction for this VM and marked it with status available. Since the VM has dispensed "
                          "this medicine, we'll still process it..."
                          .format(drugRecord.drug_slot, caseNumber, vmId))
                    return True
            else:
                print("No caseNumber {} exists for given slot {} from VM {}".format(caseNumber, slot, vmId))
                return False

        except:
            self.session.rollback()
            return False
        finally:
            self.session.close()

    def isAllQuantityDispensed(self, drugRecord):
        if drugRecord.total_dispensed == drugRecord.quantity:
            # All required quantity of this drug has been dispensed
            return True
        else:
            return False

    def populateDrugsRecords(self, jsonRecord):
        vmId = jsonRecord["vending_machine_id"]
        caseNumber = jsonRecord["case_number"]
        try:
            dr = self.session.query(DrugsRequestRecords) \
                .filter(DrugsRequestRecords.case_number == caseNumber).first()

            if dr is None:  # if no caseNumber already exists

                # print("Storing drugs record with caseNumber `{}` for vending machine id `{}`".format(caseNumber, vmId))
                vendingMachine = self.getVendingMachine(vmId)
                totalDrugRecords = len(jsonRecord["data"]["medicine"])
                drugsRequestRecords = DrugsRequestRecords(vendingMachine.id, caseNumber, totalDrugRecords, func.current_timestamp())
                self.session.add(drugsRequestRecords)
                self.session.commit()

                requestRecord = self.getDrugsRequestRecord(caseNumber)
                drugDispenseRecords = []
                for drug in jsonRecord["data"]["medicine"]:
                    drug_slot = drug["slot_number"]
                    qty = drug["quantity"]
                    drugDispenseRecord = DrugDispenseRecords(caseNumber, requestRecord.id, drug_slot, qty)
                    drugDispenseRecords.append(drugDispenseRecord)
                    # print("reqId {}, vmId {}, drug_code {}, qty {}".format(reqId, vendingMachine.id, drugCode, qty))
                self.session.bulk_save_objects(drugDispenseRecords)
                self.session.commit()
                return True
            else:
                print("Drugs request coming from doctor with already existing case Number {}.".format(caseNumber))
                return True
        except:
            self.session.rollback()
            print("failed to store drug records.")
            return False
        finally:
            self.session.close()
