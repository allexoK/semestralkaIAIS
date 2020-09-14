import pymysql
import datetime

class DatabaseCommunication:
    def initDb(self,host,login,password):
        self.db = pymysql.connect(host,login,password,"Patient" )
        self.cursor = self.db.cursor()

    def getPatients(self):
        self.cursor.execute("SELECT * FROM `Patient` WHERE 1 ")
        patients = []
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                patients.append(patData)
        return  patients

    def getDoctorName(self):
        self.cursor.execute("SELECT * FROM `Doctor` WHERE id = '" + str(self.loggedAs) +"';")
        data = self.cursor.fetchone()
        if(data == None):
            return None
        return data[1]

    def getPatientNamesAndIds(self):
        self.cursor.execute("SELECT * FROM `Patient` WHERE doctorId = '"+str(self.loggedAs)+"';")
        patientIds = ""
        patientNames = ""
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                patientIds += (str(patData[0]) + "\n")
                patientNames += (str(patData[1]) + " " + (str(patData[2]) + "\n"))
                rows+=24
        return  [patientNames,patientIds,rows]

    def getPatientData(self,id):
        self.cursor.execute("SELECT * FROM `Patient` WHERE id = '"+str(id)+"';")
        patData = self.cursor.fetchone()
        return  patData

    def getPatientInterventions(self,id):
        self.cursor.execute("SELECT * FROM `Intervention choise` WHERE patientId = '"+str(id)+"';")
        patientInterventions = []
        intRes = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                intervention = []
                intervention.append(str(patData[0]))
                intervention.append(str(patData[1]))
                intervention.append(str(patData[3]))
                intRes.append(str(patData[4]))
                patientInterventions.append(intervention)

        for i in range(len(patientInterventions)):
            self.cursor.execute("SELECT * FROM `Intervention` WHERE id = '"+str(patientInterventions[i][1])+"';")
            patData = self.cursor.fetchone()
            patientInterventions[i].append(patData[1])
            patientInterventions[i].append(patData[2])
            patientInterventions[i].append(intRes[i])

        # print([patientInterventions,rows])
        return  [patientInterventions,rows]

    def getPatientDiagnostics(self,id):
        self.cursor.execute("SELECT * FROM `Diagnostics choise` WHERE patientId = '"+str(id)+"';")
        patientDiags = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                diag = []
                diag.append(str(patData[0]))
                diag.append(str(patData[1]))
                diag.append(str(patData[3]))
                patientDiags.append(diag)

        for diag in patientDiags:
            self.cursor.execute("SELECT * FROM `Diagnostics` WHERE id = '"+str(diag[1])+"';")
            patData = self.cursor.fetchone()
            diag.append(patData[1])
            diag.append(patData[2])

        # print([patientInterventions,rows])
        return  [patientDiags,rows]


    def getPatientMedicines(self,id):
        self.cursor.execute("SELECT * FROM `Medicine choise` WHERE patientId = '"+str(id)+"';")
        patientMeds = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                med = []
                med.append(str(patData[0]))
                med.append(str(patData[0]))
                med.append(str(patData[1]))
                med.append(str(patData[2]))
                patientMeds.append(med)

        for med in patientMeds:
            self.cursor.execute("SELECT * FROM `Medicine` WHERE id = '"+str(med[1])+"';")
            patData = self.cursor.fetchone()
            med.append(patData[1])
            med.append(patData[2])

        # print([patientInterventions,rows])
        return  [patientMeds,rows]

    def visitExists(self,id):
        self.cursor.execute("SELECT * FROM `Visit` WHERE id = '"+str(id)+"';")
        exists = False
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                exists = True
        return exists

    def getVisitInterventions(self,id):
        self.cursor.execute("SELECT * FROM `Intervention choise` WHERE visitId = '"+str(id)+"';")
        patientInterventions = []
        intRes = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                intervention = []
                intervention.append(str(patData[0]))
                intervention.append(str(patData[1]))
                intervention.append(str(patData[3]))
                intRes.append(str(patData[4]))
                patientInterventions.append(intervention)

        for i in range(len(patientInterventions)):
            self.cursor.execute("SELECT * FROM `Intervention` WHERE id = '"+str(patientInterventions[i][1])+"';")
            patData = self.cursor.fetchone()
            patientInterventions[i].append(patData[1])
            patientInterventions[i].append(patData[2])
            patientInterventions[i].append(intRes[i])

        return  [patientInterventions,rows]

    def getVisitDiagnostics(self,id):
        self.cursor.execute("SELECT * FROM `Diagnostics choise` WHERE visitId = '"+str(id)+"';")
        patientDiags = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                diag = []
                diag.append(str(patData[0]))
                diag.append(str(patData[1]))
                patientDiags.append(diag)

        for diag in patientDiags:
            self.cursor.execute("SELECT * FROM `Diagnostics` WHERE id = '"+str(diag[1])+"';")
            patData = self.cursor.fetchone()
            diag.append(patData[1])
            diag.append(patData[2])

        # print([patientInterventions,rows])
        return  [patientDiags,rows]


    def getVisitMedicines(self,id):
        self.cursor.execute("SELECT * FROM `Medicine choise` WHERE visitId = '"+str(id)+"';")
        patientMeds = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 17
                med = []
                med.append(str(patData[0]))
                med.append(str(patData[0]))
                med.append(str(patData[1]))
                patientMeds.append(med)

        for med in patientMeds:
            self.cursor.execute("SELECT * FROM `Medicine` WHERE id = '"+str(med[1])+"';")
            patData = self.cursor.fetchone()
            med.append(patData[1])
            med.append(patData[2])

        # print([patientInterventions,rows])
        return  [patientMeds,rows]

    def getPatientVisits(self,id):
        self.cursor.execute("SELECT * FROM `Visit` WHERE patientId = '"+str(id)+"';")
        patientVisits = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 12
                vis = []
                vis.append(str(patData[0]))
                vis.append(str(patData[1]))
                vis.append(str(patData[2]))
                patientVisits.append(vis)

        return [patientVisits,rows]

    def logIn(self,login,password):
        self.cursor.execute("SELECT * FROM `Doctor` WHERE login = '" + login +"';")
        data = self.cursor.fetchone()
        if(data == None):
            return False
        if(data[3] != password):
            return False
        self.loggedAs = data[0]
        return True

    def updatePatientName(self,name,idp):
        command = "UPDATE `Patient` SET `name` = \""+name+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientSurname(self,surnname,idp):
        command = "UPDATE `Patient` SET `surname` = \""+surnname+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientGender(self,gender,idp):
        command = "UPDATE `Patient` SET `gender` = \""+gender+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientStatus(self,status,idp):
        command = "UPDATE `Patient` SET `status` = \""+status+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientBirthPlace(self,birthPlace,idp):
        command = "UPDATE `Patient` SET `birthPlace` = \""+birthPlace+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientBirthCity(self,birthCity,idp):
        command = "UPDATE `Patient` SET `birthCity` = \""+birthCity+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()

    def updatePatientBirthPostal(self,birthPostal,idp):
        command = "UPDATE `Patient` SET `birthPostal` = \""+birthPostal+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        self.cursor.execute(command)
        self.db.commit()


    def updatePatientBirthDate(self,birthDate,idp):
        command = "UPDATE `Patient` SET `birthDate` = \""+birthDate+"\" WHERE `Patient`.`id` = \""+idp+"\";"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass

    def insertNewPatient(self,idp,name,surname,gender,status,birthPlace,birthCity,postal,birthDate):
        if(postal.isdigit()):
            command = "INSERT INTO `Patient` (`id`, `name`, `surname`, `doctorId`, `gender`, `status`, `birthPlace`, `birthState`,`birthCity`,`birthPostal`, `birthDate`) VALUES (\"" +idp +"\", \"" +name +"\", \"" +surname +"\", '1111', \"" +gender +"\", \"" +status +"\", \"" +birthPlace +"\",\"\",\"" + birthCity + "\", \"" + postal + "\", \"" + birthDate +"\");"
            try:
                self.cursor.execute(command)
                self.db.commit()
            except:
                pass

    def insertNewProcedure(self,idp,idProc,date,res):
        command = "INSERT INTO `Intervention choise` (`id`, `interventionId`, `visitId`, `date`,`result`) VALUES (NULL, \"" + str(idProc) + "\", \""+ str(idp) +"\", \""+ date+"\""+", \""+ str(res)+"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass
        
    def insertNewDiag(self,idp,idDiag):
        command = "INSERT INTO `Diagnostics choise` (`id`, `diagnosticsId`, `visitId`) VALUES (NULL, \"" + str(idDiag) + "\", \""+ str(idp) +"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass

    def insertNewMed(self,idp,idMed):
        command = "INSERT INTO `Medicine choise` (`medicineId`, `visitId`) VALUES (\""+ str(idMed) +"\", \""+ str(idp) +"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass

    def insertNewVisit(self,idp,date):
        command = "INSERT INTO `Visit` (`id`, `patientId`, `date`) VALUES (NULL, \""+ str(idp) +"\", \""+ date +"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
            return str(self.cursor.lastrowid)
        except:
            pass
        return ""
        
    def deletePatient(self,idp):
        command = "DELETE FROM `Patient` WHERE `Patient`.`id` = "+ idp +""
        self.cursor.execute(command)
        self.db.commit()

    def deleteProcedure(self,idp):
        command = "DELETE FROM `Intervention choise` WHERE `Intervention choise`.`id` = '"+str(idp)+"';"
        self.cursor.execute(command)
        self.db.commit()

    def deleteDiag(self,idp):
        command = "DELETE FROM `Diagnostics choise` WHERE `Diagnostics choise`.`id` = '"+str(idp)+"';"
        self.cursor.execute(command)
        self.db.commit()

    def deleteMed(self,idp):
        command = "DELETE FROM `Medicine choise` WHERE `Medicine choise`.`medicineId` = '"+str(idp)+"';"
        self.cursor.execute(command)
        self.db.commit()

    def deleteVisit(self,idp):
        command = "DELETE FROM `Visit` WHERE `Visit`.`id` = '"+str(idp)+"';"
        self.cursor.execute(command)
        self.db.commit()

    def patientExists(self,idp):
        self.cursor.execute("SELECT * FROM `Patient` WHERE id = '"+str(idp)+"';")
        patData = self.cursor.fetchone()
        if(patData == None):
            return False
        else:
            return True

 
    def getProcConcepts(self):
        self.cursor.execute("SELECT * FROM `Intervention`;")
        procs = []
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                procs.append([str(patData[2]),str(patData[1]),str(patData[0])])
        return procs

    def getDiagConcepts(self):
        self.cursor.execute("SELECT * FROM `Diagnostics`;")
        diags = []
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                diags.append([str(patData[2]),str(patData[1]),str(patData[0])])
        return diags

    def getMedConcepts(self):
        self.cursor.execute("SELECT * FROM `Medicine`;")
        meds = []
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                meds.append([str(patData[2]),str(patData[1]),str(patData[0])])
        return meds
