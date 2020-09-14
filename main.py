#!/usr/bin/env python
import kivy
from DatabaseCommunication import DatabaseCommunication
from kivy.core.window import Window
Window.fullscreen = False
from kivy.config import Config
Config.set('graphics', 'width', '1800')
Config.set('graphics', 'height', '700')
Config.set("graphics", "borderless", "0")
Config.set("graphics", "resizable", "0")
Config.write()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.clock import Clock
import pathlib
import pyccda
from datetime import datetime

DB_HOST = "localhost"
DB_LOGIN = "alex"
DB_PASSWORD = "alexoidy"

class testGui(Widget):
    loginButton = ObjectProperty(None)
    loginPassword = ObjectProperty(None)
    loginLogin = ObjectProperty(None)
    doctorName = ObjectProperty(None)
    patientsNames = ObjectProperty(None)
    patientIds = ObjectProperty(None)
    scrollPage = ObjectProperty(None)
    genderFemale = ObjectProperty(None)
    genderMale = ObjectProperty(None)
    nameField = ObjectProperty(None)
    surnameField = ObjectProperty(None)
    birthPlaceField = ObjectProperty(None)
    birthDateField = ObjectProperty(None)
    birthCityField = ObjectProperty(None)
    birthPostalField = ObjectProperty(None)
    getPatientData = ObjectProperty(None)
    patientDataId = ObjectProperty(None)
    setPatientData = ObjectProperty(None)
    delPatientData = ObjectProperty(None)
    
    dateProcField = ObjectProperty(None)
    snomedProcField = ObjectProperty(None)
    addProcedure = ObjectProperty(None)
    proc = ObjectProperty(None)
    procDate = ObjectProperty(None)
    scrollPageProc = ObjectProperty(None)
    nameProcField = ObjectProperty(None)
    idDelProcField = ObjectProperty(None)
    delProcedure = ObjectProperty(None)
    procId = ObjectProperty(None)
    procName = ObjectProperty(None)
    procKonc = ObjectProperty(None)
    procRes = ObjectProperty(None)
    procPos = ObjectProperty(None)
    procNeg = ObjectProperty(None)

    snomedDiagField = ObjectProperty(None)
    addDiag = ObjectProperty(None)
    diag = ObjectProperty(None)
    scrollPageDiag = ObjectProperty(None)
    nameDiagField = ObjectProperty(None)
    idDelDiagField = ObjectProperty(None)
    delDiag = ObjectProperty(None)
    diagId = ObjectProperty(None)
    diagName = ObjectProperty(None)
    diagKonc = ObjectProperty(None)

    snomedMedField = ObjectProperty(None)
    addMed = ObjectProperty(None)
    med = ObjectProperty(None)
    scrollPageMed = ObjectProperty(None)
    nameMedField = ObjectProperty(None)
    idDelMedField = ObjectProperty(None)
    delMed = ObjectProperty(None)
    medId = ObjectProperty(None)
    medName = ObjectProperty(None)
    medKonc = ObjectProperty(None)

    visitDate = ObjectProperty(None)
    visitId = ObjectProperty(None)
    scrollPageVisits = ObjectProperty(None)
    removeVisit = ObjectProperty(None)
    addVisit = ObjectProperty(None)
    dateAddVisitField = ObjectProperty(None)
    idDelVisitField = ObjectProperty(None)

    exportAsCCDA = ObjectProperty(None)
    exportAsCCDAPath = ObjectProperty(None)
    martSingle = ObjectProperty(None)
    martMarried = ObjectProperty(None)

    modVisitButton = ObjectProperty(None)
    idModVisitText = ObjectProperty(None)

    loadedVisitId = ObjectProperty(None)
    loadedVisitDate = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.dbCom = DatabaseCommunication()
        try:
            self.dbCom.initDb(DB_HOST,DB_LOGIN,DB_PASSWORD)
        except:
            pass
        Widget.__init__(self)
        self.loginButton.on_press = self.logRequest
        self.getPatientData.on_press = self.showPatientDataById
        self.setPatientData.on_press = self.updatePatientDataById
        self.delPatientData.on_press = self.deletePatientDataById
        self.modVisitButton.on_press = self.getVisitDataByWrittenId

        self.addProcedure.on_press = self.addProcedureById
        self.delProcedure.on_press = self.delProcedureById

        self.addDiag.on_press = self.addDiagById
        self.delDiag.on_press = self.delDiagById

        self.addMed.on_press = self.addMedById
        self.delMed.on_press = self.delMedById

        self.addVisit.on_press = self.addVisitById
        self.removeVisit.on_press = self.delVisitById

        self.exportAsCCDA.on_press = self.exportAsCCDAById
        self.loginPassword.text = "jan123"
        self.loginLogin.text = "janvak"
        self.exportAsCCDAPath.text = str(pathlib.Path().absolute()) + "/output.xml"
        self.loadProcConcepts()
        self.loadDiagConcepts()
        self.loadMedConcepts()

    def logRequest(self):
        if(self.dbCom.logIn(self.loginLogin.text,self.loginPassword.text) == True):
            self.successfullLoginCallback()

    def loadProcConcepts(self):
        procs = self.dbCom.getProcConcepts()
        self.procToInsert = None
        for proc in procs:
            button = Button(size_hint_y = 0.05,text = proc[0] + " " + proc[1])
            def func(p0=proc[0],p1=proc[1],p2=proc[2]):
                self.nameProcField.text = p1
                self.snomedProcField.text = p0
                self.procToInsert = p2
            button.on_press = func
            self.procKonc.add_widget(button)
        for x in range(10-len(procs)):
            boxl = BoxLayout(orientation = 'horizontal', size_hint_y = 0.05)
            self.procKonc.add_widget(boxl)

    def loadDiagConcepts(self):
        diags = self.dbCom.getDiagConcepts()
        self.diagToInsert = None
        for diag in diags:
            button = Button(size_hint_y = 0.05,text = diag[0] + " " + diag[1])
            def func(d0=diag[0],d1=diag[1],d2=diag[2]):
                self.nameDiagField.text = d1
                self.snomedDiagField.text = d0
                self.diagToInsert = d2
            button.on_press = func
            self.diagKonc.add_widget(button)
        for x in range(10-len(diags)):
            boxl = BoxLayout(orientation = 'horizontal', size_hint_y = 0.05)
            self.diagKonc.add_widget(boxl)

    def loadMedConcepts(self):
        meds = self.dbCom.getMedConcepts()
        self.medToInsert = None
        for med in meds:
            button = Button(size_hint_y = 0.05,text = med[0] + " " + med[1])
            def func(m0=med[0],m1=med[1],m2=med[2]):
                self.nameMedField.text = m1
                self.snomedMedField.text = m0
                self.medToInsert = m2
            button.on_press = func
            self.medKonc.add_widget(button)
        for x in range(10-len(meds)):
            boxl = BoxLayout(orientation = 'horizontal', size_hint_y = 0.05)
            self.medKonc.add_widget(boxl)

    def loadScrollPage(self):
        allPat = self.dbCom.getPatientNamesAndIds()
        self.patientsNames.text = allPat[0]
        self.patientsIds.text = allPat[1]
        self.scrollPage.height = allPat[2]

    def successfullLoginCallback(self):
        self.doctorName.text = self.dbCom.getDoctorName()
        self.loadScrollPage()
    
    def writeDataToColumns(self,name,surname,gender,status,birthPlace,birthCity,birthPostal,birthDate):
        self.nameField.text = name
        self.surnameField.text = surname
        if (gender == "Male"):
            self.genderMale.active = True
        else:
            self.genderFemale.active = True
        if(status == "Single"):
            self.martSingle.active = True
        else:
            self.martMarried.active = True
        self.birthPlaceField.text = birthPlace
        self.birthCityField.text = birthCity
        self.birthPostalField.text = str(birthPostal)
        self.birthDateField.text = str(birthDate) 

    def showPatientDataById(self):
        patId = self.patientDataId.text
        if(patId.isdigit()):
            data = self.dbCom.getPatientData(patId)
            if(data != None):
                self.writeDataToColumns(data[1],data[2],data[4],data[5],data[6],data[8],data[9],data[10])

                allvis = self.dbCom.getPatientVisits(patId)
                viss = allvis[0]
                stringVDates = "Date\n"
                stringVIds = "Id\n"
                for vis in viss:
                    stringVDates += vis[1] + "\n"
                    stringVIds += vis[0] + "\n"
                self.visitDate.text = stringVDates
                self.visitId.text = stringVIds
                height = allvis[1]
                height+=50
                self.scrollPageVisits.height = height

            else:
                self.writeDataToColumns("","","","","","","","")
        else:
            self.writeDataToColumns("","","","","","","","")

    def getVisitDataByWrittenId(self):
        
        self.getVisitDataById(self.idModVisitText.text)

    def getVisitDataById(self,visitId):
        if(visitId != ""):
            if(visitId.isdigit()):
                if(self.dbCom.visitExists(visitId) == True):
                    self.loadedVisitId.text = visitId
                    allint = self.dbCom.getVisitInterventions(visitId)
                    interventions = allint[0]
                    stringProc = "Snomed ct\n"
                    stringDates = "Date\n"
                    stringNames = "Name\n"
                    stringIds = "Id\n"
                    stringResults = "Result\n"
                    for intervention in interventions:
                        stringProc += intervention[4] + "\n"
                        stringDates += intervention[2] + "\n"
                        stringNames += intervention[3] + "\n"
                        stringIds += intervention[0] + "\n"
                        stringResults += intervention[5] + "\n"
                    self.proc.text = stringProc
                    self.procDate.text = stringDates
                    self.procId.text = stringIds
                    self.procName.text = stringNames
                    self.procRes.text = stringResults
                    height = allint[1]
                    height+=50
                    self.scrollPageProc.height = height

                    alldiag = self.dbCom.getVisitDiagnostics(visitId)
                    diags = alldiag[0]
                    stringDiag = "ICD-10\n"
                    stringDNames = "Name\n"
                    stringDIds = "Id\n"
                    for diag in diags:
                        stringDiag += diag[3] + "\n"
                        stringDNames += diag[2] + "\n"
                        stringDIds += diag[0] + "\n"
                    self.diag.text = stringDiag
                    self.diagId.text = stringDIds
                    self.diagName.text = stringDNames
                    height = alldiag[1]
                    height+=50
                    self.scrollPageDiag.height = height

                    allmed = self.dbCom.getVisitMedicines(visitId)
                    meds = allmed[0]
                    stringMeds = "Snomed ct\n"
                    stringMNames = "Name\n"
                    stringMIds = "Id\n"
                    for med in meds:
                        stringMeds += med[4] + "\n"
                        stringMNames += med[3] + "\n"
                        stringMIds += med[0] + "\n"
                    self.med.text = stringMeds
                    self.medId.text = stringMIds
                    self.medName.text = stringMNames
                    height = allmed[1]
                    height+=50
                    self.scrollPageMed.height = height
                else:
                    self.loadedVisitId.text = ""

                    self.proc.text = "Snomed ct\n"
                    self.procDate.text = "Date\n"
                    self.procId.text = "Id\n"
                    self.procName.text = "Result\n"
                    self.procRes.text = "Snomed ct\n"
        
                    self.diag.text = "ICD-10\n"
                    self.diagId.text = "Id\n"
                    self.diagName.text = "Result\n"
        
                    self.med.text = "Snomed ct\n"
                    self.medId.text = "Id\n"
                    self.medName.text = "Name\n"

        else:
            self.loadedVisitId.text = ""

            self.proc.text = "Snomed ct\n"
            self.procDate.text = "Date\n"
            self.procId.text = "Id\n"
            self.procName.text = "Result\n"
            self.procRes.text = "Snomed ct\n"

            self.diag.text = "ICD-10\n"
            self.diagId.text = "Id\n"
            self.diagName.text = "Result\n"

            self.med.text = "Snomed ct\n"
            self.medId.text = "Id\n"
            self.medName.text = "Name\n"


    def updatePatientDataById(self):
        patId = self.patientDataId.text
        if(patId.isdigit()):
            gender = ""
            if (self.genderMale.active == True):
                gender = "Male"
            else:
                gender = "Female"

            marital = ""
            if(self.martSingle.active == True):
                marital = "Single"
            if(self.martMarried.active == True):
                marital = "Married"
            if(self.dbCom.patientExists(patId) == False):
                # print("Insert new patient")
                self.dbCom.insertNewPatient(idp = patId,name = self.nameField.text,surname = self.surnameField.text,gender = gender,status = marital, birthPlace = self.birthPlaceField.text, birthCity = self.birthCityField.text,postal = self.birthPostalField.text, birthDate = self.birthDateField.text)
            else:
                self.dbCom.updatePatientName(self.nameField.text,self.patientDataId.text)
                self.dbCom.updatePatientSurname(self.surnameField.text,self.patientDataId.text)
                self.dbCom.updatePatientGender(gender,self.patientDataId.text)
                self.dbCom.updatePatientStatus(marital,self.patientDataId.text)
                self.dbCom.updatePatientBirthPlace(self.birthPlaceField.text,self.patientDataId.text)
                self.dbCom.updatePatientBirthCity(self.birthCityField.text,self.patientDataId.text)
                if(self.birthPostalField.text.isdigit()):
                    self.dbCom.updatePatientBirthPostal(self.birthPostalField.text,self.patientDataId.text)
                self.dbCom.updatePatientBirthDate(self.birthDateField.text,self.patientDataId.text)
            self.loadScrollPage()

    def deletePatientDataById(self):
        patId = self.patientDataId.text
        if(patId.isdigit()):
            self.dbCom.deletePatient(patId)
        self.loadScrollPage()

    def addProcedureById(self):
        if(self.loadedVisitId.text != ""):
            visId = self.loadedVisitId.text
            if(self.procToInsert != None):
                if(self.procPos.active == True):
                    res = "pos"
                else:
                    res = "neg"
                self.dbCom.insertNewProcedure(visId,self.procToInsert,self.dateProcField.text,res)
                self.getVisitDataById(self.loadedVisitId.text)

    def delProcedureById(self):
        procId = self.idDelProcField.text
        if(procId.isdigit()):
            if(procId==self.loadedVisitId.text):
                self.loadedVisitId.text = ""
            self.dbCom.deleteProcedure(procId)
            self.getVisitDataById(self.loadedVisitId.text)

    def addDiagById(self):
        if(self.loadedVisitId.text != ""):
            visId = self.loadedVisitId.text
            if(self.diagToInsert != None):
                self.dbCom.insertNewDiag(visId,self.diagToInsert)
                self.getVisitDataById(self.loadedVisitId.text)

    def addMedById(self):
        if(self.loadedVisitId.text != ""):
            patId = self.loadedVisitId.text
            if(self.medToInsert != None):
                self.dbCom.insertNewMed(patId,self.medToInsert)
                self.getVisitDataById(self.loadedVisitId.text)

    def addVisitById(self):
        patId = self.patientDataId.text
        if(patId.isdigit()):
            self.loadedVisitId.text = self.dbCom.insertNewVisit(patId,self.dateAddVisitField.text)
            self.showPatientDataById()
            self.getVisitDataById(self.loadedVisitId.text)

    def delDiagById(self):
        diagId = self.idDelDiagField.text
        if(diagId.isdigit()):
            self.dbCom.deleteDiag(diagId)
            self.getVisitDataById(self.loadedVisitId.text)

    def delMedById(self):
        medId = self.idDelMedField.text
        if(medId.isdigit()):
            self.dbCom.deleteMed(medId)
            self.getVisitDataById(self.loadedVisitId.text)

    def delVisitById(self):
        visId = self.idDelVisitField.text
        if(visId.isdigit()):
            self.loadedVisitId.text = ""
            self.dbCom.deleteVisit(visId)
            self.showPatientDataById()
            self.getVisitDataById(self.loadedVisitId.text)

    def exportAsCCDAById(self):
        patId = self.patientDataId.text
        if(patId.isdigit()):
            ccda_doc = pyccda.CcdaDocument(open('example.xml'))
            ccda_doc._tree.set_ethnicity("","")
            if (self.genderMale.active == True):
                ccda_doc._tree.set_gender("M","Male")
            else:
                ccda_doc._tree.set_gender("F","Female")
            if(self.martSingle.active == True):
                ccda_doc._tree.set_marital_status("S","Single")
            else:
                if(self.martMarried.active == True):
                    ccda_doc._tree.set_marital_status("M","Married")
            ccda_doc._tree.set_race("","")
            ccda_doc._tree.set_ethnicity("","")
            ccda_doc._tree.set_religion("","")
            ccda_doc._tree.set_birthplace("","","",self.birthPlaceField.text)
            ccda_doc._tree.set_dob(self.birthDateField.text)
            ccda_doc.set_name(self.nameField.text,self.surnameField.text)

            # interventions = self.dbCom.getPatientInterventions(patId)[0]
            # for intervention in interventions:
            #     ccda_doc.add_procedure(intervention[1],intervention[4],intervention[2])

            ccda_doc._tree.save(self.exportAsCCDAPath.text)

    def __del__(self):
        self.dbCom.closeDb()

class mainApp(App):

    def build(self):
        
        self.title = 'Test app'
        return testGui()

if __name__ == "__main__":
    app = mainApp()
    app.run()
