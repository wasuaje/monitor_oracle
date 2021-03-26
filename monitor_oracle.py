#!/usr/bin/python

import os
import subprocess
import cx_Oracle
from prettytable import PrettyTable

ruta='/opt/app/oracle/product/11.2.0/dbhome_1/bin/'

connectString = 'exp_user/b4ll3n4@%s'
dbs=['content','clasideu','cvf3','users']

def main():
    titulo="""\t\t\t\t\t\t=========================================
              \t\t\t\t\t===== Espacio Usado de Archive Logs =====
              \t\t\t\t\t========================================="""
    #seteo de columnas
    sql2="""SELECT  (select instance_name from v$instance) as database, name,
                round(space_limit/1024/1024/1024,4) AS espacio_limite_GB,
                round(space_used/1024/1024/1024,4) AS espacio_usado_GB,
                ROUND((round(space_used/1024/1024/1024,4)*100)/round(space_limit/1024/1024/1024,4),2)  "% de Uso",
                space_reclaimable,number_of_files
                FROM v$recovery_file_dest
                """    
    db_conn = cx_Oracle.connect(connectString % 'content')
    cursor = db_conn.cursor()
    cursor.execute(sql2)
    
    col_names = [cn[0] for cn in cursor.description]
    x = PrettyTable(col_names)
    x.align[col_names[0]] = "c" 
    x.align[col_names[1]] = "c" 
    x.align[col_names[2]] = "c" 
    x.align[col_names[3]] = "c" 
    x.align[col_names[4]] = "c" 
    x.align[col_names[5]] = "c" 
    x.align[col_names[6]] = "c" 
    x.padding_width = 1    

    for i in dbs:
        db_conn = cx_Oracle.connect(connectString % i)        
        cursor2 = db_conn.cursor()        
        cursor2.execute(sql2)
        registros = cursor2.fetchall()
        for row in registros:
            x.add_row(row)                           

    tabstring = x.get_string()
    if os.path.exists("export.txt"):
        os.remove("export.txt")
    output=open("export.txt","w")
    output.write(titulo+"\n")
    output.write(tabstring)
    output.close()
    output=open("export.txt","r")
    a=output.read()
    print a
    output.close()
                

if __name__ == "__main__":
   a=main()
