Logs = ['syslog','repolog','dpklog','applog','demolog','filterlog','errlog','msglog','stremlog','apachelog','yarnlog']
# display from applog to msglog
#             ------------------
# skip the remaining logs
# Note: use enumerate - iterate the logs
# -----------------------------------------
for index,value in enumerate(Logs):
    if(index >=3 and index <=7):
        print(index,value)
