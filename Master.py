import importlib, smtplib, os.path, datetime
from email.mime.text import MIMEText

t = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
scripts = ['Cert','Careers','About_Us','Contact','FAQ', 'Navigate', 'Partner',
          'Press', 'Scorm','SignUp', 'Video' ]

check = []
x = 0
f = os.listdir('')
for k in scripts:
    try:
        globals()[k] = importlib.import_module(k)
        if os.path.isfile(''):
            print(k, ': Failed')
            check.append((k, ': Failed', t))
            check.append('\n')
            x += 1
            #print(check)
        else:
            print(k, ': Passed')
            check.append('\n')
            check.append((k, ': Passed'))
            #print(checck)
    except Exception:
        print('Script Error @', k)
        check.append('\n')
        check.append((k, ': Failed', t))
        pass


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
except:
    print ('error sending mail')

server.quit()
