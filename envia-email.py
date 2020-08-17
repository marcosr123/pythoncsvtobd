# -*- coding: UTF-8 -*-

import smtplib
import publicip
from getmac import get_mac_address as getmac

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()

smtp.login('testesrt123@gmail.com', 'Suporte@123')
mac = str(getmac())
ip = str(publicip.get())
de = 'testesrt123@gmail.com'
para = ['mrcutrim@gmail.com']
msg = """From: %s
To: %s
Subject: Teste de Email SRT

Endereco de IP:{} 
MAC:{} """.format(ip,mac) % (de, ','.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()