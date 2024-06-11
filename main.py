import pyodbc
import randomname
import random
from multiprocessing import Process

conn = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testDB;UID=sa;PWD=ahmad@123;Encrypt=no'

cnxn = pyodbc.connect(conn, autocommit=True)
crsr = cnxn.cursor()


def rundbinsertiontask():

    for x in range(100):
        # print(name, rand)
        print("carnage ensues...")
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Female, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Female, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Female, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Female, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Female, ?", randomname.get_name(), random.randint(10000, 30000))
        crsr.execute("exec Sp_AddEmployee ?, Male, ?", randomname.get_name(), random.randint(10000, 30000))


if __name__ == '__main__':
    p1 = Process(target=rundbinsertiontask)
    p2 = Process(target=rundbinsertiontask)
    p3 = Process(target=rundbinsertiontask)
    p4 = Process(target=rundbinsertiontask)
    p5 = Process(target=rundbinsertiontask)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print("mass insert finished")