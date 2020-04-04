import re
import csv
import operator

#Open teh file to be processed
with open('syslog.log') as file:
    #Writing regular expression and capturing groups to process
    pattern=r'([\w: .]*)ticky: ([A-Z]*)([\w #\[\]\']*)\(([\w .]*)\)'
    #Initializing required data structures
    error={}
    per_user={}
    #Reading Each Line from sysylog.log FIle
    for line in file:
        #Checking if the pattern matches
        if re.search(pattern,line):
            #Captring the matched groups
            res=re.search(pattern,line)
            #Updating per_user Dictionary for captured user
            #If don't exist then make a new entry
            if not res.group(4) in per_user:
                per_user[res.group(4)]={}
                per_user[res.group(4)]["ERROR"]=0
                per_user[res.group(4)]["INFO"]=0
            #If the log line is ERROR
            if res.group(2).strip()=='ERROR':
                #If error dictionary already consist of the error captured then add 1 to the error as it repeats again
                if res.group(3).strip() in error:
                    error[res.group(3).strip()]+=1
                #Else make a fresh entry starting with 1
                else:
                    error[res.group(3).strip()]=1
                # Again checking if user already in per_user dictionary
                if res.group(4) in per_user:
                    #If ERROR part of that user exist than add 1
                    if "ERROR" in per_user[res.group(4)]:
                        per_user[res.group(4)]['ERROR']+=1
                    #Else start with 1
                    else:
                        per_user[res.group(4)]['ERROR']=1
            #If the log line is INFO
            if res.group(2).strip()=='INFO':
                # Again checking if user already in per_user dictionary
                if res.group(4) in per_user:
                    #If INFO part of that user exist than add 1
                    if "INFO" in per_user[res.group(4)]:
                        per_user[res.group(4)]['INFO']+=1
                    #Else start with 1
                    else:
                        per_user[res.group(4)]['INFO']=1
        else:
            #Prints line which does'nt match with our regular expression
            print(line)
#Making tuples and sorting them by numbers Decending
error=sorted(error.items(), key=operator.itemgetter(1),reverse=True)
userdic=sorted(per_user.items(), key=operator.itemgetter(0))
#Making tuples and sorting them by usernames
user=[(a,b['INFO'],b["ERROR"]) for a,b in userdic]
headerserror=["Error", "Count"]
headeruserstat=["Username","INFO","ERROR"]
#Writing Files
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
