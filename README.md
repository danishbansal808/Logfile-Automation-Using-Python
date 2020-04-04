# Logfile-Automation-Using-Python
This script is used to process log files. It counts the error which are repeating most number of times and display them as html tables and also processing which user is generating how mny number of erroes and info logs.

Log file has following type of log format.
```txt
    Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)
    Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)
    Jan 31 01:29:16 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)
    Jan 31 01:33:12 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)
    Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)
```
    
The file naming **processor.py** processes the **syslog.log** file and generate two files

    error_message.csv
        It consist the list of all erros present in log file in order of how many times each error occured.
    user_statastics.csv
        It consist of user data ordered alphabetically how many error and info logs are generated by each user.
 
The file **csv_to_html.py** takes **2 system arguments** 

    First the path of csv file
    Second the path of html file to be generated or overwritten

The HTML file produces the folowing results when opened

### error_message.html

| Error | Count |
| --- | --- |
| Timeout while retrieving information | 15 |
| Connection to DB failed | 13 |
| Tried to add information to closed ticket | 12 |
| Permission denied while closing ticket | 10 |
| The ticket was modified while updating | 9 |
| Ticket doesn't exist |7 |

### user_statastics.html

| Username | INFO | ERROR |
| --- | --- | --- |
| ac | 2 | 2 |
| ahmed.miller | 2 | 4 |
| blossom | 2 | 6 |
| bpacheco | 0 | 2 |
| breee | 1 | 5 |
| britanni | 1 | 1 |
| enim.non | 2 | 3 |