import imapclient
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# logging into account
conn.login('balaji02493@gmail.com', 'Mcc@1234')
#selecting the folder to read
select_info=conn.select_folder('INBOX', readonly=True)
print('%d messages in INBOX' % select_info[b'EXISTS'])
#Searching for mail
messages = conn.search(['FROM', 'arti04294@gmail.com'])
print("%d messages from our best friend" % len(messages))
for msgid, data in conn.fetch(messages, ['ENVELOPE']).items():
 envelope = data[b'ENVELOPE']
 print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
#UIDS=imap.search(['SINCE 01-May-2020'])
#rawMessage=conn.fetch(UIDS[0], ['BODY[]', 'FLAGS'])

#import imaplib
#import pprint

#imap_host = 'imap.gmail.com'
#imap_user = 'balaji02493@gmail.com'
#imap_pass = 'Mcc@1234'

# connect to host using SSL
#imap = imaplib.IMAP4_SSL(imap_host)

## login to server
#imap.login(imap_user, imap_pass)

#imap.select('Inbox')

#tmp, data = imap.search(None, 'ALL')
#for num in data[0].split():
#	tmp, data = imap.fetch(num, '(RFC822)')
#	print('Message: {0}\n'.format(num))
#	pprint.pprint(data[0][1])
#	break
#imap.close()



