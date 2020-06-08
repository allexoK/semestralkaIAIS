#!/usr/bin/env python
import kivy
from DatabaseCommunication import DatabaseCommunication
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
    exportAsCCDA = ObjectProperty(None)
    exportAsCCDAPath = ObjectProperty(None)
    martSingle = ObjectProperty(None)
    martMarried = ObjectProperty(None)
    procName = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.dbCom = DatabaseCommunication()
        try:
            self.dbCom.initDb(DB_HOST,DB_LOGIN,DB_PASSWORD)
        except :
            pass
        Widget.__init__(self)
        self.loginButton.on_press = self.logRequest
        self.getPatientData.on_press = self.showPatientDataById
        self.setPatientData.on_press = self.updatePatientDataById
        self.delPatientData.on_press = self.deletePatientDataById
        self.addProcedure.on_press = self.addProcedureById
        self.delProcedure.on_press = self.delProcedureById
        self.exportAsCCDA.on_press = self.exportAsCCDAById
        self.loginPassword.text = "jan123"
        self.loginLogin.text = "janvak"
        self.exportAsCCDAPath.text = str(pathlib.Path().absolute()) + "/output.xml"

    def logRequest(self):
        if(self.dbCom.logIn(self.loginLogin.text,self.loginPassword.text) == True):
            self.successfullLoginCallback()

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
                allint = self.dbCom.getPatientInterventions(patId)
                interventions = allint[0]
                stringProc = "Snomed ct\n"
                stringDates = "Date\n"
                stringNames = "Name\n"
                stringIds = "Id\n"
                for intervention in interventions:
                    stringProc += intervention[4] + "\n"
                    stringDates += intervention[2] + "\n"
                    stringNames += intervention[1] + "\n"
                    stringIds += intervention[0] + "\n"
                self.proc.text = stringProc
                self.procDate.text = stringDates
                self.procId.text = stringIds
                self.procName.text = stringNames
                height = allint[1]
                height+=50
                self.scrollPageProc.height = height
            else:
                self.writeDataToColumns("","","","","","","","")
        else:
            self.writeDataToColumns("","","","","","","","")

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
                self.dbCom.insertNewPatient(patId,self.nameField.text,self.surnameField.text,gender,marital,self.birthPlaceField.text,self.birthDateField.text)
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
        patId = self.patientDataId.text
        if(patId.isdigit()):
            self.dbCom.insertNewProcedure(patId,self.nameProcField.text,self.snomedProcField.text,self.dateProcField.text)
            self.showPatientDataById()

    def delProcedureById(self):
        procId = self.idDelProcField.text
        if(procId.isdigit()):
            self.dbCom.deleteProcedure(procId)
            self.showPatientDataById()

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

            interventions = self.dbCom.getPatientInterventions(patId)[0]
            for intervention in interventions:
                ccda_doc.add_procedure(intervention[1],intervention[4],intervention[2])

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
