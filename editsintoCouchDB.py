import re, json, couchdb

couch = couchdb.Server('http://localhost:5984/')
db = couch.create('participant_logs')

def addupdatecomplete(word, aline, oldcomplete):
    if word in aline and word not in oldcomplete:
        newcomplete = oldcomplete + ' ' + word   
    else:
        newcomplete = oldcomplete
    return newcomplete

fmiddle = open('middle.txt', 'r')
mparticipantlist = [None] * 500
maline = fmiddle.readline()
while maline != '':
    if 'id' in maline:
        midlist = re.split(' |/n', maline)
        midlistlen = len(midlist)
        mparticipantid = midlist[midlistlen - 1]
        midnum = int(mparticipantid)
        mpostline = fmiddle.readline()
        mparameterline = fmiddle.readline()
        if 'local_id' in mparameterline:
            mgetlocalidlist = re.split('"|=>|,', mparameterline)
            mlocalidposition = mgetlocalidlist.index('local_id')
            mtotallocalid = mgetlocalidlist[mlocalidposition + 3]
            if len(mtotallocalid) < 4:
                mlocalid = mtotallocalid
            elif len(mtotallocalid) > 3 and re.search('[a-zA-Z]', mtotallocalid):
                mlocalidlist = re.split(' |-', mtotallocalid)
                mlocalidlistlen = len(mlocalidlist)
                mlocalid = mlocalidlist[mlocalidlistlen - 1]
            else :
                mlocalid = mtotallocalid[:2]
            
            mcentreidposition = mgetlocalidlist.index('clinical_centre_id')
            mcentreid = mgetlocalidlist[mcentreidposition + 3]
            
            if mparticipantlist[midnum] == None:
                mparticipantlist[midnum] = mcentreid + ' ' + mlocalid
            elif mparticipantlist[midnum] == mcentreid + ' ' + mlocalid:
                mparticipantlist[midnum] = mcentreid + ' ' + mlocalid
            else:
                midnumold = mparticipantlist[midnum]
                midnumnew = mcentreid + ' ' + mlocalid
    maline = fmiddle.readline()
fmiddle.close()

flag = 0
parversion = 0
parcompleteness = 0
paroldcontent =''
parversionlist = [0] * 500
paroldcontentlist = [None] * 500
parcompletenesslist = [None] * 500

faversion = 0
facompleteness = 0
faoldcontent =''
faversionlist = [0] * 500
faoldcontentlist = [None] * 500

moversion = 0
mocompleteness = 0
mooldcontent =''
moversionlist = [0] * 500
mooldcontentlist = [None] * 500

famiversion = 0
famicompleteness = 0
famioldcontent =''
famiversionlist = [0] * 500
famioldcontentlist = [None] * 500

proversion = 0
procompleteness = 0
prooldcontent =''
proversionlist = [0] * 500
prooldcontentlist = [None] * 500

ppversion = 0
ppcompleteness = 0
ppoldcontent =''
ppversionlist = [0] * 500
ppoldcontentlist = [None] * 500

preversion = 0
precompleteness = 0
preoldcontent =''
preversionlist = [0] * 500
preoldcontentlist = [None] * 500

matversion = 0
matcompleteness = 0
matoldcontent =''
matversionlist = [0] * 500
matoldcontentlist = [None] * 500

b1version = 0
b1completeness = 0
b1oldcontent =''
b1versionlist = [0] * 500
b1oldcontentlist = [None] * 500

b2version = 0
b2completeness = 0
b2oldcontent =''
b2versionlist = [0] * 500
b2oldcontentlist = [None] * 500

t1version = 0
t1completeness = 0
t1oldcontent =''
t1versionlist = [0] * 500
t1oldcontentlist = [None] * 500

t2version = 0
t2completeness = 0
t2oldcontent =''
t2versionlist = [0] * 500
t2oldcontentlist = [None] * 500

t3version = 0
t3completeness = 0
t3oldcontent =''
t3versionlist = [0] * 500
t3oldcontentlist = [None] * 500

v1version = 0
v1completeness = 0
v1oldcontent =''
v1versionlist = [0] * 500
v1oldcontentlist = [None] * 500

v2version = 0
v2completeness = 0
v2oldcontent =''
v2versionlist = [0] * 500
v2oldcontentlist = [None] * 500

v3version = 0
v3completeness = 0
v3oldcontent =''
v3versionlist = [0] * 500
v3oldcontentlist = [None] * 500

v4version = 0
v4completeness = 0
v4oldcontent =''
v4versionlist = [0] * 500
v4oldcontentlist = [None] * 500

v5version = 0
v5completeness = 0
v5oldcontent =''
v5versionlist = [0] * 500
v5oldcontentlist = [None] * 500

v6version = 0
v6completeness = 0
v6oldcontent =''
v6versionlist = [0] * 500
v6oldcontentlist = [None] * 500

v7version = 0
v7completeness = 0
v7oldcontent =''
v7versionlist = [0] * 500
v7oldcontentlist = [None] * 500

v8version = 0
v8completeness = 0
v8oldcontent =''
v8versionlist = [0] * 500
v8oldcontentlist = [None] * 500

v9version = 0
v9completeness = 0
v9oldcontent =''
v9versionlist = [0] * 500
v9oldcontentlist = [None] * 500

v10version = 0
v10completeness = 0
v10oldcontent =''
v10versionlist = [0] * 500
v10oldcontentlist = [None] * 500

totaleditlist = [0] * 500
accurateaveragecomplete = 0
averagecompletelist = [0] *500

totaldocument = 0
totaldocumentlist =[None] * 500

f = open('production.txt', 'r')

aline = f.readline()
while aline != '':
    if 'Started POST' in aline:
        matchObj = re.search(r'/participants(/[0-9]+(.[0-9]{1,3})?)?"', aline, re.M|re.I)
        if matchObj:
            putline = aline
            postlinelist = re.split(' |"', putline)
            ipaddress = postlinelist[6]
            processline = f.readline()
            parameterline = f.readline()
            idline = f.readline()
            if 'Started POST' not in idline and 'Started PUT' not in idline:
                canfind = re.search(r'Started GET "/participants/[0-9]+(.[0-9]{1,3})?"', idline, re.M|re.I) and re.split(' |"', idline)[6][:9] == ipaddress[:9]
                while not canfind:
                    idline = f.readline()
                    if 'Started POST' in idline or 'Started PUT' in idline:
                        flag = 1
                        break
                    else:
                        canfind = re.search(r'Started GET "/participants/[0-9]+(.[0-9]{1,3})?"', idline, re.M|re.I) and re.split(' |"', idline)[6][:9] == ipaddress[:9]
                if flag == 0:
                    idlist = re.split('/| |"', idline)
                    parparid = int(idlist[5])
                    parversionlist[parparid] = 1
                    totaleditlist[parparid] = 1
                    clilocalline = mparticipantlist[parparid]
                    parcentreid = re.split(' ', clilocalline)[0]
                    parlocalid = re.split(' ', clilocalline)[1]
                  
                    pardate = postlinelist[8]
                    partime = postlinelist[9]
                    paractivity = 'Create'
                    paractivitytype = 'Participant'
                    parversion = parversionlist[parparid]
                    paroldcontent = ''
                    
                    parameterposition = parameterline.find('Parameters')
                    commitposition = parameterline.find('commit')
                    contentstart = parameterposition + 12
                    contentend = commitposition - 3
                    parnew1content = parameterline[contentstart:contentend]
                    parnew2content = parnew1content.replace('"', '')
                    parnew3content = parnew2content.replace('{', '')
                    parnewcontent = parnew3content.replace('}', '')
                    paroldcontentlist[parparid] = parnewcontent
                    
                    parcompletenesslist[parparid] = 'PersonalDetail'
                    parcompleteness = 0.2
                    totaldocumentlist[parparid] = 'Participant'
                    totaldocument = 1
                    averagecompletelist[parparid] = 0.2
                    
                    data = {"participant_id":parparid,"Centre_id":parcentreid,"local_id":parlocalid,"date":pardate,"time":partime,"activity":paractivity,"type":paractivitytype,"version":parversion,"old_content":paroldcontent,"newcontent":parnewcontent,"completeness":parcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[parparid],"total_edits":totaleditlist[parparid]}
                    db.save(data)
            else:
                flag = 1
        
        elif 'fathers' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0:
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        faparid = int(idlist[idposition + 3])
                
                        if faversionlist[faparid] == 0:
                            faactivity = 'Create'
                        else:
                            faactivity = 'Update'
                        faversionlist[faparid] = faversionlist[faparid] + 1
                        faactivitytype = 'Father_Form'
                        totaleditlist[faparid] = totaleditlist[faparid] + 1
                        
                        clilocalline = mparticipantlist[faparid]
                        facentreid = re.split(' ', clilocalline)[0]
                        falocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        fadate = postlinelist[8]
                        fatime = postlinelist[9]
                        
                        faversion = faversionlist[faparid]
                        if faoldcontentlist[faparid] == None:
                            faoldcontentlist[faparid] = ''
                        faoldcontent = faoldcontentlist[faparid]
            
                        fatherposition = parameterline.find('father')
                        commitposition = parameterline.find('commit')
                        contentstart = fatherposition -1
                        contentend = commitposition - 3
                        fanew1content = parameterline[contentstart:contentend]
                        fanew2content = fanew1content.replace('"', '')
                        fanew3content = fanew2content.replace('{', '')
                        fanewcontent = fanew3content.replace('}', '')
                        faoldcontentlist[faparid] = fanewcontent
                    
                        fatotalquestions = fanew1content.count(',') + 1
                        faunanswerednum = fanew1content.count('""')
                        accuratefacompleteness = (fatotalquestions - faunanswerednum)/fatotalquestions
                        facompleteness = round(accuratefacompleteness, 2)
            
                        if totaldocumentlist[faparid] == None:
                            totaldocumentlist[faparid] =  'Father_Form'
                            totaldocument = 1
                        elif 'Father_Form' not in totaldocumentlist[faparid]:
                            totaldocumentlist[faparid] = totaldocumentlist[faparid] + ' Father_Form'
                            splitstring = totaldocumentlist[faparid][1:]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[faparid])
                            totaldocument = len(totaldocumentsplitlist)
                            
                        accurateaveragecomplete = (averagecompletelist[faparid] * (totaldocument - 1) + accuratefacompleteness)/ totaldocument
                        averagecompletelist[faparid] = round(accurateaveragecomplete, 2)
                    
                        data = {"participant_id":faparid,"Centre_id":facentreid,"local_id":falocalid,"date":fadate,"time":fatime,"activity":faactivity,"type":faactivitytype,"version":faversion,"old_content":faoldcontent,"newcontent":fanewcontent,"completeness":facompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[faparid],"total_edits":totaleditlist[faparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'family_members' in aline:
            processline = f.readline()
            parameterline = f.readline()
            
            if 'participant_id' in parameterline:
                idlist = re.split('"|=>|,', parameterline)
                idposition = idlist.index('participant_id')
                famiparid = int(idlist[idposition + 3])
            
                if famiversionlist[famiparid] == 0:
                    famiactivity = 'Create'   
                else:
                    famiactivity = 'Update'
                
                famiversionlist[famiparid] = famiversionlist[famiparid] + 1
                famiactivitytype = 'Family_Members_Form'
                totaleditlist[famiparid] = totaleditlist[famiparid] + 1
                
                clilocalline = mparticipantlist[famiparid]
                famicentreid = re.split(' ', clilocalline)[0]
                familocalid = re.split(' ', clilocalline)[1]
                postlinelist = re.split(' |"', aline)
                famidate = postlinelist[8]
                famitime = postlinelist[9]
                famiversion = famiversionlist[famiparid]
                if famioldcontentlist[famiparid] == None:
                    famioldcontentlist[famiparid] = ''
                famioldcontent = famioldcontentlist[famiparid]
            
                famimposition = parameterline.find('family_member')
                commitposition = parameterline.find('commit')
                contentstart = famimposition -1
                contentend = commitposition - 3
                faminew1content = parameterline[contentstart:contentend]
                faminew2content = faminew1content.replace('"', '')
                faminew3content = faminew2content.replace('{', '')
                faminewcontent = faminew3content.replace('}', '')
                famioldcontentlist[famiparid] = faminewcontent
                    
                famitotalquestions = faminew1content.count(',') + 1
                famiunanswerednum = faminew1content.count('""')
                accuratefamicompleteness = (famitotalquestions - famiunanswerednum)/famitotalquestions
                famicompleteness = round(accuratefamicompleteness, 2)
            
                if totaldocumentlist[famiparid] == None:
                    totaldocumentlist[famiparid] =  'Family_Members_Form'
                    totaldocument = 1
                elif 'Family_Members_Form' not in totaldocumentlist[famiparid]:
                    totaldocumentlist[famiparid] = totaldocumentlist[famiparid] + ' Family_Members_Form'
                    splitstring = totaldocumentlist[famiparid][1:]
                    totaldocumentsplitlist = re.split(' ', splitstring)
                    totaldocument = len(totaldocumentsplitlist)
                else:
                    totaldocumentsplitlist = re.split(' ', totaldocumentlist[famiparid])
                    totaldocument = len(totaldocumentsplitlist)
                    
                accurateaveragecomplete = (averagecompletelist[famiparid] * (totaldocument - 1) + accuratefamicompleteness)/ totaldocument
                averagecompletelist[famiparid] = round(accurateaveragecomplete, 2)
                
                data = {"participant_id":famiparid,"Centre_id":famicentreid,"local_id":familocalid,"date":famidate,"time":famitime,"activity":famiactivity,"type":famiactivitytype,"version":famiversion,"old_content":famioldcontent,"newcontent":faminewcontent,"completeness":famicompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[famiparid],"total_edits":totaleditlist[famiparid]}
                db.save(data)
                
        elif 'probands' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        proparid = int(idlist[idposition + 3])
            
                        if proversionlist[proparid] == 0:
                            proactivity = 'Create'   
                        else:
                            proactivity = 'Update'
                
                        proversionlist[proparid] = proversionlist[proparid] + 1
                        proactivitytype = 'Proband_Form'
                        totaleditlist[proparid] = totaleditlist[proparid] + 1
                
                        clilocalline = mparticipantlist[proparid]
                        procentreid = re.split(' ', clilocalline)[0]
                        prolocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        prodate = postlinelist[8]
                        protime = postlinelist[9]
                        proversion = proversionlist[proparid]
                        if prooldcontentlist[proparid] == None:
                            prooldcontentlist[proparid] = ''
                        prooldcontent = prooldcontentlist[proparid]
            
                        proposition = parameterline.find('"proband')
                        commitposition = parameterline.find('commit')
                        contentstart = proposition
                        contentend = commitposition - 3
                        pronew1content = parameterline[contentstart:contentend]
                        pronew2content = pronew1content.replace('"', '')
                        pronew3content = pronew2content.replace('{', '')
                        pronewcontent = pronew3content.replace('}', '')
                        prooldcontentlist[proparid] = pronewcontent
                    
                        prototalquestions = pronew1content.count(',') + 1
                        prounanswerednum = pronew1content.count('""')
                        accurateprocompleteness = (prototalquestions - prounanswerednum)/prototalquestions
                        procompleteness = round(accurateprocompleteness, 2)
            
                        if totaldocumentlist[proparid] == None:
                            totaldocumentlist[proparid] =  'Proband_Form'
                            totaldocument = 1
                        elif 'Proband_Form' not in totaldocumentlist[proparid]:
                            totaldocumentlist[proparid] = totaldocumentlist[proparid] + ' Proband_Form'
                            splitstring = totaldocumentlist[proparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[proparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[proparid] * (totaldocument - 1) + accurateprocompleteness)/ totaldocument
                        averagecompletelist[proparid] = round(accurateaveragecomplete, 2)
                        
                        data = {"participant_id":proparid,"Centre_id":procentreid,"local_id":prolocalid,"date":prodate,"time":protime,"activity":proactivity,"type":proactivitytype,"version":proversion,"old_content":prooldcontent,"newcontent":pronewcontent,"completeness":procompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[proparid],"total_edits":totaleditlist[proparid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'ppaqs' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        ppparid = int(idlist[idposition + 3])
            
                        if ppversionlist[ppparid] == 0:
                            ppactivity = 'Create'   
                        else:
                            ppactivity = 'Update'
                
                        ppversionlist[ppparid] = ppversionlist[ppparid] + 1
                        ppactivitytype = 'PPAQ_Form'
                        totaleditlist[ppparid] = totaleditlist[ppparid] + 1
                
                        clilocalline = mparticipantlist[ppparid]
                        ppcentreid = re.split(' ', clilocalline)[0]
                        pplocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        ppdate = postlinelist[8]
                        pptime = postlinelist[9]
                        ppversion = ppversionlist[ppparid]
                        if ppoldcontentlist[ppparid] == None:
                            ppoldcontentlist[ppparid] = ''
                        ppoldcontent = ppoldcontentlist[ppparid]
            
                        ppposition = parameterline.find('"ppaq')
                        commitposition = parameterline.find('commit')
                        contentstart = ppposition
                        contentend = commitposition - 3
                        ppnew1content = parameterline[contentstart:contentend]
                        ppnew2content = ppnew1content.replace('"', '')
                        ppnew3content = ppnew2content.replace('{', '')
                        ppnewcontent = ppnew3content.replace('}', '')
                        ppoldcontentlist[ppparid] = ppnewcontent
                    
                        pptotalquestions = ppnew1content.count(',') + 1
                        ppunanswerednum = ppnew1content.count('""')
                        accurateppcompleteness = (pptotalquestions - ppunanswerednum)/pptotalquestions
                        ppcompleteness = round(accurateppcompleteness, 2)
            
                        if totaldocumentlist[ppparid] == None:
                            totaldocumentlist[ppparid] =  'PPAQ_Form'
                            totaldocument = 1
                        elif 'PPAQ_Form' not in totaldocumentlist[ppparid]:
                            totaldocumentlist[ppparid] = totaldocumentlist[ppparid] + ' PPAQ_Form'
                            splitstring = totaldocumentlist[ppparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[ppparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[ppparid] * (totaldocument - 1) + accurateppcompleteness)/ totaldocument
                        averagecompletelist[ppparid] = round(accurateaveragecomplete, 2)
                        
                        data = {"participant_id":ppparid,"Centre_id":ppcentreid,"local_id":pplocalid,"date":ppdate,"time":pptime,"activity":ppactivity,"type":ppactivitytype,"version":ppversion,"old_content":ppoldcontent,"newcontent":ppnewcontent,"completeness":ppcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[ppparid],"total_edits":totaleditlist[ppparid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        elif 'pregnancy_lifestyle_questionnaires' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        preparid = int(idlist[idposition + 3])
            
                        if preversionlist[preparid] == 0:
                            preactivity = 'Create'   
                        else:
                            preactivity = 'Update'
                
                        preversionlist[preparid] = preversionlist[preparid] + 1
                        preactivitytype = 'Pregnancy_Questionnaires'
                        totaleditlist[preparid] = totaleditlist[preparid] + 1
                
                        clilocalline = mparticipantlist[preparid]
                        precentreid = re.split(' ', clilocalline)[0]
                        prelocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        predate = postlinelist[8]
                        pretime = postlinelist[9]
                        preversion = preversionlist[preparid]
                        if preoldcontentlist[preparid] == None:
                            preoldcontentlist[preparid] = ''
                        preoldcontent = preoldcontentlist[preparid]
            
                        preposition = parameterline.find('"pregnancy_lifestyle_questionnaire')
                        commitposition = parameterline.find('commit')
                        contentstart = preposition
                        contentend = commitposition - 3
                        prenew1content = parameterline[contentstart:contentend]
                        prenew2content = prenew1content.replace('"', '')
                        prenew3content = prenew2content.replace('{', '')
                        prenewcontent = prenew3content.replace('}', '')
                        preoldcontentlist[preparid] = prenewcontent
                    
                        pretotalquestions = prenew1content.count(',') + 1
                        preunanswerednum = prenew1content.count('""')
                        accurateprecompleteness = (pretotalquestions - preunanswerednum)/pretotalquestions
                        precompleteness = round(accurateprecompleteness, 2)
            
                        if totaldocumentlist[preparid] == None:
                            totaldocumentlist[preparid] =  'Pregnancy_Questionnaires'
                            totaldocument = 1
                        elif 'Pregnancy_Questionnaires' not in totaldocumentlist[preparid]:
                            totaldocumentlist[preparid] = totaldocumentlist[preparid] + ' Pregnancy_Questionnaires'
                            splitstring = totaldocumentlist[preparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[preparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[preparid] * (totaldocument - 1) + accurateprecompleteness)/ totaldocument
                        averagecompletelist[preparid] = round(accurateaveragecomplete, 2)

                        data = {"participant_id":preparid,"Centre_id":precentreid,"local_id":prelocalid,"date":predate,"time":pretime,"activity":preactivity,"type":preactivitytype,"version":preversion,"old_content":preoldcontent,"newcontent":prenewcontent,"completeness":precompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[preparid],"total_edits":totaleditlist[preparid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'maternal_lifestyle_postpartum_questionnaires' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        matparid = int(idlist[idposition + 3])
                        
                        if matversionlist[matparid] == 0:
                            matactivity = 'Create'   
                        else:
                            matactivity = 'Update'
                
                        matversionlist[matparid] = matversionlist[matparid] + 1
                        matactivitytype = 'Maternal_Questionnaires'
                        totaleditlist[matparid] = totaleditlist[matparid] + 1
                
                        clilocalline = mparticipantlist[matparid]
                        matcentreid = re.split(' ', clilocalline)[0]
                        matlocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        matdate = postlinelist[8]
                        mattime = postlinelist[9]
                        matversion = matversionlist[matparid]
                        if matoldcontentlist[matparid] == None:
                            matoldcontentlist[matparid] = ''
                        matoldcontent = matoldcontentlist[matparid]
            
                        matposition = parameterline.find('"maternal_lifestyle_postpartum_questionnaire')
                        commitposition = parameterline.find('commit')
                        contentstart = matposition
                        contentend = commitposition - 3
                        matnew1content = parameterline[contentstart:contentend]
                        matnew2content = matnew1content.replace('"', '')
                        matnew3content = matnew2content.replace('{', '')
                        matnewcontent = matnew3content.replace('}', '')
                        matoldcontentlist[matparid] = matnewcontent
                    
                        mattotalquestions = matnew1content.count(',') + 1
                        matunanswerednum = matnew1content.count('""')
                        accuratematcompleteness = (mattotalquestions - matunanswerednum)/mattotalquestions
                        matcompleteness = round(accuratematcompleteness, 2)
            
                        if totaldocumentlist[matparid] == None:
                            totaldocumentlist[matparid] =  'Maternal_Questionnaires'
                            totaldocument = 1
                        elif 'Maternal_Questionnaires' not in totaldocumentlist[matparid]:
                            totaldocumentlist[matparid] = totaldocumentlist[matparid] + ' Maternal_Questionnaires'
                            splitstring = totaldocumentlist[matparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[matparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[matparid] * (totaldocument - 1) + accuratematcompleteness)/ totaldocument
                        averagecompletelist[matparid] = round(accurateaveragecomplete, 2)
                        
                        data = {"participant_id":matparid,"Centre_id":matcentreid,"local_id":matlocalid,"date":matdate,"time":mattime,"activity":matactivity,"type":matactivitytype,"version":matversion,"old_content":matoldcontent,"newcontent":matnewcontent,"completeness":matcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[matparid],"total_edits":totaleditlist[matparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        elif '/b1' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        b1parid = int(idlist[idposition + 3])
                        
                        if b1versionlist[b1parid] == 0:
                            b1activity = 'Create'   
                        else:
                            b1activity = 'Update'
                
                        b1versionlist[b1parid] = b1versionlist[b1parid] + 1
                        b1activitytype = 'B1_Form'
                        totaleditlist[b1parid] = totaleditlist[b1parid] + 1
                
                        clilocalline = mparticipantlist[b1parid]
                        b1centreid = re.split(' ', clilocalline)[0]
                        b1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        b1date = postlinelist[8]
                        b1time = postlinelist[9]
                        b1version = b1versionlist[b1parid]
                        if b1oldcontentlist[b1parid] == None:
                            b1oldcontentlist[b1parid] = ''
                        b1oldcontent = b1oldcontentlist[b1parid]
            
                        b1position = parameterline.find('"b1')
                        commitposition = parameterline.find('commit')
                        contentstart = b1position
                        contentend = commitposition - 3
                        b1new1content = parameterline[contentstart:contentend]
                        b1new2content = b1new1content.replace('"', '')
                        b1new3content = b1new2content.replace('{', '')
                        b1newcontent = b1new3content.replace('}', '')
                        b1oldcontentlist[b1parid] = b1newcontent
                    
                        b1totalquestions = b1new1content.count(',') + 1
                        b1unanswerednum = b1new1content.count('""')
                        accurateb1completeness = (b1totalquestions - b1unanswerednum)/b1totalquestions
                        b1completeness = round(accurateb1completeness, 2)
            
                        if totaldocumentlist[b1parid] == None:
                            totaldocumentlist[b1parid] =  'B1_Form'
                            totaldocument = 1
                        elif 'B1_Form' not in totaldocumentlist[b1parid]:
                            totaldocumentlist[b1parid] = totaldocumentlist[b1parid] + ' B1_Form'
                            splitstring = totaldocumentlist[b1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[b1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[b1parid] * (totaldocument - 1) + accurateb1completeness)/ totaldocument
                        averagecompletelist[b1parid] = round(accurateaveragecomplete, 2)

                        data = {"participant_id":b1parid,"Centre_id":b1centreid,"local_id":b1localid,"date":b1date,"time":b1time,"activity":b1activity,"type":b1activitytype,"version":b1version,"old_content":b1oldcontent,"newcontent":b1newcontent,"completeness":b1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[b1parid],"total_edits":totaleditlist[b1parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/b2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        b2parid = int(idlist[idposition + 3])
                        
                        if b2versionlist[b2parid] == 0:
                            b2activity = 'Create'
                        else:
                            b2activity = 'Update'
                
                        b2versionlist[b2parid] = b2versionlist[b2parid] + 1
                        b2activitytype = 'B2_Form'
                        totaleditlist[b2parid] = totaleditlist[b2parid] + 1
                
                        clilocalline = mparticipantlist[b2parid]
                        b2centreid = re.split(' ', clilocalline)[0]
                        b2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        b2date = postlinelist[8]
                        b2time = postlinelist[9]
                        b2version = b2versionlist[b2parid]
                        if b2oldcontentlist[b2parid] == None:
                            b2oldcontentlist[b2parid] = ''
                        b2oldcontent = b2oldcontentlist[b2parid]
            
                        b2position = parameterline.find('"b2')
                        commitposition = parameterline.find('commit')
                        contentstart = b2position
                        contentend = commitposition - 3
                        b2new1content = parameterline[contentstart:contentend]
                        b2new2content = b2new1content.replace('"', '')
                        b2new3content = b2new2content.replace('{', '')
                        b2newcontent = b2new3content.replace('}', '')
                        b2oldcontentlist[b2parid] = b2newcontent
                    
                        b2totalquestions = b2new1content.count(',') + 1
                        b2unanswerednum = b2new1content.count('""')
                        accurateb2completeness = (b2totalquestions - b2unanswerednum)/b2totalquestions
                        b2completeness = round(accurateb2completeness, 2)
            
                        if totaldocumentlist[b2parid] == None:
                            totaldocumentlist[b2parid] =  'B2_Form'
                            totaldocument = 1
                        elif 'B2_Form' not in totaldocumentlist[b2parid]:
                            totaldocumentlist[b2parid] = totaldocumentlist[b2parid] + ' B2_Form'
                            splitstring = totaldocumentlist[b2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[b2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[b2parid] * (totaldocument - 1) + accurateb2completeness)/ totaldocument
                        averagecompletelist[b2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":b2parid,"Centre_id":b2centreid,"local_id":b2localid,"date":b2date,"time":b2time,"activity":b2activity,"type":b2activitytype,"version":b2version,"old_content":b2oldcontent,"newcontent":b2newcontent,"completeness":b2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[b2parid],"total_edits":totaleditlist[b2parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        elif '/t1' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t1parid = int(idlist[idposition + 3])
                        
                        if t1versionlist[t1parid] == 0:
                            t1activity = 'Create'   
                        else:
                            t1activity = 'Update'
                
                        t1versionlist[t1parid] = t1versionlist[t1parid] + 1
                        t1activitytype = 'T1_Form'
                        totaleditlist[t1parid] = totaleditlist[t1parid] + 1
                
                        clilocalline = mparticipantlist[t1parid]
                        t1centreid = re.split(' ', clilocalline)[0]
                        t1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t1date = postlinelist[8]
                        t1time = postlinelist[9]
                        t1version = t1versionlist[t1parid]
                        if t1oldcontentlist[t1parid] == None:
                            t1oldcontentlist[t1parid] = ''
                        t1oldcontent = t1oldcontentlist[t1parid]
            
                        t1position = parameterline.find('"t1')
                        commitposition = parameterline.find('commit')
                        contentstart = t1position
                        contentend = commitposition - 3
                        t1new1content = parameterline[contentstart:contentend]
                        t1new2content = t1new1content.replace('"', '')
                        t1new3content = t1new2content.replace('{', '')
                        t1newcontent = t1new3content.replace('}', '')
                        t1oldcontentlist[t1parid] = t1newcontent
                    
                        t1totalquestions = t1new1content.count(',') + 1
                        t1unanswerednum = t1new1content.count('""')
                        accuratet1completeness = (t1totalquestions - t1unanswerednum)/t1totalquestions
                        t1completeness = round(accuratet1completeness, 2)
            
                        if totaldocumentlist[t1parid] == None:
                            totaldocumentlist[t1parid] =  'T1_Form'
                            totaldocument = 1
                        elif 'T1_Form' not in totaldocumentlist[t1parid]:
                            totaldocumentlist[t1parid] = totaldocumentlist[t1parid] + ' T1_Form'
                            splitstring = totaldocumentlist[t1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t1parid] * (totaldocument - 1) + accuratet1completeness)/ totaldocument
                        averagecompletelist[t1parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t1parid,"Centre_id":t1centreid,"local_id":t1localid,"date":t1date,"time":t1time,"activity":t1activity,"type":t1activitytype,"version":t1version,"old_content":t1oldcontent,"newcontent":t1newcontent,"completeness":t1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t1parid],"total_edits":totaleditlist[t1parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/t2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t2parid = int(idlist[idposition + 3])
                        
                        if t2versionlist[t2parid] == 0:
                            t2activity = 'Create'   
                        else:
                            t2activity = 'Update'
                
                        t2versionlist[t2parid] = t2versionlist[t2parid] + 1
                        t2activitytype = 'T2_Form'
                        totaleditlist[t2parid] = totaleditlist[t2parid] + 1
                
                        clilocalline = mparticipantlist[t2parid]
                        t2centreid = re.split(' ', clilocalline)[0]
                        t2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t2date = postlinelist[8]
                        t2time = postlinelist[9]
                        t2version = t2versionlist[t2parid]
                        if t2oldcontentlist[t2parid] == None:
                            t2oldcontentlist[t2parid] = ''
                        t2oldcontent = t2oldcontentlist[t2parid]
            
                        t2position = parameterline.find('"t2')
                        commitposition = parameterline.find('commit')
                        contentstart = t2position
                        contentend = commitposition - 3
                        t2new1content = parameterline[contentstart:contentend]
                        t2new2content = t2new1content.replace('"', '')
                        t2new3content = t2new2content.replace('{', '')
                        t2newcontent = t2new3content.replace('}', '')
                        t2oldcontentlist[t2parid] = t2newcontent
                    
                        t2totalquestions = t2new1content.count(',') + 1
                        t2unanswerednum = t2new1content.count('""')
                        accuratet2completeness = (t2totalquestions - t2unanswerednum)/t2totalquestions
                        t2completeness = round(accuratet2completeness, 2)
            
                        if totaldocumentlist[t2parid] == None:
                            totaldocumentlist[t2parid] =  'T2_Form'
                            totaldocument = 1
                        elif 'T2_Form' not in totaldocumentlist[t2parid]:
                            totaldocumentlist[t2parid] = totaldocumentlist[t2parid] + ' T2_Form'
                            splitstring = totaldocumentlist[t2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t2parid] * (totaldocument - 1) + accuratet2completeness)/ totaldocument
                        averagecompletelist[t2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t2parid,"Centre_id":t2centreid,"local_id":t2localid,"date":t2date,"time":t2time,"activity":t2activity,"type":t2activitytype,"version":t2version,"old_content":t2oldcontent,"newcontent":t2newcontent,"completeness":t2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t2parid],"total_edits":totaleditlist[t2parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/t3' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t3parid = int(idlist[idposition + 3])
                        
                        if t3versionlist[t3parid] == 0:
                            t3activity = 'Create'   
                        else:
                            t3activity = 'Update'
                
                        t3versionlist[t3parid] = t3versionlist[t3parid] + 1
                        t3activitytype = 'T3_Form'
                        totaleditlist[t3parid] = totaleditlist[t3parid] + 1
                
                        clilocalline = mparticipantlist[t3parid]
                        t3centreid = re.split(' ', clilocalline)[0]
                        t3localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t3date = postlinelist[8]
                        t3time = postlinelist[9]
                        t3version = t3versionlist[t3parid]
                        if t3oldcontentlist[t3parid] == None:
                            t3oldcontentlist[t3parid] = ''
                        t3oldcontent = t3oldcontentlist[t3parid]
            
                        t3position = parameterline.find('"t3')
                        commitposition = parameterline.find('commit')
                        contentstart = t3position
                        contentend = commitposition - 3
                        t3new1content = parameterline[contentstart:contentend]
                        t3new2content = t3new1content.replace('"', '')
                        t3new3content = t3new2content.replace('{', '')
                        t3newcontent = t3new3content.replace('}', '')
                        t3oldcontentlist[t3parid] = t3newcontent
                    
                        t3totalquestions = t3new1content.count(',') + 1
                        t3unanswerednum = t3new1content.count('""')
                        accuratet3completeness = (t3totalquestions - t3unanswerednum)/t3totalquestions
                        t3completeness = round(accuratet3completeness, 2)
            
                        if totaldocumentlist[t3parid] == None:
                            totaldocumentlist[t3parid] =  'T3_Form'
                            totaldocument = 1
                        elif 'T3_Form' not in totaldocumentlist[t3parid]:
                            totaldocumentlist[t3parid] = totaldocumentlist[t3parid] + ' T3_Form'
                            splitstring = totaldocumentlist[t3parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t3parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t3parid] * (totaldocument - 1) + accuratet3completeness)/ totaldocument
                        averagecompletelist[t3parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t3parid,"Centre_id":t3centreid,"local_id":t3localid,"date":t3date,"time":t3time,"activity":t3activity,"type":t3activitytype,"version":t3version,"old_content":t3oldcontent,"newcontent":t3newcontent,"completeness":t3completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t3parid],"total_edits":totaleditlist[t3parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v1"' in aline or '/v1/' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v1parid = int(idlist[idposition + 3])
                        
                        if v1versionlist[v1parid] == 0:
                            v1activity = 'Create'   
                        else:
                            v1activity = 'Update'
                
                        v1versionlist[v1parid] = v1versionlist[v1parid] + 1
                        v1activitytype = 'V1_Form'
                        totaleditlist[v1parid] = totaleditlist[v1parid] + 1
                
                        clilocalline = mparticipantlist[v1parid]
                        v1centreid = re.split(' ', clilocalline)[0]
                        v1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v1date = postlinelist[8]
                        v1time = postlinelist[9]
                        v1version = v1versionlist[v1parid]
                        if v1oldcontentlist[v1parid] == None:
                            v1oldcontentlist[v1parid] = ''
                        v1oldcontent = v1oldcontentlist[v1parid]
            
                        v1position = parameterline.find('"v1')
                        commitposition = parameterline.find('commit')
                        contentstart = v1position
                        contentend = commitposition - 3
                        v1new1content = parameterline[contentstart:contentend]
                        v1new2content = v1new1content.replace('"', '')
                        v1new3content = v1new2content.replace('{', '')
                        v1newcontent = v1new3content.replace('}', '')
                        v1oldcontentlist[v1parid] = v1newcontent
                    
                        v1totalquestions = v1new1content.count(',') + 1
                        v1unanswerednum = v1new1content.count('""')
                        accuratev1completeness = (v1totalquestions - v1unanswerednum)/v1totalquestions
                        v1completeness = round(accuratev1completeness, 2)
            
                        if totaldocumentlist[v1parid] == None:
                            totaldocumentlist[v1parid] =  'V1_Form'
                            totaldocument = 1
                        elif 'V1_Form' not in totaldocumentlist[v1parid]:
                            totaldocumentlist[v1parid] = totaldocumentlist[v1parid] + ' V1_Form'
                            splitstring = totaldocumentlist[v1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v1parid] * (totaldocument - 1) + accuratev1completeness)/ totaldocument
                        averagecompletelist[v1parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v1parid,"Centre_id":v1centreid,"local_id":v1localid,"date":v1date,"time":v1time,"activity":v1activity,"type":v1activitytype,"version":v1version,"old_content":v1oldcontent,"newcontent":v1newcontent,"completeness":v1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v1parid],"total_edits":totaleditlist[v1parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v2parid = int(idlist[idposition + 3])
                        
                        if v2versionlist[v2parid] == 0:
                            v2activity = 'Create'   
                        else:
                            v2activity = 'Update'
                
                        v2versionlist[v2parid] = v2versionlist[v2parid] + 1
                        v2activitytype = 'V2_Form'
                        totaleditlist[v2parid] = totaleditlist[v2parid] + 1
                
                        clilocalline = mparticipantlist[v2parid]
                        v2centreid = re.split(' ', clilocalline)[0]
                        v2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v2date = postlinelist[8]
                        v2time = postlinelist[9]
                        v2version = v2versionlist[v2parid]
                        if v2oldcontentlist[v2parid] == None:
                            v2oldcontentlist[v2parid] = ''
                        v2oldcontent = v2oldcontentlist[v2parid]
            
                        v2position = parameterline.find('"v2')
                        commitposition = parameterline.find('commit')
                        contentstart = v2position
                        contentend = commitposition - 3
                        v2new1content = parameterline[contentstart:contentend]
                        v2new2content = v2new1content.replace('"', '')
                        v2new3content = v2new2content.replace('{', '')
                        v2newcontent = v2new3content.replace('}', '')
                        v2oldcontentlist[v2parid] = v2newcontent
                    
                        v2totalquestions = v2new1content.count(',') + 1
                        v2unanswerednum = v2new1content.count('""')
                        accuratev2completeness = (v2totalquestions - v2unanswerednum)/v2totalquestions
                        v2completeness = round(accuratev2completeness, 2)
            
                        if totaldocumentlist[v2parid] == None:
                            totaldocumentlist[v2parid] =  'V2_Form'
                            totaldocument = 1
                        elif 'V2_Form' not in totaldocumentlist[v2parid]:
                            totaldocumentlist[v2parid] = totaldocumentlist[v2parid] + ' V2_Form'
                            splitstring = totaldocumentlist[v2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v2parid] * (totaldocument - 1) + accuratev2completeness)/ totaldocument
                        averagecompletelist[v2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v2parid,"Centre_id":v2centreid,"local_id":v2localid,"date":v2date,"time":v2time,"activity":v2activity,"type":v2activitytype,"version":v2version,"old_content":v2oldcontent,"newcontent":v2newcontent,"completeness":v2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v2parid],"total_edits":totaleditlist[v2parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v3' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v3parid = int(idlist[idposition + 3])
                        
                        if v3versionlist[v3parid] == 0:
                            v3activity = 'Create'   
                        else:
                            v3activity = 'Update'
                
                        v3versionlist[v3parid] = v3versionlist[v3parid] + 1
                        v3activitytype = 'V3_Form'
                        totaleditlist[v3parid] = totaleditlist[v3parid] + 1
                
                        clilocalline = mparticipantlist[v3parid]
                        v3centreid = re.split(' ', clilocalline)[0]
                        v3localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v3date = postlinelist[8]
                        v3time = postlinelist[9]
                        v3version = v3versionlist[v3parid]
                        if v3oldcontentlist[v3parid] == None:
                            v3oldcontentlist[v3parid] = ''
                        v3oldcontent = v3oldcontentlist[v3parid]
            
                        v3position = parameterline.find('"v3')
                        commitposition = parameterline.find('commit')
                        contentstart = v3position
                        contentend = commitposition - 3
                        v3new1content = parameterline[contentstart:contentend]
                        v3new2content = v3new1content.replace('"', '')
                        v3new3content = v3new2content.replace('{', '')
                        v3newcontent = v3new3content.replace('}', '')
                        v3oldcontentlist[v3parid] = v3newcontent
                    
                        v3totalquestions = v3new1content.count(',') + 1
                        v3unanswerednum = v3new1content.count('""')
                        accuratev3completeness = (v3totalquestions - v3unanswerednum)/v3totalquestions
                        v3completeness = round(accuratev3completeness, 2)
            
                        if totaldocumentlist[v3parid] == None:
                            totaldocumentlist[v3parid] =  'V3_Form'
                            totaldocument = 1
                        elif 'V3_Form' not in totaldocumentlist[v3parid]:
                            totaldocumentlist[v3parid] = totaldocumentlist[v3parid] + ' V3_Form'
                            splitstring = totaldocumentlist[v3parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v3parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v3parid] * (totaldocument - 1) + accuratev3completeness)/ totaldocument
                        averagecompletelist[v3parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v3parid,"Centre_id":v3centreid,"local_id":v3localid,"date":v3date,"time":v3time,"activity":v3activity,"type":v3activitytype,"version":v3version,"old_content":v3oldcontent,"newcontent":v3newcontent,"completeness":v3completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v3parid],"total_edits":totaleditlist[v3parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v4' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v4parid = int(idlist[idposition + 3])
                        
                        if v4versionlist[v4parid] == 0:
                            v4activity = 'Create'   
                        else:
                            v4activity = 'Update'
                
                        v4versionlist[v4parid] = v4versionlist[v4parid] + 1
                        v4activitytype = 'V4_Form'
                        totaleditlist[v4parid] = totaleditlist[v4parid] + 1
                
                        clilocalline = mparticipantlist[v4parid]
                        v4centreid = re.split(' ', clilocalline)[0]
                        v4localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v4date = postlinelist[8]
                        v4time = postlinelist[9]
                        v4version = v4versionlist[v4parid]
                        if v4oldcontentlist[v4parid] == None:
                            v4oldcontentlist[v4parid] = ''
                        v4oldcontent = v4oldcontentlist[v4parid]
            
                        v4position = parameterline.find('"v4')
                        commitposition = parameterline.find('commit')
                        contentstart = v4position
                        contentend = commitposition - 3
                        v4new1content = parameterline[contentstart:contentend]
                        v4new2content = v4new1content.replace('"', '')
                        v4new3content = v4new2content.replace('{', '')
                        v4newcontent = v4new3content.replace('}', '')
                        v4oldcontentlist[v4parid] = v4newcontent
                    
                        v4totalquestions = v4new1content.count(',') + 1
                        v4unanswerednum = v4new1content.count('""')
                        accuratev4completeness = (v4totalquestions - v4unanswerednum)/v4totalquestions
                        v4completeness = round(accuratev4completeness, 2)
            
                        if totaldocumentlist[v4parid] == None:
                            totaldocumentlist[v4parid] =  'V4_Form'
                            totaldocument = 1
                        elif 'V4_Form' not in totaldocumentlist[v4parid]:
                            totaldocumentlist[v4parid] = totaldocumentlist[v4parid] + ' V4_Form'
                            splitstring = totaldocumentlist[v4parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v4parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v4parid] * (totaldocument - 1) + accuratev4completeness)/ totaldocument
                        averagecompletelist[v4parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v4parid,"Centre_id":v4centreid,"local_id":v4localid,"date":v4date,"time":v4time,"activity":v4activity,"type":v4activitytype,"version":v4version,"old_content":v4oldcontent,"newcontent":v4newcontent,"completeness":v4completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v4parid],"total_edits":totaleditlist[v4parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v5' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v5parid = int(idlist[idposition + 3])
                        
                        if v5versionlist[v5parid] == 0:
                            v5activity = 'Create'   
                        else:
                            v5activity = 'Update'
                
                        v5versionlist[v5parid] = v5versionlist[v5parid] + 1
                        v5activitytype = 'V5_Form'
                        totaleditlist[v5parid] = totaleditlist[v5parid] + 1
                
                        clilocalline = mparticipantlist[v5parid]
                        v5centreid = re.split(' ', clilocalline)[0]
                        v5localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v5date = postlinelist[8]
                        v5time = postlinelist[9]
                        v5version = v5versionlist[v5parid]
                        if v5oldcontentlist[v5parid] == None:
                            v5oldcontentlist[v5parid] = ''
                        v5oldcontent = v5oldcontentlist[v5parid]
            
                        v5position = parameterline.find('"v5')
                        commitposition = parameterline.find('commit')
                        contentstart = v5position
                        contentend = commitposition - 3
                        v5new1content = parameterline[contentstart:contentend]
                        v5new2content = v5new1content.replace('"', '')
                        v5new3content = v5new2content.replace('{', '')
                        v5newcontent = v5new3content.replace('}', '')
                        v5oldcontentlist[v5parid] = v5newcontent
                    
                        v5totalquestions = v5new1content.count(',') + 1
                        v5unanswerednum = v5new1content.count('""')
                        accuratev5completeness = (v5totalquestions - v5unanswerednum)/v5totalquestions
                        v5completeness = round(accuratev5completeness, 2)
            
                        if totaldocumentlist[v5parid] == None:
                            totaldocumentlist[v5parid] =  'V5_Form'
                            totaldocument = 1
                        elif 'V5_Form' not in totaldocumentlist[v5parid]:
                            totaldocumentlist[v5parid] = totaldocumentlist[v5parid] + ' V5_Form'
                            splitstring = totaldocumentlist[v5parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v5parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v5parid] * (totaldocument - 1) + accuratev5completeness)/ totaldocument
                        averagecompletelist[v5parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v5parid,"Centre_id":v5centreid,"local_id":v5localid,"date":v5date,"time":v5time,"activity":v5activity,"type":v5activitytype,"version":v5version,"old_content":v5oldcontent,"newcontent":v5newcontent,"completeness":v5completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v5parid],"total_edits":totaleditlist[v5parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v6' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v6parid = int(idlist[idposition + 3])
                        
                        if v6versionlist[v6parid] == 0:
                            v6activity = 'Create'   
                        else:
                            v6activity = 'Update'
                
                        v6versionlist[v6parid] = v6versionlist[v6parid] + 1
                        v6activitytype = 'V6_Form'
                        totaleditlist[v6parid] = totaleditlist[v6parid] + 1
                
                        clilocalline = mparticipantlist[v6parid]
                        v6centreid = re.split(' ', clilocalline)[0]
                        v6localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v6date = postlinelist[8]
                        v6time = postlinelist[9]
                        v6version = v6versionlist[v6parid]
                        if v6oldcontentlist[v6parid] == None:
                            v6oldcontentlist[v6parid] = ''
                        v6oldcontent = v6oldcontentlist[v6parid]
            
                        v6position = parameterline.find('"v6')
                        commitposition = parameterline.find('commit')
                        contentstart = v6position
                        contentend = commitposition - 3
                        v6new1content = parameterline[contentstart:contentend]
                        v6new2content = v6new1content.replace('"', '')
                        v6new3content = v6new2content.replace('{', '')
                        v6newcontent = v6new3content.replace('}', '')
                        v6oldcontentlist[v6parid] = v6newcontent
                    
                        v6totalquestions = v6new1content.count(',') + 1
                        v6unanswerednum = v6new1content.count('""')
                        accuratev6completeness = (v6totalquestions - v6unanswerednum)/v6totalquestions
                        v6completeness = round(accuratev6completeness, 2)
            
                        if totaldocumentlist[v6parid] == None:
                            totaldocumentlist[v6parid] =  'V6_Form'
                            totaldocument = 1
                        elif 'V6_Form' not in totaldocumentlist[v6parid]:
                            totaldocumentlist[v6parid] = totaldocumentlist[v6parid] + ' V6_Form'
                            splitstring = totaldocumentlist[v6parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v6parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v6parid] * (totaldocument - 1) + accuratev6completeness)/ totaldocument
                        averagecompletelist[v6parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v6parid,"Centre_id":v6centreid,"local_id":v6localid,"date":v6date,"time":v6time,"activity":v6activity,"type":v6activitytype,"version":v6version,"old_content":v6oldcontent,"newcontent":v6newcontent,"completeness":v6completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v6parid],"total_edits":totaleditlist[v6parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v7' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v7parid = int(idlist[idposition + 3])
                        
                        if v7versionlist[v7parid] == 0:
                            v7activity = 'Create'   
                        else:
                            v7activity = 'Update'
                
                        v7versionlist[v7parid] = v7versionlist[v7parid] + 1
                        v7activitytype = 'V7_Form'
                        totaleditlist[v7parid] = totaleditlist[v7parid] + 1
                
                        clilocalline = mparticipantlist[v7parid]
                        v7centreid = re.split(' ', clilocalline)[0]
                        v7localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v7date = postlinelist[8]
                        v7time = postlinelist[9]
                        v7version = v7versionlist[v7parid]
                        if v7oldcontentlist[v7parid] == None:
                            v7oldcontentlist[v7parid] = ''
                        v7oldcontent = v7oldcontentlist[v7parid]
            
                        v7position = parameterline.find('"v7')
                        commitposition = parameterline.find('commit')
                        contentstart = v7position
                        contentend = commitposition - 3
                        v7new1content = parameterline[contentstart:contentend]
                        v7new2content = v7new1content.replace('"', '')
                        v7new3content = v7new2content.replace('{', '')
                        v7newcontent = v7new3content.replace('}', '')
                        v7oldcontentlist[v7parid] = v7newcontent
                    
                        v7totalquestions = v7new1content.count(',') + 1
                        v7unanswerednum = v7new1content.count('""')
                        accuratev7completeness = (v7totalquestions - v7unanswerednum)/v7totalquestions
                        v7completeness = round(accuratev7completeness, 2)
            
                        if totaldocumentlist[v7parid] == None:
                            totaldocumentlist[v7parid] =  'V7_Form'
                            totaldocument = 1
                        elif 'V7_Form' not in totaldocumentlist[v7parid]:
                            totaldocumentlist[v7parid] = totaldocumentlist[v7parid] + ' V7_Form'
                            splitstring = totaldocumentlist[v7parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v7parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v7parid] * (totaldocument - 1) + accuratev7completeness)/ totaldocument
                        averagecompletelist[v7parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v7parid,"Centre_id":v7centreid,"local_id":v7localid,"date":v7date,"time":v7time,"activity":v7activity,"type":v7activitytype,"version":v7version,"old_content":v7oldcontent,"newcontent":v7newcontent,"completeness":v7completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v7parid],"total_edits":totaleditlist[v7parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v8' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v8parid = int(idlist[idposition + 3])
                        
                        if v8versionlist[v8parid] == 0:
                            v8activity = 'Create'   
                        else:
                            v8activity = 'Update'
                
                        v8versionlist[v8parid] = v8versionlist[v8parid] + 1
                        v8activitytype = 'V8_Form'
                        totaleditlist[v8parid] = totaleditlist[v8parid] + 1
                
                        clilocalline = mparticipantlist[v8parid]
                        v8centreid = re.split(' ', clilocalline)[0]
                        v8localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v8date = postlinelist[8]
                        v8time = postlinelist[9]
                        v8version = v8versionlist[v8parid]
                        if v8oldcontentlist[v8parid] == None:
                            v8oldcontentlist[v8parid] = ''
                        v8oldcontent = v8oldcontentlist[v8parid]
            
                        v8position = parameterline.find('"v8')
                        commitposition = parameterline.find('commit')
                        contentstart = v8position
                        contentend = commitposition - 3
                        v8new1content = parameterline[contentstart:contentend]
                        v8new2content = v8new1content.replace('"', '')
                        v8new3content = v8new2content.replace('{', '')
                        v8newcontent = v8new3content.replace('}', '')
                        v8oldcontentlist[v8parid] = v8newcontent
                    
                        v8totalquestions = v8new1content.count(',') + 1
                        v8unanswerednum = v8new1content.count('""')
                        accuratev8completeness = (v8totalquestions - v8unanswerednum)/v8totalquestions
                        v8completeness = round(accuratev8completeness, 2)
            
                        if totaldocumentlist[v8parid] == None:
                            totaldocumentlist[v8parid] =  'V8_Form'
                            totaldocument = 1
                        elif 'V8_Form' not in totaldocumentlist[v8parid]:
                            totaldocumentlist[v8parid] = totaldocumentlist[v8parid] + ' V8_Form'
                            splitstring = totaldocumentlist[v8parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v8parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v8parid] * (totaldocument - 1) + accuratev8completeness)/ totaldocument
                        averagecompletelist[v8parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v8parid,"Centre_id":v8centreid,"local_id":v8localid,"date":v8date,"time":v8time,"activity":v8activity,"type":v8activitytype,"version":v8version,"old_content":v8oldcontent,"newcontent":v8newcontent,"completeness":v8completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v8parid],"total_edits":totaleditlist[v8parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v9' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v9parid = int(idlist[idposition + 3])
                        
                        if v9versionlist[v9parid] == 0:
                            v9activity = 'Create'   
                        else:
                            v9activity = 'Update'
                
                        v9versionlist[v9parid] = v9versionlist[v9parid] + 1
                        v9activitytype = 'V9_Form'
                        totaleditlist[v9parid] = totaleditlist[v9parid] + 1
                
                        clilocalline = mparticipantlist[v9parid]
                        v9centreid = re.split(' ', clilocalline)[0]
                        v9localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v9date = postlinelist[8]
                        v9time = postlinelist[9]
                        v9version = v9versionlist[v9parid]
                        if v9oldcontentlist[v9parid] == None:
                            v9oldcontentlist[v9parid] = ''
                        v9oldcontent = v9oldcontentlist[v9parid]
            
                        v9position = parameterline.find('"v9')
                        commitposition = parameterline.find('commit')
                        contentstart = v9position
                        contentend = commitposition - 3
                        v9new1content = parameterline[contentstart:contentend]
                        v9new2content = v9new1content.replace('"', '')
                        v9new3content = v9new2content.replace('{', '')
                        v9newcontent = v9new3content.replace('}', '')
                        v9oldcontentlist[v9parid] = v9newcontent
                    
                        v9totalquestions = v9new1content.count(',') + 1
                        v9unanswerednum = v9new1content.count('""')
                        accuratev9completeness = (v9totalquestions - v9unanswerednum)/v9totalquestions
                        v9completeness = round(accuratev9completeness, 2)
            
                        if totaldocumentlist[v9parid] == None:
                            totaldocumentlist[v9parid] =  'V9_Form'
                            totaldocument = 1
                        elif 'V9_Form' not in totaldocumentlist[v9parid]:
                            totaldocumentlist[v9parid] = totaldocumentlist[v9parid] + ' V9_Form'
                            splitstring = totaldocumentlist[v9parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v9parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v9parid] * (totaldocument - 1) + accuratev9completeness)/ totaldocument
                        averagecompletelist[v9parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v9parid,"Centre_id":v9centreid,"local_id":v9localid,"date":v9date,"time":v9time,"activity":v9activity,"type":v9activitytype,"version":v9version,"old_content":v9oldcontent,"newcontent":v9newcontent,"completeness":v9completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v9parid],"total_edits":totaleditlist[v9parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v10' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v10parid = int(idlist[idposition + 3])
                        
                        if v10versionlist[v10parid] == 0:
                            v10activity = 'Create'   
                        else:
                            v10activity = 'Update'
                
                        v10versionlist[v10parid] = v10versionlist[v10parid] + 1
                        v10activitytype = 'V10_Form'
                        totaleditlist[v10parid] = totaleditlist[v10parid] + 1
                
                        clilocalline = mparticipantlist[v10parid]
                        v10centreid = re.split(' ', clilocalline)[0]
                        v10localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v10date = postlinelist[8]
                        v10time = postlinelist[9]
                        v10version = v10versionlist[v10parid]
                        if v10oldcontentlist[v10parid] == None:
                            v10oldcontentlist[v10parid] = ''
                        v10oldcontent = v10oldcontentlist[v10parid]
            
                        v10position = parameterline.find('"v10')
                        commitposition = parameterline.find('commit')
                        contentstart = v10position
                        contentend = commitposition - 3
                        v10new1content = parameterline[contentstart:contentend]
                        v10new2content = v10new1content.replace('"', '')
                        v10new3content = v10new2content.replace('{', '')
                        v10newcontent = v10new3content.replace('}', '')
                        v10oldcontentlist[v10parid] = v10newcontent
                    
                        v10totalquestions = v10new1content.count(',') + 1
                        v10unanswerednum = v10new1content.count('""')
                        accuratev10completeness = (v10totalquestions - v10unanswerednum)/v10totalquestions
                        v10completeness = round(accuratev10completeness, 2)
            
                        if totaldocumentlist[v10parid] == None:
                            totaldocumentlist[v10parid] =  'V10_Form'
                            totaldocument = 1
                        elif 'V10_Form' not in totaldocumentlist[v10parid]:
                            totaldocumentlist[v10parid] = totaldocumentlist[v10parid] + ' V10_Form'
                            splitstring = totaldocumentlist[v10parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v10parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v10parid] * (totaldocument - 1) + accuratev10completeness)/ totaldocument
                        averagecompletelist[v10parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v10parid,"Centre_id":v10centreid,"local_id":v10localid,"date":v10date,"time":v10time,"activity":v10activity,"type":v10activitytype,"version":v10version,"old_content":v10oldcontent,"newcontent":v10newcontent,"completeness":v10completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v10parid],"total_edits":totaleditlist[v10parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
    elif 'Started PUT' in aline:
        matchObj = re.search(r'/participants(/[0-9]+(.[0-9]{1,3})?)?"', aline, re.M|re.I)
        if matchObj:
            putline = aline
            postlinelist = re.split(' |"', putline)
            ipaddress = postlinelist[6]
            processline = f.readline()
            parameterline = f.readline()
            idline = f.readline()
            if 'Started POST' not in idline and 'Started PUT' not in idline:
                canfind = re.search(r'Started GET "/participants/[0-9]+(.[0-9]{1,3})?"', idline, re.M|re.I) and re.split(' |"', idline)[6][:9] == ipaddress[:9]
                while not canfind:
                    idline = f.readline()
                    if 'Started POST' in idline or 'Started PUT' in idline:
                        flag = 1
                        break
                    else:
                        canfind = re.search(r'Started GET "/participants/[0-9]+(.[0-9]{1,3})?"', idline, re.M|re.I) and re.split(' |"', idline)[6][:9] == ipaddress[:9]
                if flag == 0:
                    idlist = re.split('/| |"', idline)
                    parparid = int(idlist[5])
                    parversionlist[parparid] = parversionlist[parparid] + 1
                    totaleditlist[parparid] = totaleditlist[parparid] + 1
                    clilocalline = mparticipantlist[parparid]
                    parcentreid = re.split(' ', clilocalline)[0]
                    parlocalid = re.split(' ', clilocalline)[1]
                    
                    pardate = postlinelist[8]
                    partime = postlinelist[9]
                    paractivity = 'Update'
                    paractivitytype = 'Participant'
                    parversion = parversionlist[parparid]
                    if paroldcontentlist[parparid] == None:
                        paroldcontentlist[parparid] = ''
                    paroldcontent = paroldcontentlist[parparid]
                    
                    parameterposition = parameterline.find('Parameters')
                    commitposition = parameterline.find('commit')
                    contentstart = parameterposition + 12
                    contentend = commitposition - 3
                    parnew1content = parameterline[contentstart:contentend]
                    parnew2content = parnew1content.replace('"', '')
                    parnew3content = parnew2content.replace('{', '')
                    parnewcontent = parnew3content.replace('}', '')
                    paroldcontentlist[parparid] = parnewcontent
                    
                    if parcompletenesslist[parparid] == None:
                        parcompletenesslist[parparid] = 'PersonalDetail'
                    newparcomplete = addupdatecomplete('mother_attributes', parnewcontent, parcompletenesslist[parparid])
                    newparcomplete = addupdatecomplete('father_attributes', parnewcontent, newparcomplete)
                    newparcomplete = addupdatecomplete('b1_attributes', parnewcontent, newparcomplete)
                    newparcomplete = addupdatecomplete('probands_attributes', parnewcontent, newparcomplete)
                    newparcomplete = addupdatecomplete('family_members_attributes', parnewcontent, newparcomplete)
                    parcompletesplitlist = re.split(' ', newparcomplete)
                    parcompletenesslist[parparid] = newparcomplete
                    parcompleteness = len(parcompletesplitlist)/5
                    
                    if totaldocumentlist[parparid] == None:
                        totaldocumentlist[parparid] =  'Participant'
                        totaldocument = 1
                    elif 'Participant' not in totaldocumentlist[parparid]:
                        totaldocumentlist[parparid] = totaldocumentlist[parparid] + ' Participant'
                        splitstring = totaldocumentlist[parparid][1:]
                        totaldocumentsplitlist = re.split(' ', splitstring)
                        totaldocument = len(totaldocumentsplitlist)
                    else:
                        totaldocumentsplitlist = re.split(' ', totaldocumentlist[parparid])
                        totaldocument = len(totaldocumentsplitlist)
                    
                    accurateaveragecomplete = (averagecompletelist[parparid] * (totaldocument - 1) + parcompleteness)/ totaldocument
                    averagecompletelist[parparid] = round(accurateaveragecomplete, 2)
                    data = {"participant_id":parparid,"Centre_id":parcentreid,"local_id":parlocalid,"date":pardate,"time":partime,"activity":paractivity,"type":paractivitytype,"version":parversion,"old_content":paroldcontent,"newcontent":parnewcontent,"completeness":parcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[parparid],"total_edits":totaleditlist[parparid]}
                    db.save(data)
            else:
                flag = 1

        elif 'fathers' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0:        
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        faparid = int(idlist[idposition + 3])
            
                        faversionlist[faparid] = faversionlist[faparid] + 1
                        totaleditlist[faparid] = totaleditlist[faparid] + 1
                        clilocalline = mparticipantlist[faparid]
                        facentreid = re.split(' ', clilocalline)[0]
                        falocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        fadate = postlinelist[8]
                        fatime = postlinelist[9]
                        if faversionlist[faparid] == 0:
                            faactivity = 'Create'
                        else:
                            faactivity = 'Update'
                        
                        faactivitytype = 'Father_Form'
                        faversion = faversionlist[faparid]
                        if faoldcontentlist[faparid] == None:
                            faoldcontentlist[faparid] = ''
                        faoldcontent = faoldcontentlist[faparid]
            
                        fatherposition = parameterline.find('father')
                        commitposition = parameterline.find('commit')
                        contentstart = fatherposition -1
                        contentend = commitposition - 3
                        fanew1content = parameterline[contentstart:contentend]
                        fanew2content = fanew1content.replace('"', '')
                        fanew3content = fanew2content.replace('{', '')
                        fanewcontent = fanew3content.replace('}', '')
                        faoldcontentlist[faparid] = fanewcontent
                    
                        fatotalquestions = fanew1content.count(',') + 1
                        faunanswerednum = fanew1content.count('""')
                        accuratefacompleteness = (fatotalquestions - faunanswerednum)/fatotalquestions
                        facompleteness = round(accuratefacompleteness, 2)
            
                        if totaldocumentlist[faparid] == None:
                            totaldocumentlist[faparid] =  'Father_Form'
                            totaldocument = 1
                        elif 'Father_Form' not in totaldocumentlist[faparid]:
                            totaldocumentlist[faparid] = totaldocumentlist[faparid] + ' Father_Form'
                            splitstring = totaldocumentlist[faparid][1:]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[faparid])
                            totaldocument = len(totaldocumentsplitlist)
                
                        accurateaveragecomplete = (averagecompletelist[faparid] * (totaldocument - 1) + accuratefacompleteness)/ totaldocument
                        averagecompletelist[faparid] = round(accurateaveragecomplete, 2)    
                        data = {"participant_id":faparid,"Centre_id":facentreid,"local_id":falocalid,"date":fadate,"time":fatime,"activity":faactivity,"type":faactivitytype,"version":faversion,"old_content":faoldcontent,"newcontent":fanewcontent,"completeness":facompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[faparid],"total_edits":totaleditlist[faparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                    
        elif 'mothers' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        moparid = int(idlist[idposition + 3])
            
                        if moversionlist[moparid] == 0:
                            moactivity = 'Create'
                        else:
                            moactivity = 'Update'
                        
                        moactivitytype = 'Mother_Form'
                        moversionlist[moparid] = moversionlist[moparid] + 1
                        totaleditlist[moparid] = totaleditlist[moparid] + 1
                        clilocalline = mparticipantlist[moparid]
                        mocentreid = re.split(' ', clilocalline)[0]
                        molocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        modate = postlinelist[8]
                        motime = postlinelist[9]
                        moversion = moversionlist[moparid]
                        if mooldcontentlist[moparid] == None:
                            mooldcontentlist[moparid] = ''
                        mooldcontent = mooldcontentlist[moparid]
            
                        motherposition = parameterline.find('mother')
                        commitposition = parameterline.find('commit')
                        contentstart = motherposition -1
                        contentend = commitposition - 3
                        monew1content = parameterline[contentstart:contentend]
                        monew2content = monew1content.replace('"', '')
                        monew3content = monew2content.replace('{', '')
                        monewcontent = monew3content.replace('}', '')
                        mooldcontentlist[moparid] = monewcontent
                    
                        mototalquestions = monew1content.count(',') + 1
                        mounanswerednum = monew1content.count('""')
                        accuratemocompleteness = (mototalquestions - mounanswerednum)/mototalquestions
                        mocompleteness = round(accuratemocompleteness, 2)
            
                        if totaldocumentlist[moparid] == None:
                            totaldocumentlist[moparid] =  'Mother_Form'
                            totaldocument = 1
                        elif 'Mother_Form' not in totaldocumentlist[moparid]:
                            totaldocumentlist[moparid] = totaldocumentlist[moparid] + ' Mother_Form'
                            splitstring = totaldocumentlist[moparid][1:]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[moparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[moparid] * (totaldocument - 1) + accuratemocompleteness)/ totaldocument
                        averagecompletelist[moparid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":moparid,"Centre_id":mocentreid,"local_id":molocalid,"date":modate,"time":motime,"activity":moactivity,"type":moactivitytype,"version":moversion,"old_content":mooldcontent,"newcontent":monewcontent,"completeness":mocompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[moparid],"total_edits":totaleditlist[moparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'family_members' in aline:
            processline = f.readline()
            parameterline = f.readline()
            
            if 'participant_id' in parameterline:
                idlist = re.split('"|=>|,', parameterline)
                idposition = idlist.index('participant_id')
                famiparid = int(idlist[idposition + 3])
            
                if famiversionlist[famiparid] == 0:
                    famiactivity = 'Create'
                else:
                    famiactivity = 'Update'
                famiactivitytype = 'Family_Members_Form'
                
                famiversionlist[famiparid] = famiversionlist[famiparid] + 1
                totaleditlist[famiparid] = totaleditlist[famiparid] + 1
                clilocalline = mparticipantlist[famiparid]
                famicentreid = re.split(' ', clilocalline)[0]
                familocalid = re.split(' ', clilocalline)[1]
                postlinelist = re.split(' |"', aline)
                famidate = postlinelist[8]
                famitime = postlinelist[9]
                famiversion = famiversionlist[famiparid]
                if famioldcontentlist[famiparid] == None:
                    famioldcontentlist[famiparid] = ''
                famioldcontent = famioldcontentlist[famiparid]
            
                famimposition = parameterline.find('family_member')
                commitposition = parameterline.find('commit')
                contentstart = famimposition -1
                contentend = commitposition - 3
                faminew1content = parameterline[contentstart:contentend]
                faminew2content = faminew1content.replace('"', '')
                faminew3content = faminew2content.replace('{', '')
                faminewcontent = faminew3content.replace('}', '')
                famioldcontentlist[famiparid] = faminewcontent
                    
                famitotalquestions = faminew1content.count(',') + 1
                famiunanswerednum = faminew1content.count('""')
                accuratefamicompleteness = (famitotalquestions - famiunanswerednum)/famitotalquestions
                famicompleteness = round(accuratefamicompleteness, 2)
            
                if totaldocumentlist[famiparid] == None:
                    totaldocumentlist[famiparid] =  'Family_Members_Form'
                    totaldocument = 1
                elif 'Family_Members_Form' not in totaldocumentlist[famiparid]:
                    totaldocumentlist[famiparid] = totaldocumentlist[famiparid] + ' Family_Members_Form'
                    splitstring = totaldocumentlist[famiparid][1:]
                    totaldocumentsplitlist = re.split(' ', splitstring)
                    totaldocument = len(totaldocumentsplitlist)
                else:
                    totaldocumentsplitlist = re.split(' ', totaldocumentlist[famiparid])
                    totaldocument = len(totaldocumentsplitlist)
                    
                accurateaveragecomplete = (averagecompletelist[famiparid] * (totaldocument - 1) + accuratefamicompleteness)/ totaldocument
                averagecompletelist[famiparid] = round(accurateaveragecomplete, 2)
                data = {"participant_id":famiparid,"Centre_id":famicentreid,"local_id":familocalid,"date":famidate,"time":famitime,"activity":famiactivity,"type":famiactivitytype,"version":famiversion,"old_content":famioldcontent,"newcontent":faminewcontent,"completeness":famicompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[famiparid],"total_edits":totaleditlist[famiparid]}
                db.save(data)
                
        elif 'probands' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        proparid = int(idlist[idposition + 3])
            
                        if proversionlist[proparid] == 0:
                            proactivity = 'Create'
                        else:
                            proactivity = 'Update'
                        proactivitytype = 'Proband_Form'
                
                        proversionlist[proparid] = proversionlist[proparid] + 1
                        totaleditlist[proparid] = totaleditlist[proparid] + 1
                        clilocalline = mparticipantlist[proparid]
                        procentreid = re.split(' ', clilocalline)[0]
                        prolocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        prodate = postlinelist[8]
                        protime = postlinelist[9]
                        proversion = proversionlist[proparid]
                        if prooldcontentlist[proparid] == None:
                            prooldcontentlist[proparid] = ''
                        prooldcontent = prooldcontentlist[proparid]
            
                        proposition = parameterline.find('"proband')
                        commitposition = parameterline.find('commit')
                        contentstart = proposition
                        contentend = commitposition - 3
                        pronew1content = parameterline[contentstart:contentend]
                        pronew2content = pronew1content.replace('"', '')
                        pronew3content = pronew2content.replace('{', '')
                        pronewcontent = pronew3content.replace('}', '')
                        prooldcontentlist[proparid] = pronewcontent
                    
                        prototalquestions = pronew1content.count(',') + 1
                        prounanswerednum = pronew1content.count('""')
                        accurateprocompleteness = (prototalquestions - prounanswerednum)/prototalquestions
                        procompleteness = round(accurateprocompleteness, 2)
            
                        if totaldocumentlist[proparid] == None:
                            totaldocumentlist[proparid] =  'Proband_Form'
                            totaldocument = 1
                        elif 'Proband_Form' not in totaldocumentlist[proparid]:
                            totaldocumentlist[proparid] = totaldocumentlist[proparid] + ' Proband_Form'
                            splitstring = totaldocumentlist[proparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[proparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[proparid] * (totaldocument - 1) + accurateprocompleteness)/ totaldocument
                        averagecompletelist[proparid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":proparid,"Centre_id":procentreid,"local_id":prolocalid,"date":prodate,"time":protime,"activity":proactivity,"type":proactivitytype,"version":proversion,"old_content":prooldcontent,"newcontent":pronewcontent,"completeness":procompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[proparid],"total_edits":totaleditlist[proparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'ppaqs' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        ppparid = int(idlist[idposition + 3])
            
                        if ppversionlist[ppparid] == 0:
                            ppactivity = 'Create'
                        else:
                            ppactivity = 'Update'
                        ppactivitytype = 'PPAQ_Form'
                
                        ppversionlist[ppparid] = ppversionlist[ppparid] + 1
                        totaleditlist[ppparid] = totaleditlist[ppparid] + 1
                        clilocalline = mparticipantlist[ppparid]
                        ppcentreid = re.split(' ', clilocalline)[0]
                        pplocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        ppdate = postlinelist[8]
                        pptime = postlinelist[9]
                        ppversion = ppversionlist[ppparid]
                        if ppoldcontentlist[ppparid] == None:
                            ppoldcontentlist[ppparid] = ''
                        ppoldcontent = ppoldcontentlist[ppparid]
            
                        ppposition = parameterline.find('"ppaq')
                        commitposition = parameterline.find('commit')
                        contentstart = ppposition
                        contentend = commitposition - 3
                        ppnew1content = parameterline[contentstart:contentend]
                        ppnew2content = ppnew1content.replace('"', '')
                        ppnew3content = ppnew2content.replace('{', '')
                        ppnewcontent = ppnew3content.replace('}', '')
                        ppoldcontentlist[ppparid] = ppnewcontent
                    
                        pptotalquestions = ppnew1content.count(',') + 1
                        ppunanswerednum = ppnew1content.count('""')
                        accurateppcompleteness = (pptotalquestions - ppunanswerednum)/pptotalquestions
                        ppcompleteness = round(accurateppcompleteness, 2)
            
                        if totaldocumentlist[ppparid] == None:
                            totaldocumentlist[ppparid] =  'PPAQ_Form'
                            totaldocument = 1
                        elif 'PPAQ_Form' not in totaldocumentlist[ppparid]:
                            totaldocumentlist[ppparid] = totaldocumentlist[ppparid] + ' PPAQ_Form'
                            splitstring = totaldocumentlist[ppparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[ppparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[ppparid] * (totaldocument - 1) + accurateppcompleteness)/ totaldocument
                        averagecompletelist[ppparid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":ppparid,"Centre_id":ppcentreid,"local_id":pplocalid,"date":ppdate,"time":pptime,"activity":ppactivity,"type":ppactivitytype,"version":ppversion,"old_content":ppoldcontent,"newcontent":ppnewcontent,"completeness":ppcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[ppparid],"total_edits":totaleditlist[ppparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'pregnancy_lifestyle_questionnaires' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        preparid = int(idlist[idposition + 3])
            
                        if preversionlist[preparid] == 0:
                            preactivity = 'Create'
                        else:
                            preactivity = 'Update'
                        preactivitytype = 'Pregnancy_Questionnaires'
                
                        preversionlist[preparid] = preversionlist[preparid] + 1
                        totaleditlist[preparid] = totaleditlist[preparid] + 1
                        clilocalline = mparticipantlist[preparid]
                        precentreid = re.split(' ', clilocalline)[0]
                        prelocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        predate = postlinelist[8]
                        pretime = postlinelist[9]
                        preversion = preversionlist[preparid]
                        if preoldcontentlist[preparid] == None:
                            preoldcontentlist[preparid] = ''
                        preoldcontent = preoldcontentlist[preparid]
            
                        preposition = parameterline.find('"pregnancy_lifestyle_questionnaire')
                        commitposition = parameterline.find('commit')
                        contentstart = preposition
                        contentend = commitposition - 3
                        prenew1content = parameterline[contentstart:contentend]
                        prenew2content = prenew1content.replace('"', '')
                        prenew3content = prenew2content.replace('{', '')
                        prenewcontent = prenew3content.replace('}', '')
                        preoldcontentlist[preparid] = prenewcontent
                    
                        pretotalquestions = prenew1content.count(',') + 1
                        preunanswerednum = prenew1content.count('""')
                        accurateprecompleteness = (pretotalquestions - preunanswerednum)/pretotalquestions
                        precompleteness = round(accurateprecompleteness, 2)
            
                        if totaldocumentlist[preparid] == None:
                            totaldocumentlist[preparid] =  'Pregnancy_Questionnaires'
                            totaldocument = 1
                        elif 'Pregnancy_Questionnaires' not in totaldocumentlist[preparid]:
                            totaldocumentlist[preparid] = totaldocumentlist[preparid] + ' Pregnancy_Questionnaires'
                            splitstring = totaldocumentlist[preparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[preparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[preparid] * (totaldocument - 1) + accurateprecompleteness)/ totaldocument
                        averagecompletelist[preparid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":preparid,"Centre_id":precentreid,"local_id":prelocalid,"date":predate,"time":pretime,"activity":preactivity,"type":preactivitytype,"version":preversion,"old_content":preoldcontent,"newcontent":prenewcontent,"completeness":precompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[preparid],"total_edits":totaleditlist[preparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif 'maternal_lifestyle_postpartum_questionnaires' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        matparid = int(idlist[idposition + 3])
            
                        if matversionlist[matparid] == 0:
                            matactivity = 'Create'
                        else:
                            matactivity = 'Update'
                        matactivitytype = 'Maternal_Questionnaires'
                
                        matversionlist[matparid] = matversionlist[matparid] + 1
                        totaleditlist[matparid] = totaleditlist[matparid] + 1
                        clilocalline = mparticipantlist[matparid]
                        matcentreid = re.split(' ', clilocalline)[0]
                        matlocalid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        matdate = postlinelist[8]
                        mattime = postlinelist[9]
                        matversion = matversionlist[matparid]
                        if matoldcontentlist[matparid] == None:
                            matoldcontentlist[matparid] = ''
                        matoldcontent = matoldcontentlist[matparid]
            
                        matposition = parameterline.find('"maternal_lifestyle_postpartum_questionnaire')
                        commitposition = parameterline.find('commit')
                        contentstart = matposition
                        contentend = commitposition - 3
                        matnew1content = parameterline[contentstart:contentend]
                        matnew2content = matnew1content.replace('"', '')
                        matnew3content = matnew2content.replace('{', '')
                        matnewcontent = matnew3content.replace('}', '')
                        matoldcontentlist[matparid] = matnewcontent
                    
                        mattotalquestions = matnew1content.count(',') + 1
                        matunanswerednum = matnew1content.count('""')
                        accuratematcompleteness = (mattotalquestions - matunanswerednum)/mattotalquestions
                        matcompleteness = round(accuratematcompleteness, 2)
            
                        if totaldocumentlist[matparid] == None:
                            totaldocumentlist[matparid] =  'Maternal_Questionnaires'
                            totaldocument = 1
                        elif 'Maternal_Questionnaires' not in totaldocumentlist[matparid]:
                            totaldocumentlist[matparid] = totaldocumentlist[matparid] + ' Maternal_Questionnaires'
                            splitstring = totaldocumentlist[matparid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[matparid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[matparid] * (totaldocument - 1) + accuratematcompleteness)/ totaldocument
                        averagecompletelist[matparid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":matparid,"Centre_id":matcentreid,"local_id":matlocalid,"date":matdate,"time":mattime,"activity":matactivity,"type":matactivitytype,"version":matversion,"old_content":matoldcontent,"newcontent":matnewcontent,"completeness":matcompleteness,"document_finished":totaldocument,"average_completeness":averagecompletelist[matparid],"total_edits":totaleditlist[matparid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        elif '/b1' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        b1parid = int(idlist[idposition + 3])
            
                        if b1versionlist[b1parid] == 0:
                            b1activity = 'Create'
                        else:
                            b1activity = 'Update'
                        b1activitytype = 'B1_Form'
                
                        b1versionlist[b1parid] = b1versionlist[b1parid] + 1
                        totaleditlist[b1parid] = totaleditlist[b1parid] + 1
                        clilocalline = mparticipantlist[b1parid]
                        b1centreid = re.split(' ', clilocalline)[0]
                        b1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        b1date = postlinelist[8]
                        b1time = postlinelist[9]
                        b1version = b1versionlist[b1parid]
                        if b1oldcontentlist[b1parid] == None:
                            b1oldcontentlist[b1parid] = ''
                        b1oldcontent = b1oldcontentlist[b1parid]
            
                        b1position = parameterline.find('"b1')
                        commitposition = parameterline.find('commit')
                        contentstart = b1position
                        contentend = commitposition - 3
                        b1new1content = parameterline[contentstart:contentend]
                        b1new2content = b1new1content.replace('"', '')
                        b1new3content = b1new2content.replace('{', '')
                        b1newcontent = b1new3content.replace('}', '')
                        b1oldcontentlist[b1parid] = b1newcontent
                    
                        b1totalquestions = b1new1content.count(',') + 1
                        b1unanswerednum = b1new1content.count('""')
                        accurateb1completeness = (b1totalquestions - b1unanswerednum)/b1totalquestions
                        b1completeness = round(accurateb1completeness, 2)
            
                        if totaldocumentlist[b1parid] == None:
                            totaldocumentlist[b1parid] =  'B1_Form'
                            totaldocument = 1
                        elif 'B1_Form' not in totaldocumentlist[b1parid]:
                            totaldocumentlist[b1parid] = totaldocumentlist[b1parid] + ' B1_Form'
                            splitstring = totaldocumentlist[b1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[b1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[b1parid] * (totaldocument - 1) + accurateb1completeness)/ totaldocument
                        averagecompletelist[b1parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":b1parid,"Centre_id":b1centreid,"local_id":b1localid,"date":b1date,"time":b1time,"activity":b1activity,"type":b1activitytype,"version":b1version,"old_content":b1oldcontent,"newcontent":b1newcontent,"completeness":b1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[b1parid],"total_edits":totaleditlist[b1parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        
        elif '/b2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        b2parid = int(idlist[idposition + 3])
            
                        if b2versionlist[b2parid] == 0:
                            b2activity = 'Create'
                        else:
                            b2activity = 'Update'
                        b2activitytype = 'B2_Form'
                
                        b2versionlist[b2parid] = b2versionlist[b2parid] + 1
                        totaleditlist[b2parid] = totaleditlist[b2parid] + 1
                        clilocalline = mparticipantlist[b2parid]
                        b2centreid = re.split(' ', clilocalline)[0]
                        b2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        b2date = postlinelist[8]
                        b2time = postlinelist[9]
                        b2version = b2versionlist[b2parid]
                        if b2oldcontentlist[b2parid] == None:
                            b2oldcontentlist[b2parid] = ''
                        b2oldcontent = b2oldcontentlist[b2parid]
            
                        b2position = parameterline.find('"b2')
                        commitposition = parameterline.find('commit')
                        contentstart = b2position
                        contentend = commitposition - 3
                        b2new1content = parameterline[contentstart:contentend]
                        b2new2content = b2new1content.replace('"', '')
                        b2new3content = b2new2content.replace('{', '')
                        b2newcontent = b2new3content.replace('}', '')
                        b2oldcontentlist[b2parid] = b2newcontent
                    
                        b2totalquestions = b2new1content.count(',') + 1
                        b2unanswerednum = b2new1content.count('""')
                        accurateb2completeness = (b2totalquestions - b2unanswerednum)/b2totalquestions
                        b2completeness = round(accurateb2completeness, 2)
            
                        if totaldocumentlist[b2parid] == None:
                            totaldocumentlist[b2parid] =  'B2_Form'
                            totaldocument = 1
                        elif 'B2_Form' not in totaldocumentlist[b2parid]:
                            totaldocumentlist[b2parid] = totaldocumentlist[b2parid] + ' B2_Form'
                            splitstring = totaldocumentlist[b2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[b2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[b2parid] * (totaldocument - 1) + accurateb2completeness)/ totaldocument
                        averagecompletelist[b2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":b2parid,"Centre_id":b2centreid,"local_id":b2localid,"date":b2date,"time":b2time,"activity":b2activity,"type":b2activitytype,"version":b2version,"old_content":b2oldcontent,"newcontent":b2newcontent,"completeness":b2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[b2parid],"total_edits":totaleditlist[b2parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/t1' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t1parid = int(idlist[idposition + 3])
            
                        if t1versionlist[t1parid] == 0:
                            t1activity = 'Create'
                        else:
                            t1activity = 'Update'
                        t1activitytype = 'T1_Form'
                
                        t1versionlist[t1parid] = t1versionlist[t1parid] + 1
                        totaleditlist[t1parid] = totaleditlist[t1parid] + 1
                        clilocalline = mparticipantlist[t1parid]
                        t1centreid = re.split(' ', clilocalline)[0]
                        t1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t1date = postlinelist[8]
                        t1time = postlinelist[9]
                        t1version = t1versionlist[t1parid]
                        if t1oldcontentlist[t1parid] == None:
                            t1oldcontentlist[t1parid] = ''
                        t1oldcontent = t1oldcontentlist[t1parid]
            
                        t1position = parameterline.find('"t1')
                        commitposition = parameterline.find('commit')
                        contentstart = t1position
                        contentend = commitposition - 3
                        t1new1content = parameterline[contentstart:contentend]
                        t1new2content = t1new1content.replace('"', '')
                        t1new3content = t1new2content.replace('{', '')
                        t1newcontent = t1new3content.replace('}', '')
                        t1oldcontentlist[t1parid] = t1newcontent
                    
                        t1totalquestions = t1new1content.count(',') + 1
                        t1unanswerednum = t1new1content.count('""')
                        accuratet1completeness = (t1totalquestions - t1unanswerednum)/t1totalquestions
                        t1completeness = round(accuratet1completeness, 2)
            
                        if totaldocumentlist[t1parid] == None:
                            totaldocumentlist[t1parid] =  'T1_Form'
                            totaldocument = 1
                        elif 'T1_Form' not in totaldocumentlist[t1parid]:
                            totaldocumentlist[t1parid] = totaldocumentlist[t1parid] + ' T1_Form'
                            splitstring = totaldocumentlist[t1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t1parid] * (totaldocument - 1) + accuratet1completeness)/ totaldocument
                        averagecompletelist[t1parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t1parid,"Centre_id":t1centreid,"local_id":t1localid,"date":t1date,"time":t1time,"activity":t1activity,"type":t1activitytype,"version":t1version,"old_content":t1oldcontent,"newcontent":t1newcontent,"completeness":t1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t1parid],"total_edits":totaleditlist[t1parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
       
        elif '/t2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t2parid = int(idlist[idposition + 3])
            
                        if t2versionlist[t2parid] == 0:
                            t2activity = 'Create'
                        else:
                            t2activity = 'Update'
                        t2activitytype = 'T2_Form'
                
                        t2versionlist[t2parid] = t2versionlist[t2parid] + 1
                        totaleditlist[t2parid] = totaleditlist[t2parid] + 1
                        clilocalline = mparticipantlist[t2parid]
                        t2centreid = re.split(' ', clilocalline)[0]
                        t2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t2date = postlinelist[8]
                        t2time = postlinelist[9]
                        t2version = t2versionlist[t2parid]
                        if t2oldcontentlist[t2parid] == None:
                            t2oldcontentlist[t2parid] = ''
                        t2oldcontent = t2oldcontentlist[t2parid]
            
                        t2position = parameterline.find('"t2')
                        commitposition = parameterline.find('commit')
                        contentstart = t2position
                        contentend = commitposition - 3
                        t2new1content = parameterline[contentstart:contentend]
                        t2new2content = t2new1content.replace('"', '')
                        t2new3content = t2new2content.replace('{', '')
                        t2newcontent = t2new3content.replace('}', '')
                        t2oldcontentlist[t2parid] = t2newcontent
                    
                        t2totalquestions = t2new1content.count(',') + 1
                        t2unanswerednum = t2new1content.count('""')
                        accuratet2completeness = (t2totalquestions - t2unanswerednum)/t2totalquestions
                        t2completeness = round(accuratet2completeness, 2)
            
                        if totaldocumentlist[t2parid] == None:
                            totaldocumentlist[t2parid] =  'T2_Form'
                            totaldocument = 1
                        elif 'T2_Form' not in totaldocumentlist[t2parid]:
                            totaldocumentlist[t2parid] = totaldocumentlist[t2parid] + ' T2_Form'
                            splitstring = totaldocumentlist[t2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t2parid] * (totaldocument - 1) + accuratet2completeness)/ totaldocument
                        averagecompletelist[t2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t2parid,"Centre_id":t2centreid,"local_id":t2localid,"date":t2date,"time":t2time,"activity":t2activity,"type":t2activitytype,"version":t2version,"old_content":t2oldcontent,"newcontent":t2newcontent,"completeness":t2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t2parid],"total_edits":totaleditlist[t2parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/t3' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        t3parid = int(idlist[idposition + 3])
            
                        if t3versionlist[t3parid] == 0:
                            t3activity = 'Create'
                        else:
                            t3activity = 'Update'
                        t3activitytype = 'T3_Form'
                
                        t3versionlist[t3parid] = t3versionlist[t3parid] + 1
                        totaleditlist[t3parid] = totaleditlist[t3parid] + 1
                        clilocalline = mparticipantlist[t3parid]
                        t3centreid = re.split(' ', clilocalline)[0]
                        t3localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        t3date = postlinelist[8]
                        t3time = postlinelist[9]
                        t3version = t3versionlist[t3parid]
                        if t3oldcontentlist[t3parid] == None:
                            t3oldcontentlist[t3parid] = ''
                        t3oldcontent = t3oldcontentlist[t3parid]
            
                        t3position = parameterline.find('"t3')
                        commitposition = parameterline.find('commit')
                        contentstart = t3position
                        contentend = commitposition - 3
                        t3new1content = parameterline[contentstart:contentend]
                        t3new2content = t3new1content.replace('"', '')
                        t3new3content = t3new2content.replace('{', '')
                        t3newcontent = t3new3content.replace('}', '')
                        t3oldcontentlist[t3parid] = t3newcontent
                    
                        t3totalquestions = t3new1content.count(',') + 1
                        t3unanswerednum = t3new1content.count('""')
                        accuratet3completeness = (t3totalquestions - t3unanswerednum)/t3totalquestions
                        t3completeness = round(accuratet3completeness, 2)
            
                        if totaldocumentlist[t3parid] == None:
                            totaldocumentlist[t3parid] =  'T3_Form'
                            totaldocument = 1
                        elif 'T3_Form' not in totaldocumentlist[t3parid]:
                            totaldocumentlist[t3parid] = totaldocumentlist[t3parid] + ' T3_Form'
                            splitstring = totaldocumentlist[t3parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[t3parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[t3parid] * (totaldocument - 1) + accuratet3completeness)/ totaldocument
                        averagecompletelist[t3parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":t3parid,"Centre_id":t3centreid,"local_id":t3localid,"date":t3date,"time":t3time,"activity":t3activity,"type":t3activitytype,"version":t3version,"old_content":t3oldcontent,"newcontent":t3newcontent,"completeness":t3completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[t3parid],"total_edits":totaleditlist[t3parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
        
        elif '/v1"' in aline or '/v1/' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v1parid = int(idlist[idposition + 3])
            
                        if v1versionlist[v1parid] == 0:
                            v1activity = 'Create'
                        else:
                            v1activity = 'Update'
                        v1activitytype = 'V1_Form'
                
                        v1versionlist[v1parid] = v1versionlist[v1parid] + 1
                        totaleditlist[v1parid] = totaleditlist[v1parid] + 1
                        clilocalline = mparticipantlist[v1parid]
                        v1centreid = re.split(' ', clilocalline)[0]
                        v1localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v1date = postlinelist[8]
                        v1time = postlinelist[9]
                        v1version = v1versionlist[v1parid]
                        if v1oldcontentlist[v1parid] == None:
                            v1oldcontentlist[v1parid] = ''
                        v1oldcontent = v1oldcontentlist[v1parid]
            
                        v1position = parameterline.find('"v1')
                        commitposition = parameterline.find('commit')
                        contentstart = v1position
                        contentend = commitposition - 3
                        v1new1content = parameterline[contentstart:contentend]
                        v1new2content = v1new1content.replace('"', '')
                        v1new3content = v1new2content.replace('{', '')
                        v1newcontent = v1new3content.replace('}', '')
                        v1oldcontentlist[v1parid] = v1newcontent
                    
                        v1totalquestions = v1new1content.count(',') + 1
                        v1unanswerednum = v1new1content.count('""')
                        accuratev1completeness = (v1totalquestions - v1unanswerednum)/v1totalquestions
                        v1completeness = round(accuratev1completeness, 2)
            
                        if totaldocumentlist[v1parid] == None:
                            totaldocumentlist[v1parid] =  'V1_Form'
                            totaldocument = 1
                        elif 'V1_Form' not in totaldocumentlist[v1parid]:
                            totaldocumentlist[v1parid] = totaldocumentlist[v1parid] + ' V1_Form'
                            splitstring = totaldocumentlist[v1parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v1parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v1parid] * (totaldocument - 1) + accuratev1completeness)/ totaldocument
                        averagecompletelist[v1parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v1parid,"Centre_id":v1centreid,"local_id":v1localid,"date":v1date,"time":v1time,"activity":v1activity,"type":v1activitytype,"version":v1version,"old_content":v1oldcontent,"newcontent":v1newcontent,"completeness":v1completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v1parid],"total_edits":totaleditlist[v1parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v2' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v2parid = int(idlist[idposition + 3])
            
                        if v2versionlist[v2parid] == 0:
                            v2activity = 'Create'
                        else:
                            v2activity = 'Update'
                        v2activitytype = 'V2_Form'
                
                        v2versionlist[v2parid] = v2versionlist[v2parid] + 1
                        totaleditlist[v2parid] = totaleditlist[v2parid] + 1
                        clilocalline = mparticipantlist[v2parid]
                        v2centreid = re.split(' ', clilocalline)[0]
                        v2localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v2date = postlinelist[8]
                        v2time = postlinelist[9]
                        v2version = v2versionlist[v2parid]
                        if v2oldcontentlist[v2parid] == None:
                            v2oldcontentlist[v2parid] = ''
                        v2oldcontent = v2oldcontentlist[v2parid]
            
                        v2position = parameterline.find('"v2')
                        commitposition = parameterline.find('commit')
                        contentstart = v2position
                        contentend = commitposition - 3
                        v2new1content = parameterline[contentstart:contentend]
                        v2new2content = v2new1content.replace('"', '')
                        v2new3content = v2new2content.replace('{', '')
                        v2newcontent = v2new3content.replace('}', '')
                        v2oldcontentlist[v2parid] = v2newcontent
                    
                        v2totalquestions = v2new1content.count(',') + 1
                        v2unanswerednum = v2new1content.count('""')
                        accuratev2completeness = (v2totalquestions - v2unanswerednum)/v2totalquestions
                        v2completeness = round(accuratev2completeness, 2)
            
                        if totaldocumentlist[v2parid] == None:
                            totaldocumentlist[v2parid] =  'V2_Form'
                            totaldocument = 1
                        elif 'V2_Form' not in totaldocumentlist[v2parid]:
                            totaldocumentlist[v2parid] = totaldocumentlist[v2parid] + ' V2_Form'
                            splitstring = totaldocumentlist[v2parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v2parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v2parid] * (totaldocument - 1) + accuratev2completeness)/ totaldocument
                        averagecompletelist[v2parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v2parid,"Centre_id":v2centreid,"local_id":v2localid,"date":v2date,"time":v2time,"activity":v2activity,"type":v2activitytype,"version":v2version,"old_content":v2oldcontent,"newcontent":v2newcontent,"completeness":v2completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v2parid],"total_edits":totaleditlist[v2parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v3' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v3parid = int(idlist[idposition + 3])
            
                        if v3versionlist[v3parid] == 0:
                            v3activity = 'Create'
                        else:
                            v3activity = 'Update'
                        v3activitytype = 'V3_Form'
                
                        v3versionlist[v3parid] = v3versionlist[v3parid] + 1
                        totaleditlist[v3parid] = totaleditlist[v3parid] + 1
                        clilocalline = mparticipantlist[v3parid]
                        v3centreid = re.split(' ', clilocalline)[0]
                        v3localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v3date = postlinelist[8]
                        v3time = postlinelist[9]
                        v3version = v3versionlist[v3parid]
                        if v3oldcontentlist[v3parid] == None:
                            v3oldcontentlist[v3parid] = ''
                        v3oldcontent = v3oldcontentlist[v3parid]
            
                        v3position = parameterline.find('"v3')
                        commitposition = parameterline.find('commit')
                        contentstart = v3position
                        contentend = commitposition - 3
                        v3new1content = parameterline[contentstart:contentend]
                        v3new2content = v3new1content.replace('"', '')
                        v3new3content = v3new2content.replace('{', '')
                        v3newcontent = v3new3content.replace('}', '')
                        v3oldcontentlist[v3parid] = v3newcontent
                    
                        v3totalquestions = v3new1content.count(',') + 1
                        v3unanswerednum = v3new1content.count('""')
                        accuratev3completeness = (v3totalquestions - v3unanswerednum)/v3totalquestions
                        v3completeness = round(accuratev3completeness, 2)
            
                        if totaldocumentlist[v3parid] == None:
                            totaldocumentlist[v3parid] =  'V3_Form'
                            totaldocument = 1
                        elif 'V3_Form' not in totaldocumentlist[v3parid]:
                            totaldocumentlist[v3parid] = totaldocumentlist[v3parid] + ' V3_Form'
                            splitstring = totaldocumentlist[v3parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v3parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v3parid] * (totaldocument - 1) + accuratev3completeness)/ totaldocument
                        averagecompletelist[v3parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v3parid,"Centre_id":v3centreid,"local_id":v3localid,"date":v3date,"time":v3time,"activity":v3activity,"type":v3activitytype,"version":v3version,"old_content":v3oldcontent,"newcontent":v3newcontent,"completeness":v3completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v3parid],"total_edits":totaleditlist[v3parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v4' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v4parid = int(idlist[idposition + 3])
            
                        if v4versionlist[v4parid] == 0:
                            v4activity = 'Create'
                        else:
                            v4activity = 'Update'
                        v4activitytype = 'V4_Form'
                
                        v4versionlist[v4parid] = v4versionlist[v4parid] + 1
                        totaleditlist[v4parid] = totaleditlist[v4parid] + 1
                        clilocalline = mparticipantlist[v4parid]
                        v4centreid = re.split(' ', clilocalline)[0]
                        v4localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v4date = postlinelist[8]
                        v4time = postlinelist[9]
                        v4version = v4versionlist[v4parid]
                        if v4oldcontentlist[v4parid] == None:
                            v4oldcontentlist[v4parid] = ''
                        v4oldcontent = v4oldcontentlist[v4parid]
            
                        v4position = parameterline.find('"v4')
                        commitposition = parameterline.find('commit')
                        contentstart = v4position
                        contentend = commitposition - 3
                        v4new1content = parameterline[contentstart:contentend]
                        v4new2content = v4new1content.replace('"', '')
                        v4new3content = v4new2content.replace('{', '')
                        v4newcontent = v4new3content.replace('}', '')
                        v4oldcontentlist[v4parid] = v4newcontent
                    
                        v4totalquestions = v4new1content.count(',') + 1
                        v4unanswerednum = v4new1content.count('""')
                        accuratev4completeness = (v4totalquestions - v4unanswerednum)/v4totalquestions
                        v4completeness = round(accuratev4completeness, 2)
            
                        if totaldocumentlist[v4parid] == None:
                            totaldocumentlist[v4parid] =  'V4_Form'
                            totaldocument = 1
                        elif 'V4_Form' not in totaldocumentlist[v4parid]:
                            totaldocumentlist[v4parid] = totaldocumentlist[v4parid] + ' V4_Form'
                            splitstring = totaldocumentlist[v4parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v4parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v4parid] * (totaldocument - 1) + accuratev4completeness)/ totaldocument
                        averagecompletelist[v4parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v4parid,"Centre_id":v4centreid,"local_id":v4localid,"date":v4date,"time":v4time,"activity":v4activity,"type":v4activitytype,"version":v4version,"old_content":v4oldcontent,"newcontent":v4newcontent,"completeness":v4completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v4parid],"total_edits":totaleditlist[v4parid]}
                        db.save(data)
                        
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v5' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v5parid = int(idlist[idposition + 3])
            
                        if v5versionlist[v5parid] == 0:
                            v5activity = 'Create'
                        else:
                            v5activity = 'Update'
                        v5activitytype = 'V5_Form'
                
                        v5versionlist[v5parid] = v5versionlist[v5parid] + 1
                        totaleditlist[v5parid] = totaleditlist[v5parid] + 1
                        clilocalline = mparticipantlist[v5parid]
                        v5centreid = re.split(' ', clilocalline)[0]
                        v5localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v5date = postlinelist[8]
                        v5time = postlinelist[9]
                        v5version = v5versionlist[v5parid]
                        if v5oldcontentlist[v5parid] == None:
                            v5oldcontentlist[v5parid] = ''
                        v5oldcontent = v5oldcontentlist[v5parid]
            
                        v5position = parameterline.find('"v5')
                        commitposition = parameterline.find('commit')
                        contentstart = v5position
                        contentend = commitposition - 3
                        v5new1content = parameterline[contentstart:contentend]
                        v5new2content = v5new1content.replace('"', '')
                        v5new3content = v5new2content.replace('{', '')
                        v5newcontent = v5new3content.replace('}', '')
                        v5oldcontentlist[v5parid] = v5newcontent
                    
                        v5totalquestions = v5new1content.count(',') + 1
                        v5unanswerednum = v5new1content.count('""')
                        accuratev5completeness = (v5totalquestions - v5unanswerednum)/v5totalquestions
                        v5completeness = round(accuratev5completeness, 2)
            
                        if totaldocumentlist[v5parid] == None:
                            totaldocumentlist[v5parid] =  'V5_Form'
                            totaldocument = 1
                        elif 'V5_Form' not in totaldocumentlist[v5parid]:
                            totaldocumentlist[v5parid] = totaldocumentlist[v5parid] + ' V5_Form'
                            splitstring = totaldocumentlist[v5parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v5parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v5parid] * (totaldocument - 1) + accuratev5completeness)/ totaldocument
                        averagecompletelist[v5parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v5parid,"Centre_id":v5centreid,"local_id":v5localid,"date":v5date,"time":v5time,"activity":v5activity,"type":v5activitytype,"version":v5version,"old_content":v5oldcontent,"newcontent":v5newcontent,"completeness":v5completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v5parid],"total_edits":totaleditlist[v5parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v6' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v6parid = int(idlist[idposition + 3])
            
                        if v6versionlist[v6parid] == 0:
                            v6activity = 'Create'
                        else:
                            v6activity = 'Update'
                        v6activitytype = 'V6_Form'
                
                        v6versionlist[v6parid] = v6versionlist[v6parid] + 1
                        totaleditlist[v6parid] = totaleditlist[v6parid] + 1
                        clilocalline = mparticipantlist[v6parid]
                        v6centreid = re.split(' ', clilocalline)[0]
                        v6localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v6date = postlinelist[8]
                        v6time = postlinelist[9]
                        v6version = v6versionlist[v6parid]
                        if v6oldcontentlist[v6parid] == None:
                            v6oldcontentlist[v6parid] = ''
                        v6oldcontent = v6oldcontentlist[v6parid]
            
                        v6position = parameterline.find('"v6')
                        commitposition = parameterline.find('commit')
                        contentstart = v6position
                        contentend = commitposition - 3
                        v6new1content = parameterline[contentstart:contentend]
                        v6new2content = v6new1content.replace('"', '')
                        v6new3content = v6new2content.replace('{', '')
                        v6newcontent = v6new3content.replace('}', '')
                        v6oldcontentlist[v6parid] = v6newcontent
                    
                        v6totalquestions = v6new1content.count(',') + 1
                        v6unanswerednum = v6new1content.count('""')
                        accuratev6completeness = (v6totalquestions - v6unanswerednum)/v6totalquestions
                        v6completeness = round(accuratev6completeness, 2)
            
                        if totaldocumentlist[v6parid] == None:
                            totaldocumentlist[v6parid] =  'V6_Form'
                            totaldocument = 1
                        elif 'V6_Form' not in totaldocumentlist[v6parid]:
                            totaldocumentlist[v6parid] = totaldocumentlist[v6parid] + ' V6_Form'
                            splitstring = totaldocumentlist[v6parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v6parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v6parid] * (totaldocument - 1) + accuratev6completeness)/ totaldocument
                        averagecompletelist[v6parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v6parid,"Centre_id":v6centreid,"local_id":v6localid,"date":v6date,"time":v6time,"activity":v6activity,"type":v6activitytype,"version":v6version,"old_content":v6oldcontent,"newcontent":v6newcontent,"completeness":v6completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v6parid],"total_edits":totaleditlist[v6parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v7' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v7parid = int(idlist[idposition + 3])
            
                        if v7versionlist[v7parid] == 0:
                            v7activity = 'Create'
                        else:
                            v7activity = 'Update'
                        v7activitytype = 'V7_Form'
                
                        v7versionlist[v7parid] = v7versionlist[v7parid] + 1
                        totaleditlist[v7parid] = totaleditlist[v7parid] + 1
                        clilocalline = mparticipantlist[v7parid]
                        v7centreid = re.split(' ', clilocalline)[0]
                        v7localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v7date = postlinelist[8]
                        v7time = postlinelist[9]
                        v7version = v7versionlist[v7parid]
                        if v7oldcontentlist[v7parid] == None:
                            v7oldcontentlist[v7parid] = ''
                        v7oldcontent = v7oldcontentlist[v7parid]
            
                        v7position = parameterline.find('"v7')
                        commitposition = parameterline.find('commit')
                        contentstart = v7position
                        contentend = commitposition - 3
                        v7new1content = parameterline[contentstart:contentend]
                        v7new2content = v7new1content.replace('"', '')
                        v7new3content = v7new2content.replace('{', '')
                        v7newcontent = v7new3content.replace('}', '')
                        v7oldcontentlist[v7parid] = v7newcontent
                    
                        v7totalquestions = v7new1content.count(',') + 1
                        v7unanswerednum = v7new1content.count('""')
                        accuratev7completeness = (v7totalquestions - v7unanswerednum)/v7totalquestions
                        v7completeness = round(accuratev7completeness, 2)
            
                        if totaldocumentlist[v7parid] == None:
                            totaldocumentlist[v7parid] =  'V7_Form'
                            totaldocument = 1
                        elif 'V7_Form' not in totaldocumentlist[v7parid]:
                            totaldocumentlist[v7parid] = totaldocumentlist[v7parid] + ' V7_Form'
                            splitstring = totaldocumentlist[v7parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v7parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v7parid] * (totaldocument - 1) + accuratev7completeness)/ totaldocument
                        averagecompletelist[v7parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v7parid,"Centre_id":v7centreid,"local_id":v7localid,"date":v7date,"time":v7time,"activity":v7activity,"type":v7activitytype,"version":v7version,"old_content":v7oldcontent,"newcontent":v7newcontent,"completeness":v7completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v7parid],"total_edits":totaleditlist[v7parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v8' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v8parid = int(idlist[idposition + 3])
            
                        if v8versionlist[v8parid] == 0:
                            v8activity = 'Create'
                        else:
                            v8activity = 'Update'
                        v8activitytype = 'V8_Form'
                
                        v8versionlist[v8parid] = v8versionlist[v8parid] + 1
                        totaleditlist[v8parid] = totaleditlist[v8parid] + 1
                        clilocalline = mparticipantlist[v8parid]
                        v8centreid = re.split(' ', clilocalline)[0]
                        v8localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v8date = postlinelist[8]
                        v8time = postlinelist[9]
                        v8version = v8versionlist[v8parid]
                        if v8oldcontentlist[v8parid] == None:
                            v8oldcontentlist[v8parid] = ''
                        v8oldcontent = v8oldcontentlist[v8parid]
            
                        v8position = parameterline.find('"v8')
                        commitposition = parameterline.find('commit')
                        contentstart = v8position
                        contentend = commitposition - 3
                        v8new1content = parameterline[contentstart:contentend]
                        v8new2content = v8new1content.replace('"', '')
                        v8new3content = v8new2content.replace('{', '')
                        v8newcontent = v8new3content.replace('}', '')
                        v8oldcontentlist[v8parid] = v8newcontent
                    
                        v8totalquestions = v8new1content.count(',') + 1
                        v8unanswerednum = v8new1content.count('""')
                        accuratev8completeness = (v8totalquestions - v8unanswerednum)/v8totalquestions
                        v8completeness = round(accuratev8completeness, 2)
            
                        if totaldocumentlist[v8parid] == None:
                            totaldocumentlist[v8parid] =  'V8_Form'
                            totaldocument = 1
                        elif 'V8_Form' not in totaldocumentlist[v8parid]:
                            totaldocumentlist[v8parid] = totaldocumentlist[v8parid] + ' V8_Form'
                            splitstring = totaldocumentlist[v8parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v8parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v8parid] * (totaldocument - 1) + accuratev8completeness)/ totaldocument
                        averagecompletelist[v8parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v8parid,"Centre_id":v8centreid,"local_id":v8localid,"date":v8date,"time":v8time,"activity":v8activity,"type":v8activitytype,"version":v8version,"old_content":v8oldcontent,"newcontent":v8newcontent,"completeness":v8completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v8parid],"total_edits":totaleditlist[v8parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v9' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v9parid = int(idlist[idposition + 3])
            
                        if v9versionlist[v9parid] == 0:
                            v9activity = 'Create'
                        else:
                            v9activity = 'Update'
                        v9activitytype = 'V9_Form'
                
                        v9versionlist[v9parid] = v9versionlist[v9parid] + 1
                        totaleditlist[v9parid] = totaleditlist[v9parid] + 1
                        clilocalline = mparticipantlist[v9parid]
                        v9centreid = re.split(' ', clilocalline)[0]
                        v9localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v9date = postlinelist[8]
                        v9time = postlinelist[9]
                        v9version = v9versionlist[v9parid]
                        if v9oldcontentlist[v9parid] == None:
                            v9oldcontentlist[v9parid] = ''
                        v9oldcontent = v9oldcontentlist[v9parid]
            
                        v9position = parameterline.find('"v9')
                        commitposition = parameterline.find('commit')
                        contentstart = v9position
                        contentend = commitposition - 3
                        v9new1content = parameterline[contentstart:contentend]
                        v9new2content = v9new1content.replace('"', '')
                        v9new3content = v9new2content.replace('{', '')
                        v9newcontent = v9new3content.replace('}', '')
                        v9oldcontentlist[v9parid] = v9newcontent
                    
                        v9totalquestions = v9new1content.count(',') + 1
                        v9unanswerednum = v9new1content.count('""')
                        accuratev9completeness = (v9totalquestions - v9unanswerednum)/v9totalquestions
                        v9completeness = round(accuratev9completeness, 2)
            
                        if totaldocumentlist[v9parid] == None:
                            totaldocumentlist[v9parid] =  'V9_Form'
                            totaldocument = 1
                        elif 'V9_Form' not in totaldocumentlist[v9parid]:
                            totaldocumentlist[v9parid] = totaldocumentlist[v9parid] + ' V9_Form'
                            splitstring = totaldocumentlist[v9parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v9parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v9parid] * (totaldocument - 1) + accuratev9completeness)/ totaldocument
                        averagecompletelist[v9parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v9parid,"Centre_id":v9centreid,"local_id":v9localid,"date":v9date,"time":v9time,"activity":v9activity,"type":v9activitytype,"version":v9version,"old_content":v9oldcontent,"newcontent":v9newcontent,"completeness":v9completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v9parid],"total_edits":totaleditlist[v9parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
                
        elif '/v10' in aline:
            parameterline = f.readline()
            if 'Started POST' not in parameterline and 'Started PUT' not in parameterline:
                while 'Parameters' not in parameterline and 'utf8'not in parameterline:
                    parameterline = f.readline()
                    if 'Started POST' in parameterline or 'Started PUT' in parameterline:
                        idline = parameterline
                        flag = 1
                        break
                if flag == 0: 
                    if 'participant_id' in parameterline:
                        idlist = re.split('"|=>|,', parameterline)
                        idposition = idlist.index('participant_id')
                        v10parid = int(idlist[idposition + 3])
            
                        if v10versionlist[v10parid] == 0:
                            v10activity = 'Create'
                        else:
                            v10activity = 'Update'
                        v10activitytype = 'V10_Form'
                
                        v10versionlist[v10parid] = v10versionlist[v10parid] + 1
                        totaleditlist[v10parid] = totaleditlist[v10parid] + 1
                        clilocalline = mparticipantlist[v10parid]
                        v10centreid = re.split(' ', clilocalline)[0]
                        v10localid = re.split(' ', clilocalline)[1]
                        postlinelist = re.split(' |"', aline)
                        v10date = postlinelist[8]
                        v10time = postlinelist[9]
                        v10version = v10versionlist[v10parid]
                        if v10oldcontentlist[v10parid] == None:
                            v10oldcontentlist[v10parid] = ''
                        v10oldcontent = v10oldcontentlist[v10parid]
            
                        v10position = parameterline.find('"v10')
                        commitposition = parameterline.find('commit')
                        contentstart = v10position
                        contentend = commitposition - 3
                        v10new1content = parameterline[contentstart:contentend]
                        v10new2content = v10new1content.replace('"', '')
                        v10new3content = v10new2content.replace('{', '')
                        v10newcontent = v10new3content.replace('}', '')
                        v10oldcontentlist[v10parid] = v10newcontent
                    
                        v10totalquestions = v10new1content.count(',') + 1
                        v10unanswerednum = v10new1content.count('""')
                        accuratev10completeness = (v10totalquestions - v10unanswerednum)/v10totalquestions
                        v10completeness = round(accuratev10completeness, 2)
            
                        if totaldocumentlist[v10parid] == None:
                            totaldocumentlist[v10parid] =  'V10_Form'
                            totaldocument = 1
                        elif 'V10_Form' not in totaldocumentlist[v10parid]:
                            totaldocumentlist[v10parid] = totaldocumentlist[v10parid] + ' V10_Form'
                            splitstring = totaldocumentlist[v10parid]
                            totaldocumentsplitlist = re.split(' ', splitstring)
                            totaldocument = len(totaldocumentsplitlist)
                        else:
                            totaldocumentsplitlist = re.split(' ', totaldocumentlist[v10parid])
                            totaldocument = len(totaldocumentsplitlist)
                    
                        accurateaveragecomplete = (averagecompletelist[v10parid] * (totaldocument - 1) + accuratev10completeness)/ totaldocument
                        averagecompletelist[v10parid] = round(accurateaveragecomplete, 2)
                        data = {"participant_id":v10parid,"Centre_id":v10centreid,"local_id":v10localid,"date":v10date,"time":v10time,"activity":v10activity,"type":v10activitytype,"version":v10version,"old_content":v10oldcontent,"newcontent":v10newcontent,"completeness":v10completeness,"document_finished":totaldocument,"average_completeness":averagecompletelist[v10parid],"total_edits":totaleditlist[v10parid]}
                        db.save(data)
                    else:
                        idline = parameterline
                        flag = 1
            else:
                idline = parameterline
                flag = 1
    
    if flag == 0:
        aline = f.readline()
    else:
        aline = idline
        flag = 0
f.close()