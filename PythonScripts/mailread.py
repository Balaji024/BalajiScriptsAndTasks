import imapclient
#> pip install setuptools==20.1.1
#> pip install pyzmail
import pyzmail

#Connect to the Server
conn= imapclient.IMAPClient('imap.gmail.com', ssl=True,  use_uid=True)

#Login to your Account
conn.login('balaji02493@gmail.com', 'Mcc@1234')

#Select the required folder(Eg: INBOX, SENT, DRAFTS)
print(conn.list_folders()) # To list all the folders available
conn.select_folder('INBOX', readonly=True)

# Get the UIDS of the your specified mails(searching for inbox mails)
UIDS = conn.search(['SINCE', '06-May-2020'])#You can use ON, BEFORE, SUBJECT, FROM, TO, SEEN, UNSEEN and somemore stuffs

#Fetching the message in python edited format
rawMessage=conn.fetch([UIDS[0]], ['BODY[]', 'FLAGS'])

#Using pyzmail module to get the mails in a easily readable manner.
message=pyzmail.PyzMessage.factory(rawMessage[UIDS[0]][b'BODY[]'])

#Retriving the mail information                                  
print("FROM :",message.get_addresses('from'))
print("CC :",message.get_addresses('cc'))
print("Subject :",message.get_subject())
print(message.text_part)
print(message.html_part,"html")
print("Content :",message.text_part.get_payload().decode('UTF-8'))


#Deleteing Mails
#conn.select_folder('INBOX', readonly=False)
#conn.delete_messages(UIDS[0])

#print(UIDS)



