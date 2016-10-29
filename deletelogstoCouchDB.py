import re, json, couchdb

couch = couchdb.Server('http://localhost:5984/')
db = couch.create('delete_logs')

f = open('production.txt', 'r')
aline = f.readline()
while aline != '':
    if 'Started DELETE' in aline and 'participants'in aline:
        idlist = re.split('"| |/', aline)
        deleparid = idlist[5]
        postlinelist = re.split(' |"', aline)
        deledate = postlinelist[8]
        deletime = postlinelist[9]
        deleactivity = 'Delete Participant'
        data = {"participant_id":deleparid,"date":deledate,"time:":deletime,"activity":deleactivity}
        db.save(data)
        
    elif 'Started POST' in aline and 'withdraw'in aline:
        idlist = re.split('"| |/', aline)
        deleparid = idlist[5]
        postlinelist = re.split(' |"', aline)
        deledate = postlinelist[8]
        deletime = postlinelist[9]
        deleactivity = 'Participant Withdraw'
        data = {"participant_id":deleparid,"date":deledate,"time:":deletime,"activity":deleactivity}
        db.save(data)
        
    aline = f.readline()
f.close()