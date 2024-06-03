import pyodbc
import randomname
import random



conn = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=testDB;UID=sa;PWD=systems@123;Encrypt=no'

cnxn = pyodbc.connect(conn, autocommit=True)
crsr = cnxn.cursor()



for x in range(2000000):
    rand = random.randint(10000, 30000)
    name = randomname.get_name()
    #print(name, rand)
    crsr.execute("exec Sp_AddEmployee ?, Male, ?", name, rand)
