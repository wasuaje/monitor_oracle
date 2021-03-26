#! /usr/bin/env python
#
#Script para 
#Elaborado por W.A. - 31/05/2010

import cx_Oracle

connstr='scott/tiger'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

curs.execute('select 2+2 "aaa" ,3*3 from dual')
print curs.description
print curs.fetchone()

conn.close()
[root@manduca10 ~ novo]# du -sh /manduca10/applications/logs/* | sort  -n
3.3G	/manduca10/applications/logs/mediaServer19
3.4G	/manduca10/applications/logs/eupublish19
4.0K	/manduca10/applications/logs/crontab
4.5G	/manduca10/applications/logs/mediaServer
9.4G	/manduca10/applications/logs/publisher
12K	/manduca10/applications/logs/resourceCalendar
13M	/manduca10/applications/logs/wc06
15M	/manduca10/applications/logs/registry
20K	/manduca10/applications/logs/trivia-new
89M	/manduca10/applications/logs/tournament
120K	/manduca10/applications/logs/ajaxConnection
188M	/manduca10/applications/logs/poll
380K	/manduca10/applications/logs/pruebas_migracion
422M	/manduca10/applications/logs/eupublish
752K	/manduca10/applications/logs/concursos
904K	/manduca10/applications/logs/formDataCollector

