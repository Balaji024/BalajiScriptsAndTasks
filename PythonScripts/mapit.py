import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
#https://www.google.co.in/maps/@19.120128,72.8858624,12z
webbrowser.open('https://www.google.com/maps/place/' + address)
    
  
