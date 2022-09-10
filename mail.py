import smtplib


def mail_send():
    my_server = smtplib.SMTP('smtp.gmail.com', 587)
    my_server.starttls()
    my_server.login('pythonbot010@gmail.com', 'herduvhpzaungvjj')
    sender_id = input("Enter sender's id : ")
    mail_body = input("Enter the message of mail-body : ")
    my_server.sendmail('pythonbot010@gmail.com',
                       sender_id,
                       mail_body)
    print("! Mail sent successfully !")
    print("")

count = 0

while (1):
    if (count == 0):
        confirm = input("Do u want to send an e-mail ? ")
    elif (count > 0):
        confirm = input("Do u want to send another e-mail ? ")   
    if (confirm != "Yes" and confirm != "yes"):
        break
    else:
        mail_send()
    count = count + 1    
