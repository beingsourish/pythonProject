import sqlite3
from sqlite3 import Error
def _make_connection():
    try:
        con=sqlite3.connect("mydb.db")
        print("connection success")
        return con
    except Error:
        print("error in connection")


def _create_table(conn):
        try:
                conn.execute("CREATE TABLE SCHOOL (SCHOOL_ID NUMBER,SCHOOL_NAME VARCHAR2(100),ADDRESS VARCHAR2(1000))")
                conn.execute("CREATE TABLE STUDENT (STUDENT_ID NUMBER,STUDENT_NAME VARCHAR2(100),SCHOOL_ID NUMBER)")
                print("TABLES CREATED success")

        except Error:
                print("error in connection",Error)
        finally:
                conn.close()


def _insert_data(conn):
        try:
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (1,'KV','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (2,'Kk','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (3,'KV','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (4,'KL','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (5,'KLL','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (6,'KOO','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (7,'KLLLPP','Portblair')")
                conn.execute("INSERT INTO SCHOOL (SCHOOL_ID ,SCHOOL_NAME ,ADDRESS ) values (8,'KOPPP','Portblair')")
                conn.execute("insert into student(student_id,student_name,school_id) values (1,'Sourishhh',1)")
                conn.execute("insert into student(student_id,student_name,school_id) values (2,'Ananya',2)")
                conn.execute("insert into student(student_id,student_name,school_id) values (3,'Sukanya',1)")
                print("Data loaded")
                conn.commit()
        except Error:
                print("error in connection",Error)
        finally:
                conn.close()





def _retrieve_student(conn):
        try:
                __data_set=conn.execute("SELECT * FROM STUDENT")

                for reg in __data_set:
                    print("student_id",reg[0])
                    print("student_name", reg[1])
                    print("shool_id", reg[2])


        except Error:
                print("error in connection",Error)
        finally:
                conn.close()




conn=_make_connection()
#_create_table(conn)
#conn=_make_connection()
#_insert_data(conn)
_retrieve_student(conn)
