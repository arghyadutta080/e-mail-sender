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
    print("")
    print("! Your Mail is successfully sent !")
    print("")


count = 0
mail_count = 0

while (1):
    if (count == 0):
        confirm = input("Do you want to send an e-mail ? (Yes/No) : ")
    elif (count > 0):
        confirm = input("Do you want to send another e-mail ? (Yes/No) : ")
    if (confirm != "Yes" and confirm != "yes" and confirm != "YES"):
        print("Thank You, for trying this program.")
        break
    else:
        mail_send()
        mail_count = mail_count + 1
        if (mail_count == 1):
            print("You have sent " + str(mail_count) + " mail.")
            print("")
        elif (mail_count > 1):
            print("You have sent " + str(mail_count) + " mails.")
            print("")
    count = count + 1