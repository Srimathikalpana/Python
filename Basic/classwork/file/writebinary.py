from pickle import *
name=open("srimathibiodat.doc","wb")

Studentdata=[123,"SRK","salem"]
collegedata=(145,"PSG","Cbe")
Frndname={'frnd':'nevetha'}
dump(Studentdata,name)
dump(collegedata,name)
dump(Frndname,name)
name.close()