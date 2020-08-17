import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login("testesrt123@gmail.com", "Suporte@123")
de = "mrcutrim@gmail.com"
para = ["testesrt123@gmail.com"]
msg = """
    From: %s
    To: %s
    Subject: SempreUpdate
    Email de teste do SempreUpdate.""" %(de, ', '.join(para))
smtp.sendmail(de, para, msg)
smtp.quit()