import smtplib, json
import threading
from email.mime.text import MIMEText



def send_mail(to_emails, first, second):
    try:
        with open("message.txt", "r") as f:
            message = f.read()    

        with open("creds.json", "r") as f:
            data = json.loads(f.read())
        to_email = data['to']
        from_email = data['from']
        password = data['password']
        server = data['server']
        subject = data['subject']
        message = 'Subject: {}\n\n{}'.format(subject, message)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From']    = from_email
        s = smtplib.SMTP(server, 587)
        s.starttls()
        s.login(from_email, password)

        for email in to_emails[first:second]:
            print(email)
            msg['To'] = email
            s.sendmail(msg['From'], msg['To'], message)
        s.quit()
    except Exception as e:
        print(e)
        with open("error.txt", "w") as f:
            f.write(str(e))

if __name__ == "__main__":

    threads = []
    # dnis
    with open("to.txt", "r") as f:
        to_emails = f.readlines()
    th = int(input("Threads number: \n"))
    to_add = int(len(to_emails)/th)+1
    x = 0
    for _ in range(th):
        first = x
        second = first+to_add
        # print(first, second)
        t = threading.Thread(target=send_mail, args= (to_emails, first, second))
        t.start()
        threads.append(t)
        x = x+to_add

    for thread in threads:
        thread.join()

    # print(to_email, from_email, password, server, subject, message)
    # send_mail(to_email, subject, message, server, from_email, password)
