import re, json, couchdb

couch = couchdb.Server('http://localhost:5984/')
db = couch.create('login_logs')

flag = 0
loginindex = 0
logintimes = 0
loginemaillist = [None] * 210
logintimeslist = [0] * 210

f = open('production.txt', 'r')

aline = f.readline()

while aline != '':        
    if 'Started POST' in aline:
        if '/sessions' in aline or '/users/sign_in' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        flag = 1
                        break
                if flag == 0: 
                    if 'email' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('email')
                        loginemailaddress = idlist[idposition + 3].lower()
                        
                        if loginemailaddress in loginemaillist:
                            loginindex = loginemaillist.index(loginemailaddress)
                        else:
                            loginindex = loginemaillist.index(None)
                            loginemaillist[loginindex] = loginemailaddress
                            
                        logintimeslist[loginindex] = logintimeslist[loginindex] + 1
                        logintimes = logintimeslist[loginindex]
            
                        logactivity = 'Log In'
                        
                        postlinelist = re.split(' |"', aline)
                        logindate = postlinelist[8]
                        logintime = postlinelist[9]
                    
                        data = {"useremail":loginemailaddress,"date":logindate,"time":logintime,"activity":logactivity,"login_times":logintimes}
                        db.save(data)
                    else:
                        flag = 1
            else:
                flag = 1
    
    if flag == 0:
        aline = f.readline()
    else:
        aline = parameterline
        flag = 0
f.close()