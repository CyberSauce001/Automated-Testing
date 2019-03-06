import importlib, smtplib, os.path, datetime, time
from email.mime.text import MIMEText
path = 'Working.lock'

if os.path.exists(path):
    print("In Progress")
    exit()
else:
    log = open(path, 'w')
    with open("{add php file here}", "a") as myfile :
        myfile.write('\n<?php echo"In Progress: %s<BR>"; ?>' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    myfile.close()



t = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
scripts = ['Cert','Careers','About_Us','Contact','FAQ', 'Navigate', 'Partner',
          'Press', 'Scorm','SignUp', 'Video']

check = []
x = 0
f = os.listdir('LogFile/')
for k in scripts:
    try:
        globals()[k] = importlib.import_module(k)
        time.sleep(5)
        if os.path.isfile('LogFile/'+k+'_Log.txt'):
            print(k, ': Failed')
            check.append((k, ': Failed', t))
            check.append('\n')
            x += 1
        else:
            print(k, ': Passed')
            check.append('\n')
            check.append((k, ': Passed'))
    except Exception:
        print('Script Error @', k)
        check.append('\n')
        check.append((k, ': Script Error', t))
        x+1
        pass

log.close()
os.remove(path)

if x > 0:
    recipients = []
else:
    recipients = []
print(recipients)
content = "  \n".join(str(x) for x in check)


gmail_sender = ''
gmail_passwd = ''

TEXT = content
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)
msg= MIMEText(TEXT)
msg['SUBJECT'] = 'Automated Testing - Windows'
msg['From'] = ''
msg['To'] = ", ".join(recipients)

try:
    server.send_message(msg)
    print ('email sent')
except Exception:
    print ('error sending mail')

server.quit()


