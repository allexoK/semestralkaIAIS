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
        self.cursor.execute("SELECT * FROM `Intervention` WHERE patientId = '"+str(id)+"';")
        patientInterventions = []
        rows = 0
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                rows += 25
                intervention = []
                intervention.append(str(patData[0]))
                intervention.append(str(patData[1]))
                intervention.append(str(patData[2]))
                intervention.append(str(patData[3]))
                intervention.append(str(patData[4]))
                patientInterventions.append(intervention)

        return  [patientInterventions,rows]

    def getPatientVisits(self,id):
        self.cursor.execute("SELECT * FROM `Visit` WHERE patientId = '"+str(id)+"';")
        patientVisits = [["Date","Goal"]]
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                intervention = []
                intervention.append(str(patData[1]))
                intervention.append(str(patData[2]))
                patientVisits.append(intervention)

        return  patientVisits

    def getPatientDiagnostics(self,id):
        self.cursor.execute("SELECT * FROM `Diagnostics` WHERE patientId = '"+str(id)+"';")
        patientDiagnostics = [["Name","Date","Result"]]
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                intervention = []
                intervention.append(str(patData[1]))
                intervention.append(str(patData[2]))
                intervention.append(str(patData[3]))
                patientDiagnostics.append(intervention)

        return  patientDiagnostics

    def getPatientMedicines(self,id):
        self.cursor.execute("SELECT * FROM `Medicine choise` WHERE patientId = '"+str(id)+"';")
        medIds = []
        while(True):
            patData = self.cursor.fetchone()
            if(not patData):
                break
            else:
                medIds.append(patData[0])

        medNames = [["Name",""]]
        for x in range(len(medIds)):
            self.cursor.execute("SELECT * FROM `Medicine` WHERE id = '"+str(medIds[x])+"';")
            medData = self.cursor.fetchone()
            medNames.append([medData[1],""])

        return medNames


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

    def insertNewPatient(self,idp,name,surname,gender,status,birthPlace,birthDate):
        command = "INSERT INTO `Patient` (`id`, `name`, `surname`, `doctorId`, `gender`, `status`, `birthPlace`, `birthDate`) VALUES (\"" +idp +"\", \"" +name +"\", \"" +surname +"\", '1111', \"" +gender +"\", \"" +status +"\", \"" +birthPlace +"\",\"" +birthDate +"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass

    def insertNewProcedure(self,idp,name,snomed,date):
        command = "INSERT INTO `Intervention` (`id`, `name`, `date`, `patientId`, `snomed`) VALUES (NULL, \"" +name +"\", \"" +date +"\", \"" +idp +"\", \""+ snomed+"\");"
        try:
            self.cursor.execute(command)
            self.db.commit()
        except:
            pass

    def deletePatient(self,idp):
        command = "DELETE FROM `Patient` WHERE `Patient`.`id` = "+ idp +""
        self.cursor.execute(command)
        self.db.commit()

    def deleteProcedure(self,idp):
        command = "DELETE FROM `Intervention` WHERE `Intervention`.`id` = '"+str(idp)+"';"
        print(command)
        self.cursor.execute(command)
        self.db.commit()


    def patientExists(self,idp):
        self.cursor.execute("SELECT * FROM `Patient` WHERE id = '"+str(idp)+"';")
        patData = self.cursor.fetchone()
        if(patData == None):
            return False
        else:
            return True
