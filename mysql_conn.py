import datetime

import mysql.connector
import os
from dotenv import load_dotenv
from collections import namedtuple


load_dotenv()
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
PetRecord = namedtuple('PetRecord', ['name', 'owner', 'species', 'sex', 'birth', 'death'])
print(PetRecord)
pet_record = PetRecord(name='nemo', owner='derby', species='fish', sex='/N', birth='00-00-0000', death='00-00-0000')
print(pet_record._asdict())
with open('pet.txt') as file:
    contents = file.read()
birth_start = datetime.date(1980, 1, 1)
birth_end = datetime.date(1990, 12, 31)
try:
    mysql_connector = mysql.connector.connect(user='root', password=MYSQL_PASSWORD, host='localhost',
                                              database='db_example')
    cursor = mysql_connector.cursor()
    # query = "SELECT name, owner, species, sex, birth FROM pet"
    query = "SELECT * FROM pet"
    cursor.execute(query)
    # for (name, owner, species, sex, birth) in cursor:
    #     print("{} {} {} {} {} ".format(name, owner, species, sex, birth))
    for p in map(PetRecord._make, cursor.fetchall()):
        print(p.name, p.owner, p.species, p.sex, p.birth, p.death)
    cursor.close()
except mysql.connector.Error as err:
    print(err)

else:
    mysql_connector.close()
