
import pyccda
from datetime import datetime

ccda_doc = pyccda.CcdaDocument(open('example.xml'))
ccda_doc._tree.set_ethnicity("123","White")
ccda_doc._tree.set_gender("M","Male")
ccda_doc._tree.set_marital_status("F","Free")
ccda_doc._tree.set_race("2106-3","White")
ccda_doc._tree.set_ethnicity("2186-5","Russian")
ccda_doc._tree.set_religion("1013","Christian")
ccda_doc._tree.set_birthplace("Perm","","27201","Russia")
ccda_doc._tree.set_dob('20111211')

ccda_doc.add_procedure("Chest X-Ray",'42011-7','20121122')
ccda_doc.add_vital("Height",'8302-2','20081123','181','cm')
ccda_doc.set_name("Alex","Jones")
ccda_doc._tree.save("output.xml")

