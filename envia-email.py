import smtplib
from uuid import getnode as get_mac

try:
    msgTo = str(input("Informe o e-mail de destino: "))
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    msgFrom = 'testesrt123@gmail.com'
    toPass = 'Suporte@123'
    smtpObj.login(msgFrom, toPass)
    msg = str(get_mac())
    smtpObj.sendmail(msgTo,msgFrom,'Subject: Titulo do email',msg)
    smtpObj.quit()
    print("Email enviado com sucesso!")
except:
    print('Erro ao enviar email!')