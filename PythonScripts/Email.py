import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
#print(conn.ehlo())
conn.starttls()
conn.login('balaji02493@gmail.com', 'Mcc@1234')
conn.sendmail('balaji02493@gmail.com','arti04294@gmail.com','Subject: FROM PYTHON \n\nDear Arti, \nI want to tell you that i love you more than anything...!!!\n\nRegards,\nBalaji')
conn.quit()
