import re
import csv
import operator

with open('H:/IT autoation Google/log file processing/syslog.log') as file:
    pattern=r'([\w: .]*)ticky: ([A-Z]*)([\w #\[\]\']*)\(([\w .]*)\)'
    error={}
    per_user={}
    print('I am inside')
    for line in file:
        print(line)
        if re.search(pattern,line):
            res=re.search(pattern,line)
            if not res.group(4) in per_user:
                per_user[res.group(4)]={}
                per_user[res.group(4)]["ERROR"]=0
                per_user[res.group(4)]["INFO"]=0
            if res.group(2).strip()=='ERROR':
                if res.group(3).strip() in error:
                    error[res.group(3).strip()]+=1
                else:
                    error[res.group(3).strip()]=1
                if res.group(4) in per_user:
                    if "ERROR" in per_user[res.group(4)]:
                        per_user[res.group(4)]['ERROR']+=1
                    else:
                        per_user[res.group(4)]['ERROR']=1
            if res.group(2).strip()=='INFO':
                if res.group(4) in per_user:
                    if "INFO" in per_user[res.group(4)]:
                        per_user[res.group(4)]['INFO']+=1
                    else:
                        per_user[res.group(4)]['INFO']=1
        else:
            print(line)
error=sorted(error.items(), key=operator.itemgetter(1),reverse=True)
userdic=sorted(per_user.items(), key=operator.itemgetter(0))
user=[(a,b['INFO'],b["ERROR"]) for a,b in userdic]
headerserror=["Error", "Count"]
headeruserstat=["Username","INFO","ERROR"]
with open('H:/IT autoation Google/log file processing/error_message.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(headerserror)
    for row in error:
        w.writerow(row)
    f.close()
with open('H:/IT autoation Google/log file processing/user_statistics.csv','w') as f:
    w=csv.writer(f)
    w.writerow(headeruserstat)
    for obj in user:
        w.writerow(obj)
    f.close()