import smtplib
server = smtplib.SMTP('smtp.mediatek.inc', 25)
server.starttls()
server.login("shekhar.agrawal@mediatek.com", "shi22she18")
msg = "Hello! /n heya"
server.sendmail("shekhar.agrawal@mediatek.com", "shekhar.agrawal@mediatek.com", msg)
server.quit()